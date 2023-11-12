library(shiny)
library(ggplot2)
choices <- c("histogram", "freqpoly", "density")

geom_choice_code <- function(geom_choice) {
  if (geom_choice == "density") {
    return(paste0(
      "geom_density(
      color='blue',
      bw = input$density_bw,
      aes(y=..density..*(nrow(diamonds)*input$histogram_bw)))"
    ))
  }

  return(paste0(
    "geom_", geom_choice, "(",
    ifelse(geom_choice == "histogram", "fill = 'transparent', color = 'red', ", ""),
    "binwidth = input$", geom_choice, "_bw)"
  ))
}

ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      selectInput("geom", "Geom function to use",
        multiple = TRUE,
        choices = choices
      ),
      tabsetPanel(
        id = "histogram",
        type = "hidden",
        tabPanelBody("histogram_empty", style = "display: none"),
        tabPanelBody(
          "histogram_params",
          numericInput("histogram_bw",
            "Histogram's binwidth",
            value = .15,
            min = .1, max = 5, step = .1
          )
        )
      ),
      tabsetPanel(
        id = "freqpoly",
        type = "hidden",
        tabPanelBody("freqpoly_empty", style = "display: none"),
        tabPanelBody(
          "freqpoly_params",
          numericInput("freqpoly_bw",
            "Freqpoly's binwidth",
            value = .15,
            min = .1, max = 5, step = .1
          )
        )
      ),
      tabsetPanel(
        id = "density",
        type = "hidden",
        tabPanelBody("density_empty", style = "display: none"),
        tabPanelBody(
          "density_params",
          numericInput("density_bw",
            "Standard deviation of smoothing kernel",
            value = .15,
            min = .01, max = 1, step = .01
          )
        )
      ),
    ),
    mainPanel(
      plotOutput("gg")
    )
  )
)

server <- function(input, output, session) {
  observeEvent(input$geom,
    {
      non_selected <- setdiff(choices, input$geom)
      purrr::map(
        choices,
        ~ updateTabsetPanel(
          inputId = .x,
          selected = paste0(
            .x, ifelse(.x %in% non_selected, "_empty", "_params")
          )
        )
      )
    },
    ignoreNULL = FALSE
  )

  gg_args <- reactive({
    req(input$geom)

    purrr::map_chr(input$geom, geom_choice_code) |>
      paste0(collapse = " + ")
  })

  output$gg <- renderPlot({
    eval(parse(text = paste0(
      "ggplot(diamonds, aes(carat)) + ",
      gg_args(), " + ",
      "labs(y = 'Count')"
    )))
  })
}

shinyApp(ui, server)
