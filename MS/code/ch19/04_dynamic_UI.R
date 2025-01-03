library(shiny)
library(purrr)

filter_ui <- function(id) {
  uiOutput(NS(id, "controls"))
}

dataset_input <- function(id, filter = NULL) {
  names <- ls("package:datasets")
  if (!is.null(filter)) {
    data <- lapply(names, get, "package:datasets")
    names <- names[vapply(data, filter, logical(1))]
  }
  selectInput(NS(id, "dataset"), "Pick a dataset", choices = names)
}

dataset_server <- function(id) {
  moduleServer(id, function(input, output, session) {
    reactive(get(input$dataset, "package:datasets"))
  })
}

make_ui <- function(x, id, var) {
  if (is.numeric(x)) {
    rng <- range(x, na.rm = TRUE)
    sliderInput(id, var, min = rng[1], max = rng[2], value = rng)
  } else if (is.factor(x)) {
    levs <- levels(x)
    selectInput(id, var, choices = levs, selected = levs, multiple = TRUE)
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
    TRUE
  }
}


filter_server <- function(id, df) {
  stopifnot(is.reactive(df))

  moduleServer(id, function(input, output, session) {
    vars <- reactive(names(df()))

    output$controls <- renderUI(
      map(vars(), function(var) make_ui(df()[[var]], NS(id, var), var))
    )

    reactive({
      each_var <- map(
        vars(),
        function(var) filter_var(df()[[var]], input[[var]])
      )
      reduce(each_var, `&`)
    })
  })
}

filter_app <- function() {
  ui <- fluidPage(
    sidebarLayout(
      sidebarPanel(
        dataset_input("data", is.data.frame),
        textOutput("n"),
        filter_ui("filter")
      ),
      mainPanel(tableOutput("table"))
    )
  )

  server <- function(input, output, session) {
    df <- dataset_server("data")
    filter <- filter_server("filter", df)
    output$table <- renderTable(df()[filter(), , drop = TRUE])
    output$n <- renderText(paste0(sum(filter()), " rows"))
  }
  shinyApp(ui, server)
}

filter_app()
