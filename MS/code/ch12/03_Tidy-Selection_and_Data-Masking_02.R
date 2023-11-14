library(shiny)
library(dplyr)

ui <- fluidPage(
  selectInput("vars_g", "Group by", names(mtcars), multiple = TRUE),
  selectInput("vars_s", "Summarise", names(mtcars), multiple = TRUE),
  tableOutput("data")
)

server <- function(input, output, session) {
  output$data <- renderTable({
    mtcars |> 
      group_by(across(all_of(input$vars_g))) |> 
      summarise(across(all_of(input$vars_s), mean), n = n())
  })
}

shinyApp(ui, server)
