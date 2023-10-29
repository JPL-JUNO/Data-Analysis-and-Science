library(shiny)
library(ggplot2)
source("./code/ch03/funcs.R")

ui <- fluidPage(
  fluidRow(
    column(
      4,
      "Distribution 1",
      numericInput("n1", label = "n", value = 1000, min = 1),
      numericInput("mean1", label = "μ", value = 0, step = .1),
      numericInput("sd1", label = "σ", value = .5, min = .1, step = .1),
    ),
    column(
      4,
      "Distribution 2",
      numericInput("n2", label = "n", value = 1000, min = 1),
      numericInput("mean2", label = "μ", value = 0, step = .1),
      numericInput("sd2", label = "σ", value = .5, min = .1, step = .1),
    ),
    column(
      4,
      "Frequency polygon",
      numericInput("binwidth", label = "Bin width", value = .1, step = .1),
      sliderInput("range", "range", value = c(-3, 3), min = -5, max = 5)
    )
  ),
  fluidRow(
    column(9, plotOutput("hist")),
    column(3, verbatimTextOutput("ttest"))
  )
)

server <- function(input, output, session) {
  x1 <- reactive(rnorm(input$n1, input$mean1, input$sd1))
  x2 <- reactive(rnorm(input$n2, input$mean2, input$sd2))
  output$hist <- renderPlot(
    {
      freqpoly(x1(), x2(), binwidth = input$binwidth, xlim = input$range)
    },
    res = 96
  )
  output$ttest <- renderText({
    t_test(x1(), x2())
  })
}

shinyApp(ui, server)
