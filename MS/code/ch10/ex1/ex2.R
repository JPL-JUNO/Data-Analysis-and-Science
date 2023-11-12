library(shiny)
library(openintro)
library(dplyr)

states <- unique(county$state)
ui <- fluidPage(
  selectInput("state", "State", choices = states),
  selectInput("county", "Country", choices = NULL)
)

server <- function(input, output, session) {
  observeEvent(input$state, {
    req(input$state)
    choices <- county |>
      filter(state == input$state) |>
      pull(name) |>
      unique()

    updateSelectInput(inputId = "county", choices = choices)
  })
}

shinyApp(ui, server)
