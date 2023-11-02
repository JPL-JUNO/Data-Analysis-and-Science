library(shiny)
sales <- readr::read_csv("../data/sales_data_sample.csv")
sales <- sales[c(
  "TERRITORY", "ORDERDATE", "ORDERNUMBER", "PRODUCTCODE",
  "QUANTITYORDERED", "PRICEEACH"
)]

# 注意这里，北美的表示为 NA，但是这个值在 R 中表示缺失值
unique(sales$TERRITORY)

ui <- fluidPage(
  selectInput("territory", "terrority", choices = unique(sales$TERRITORY)),
  tableOutput("selected")
)

server <- function(input, output, session) {
  selected <- reactive(sales[sales$TERRITORY == input$territory, ])
  output$selected <- renderTable(head(selected(), 10))
}

shinyApp(ui, server)