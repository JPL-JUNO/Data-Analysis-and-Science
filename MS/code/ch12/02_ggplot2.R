library(shiny)
library(ggplot2)

ui <- fluidPage(
  selectInput("x", "X variable", choices = names(iris)),
  selectInput("y", "Y variable", choices = names(iris)),
  selectInput("geom", "Geom", c("point", "smooth", "jitter")),
  plotOutput("plot")
)

server <- function(input, output, session) {
  plot_geom <- reactive({
    switch(input$geom,
      point = geom_point(),
      smooth = geom_smooth(se = FALSE),
      jitter = geom_jitter()
    )
  })
  output$plot <- renderPlot(
    {
      ggplot(iris, aes(.data[[input$x]], .data[[input$y]])) +
        # ggforce::position_auto()
        # 这样的方法，geom_point() 无论 x 和 y 变量是连续的还是离散的，
        # 它都能很好地工作。
        # geom_point(position = ggforce::position_auto())
        plot_geom()
    },
    res = 96
  )
}

shinyApp(ui, server)
