histogramUI <- function(id){
  # tagList()，这是一种特殊类型的布局函数，
  # 它允许您将多个组件捆绑在一起，
  # 而无需实际暗示它们将如何布局。
  tagList(
    selectInput(NS(id, "var"), "Variable", choices = names(mtcars)),
    numericInput(NS(id, "bins"), "Bins", value = 10, min = 1),
    plotOutput(NS(id, "hist"))
  )
}

histogramServer <- function(id){
  moduleServer(id, function(input, output, session){
    data <- reactive(mtcars[[input$var]])
    output$hist <- renderPlot({
      hist(data(), breaks = input$bins, main = input$var)
    }, res = 96)
  })
}

histogramApp <- function(){
  ui <- fluidPage(
    histogramUI("hist1")
  )
  
  server <- function(input, output, session){
    histogramServer("hist1")
  }
  
  shinyApp(ui, server)
}
