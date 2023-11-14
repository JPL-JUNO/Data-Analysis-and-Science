library(shiny)
library(dplyr, warn.conflicts = FALSE)
library(ggplot2)

num_vars <- c("carat", "depth", "table", "price", "x", "y", "z")

ui <- fluidPage(
  selectInput("var", "Variable", choices = num_vars),
  numericInput("min", "Minimum", value = 1),
  tableOutput("output")
)

server <- function(input, output, session) {
  data <- reactive({
    # 没有起作用，
    # 这是一个间接问题：
    # 通常在使用 tidyverse 函数时，
    # 您直接在函数调用中键入变量的名称。但现在您想间接引用它：
    # 变量 ( carat) 存储在另一个变量 ( input$var) 内。
    diamonds |> filter(input$var > input$min)
  })

  output$output <- renderTable(head(data()))
}

shinyApp(ui, server)
