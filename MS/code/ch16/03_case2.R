library(shiny)

ui <- fluidPage(
  actionButton("up", "+1"),
  actionButton("down", "-1"),
  textOutput("n")
)

server <- function(input, output, session) {
  r <- reactiveValues(n = 0)
  observeEvent(input$up, {
    r$n <- r$n + 1
  })
  observeEvent(input$down, {
    r$n <- r$n - 1
  })
  output$n <- renderText(r$n)
}

shinyApp(ui, server)
