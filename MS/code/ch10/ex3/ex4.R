library(shiny)
library(purrr)
library(tidyverse)

make_ui <- function(x, var) {
  if (is.numeric(x)) {
    rng <- range(x, na.rm = TRUE)
    sliderInput(var, var, min = rng[1], max = rng[2], value = rng)
  } else if (is.factor(x)) {
    levs <- levels(x)
    selectInput(var, var, choices = levs, selected = levs, multiple = TRUE)
  } else if (lubridate::is.Date(x)) {
    rng <- range(x, na.rm = TRUE)
    dateInput(var, var, min = rng[1], max = rng[2], value = rng[1])
  } else {
    # No control, so don't filter
    NULL
  }
}

filter_var <- function(x, val) {
  if (is.numeric(x)) {
    !is.na(x) & x >= val[1] & x <= val[2]
  } else if (is.factor(x)) {
    x %in% val
  } else {
    TRUE
  }
}

dfs <- keep(ls("package:datasets"), ~ is.data.frame(get(.x, "package:datasets")))

x <- data.frame(
  date = c(
    rep(as.Date("2020/1/1"), 5),
    rep(as.Date("2020/2/2"), 5),
    rep(as.Date("2020/3/3"), 5),
    rep(as.Date("2020/4/4"), 5),
    rep(as.Date("2020/5/5"), 5)
  ),
  fac = as.factor(c("a", "b", "c", "d", "e"))
)


ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      uiOutput("filter")
    ),
    mainPanel(
      DT::dataTableOutput("data")
    )
  )
)

server <- function(input, output, session) {
  data <- reactive(x)
  vars <- reactive(names(data()))

  output$filter <- renderUI(
    map(vars(), ~ make_ui(data()[[.x]], .x))
  )

  selected <- reactive({
    each_var <- map(vars(), ~ filter_var(data()[[.x]], input[[.x]]))

    reduce(each_var, `&`)
  })

  output$data <- DT::renderDataTable(data()[selected(), ])
}

shinyApp(ui, server)
