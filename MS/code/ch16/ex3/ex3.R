library(shiny)

ui <- fluidPage(
  selectInput("type", "Type", c("Normal", "Uniform")),
  actionButton("go", "Go"),
  plotOutput("plot")
)

server <- function(input, output, session) {
  r <- reactive({
    if (input$type == "Normal") {
      rnorm(100)
    } else if (input$type == "Uniform") {
      runif(100)
    }
  })

  output$plot <- renderPlot({
    req(input$go)
    hist(r())
  })
}

shinyApp(ui, server)
