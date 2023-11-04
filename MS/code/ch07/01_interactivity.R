library(shiny)
library(ggplot2)

ui <- fluidPage(
  textInput("desc", "通过点击更新图片"),
  plotOutput("plot", click = "plot_click"),
  verbatimTextOutput("info")
)

server <- function(input, output, session) {
  output$plot <- renderPlot(
    {
      plot(mtcars$wt, mtcars$mpg)
    },
    res = 96
  )

  output$info <- renderPrint({
    # 使用req(), 以确保应用程序在第一次单击之前不会执行任何操作
    req(input$plot_click)
    x <- round(input$plot_click$x, 2)
    y <- round(input$plot_click$y, 2)
    cat("[", x, ", ", y, "]", sep = "")
  })
}

shinyApp(ui, server)
