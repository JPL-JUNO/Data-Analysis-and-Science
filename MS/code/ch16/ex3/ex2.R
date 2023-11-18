library(shiny)

ui <- fluidPage(
  selectInput("type", "Type", c("Normal", "Uniform")),
  actionButton("go", "Go"),
  plotOutput("plot")
)

server <- function(input, output, session) {
  r <- reactiveValues(random_data = vector(mode = "numeric", length = 100))
  observeEvent(input$go, {
    if (input$type == "Normal") {
      r$random_data <- rnorm(100)
    } else {
      r$random_data <- runif(100)
    }
  })

  output$plot <- renderPlot({
    req(input$go)
    hist(r$random_data)
  })
}

shinyApp(ui, server)
