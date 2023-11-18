library(shiny)

ui <- fluidPage(
  actionButton("drink", "Drink me"),
  actionButton("eat", "Eat me"),
  textOutput("notice")
)

server <- function(input, output, session) {
  r <- reactiveValues(notice = "")

  observeEvent(input$drink, {
    r$notice <- "You are no longer thirsty"
  })

  observeEvent(input$eat, {
    r$notice <- "You are no longer hungry"
  })

  output$notice <- renderText(r$notice)
}

shinyApp(ui, server)
