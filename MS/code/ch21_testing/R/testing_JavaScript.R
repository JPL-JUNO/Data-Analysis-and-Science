library(shiny)

ui <- fluidPage(
  textInput("name", "What's your name"),
  textOutput("greeting"),
  actionButton("reset", "Reset")
)

server <- function(input, output, session) {
  output$greeting <- renderText({
    req(input$name)
    paste0("Hi ", input$name)
  })

  observeEvent(input$reset, updateTextInput(session, inputId = "name", value = ""))
}

app <- shinytest::ShinyDriver$new(shinyApp(ui, server))
app$setInputs(name = "Stephen")
app$getValue("greeting")
app$click("reset")
app$getValue("greeting")
