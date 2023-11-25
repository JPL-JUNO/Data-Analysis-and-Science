library(shiny)
library(memoise)

r <- reactive(slow_function(input$x, input$y)) |> 
  bindCache(input$x, input$y)

output$text <- renderText(slow_function2(input$z)) |> 
  bindCache(input$z)