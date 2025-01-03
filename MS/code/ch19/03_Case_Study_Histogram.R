library(shiny)

datasetInput <- function(id, filter = NULL) {
  names <- ls("package:datasets")
  if (!is.null(filter)) {
    data <- lapply(names, get, "package:datasets")
    names <- names[vapply(data, filter, logical(1))]
  }
  selectInput(NS(id, "dataset"), "Pick a dataset", choices = names)
}

datasetServer <- function(id) {
  moduleServer(id, function(input, output, session) {
    reactive(get(input$dataset, "package:datasets"))
  })
}

find_vars <- function(data, filter) {
  names(data)[vapply(data, filter, logical(1))]
}

selectVarInput <- function(id) {
  selectInput(NS(id, "var"), "Variable", choices = NULL)
}

selectVarServer <- function(id, data, filter = is.numeric) {
  moduleServer(id, function(input, output, session) {
    observeEvent(data(), {
      updateSelectInput(session, "var", choices = find_vars(data(), filter))
    })

    list(
      name = reactive(input$var),
      value = reactive(data()[[input$var]])
    )
  })
}

find_vars <- function(data, filter) {
  names(data)[vapply(data, filter, logical(1))]
}

histogramOutput <- function(id) {
  tagList(
    numericInput(NS(id, "bins"), "bins", 10, min = 1, step = 1),
    plotOutput(NS(id, "hist"))
  )
}

histogramServer <- function(id, x, title = reactive("Histogram")) {
  stopifnot(is.reactive(x))
  stopifnot(is.reactive(title))

  moduleServer(id, function(input, output, session) {
    output$hist <- renderPlot(
      {
        req(is.numeric(x()))
        main <- paste0(title(), " [", input$bins, "]")
        hist(x(), breaks = input$bins, main = main)
      },
      res = 96
    )
  })
}

histogramApp <- function() {
  ui <- fluidPage(
    sidebarLayout(
      sidebarPanel(
        datasetInput("data", is.data.frame),
        selectVarInput("var")
      ),
      mainPanel(
        histogramOutput("hist")
      )
    )
  )

  server <- function(input, output, session) {
    data <- datasetServer("data")
    x <- selectVarServer("var", data)
    histogramServer("hist", x$value, x$name)
  }

  shinyApp(ui, server)
}

histogramApp()
