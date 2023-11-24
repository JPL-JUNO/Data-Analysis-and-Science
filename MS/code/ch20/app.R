library(shiny)
stones <- vroom::vroom("birthstones.csv")

ui <- navbarPage(
  "Sample app",
  tabPanel(
    "Pick a month",
    selectInput("month", "What's your favourite month?", choices = months)
  ),
  tabPanel("Feedback", monthFeedbackUI("tab1")),
  tabPanel("Birthstone", birthstoneUI("tab2"))
)

server <- function(input, output, session) {
  monthFeedBackServer("tab1", reactive(input$month))
  birthstoneServer("tab2", reactive(input$month))
}

shinyApp(ui, server)