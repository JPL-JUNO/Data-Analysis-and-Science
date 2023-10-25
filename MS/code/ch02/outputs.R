library(shiny)
ui <- fluidPage(
  textOutput("text"),
  verbatimTextOutput("code"),
  tableOutput("static"),
  dataTableOutput("dynamic"),

  # 图片
  plotOutput("plot", width = "400px")
)

server <- function(input, output, session) {
  output$text <- renderText({
    "Hello friend!"
  })
  # 单行的渲染函数可以不写在 {} 中
  output$code <- renderPrint(
    summary(1:10)
  )

  # 表格
  output$static <- renderTable(head(mtcars))
  output$dynamic <- renderDataTable(mtcars, options = list(pageLength = 5))

  output$plot <- renderPlot(plot(1:5), res = 96)
}

shinyApp(ui, server)
