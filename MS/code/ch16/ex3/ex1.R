library(shiny)

ui <- fluidPage(
  actionButton("rnorm", "Normal"),
  actionButton("runif", "Uniform"),
  plotOutput("plot")
)

server <- function(input, output, session) {
  r <- reactiveValues(random_data = vector(mode = "numeric", length = 100))
  observeEvent(input$rnorm, {
    r$random_data <- rnorm(100)
  })

  observeEvent(input$runif, {
    r$random_data <- runif(100)
  })

  output$plot <- renderPlot({
    req(input$rnorm | input$runif)
    hist(r$random_data)
  })
}

shinyApp(ui, server)
