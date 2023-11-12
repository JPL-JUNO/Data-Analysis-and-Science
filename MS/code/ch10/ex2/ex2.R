library(shiny)
library(ggplot2)
choices <- c("histogram", "freqpoly", "density")
ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      selectInput("geom", "", choices = choices),
      tabsetPanel(
        id = "params",
        type = "hidden",
        tabPanel(
          "histogram",
          numericInput("hist_bw", "Binwidth",
            value = .1,
            min = .1, max = 5, step = .1
          )
        ),
        tabPanel(
          "freqpoly",
          numericInput("freq_bw", "Binwidth",
            value = .1,
            max = 5, min = .1, step = .1
          )
        ),
        tabPanel(
          "density",
          numericInput("density_bw", "Standard deviation of smoothing kernel",
            value = .01,
            max = 1, min = .01, step = .01
          )
        )
      )
    ),
    mainPanel(
      plotOutput("gg")
    )
  )
)

server <- function(input, output, session) {
  observeEvent(input$geom, {
    updateTabsetPanel(inputId = "params", selected = input$geom)
  })

  gg_args <- reactive({
    switch(input$geom,
      histogram = geom_histogram(binwidth = input$hist_bw),
      freqpoly = geom_freqpoly(binwidth = input$freq_bw),
      density = geom_density(bw = input$density_bw)
    )
  })

  output$gg <- renderPlot({
    ggplot(diamonds, aes(carat)) +
      gg_args()
  })
}

shinyApp(ui, server)
