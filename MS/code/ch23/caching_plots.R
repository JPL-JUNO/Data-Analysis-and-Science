library(shiny)
library(tidyverse)

ui <- fluidPage(
  selectInput("x", "x", choices = names(diamonds), selected = "carat"),
  selectInput("y", "y", choices = names(diamonds), selected = "price"),
  plotOutput("diamonds")
)

server <- function(input, output, session) {
  output$diamonds <- renderPlot({
    ggplot(diamonds, aes(.data[[input$x]], .data[[input$y]])) +
      geom_point()
  }) |> bindCache(input$x, input$y)
}

shinyApp(ui, server)
