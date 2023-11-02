library(shiny)

ui <- fluidPage(
  fluidPage(
    titlePanel("Central Limit Theorem"),
    sidebarLayout(
      sidebarPanel(
        numericInput("m", "Number of samples:", 2, min=1, max = 100)
      ),
      mainPanel(
        plotOutput("hist")
      )
    )
  )
)

server <- function(input, output, session) {
  output$hist <- renderPlot({
    means <- replicate(1e4, mean(runif(input$m)))
    hist(means, breaks=20)
  }, res = 96)
}

shinyApp(ui, server)