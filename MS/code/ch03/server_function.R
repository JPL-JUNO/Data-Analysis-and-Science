library(shiny)

ui <- fluidPage(
  numericInput("count", "Number of values", value = 100),
  textOutput("greeting")
)

server <- function(input, output, session) {
  # input$count <- 10 # error, 只读的

  output$greeting <- renderText("Hello, Shiny!")
  # output$greeting <- "Hello, Shiny!"
  # error: 不能在渲染函数外使用

  # message("The greeting is ", output$greeting)
  # error 从 output 对象读取值是允许的
}

shinyApp(ui, server)
