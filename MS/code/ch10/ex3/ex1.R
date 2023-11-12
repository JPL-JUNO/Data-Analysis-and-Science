# library(shiny)
#
# ui <- fluidPage(
#   selectInput("type", "type", c("slider", "numeric")),
#   uiOutput("numeric")
# )
#
# server <- function(input, output, session) {
#   output$numeric <- renderUI({
#     if (input$type == "slider") {
#       sliderInput("n", "n", value = 0, max = 100, min = 0)
#     } else {
#       numericInput("n", "n", value = 0, max = 100, min = 0)
#     }
#   })
# }
#
# shinyApp(ui, server)

library(shiny)

parameter_tags <- tagList(
  tags$style("#params { display:none; }"),
  tabsetPanel(
    id = "params",
    tabPanel(
      "slider",
      sliderInput("my_slider", "n", value = 0, min = 0, max = 100)
    ),
    tabPanel(
      "numeric",
      numericInput("my_numeric", "n", value = 0, min = 0, max = 100)
    )
  )
)

ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      selectInput("my_selector", "Input Type",
        choices = c("slider", "numeric")
      ),
      parameter_tags
    ),
    mainPanel()
  )
)

server <- function(input, output, session) {
  observeEvent(input$my_slider, {
    updateNumericInput(inputId = "my_numeric", value = isolate(input$my_slider))
  })

  observeEvent(input$my_numeric, {
    updateSliderInput(inputId = "my_slider", value = isolate(input$my_numeric))
  })

  observeEvent(input$my_selector, {
    updateTabsetPanel(inputId = "params", selected = input$my_selector)
  })
}

shinyApp(ui, server)
