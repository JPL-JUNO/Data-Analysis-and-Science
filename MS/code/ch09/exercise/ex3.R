library(shiny)
library(ggplot2)
ui <- fluidPage(
  tagList(
    br(), br(),
    column(
      4,
      wellPanel(
        fileInput("file", "Upload CSV", accept = ".csv"),
        selectInput("variable", "Select Variable", choices = NULL)
      ),
      wellPanel(
        radioButtons("extension", "Save As:",
          choices = c("png", "pdf", "svg"), inline = TRUE
        ),
        downloadButton("download", "Save Plot")
      )
    ),
    column(8, plotOutput("results"))
  )
)
server <- function(input, output, session) {
  data <- reactive({
    req(input$file)

    ext <- tools::file_ext(input$file$name)

    validate(need(ext == "csv", "Invalid file. Please upload a .csv file"))

    dataset <- vroom::vroom(input$file$datapath, delim = ",")

    validate(need(
      ncol(dplyr::select_if(dataset, is.numeric)) != 0,
      "This dataset has no numeric columns."
    ))

    dataset
  })

  observeEvent(input$file, {
    req(data())
    num_cols <- dplyr::select_if(data(), is.numeric)
    updateSelectInput(session, "variable", choices = colnames(num_cols))
  })

  plot_output <- reactive({
    req(!is.null(input$variable))

    ggplot(data()) +
      aes_string(x = input$variable) +
      geom_histogram()
  })

  output$results <- renderPlot(plot_output())

  output$download <- downloadHandler(
    filename = function() {
      paste("histogram", input$extension, sep = ".")
    },
    content = function(file) {
      ggsave(file, plot_output(), device = input$extension)
    }
  )
}


shinyApp(ui, server)
