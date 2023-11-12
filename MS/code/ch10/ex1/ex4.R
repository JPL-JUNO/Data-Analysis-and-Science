library(shiny)
library(gapminder)
library(dplyr)
continents <- unique(gapminder$continent)
ui <- fluidPage(
  selectInput("continent", "Continent",
    choices = c(as.character(continents), "(ALL)")
  ),
  selectInput("country", "Country", choices = NULL),
  tableOutput("data")
)

server <- function(input, output, session) {
  observeEvent(input$continent, {
    req(input$continent)

    if (input$continent == "(ALL)") {
      choices <- gapminder |>
        pull(country) |>
        unique()
    } else {
      choices <- gapminder |>
        filter(continent == input$continent) |>
        pull(country) |>
        unique()
    }

    updateSelectInput(inputId = "country", choices = choices)
  })

  output$data <- renderTable({
    if (input$continent == "(ALL)") {
      gapminder |>
        filter(
          country == input$country
        )
    } else {
      gapminder |>
        filter(
          continent == input$continent,
          country == input$country
        )
    }
  })
}

shinyApp(ui, server)
