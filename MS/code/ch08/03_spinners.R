library(shiny)

ui <- fluidPage(
  waiter::use_waiter(),
  numericInput("steps", "How many steps?", 10),
  actionButton("go", "go"),
  textOutput("result")
)

server <- function(input, output, session) {
  data <- eventReactive(input$go, {
    waiter <- waiter::Waiter$new()
    waiter$show()
    on.exit(waiter$hide())

    Sys.sleep(sample(5, 1))

    runif(1)
  })

  output$result <- renderText(round(data(), 2))
}

ui_simple <- fluidPage(
  waiter::use_waiter(),
  actionButton("go", "run"),
  plotOutput("plot")
)
server_simple <- function(input, output, session) {
  data <- eventReactive(input$go, {
    waiter::Waiter$new(id = "plot")$show()

    Sys.sleep(3)

    data.frame(x = runif(50), y = runif(50))
  })

  output$plot <- renderPlot(plot(data()), res = 96)
}

# shinyApp(ui, server)
shinyApp(ui_simple, server_simple)
