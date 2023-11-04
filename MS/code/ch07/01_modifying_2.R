library(shiny)
library(ggplot2)

ui <- fluidPage(
  plotOutput("plot", brush = "plot_brush", dblclick = "plot_reset")
)

server <- function(input, output, session) {
  selected <- reactiveVal(rep(FALSE, nrow(mtcars)))

  observeEvent(input$plot_brush, {
    brushed <- brushedPoints(mtcars, input$plot_brush, allRows = TRUE)$selected_
    # 用传递的值更新 selected()
    # 这是 reactiveVal() 与 reactive 的不同之处
    selected(brushed | selected())
  })

  observeEvent(input$plot_reset, {
    selected(rep(FALSE, nrow(mtcars)))
  })

  output$plot <- renderPlot(
    {
      mtcars$sel <- selected()
      ggplot(mtcars, aes(wt, mpg)) +
        geom_point(aes(color = sel)) +
        # 设置比例限制，以确保图例（和颜色）在第一次单击后不会改变。
        scale_color_discrete(limits = c("TRUE", "FALSE"))
    },
    res = 96
  )
}

shinyApp(ui, server)
