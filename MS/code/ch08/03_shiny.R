library(shiny)

ui <- fluidPage(
  numericInput("steps", "How many steps?", 10),
  actionButton("go", "go"),
  textOutput("result")
)

server <- function(input, output, session) {
  data <- eventReactive(input$go, {
    withProgress(message = "Computing random number", {
      for (i in seq_len(input$steps)) {
        # Sys.sleep() 模拟一个需要长时间运行的计算
        Sys.sleep(.5)
        incProgress(1 / input$steps)
      }
      runif(1)
    })
  })

  output$result <- renderText(round(data(), 2))
}

shinyApp(ui, server)
