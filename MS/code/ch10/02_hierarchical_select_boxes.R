library(shiny)
library(dplyr, warn.conflicts = FALSE)
sales <- vroom::vroom(
  "sales_data_sample.csv",
  col_types = list(),
  na = ""
)
ui <- fluidPage(
  selectInput("territory", "Territory",
    choices = unique(sales$TERRITORY)
  ),
  selectInput("customername", "Customer",
    choices = NULL
  ),
  selectInput("ordernumber", "Order Number",
    choices = NULL
  ),
  tableOutput("data")
)

server <- function(input, output, session) {
  territory <- reactive({
    sales |> filter(TERRITORY == input$territory)
  })
  observeEvent(territory(), {
    choices <- unique(territory()$CUSTOMERNAME)
    updateSelectInput(inputId = "customername", choices = choices)
  })

  customer <- reactive({
    req(input$customername)
    territory() |>
      filter(CUSTOMERNAME == input$customername)
  })

  observeEvent(customer(), {
    choices <- unique(customer()$ORDERNUMBER)
    updateSelectInput(inputId = "ordernumber", choices = choices)
  })

  output$data <- renderTable({
    req(input$ordernumber)
    customer() |>
      filter(ORDERNUMBER == input$ordernumber) |>
      select(QUANTITYORDERED, PRICEEACH, PRODUCTCODE)
  })
}

shinyApp(ui, server)
