library(shiny)
ui <- fluidPage(
  selectInput("dataset", label = "Dataset", choices = ls("package:datasets")),
  verbatimTextOutput("summary"),
  tableOutput("table")
)
server <- function(input, output, session) {
    dataset <- reactive({
        get(input$dataset, "package:datasets")
    })
  output$summary <- renderPrint({
    # dataset <- get(input$dataset, "package:datasets")
    summary(dataset())
  })

  output$table <- renderTable({
    # dataset <- get(input$dataset, "package:datasets")
    dataset()
  })
}
shinyApp(ui, server)
