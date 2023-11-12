library(shiny)

ui <- fluidPage(
  numericInput("year", "year", value = 2020),
  dateInput("date", "date")
)

server <- function(input, output, session) {
  observeEvent(input$year, {
    req(input$year)
    date_range <- range(
      as.Date(paste0(input$year, "-01-01")),
      as.Date(paste0(input$year, "-12-31"))
    )
    updateDateInput(
      inputId = "date",
      min = date_range[1],
      max = date_range[2]
    )
  })
}

shinyApp(ui, server)
