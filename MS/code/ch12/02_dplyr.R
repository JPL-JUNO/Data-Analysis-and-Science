library(shiny)
library(dplyr)

ui <- fluidPage(
  selectInput("var", "Select variable", choices = names(mtcars)),
  sliderInput("min", "Minimum value", 0, min = 0, max = 100),
  selectInput("sort", "Sort by", choices = names(mtcars)),
  tableOutput("data")
)

server <- function(input, output, session) {
  observeEvent(input$var, {
    rng <- range(mtcars[[input$var]])
    updateSliderInput(
      inputId = "min",
      value = rng[[1]],
      min = rng[[1]],
      max = rng[[2]]
    )
  })

  output$data <- renderTable({
    mtcars |>
      filter(.data[[input$var]] > input$min) |>
      arrange(.data[[input$sort]])
  })
}

ui_sorted <- fluidPage(
  selectInput("var", "Sort by", choices = names(mtcars)),
  checkboxInput("desc", "Descending order?"),
  tableOutput("data")
)
server_sorted <- function(input, output, session) {
  sorted <- reactive({
    if (input$desc) {
      arrange(mtcars, desc(.data[[input$var]]))
    } else {
      arrange(mtcars, .data[[input$var]])
    }
  })

  output$data <- renderTable(sorted())
}
shinyApp(ui_sorted, server_sorted)
