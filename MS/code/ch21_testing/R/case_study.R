library(shiny)

ui <- fluidPage(
  radioButtons("fruit", "What's your favourite fruit?",
    choiceNames = list(
      "apple",
      "pear",
      textInput("other", label = NULL, placeholder = "Other")
    ),
    choiceValues = c("apple", "pear", "other")
  ),
  textOutput("value")
)

server <- function(input, output, session) {
  observeEvent(input$other, ignoreInit = TRUE, {
    updateRadioButtons(session, "fruit", selected = "other")
  })
  output$value <- renderText({
    if (input$fruit == "other") {
      req(input$other)
      input$other
    } else {
      input$fruit
    }
  })
}

shinyApp(ui, server)
