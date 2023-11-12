# File         : 03_dynamic_filtering
# Author(s)    : Stephen CUI
# LastEditor(s): Stephen CUI
# CreatedTime  : 2023-11-12 15:32:31
# Description  : 更一般的过滤分析

library(shiny)
dfs <- keep(ls("package:datasets"), ~ is.data.frame(get(.x, "package:datasets")))
make_ui <- function(x, var) {
  if (is.numeric(x)) {
    rng <- range(x, na.rm = TRUE)
    sliderInput(var, var, min = rng[1], max = rng[2], value = rng)
  } else if (is.factor(x)) {
    levs <- levels(x)
    selectInput(var, var, choices = levs, selected = levs, multiple = TRUE)
  } else {
    NULL
  }
}

filter_var <- function(x, val) {
  if (is.numeric(x)) {
    !is.na(x) & x >= val[1] & x <= val[2]
  } else if (is.factor(x)) {
    x %in% val
  } else {
    # No control, so don't filter
    TRUE
  }
}
ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      # make_ui(iris$Sepal.Length, "Sepal.Length"),
      # make_ui(iris$Sepal.Width, "Sepal.Width"),
      # make_ui(iris$Species, "Species")
      # map(names(iris), ~ make_ui(iris[[.x]], .x))
      selectInput("dataset", label = "Dataset", choices = dfs),
      uiOutput("filter")
    ),
    mainPanel(
      tableOutput("data")
    )
  )
)

server <- function(input, output, session) {
  data <- reactive({
    get(input$dataset, "package:datasets")
  })

  vars <- reactive(names(data()))

  output$filter <- renderUI(
    map(vars(), ~ make_ui(data()[[.x]], .x))
  )
  selected <- reactive({
    # filter_var(iris$Sepal.Length, input$Sepal.Length) &
    #   filter_var(iris$Sepal.Width, input$Sepal.Width) &
    #   filter_var(iris$Species, input$Species)
    each_var <- map(vars(), ~ filter_var(data()[[.x]], input[[.x]]))
    reduce(each_var, `&`)
  })

  output$data <- renderTable(
    head(data()[selected(), ], 12)
  )
}

shinyApp(ui, server)
