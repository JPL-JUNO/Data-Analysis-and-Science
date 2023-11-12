library(shiny)
# 建一个输入控件，并通过其他两个输入来控制类型和标签
ui <- fluidPage(
  textInput("label", "label"),
  selectInput("type", "type", c("slider", "numeric")),
  uiOutput("numeric")
)

server <- function(input, output, session) {
  output$numeric <- renderUI({
    # 会有一个简单的错误，因为 slider 不能设置空置
    value <- isolate(input$dynamic)
    # isolate() 可以用来隔离每次 ui 改变值消失的情况
    if (input$type == "slider") {
      sliderInput("dynamic", input$label, value = value, min = 0, max = 10)
    } else {
      numericInput("dynamic", input$label, value = value, min = 0, max = 10)
    }
  })
}


shinyApp(ui, server)
