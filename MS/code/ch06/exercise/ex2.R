library(shiny)

ui <- fluidPage(
  titlePanel("Central Limit Theorem"),
  sidebarLayout(
    sidebarPanel(
      numericInput("m", "Number of samples:", 2, min = 1, max = 100)
    ),
    mainPanel(
      plotOutput("hist")
    ),
    # q2
    position = "right"
  ),
  fluidRow(
    column(
      4,
      numericInput("m_ex", "Number of samples:", 2, min = 1, max = 100, width = "100%")
    ),
    column(
      8,
      plotOutput("hist_ex")
    )
  ),
  fluidRow(
    column(
      6,
      plotOutput("hist_ex3_1")
    ),
    column(
      6,
      plotOutput("hist_ex3_2")
    )
  ),
  fluidRow(
    column(
      12,
      numericInput("ex3", 
                   "每个绘图占据一半的宽度，将控件放在绘图下方的全宽容器中", 
                   2,width="100%")
    )
  )
)

server <- function(input, output, session) {
  output$hist <- renderPlot(
    {
      means <- replicate(1e4, mean(runif(input$m)))
      hist(means, breaks = 20)
    },
    res = 96
  )
  output$hist_ex3_2 <- renderPlot(
    {
      means <- replicate(1e4, mean(runif(input$m_ex)))
      hist(means, breaks = 20)
    },
    res = 96
  )
  output$hist_ex3_1 <- renderPlot(
    {
      means <- replicate(1e4, mean(runif(input$m_ex)))
      hist(means, breaks = 20)
    },
    res = 96
  )
  output$hist_ex <- renderPlot(
    {
      means <- replicate(1e4, mean(runif(input$m_ex)))
      hist(means, breaks = 20)
    },
    res = 96
  )
}

shinyApp(ui, server)
