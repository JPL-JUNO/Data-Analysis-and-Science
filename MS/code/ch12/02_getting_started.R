library(shiny)
library(dplyr)
library(ggplot2)

min <- 1
diamonds |> filter(carat > min)

var <- "carat"
diamonds[diamonds[[var]] > min, ]


# 在数据屏蔽函数内部，
# 您可以使用 .data 或者 .env
# 如果您想明确您正在谈论的是数据变量还是环境变量：
diamonds |>
  filter(.data$carat > .env$min)

num_vars <- c("carat", "depth", "table", "price", "x", "y", "z")
ui <- fluidPage(
  selectInput("var", "Variable", choices = num_vars),
  numericInput("min", "Minimum", value = 1),
  tableOutput("output")
)

server <- function(input, output, session) {
  data <- reactive(
    diamonds |> filter(.data[[input$var]] > .env$input$min)
  )

  output$output <- renderTable(head(data()))
}

shinyApp(ui, server)
