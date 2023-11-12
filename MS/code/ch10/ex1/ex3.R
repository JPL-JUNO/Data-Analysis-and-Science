library(shiny)
library(gapminder)
library(dplyr)
continents <- unique(gapminder$continent)
ui <- fluidPage(
  selectInput("continent", "Continent", choices = continents),
  selectInput("country", "Country", choices = NULL),
  tableOutput("data")
)

server <- function(input, output, session) {
  observeEvent(input$continent, {
    req(input$continent)
    choices <- gapminder |>
      filter(continent == input$continent) |>
      pull(country) |>
      unique()

    updateSelectInput(inputId = "country", choices = choices)
  })

  output$data <- renderTable({
    gapminder |>
      filter(
        continent == input$continent,
        country == input$country
      )
  })
}

shinyApp(ui, server)
