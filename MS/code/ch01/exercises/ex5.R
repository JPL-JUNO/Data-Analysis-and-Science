library(shiny)
library(ggplot2)

datasets <- c("economics", "faithfuld", "seals")
ui <- fluidPage(
  selectInput("dataset", "Dataset", choices = datasets),
  verbatimTextOutput("summary"),
  plotOutput("plot") # 错误1，组件类型错误 plotOutput 而不是 tableOutput
)

server <- function(input, output, session) {
  dataset <- reactive({
    get(input$dataset, "package:ggplot2")
  })
  output$summary <- renderPrint({ # 错误2，拼写错误
    summary(dataset())
  })
  output$plot <- renderPlot(plot(dataset()), res = 96) # 错误3， 没有加 ()
}

shinyApp(ui, server)
