library(shiny)

ui <- fluidPage(
  textInput("name", "What's your name?"),
  textOutput("greeting")
)

server1 <- function(input, output, server) {
  # input$greeting <- renderText(paste0("Hello ", name)) # error
  output$greeting <- renderText(paste0("Hello ", input$name))
}

shinyApp(ui, server1)
