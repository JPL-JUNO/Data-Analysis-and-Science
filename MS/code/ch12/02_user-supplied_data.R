library(shiny)

ui <- fluidPage(
  fileInput("data", "Dataset", accept = ".csv"),
  selectInput("var", "Var", character()),
  numericInput("min", "Min", 1, min = 0, step = 1),
  tableOutput("output")
)

server <- function(input, output, session) {
  data <- reactive({
    req(input$data)
    vroom::vroom(input$data$datapath)
  })

  observeEvent(
    data(),
    updateSelectInput(session, inputId = "var", choices = names(data()))
  )

  observeEvent(input$var, {
    val <- data()[[input$var]]
    updateNumericInput(session, inputId = "min", value = min(val))
  })

  output$output <- renderTable({
    req(input$var)

    data() |>
      filter(.data[[input$var]] > input$min) |>
      arrange(.data[[input$var]]) |>
      head(10)
  })
}

shinyApp(ui, server)
