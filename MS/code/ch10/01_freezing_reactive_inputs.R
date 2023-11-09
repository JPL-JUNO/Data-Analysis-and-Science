library(shiny)

ui <- fluidPage(
  selectInput("dataset", "Choose a dataset", c("pressure", "cars")),
  selectInput("column", "Choose column", character(0)),
  verbatimTextOutput("summary")
)

server <- function(input, output, session) {
  dataset <- reactive({
    get(input$dataset, "package:datasets")
  })
  observeEvent(input$dataset, {
    # 这确保了使用该输入的任何反应或输出在下一轮完整的失效之前不会被更新
    # To be more precise,
    # any attempt to read a frozen input will result in req(FALSE).
    freezeReactiveValue(input, "column")

    updateSelectInput(inputId = "column", choices = names(dataset()))
  })
  output$summary <- renderPrint({
    summary(dataset()[[input$column]])
  })
}

shinyApp(ui, server)
