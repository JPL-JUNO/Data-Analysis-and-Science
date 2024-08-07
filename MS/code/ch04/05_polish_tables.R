################################################################
# File         : 05_polish_tables
# Author(s)    : Stephen CUI
# LastEditor(s): Stephen CUI
# CreatedTime  : 2023-11-01 23:03:23
# Description  :
################################################################
library(shiny)
library(vroom)
library(tidyverse)

# 对表格进行一些润色

injuries <- vroom::vroom("neiss/injuries.tsv.gz")
products <- vroom::vroom("neiss/products.tsv")
population <- vroom::vroom("neiss/population.tsv")

# injuries |>
#   mutate(diag = fct_lump(fct_infreq(diag), n = 5)) |>
#   group_by(diag) |>
#   summarise(n = as.integer(sum(weight)))
# 转为下面的函数

count_top <- function(df, var, n = 5) {
  df |>
    mutate({{ var }} := fct_lump(fct_infreq({{ var }}), n = n)) |>
    group_by({{ var }}) |>
    summarise(n = as.integer(sum(weight)))
}


prod_codes <- setNames(products$prod_code, products$title)
ui <- fluidPage(
  fluidRow(
    column(
      6,
      selectInput("code",
        "Product",
        choices = prod_codes
      )
    )
  ),
  fluidRow(
    column(
      4,
      tableOutput("diag")
    ),
    column(
      4,
      tableOutput("body_part")
    ),
    column(
      4,
      tableOutput("location")
    ),
  ),
  fluidRow(
    column(12, plotOutput("age_sex"))
  )
)

server <- function(input, output, session) {
  selected <- reactive(injuries |> filter(prod_code == input$code))

  output$diag <- renderTable(
    count_top(selected(), diag),
    width = "100%"
  )
  output$body_part <- renderTable(
    count_top(selected(), body_part),
    width = "100%"
  )
  # width 强制所有表格占据最大宽度（即填充它们出现的列）。这使得输出更加美观，因为它减少了偶然变化的量。
  output$location <- renderTable(
    count_top(selected(), location),
    width = "100%"
  )

  summary <- reactive({
    selected() |>
      count(age, sex, wt = weight) |>
      left_join(population, by = c("age", "sex")) |>
      mutate(rate = n / population * 1e4)
  })

  output$age_sex <- renderPlot(
    {
      summary() |>
        ggplot(aes(age, n, color = sex)) +
        geom_line() +
        labs(y = "Estimated number of 10,000")
    },
    res = 96
  )
}

shinyApp(ui, server)
