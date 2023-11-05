library(shiny)

ui <- fluidPage(
  waiter::use_waitress(),
  numericInput("steps", "How many steps?", 10),
  actionButton("go", "go"),
  textOutput("result")
)

server <- function(input, output, session) {
  data <- eventReactive(input$go, {
    waitress <- waiter::Waitress$new(max = input$steps)
    on.exit(waitress$close())

    for (i in seq_len(input$steps)) {
      Sys.sleep(.5)
      waitress$inc(1)
    }

    runif(1)
  })

  output$result <- renderText(round(data(), 2))
}

shinyApp(ui, server)
