library(shiny)

ui <- fluidPage(
  shinyFeedback::useShinyFeedback(),
  textInput("dataset", "Dataset name"),
  tableOutput("data")
)

server <- function(input, output, session) {
  data <- reactive({
    req(input$dataset)

    exists <- exists(input$dataset, "package:datasets")
    shinyFeedback::feedbackDanger("dataset", !exists, "Unknown dataset")


    # 通常，取消响应式将会重置下游的输出，
    # 使用 cancelOutput = TRUE 将会保存最近一个满足条件的结果
    req(exists, cancelOutput = TRUE)

    get(input$dataset, "package:datasets")
  })

  output$data <- renderTable({
    head(data())
  })
}

shinyApp(ui, server)
