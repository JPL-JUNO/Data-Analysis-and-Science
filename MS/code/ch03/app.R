library(shiny)
freqpoly <- function(x1, x2, binwidth = .1, xlim = c(-3, 3)) {
  df <- data.frame(
    x = c(x1, x2),
    g = c(rep("x1", length(x1)), rep("x2", length(x2)))
  )
  # print(x1[0:10])
  # 为了验证画图和计算 t 统计量的确实不是一个x1, x2
  ggplot(df, aes(x, color=g))+
    geom_freqpoly(binwidth=binwidth, linewidth=1)+
    coord_cartesian(xlim=xlim)
}

t_test <- function(x1, x2){
  test <- t.test(x1, x2)
  # print(x1[0:10])
  sprintf(
    "p value: %0.3f\n[%0.2f, %0.2f]",
    test$p.value, test$conf.int[1], test$conf.int[2]
  )
}

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
  )),
  fluidRow(
    column(9, plotOutput("hist")),
    column(3, verbatimTextOutput("ttest"))
  )
)

server <- function(input, output, session) {
  output$hist<-renderPlot({
    x1 <- rnorm(input$n1, input$mean1, input$sd1)
    x2 <- rnorm(input$n2, input$mean2, input$sd2)
    freqpoly(x1, x2, binwidth = input$binwidth, xlim=input$range)
  }, res=96)
  output$ttest<- renderText({
    x1 <- rnorm(input$n1, input$mean1, input$sd1)
    x2 <- rnorm(input$n2, input$mean2, input$sd2)
    t_test(x1, x2)
  })
}

shinyApp(ui, server)
