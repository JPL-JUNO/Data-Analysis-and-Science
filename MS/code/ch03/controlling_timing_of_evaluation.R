library(ggplot2)
library(shiny)
ui <- fluidPage(
  fluidRow(
    column(
      3,
      numericInput("lambda1", "lambda1", value = 3, min = 0),
      numericInput("lambda2", "lambda2", value = 5, min = 0),
      numericInput("n", "n", value = 1e4, min = 0)
    ),
    column(9, plotOutput("hist"))
  )
)

server <- function(input, output, session) {
  x1 <- reactive(rpois(input$n, input$lambda1))
  x2 <- reactive(rpois(input$n, input$lambda2))

  output$hist <- renderPlot(
    {
      freqpoly(x1(), x2(), binwidth = 1, xlim = c(0, 40))
    },
    res = 96
  )
}

server1 <- function(input, output, session) {
  timer <- reactiveTimer(500)

  x1 <- reactive({
    timer()
    rpois(input$n, input$lambda1)
  })
  x2 <- reactive({
    timer()
    rpois(input$n, input$lambda2)
  })

  output$hist <- renderPlot(
    {
      freqpoly(x1(), x2(), binwidth = 1, xlim = c(0, 40))
    },
    res = 96
  )
}

on_click_ui <- fluidPage(
  fluidRow(
    column(
      3,
      numericInput("lambda1", "lambda1", value = 3, min = 0),
      numericInput("lambda2", "lambda2", value = 5, min = 0),
      numericInput("n", "n", value = 1e4, min = 0),
      actionButton("simulate", "Simulate!")
    ),
    column(9, plotOutput("hist"))
  )
)
on_click_server1 <- function(input, output, session) {
  # 这个问题在于不仅仅点击这个动作会改变 x1 和 x2
  # 而且在修改 lambda1, lambda2, n 的时候也会改变 hist，即使还没有点击模拟
  x1 <- reactive({
    input$simulate
    rpois(input$n, input$lambda1)
  })
  x2 <- reactive({
    input$simulate
    rpois(input$n, input$lambda2)
  })

  output$hist <- renderPlot({
    freqpoly(x1(), x2(), binwidth = 1, xlim = c(0, 40))
  })
}

on_click_server <- function(input, output, session) {
  x1 <- eventReactive(
    input$simulate,
    {
      rpois(input$n, input$lambda1)
    }
  )
  x2 <- eventReactive(
    input$simulate,
    {
      rpois(input$n, input$lambda2)
    }
  )
  output$hist <- renderPlot(
    {
      freqpoly(x1(), x2(), binwidth = 1, xlim = c(0, 40))
    },
    res = 96
  )
}
shinyApp(ui, server)
shinyApp(ui, server1)

shinyApp(on_click_ui, on_click_server1)
shinyApp(on_click_ui, on_click_server)
