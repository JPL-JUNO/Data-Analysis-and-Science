library(shiny)

ui <- fluidPage(
  textInput("name", "What's your name?"),
  textOutput("greeting")
)

server2 <- function(input, output, server) {
  greeting <- reactive(paste0("Hello ", input$name))
  output$greeting <- renderText(greeting())

  # error
  # greeting <- paste0("Hello ", input$name)
  # output$greeting <- renderText(greeting)
}

shinyApp(ui, server2)
