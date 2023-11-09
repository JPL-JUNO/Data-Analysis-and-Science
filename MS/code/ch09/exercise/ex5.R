library(shiny)
ui_load <- sidebarLayout(
  sidebarPanel(
    fileInput("file", "Data", buttonLabel = "Upload,,,"),
    textInput("delim", "Delimiter (leave blank to guess)", ""),
    numericInput("skip", "Rows to skip", 0, min = 0),
    numericInput("rows", "Rows to preview", 10, min = 1),
  ),
  mainPanel(
    h3("Raw data"),
    tableOutput("preview1")
  )
)

ui_clean <- sidebarLayout(
  sidebarPanel(
    checkboxInput("snake", "Rename columns to snake case?"),
    checkboxInput("constant", "Rename constant columns?"),
    checkboxInput("empty", "Rename empty cols?"),
  ),
  mainPanel(
    h3("Cleaner data"),
    tableOutput("preview2")
  )
)

ui_download <- fluidRow(
  column(width = 12, downloadButton("download", class = "btn-block"))
)
ui <- fluidPage(
  ui_load,
  ui_clean,
  ui_download
)

server <- function(input, output, session) {
  raw <- reactive({
    req(input$file)
    delim <- if (input$delim == "") NULL else input$delim

    vroom::vroom(input$file$datapath, delim = delim, skip = input$skip)
  })

  output$preview1 <- renderTable(head(raw(), input$rows))

  cleaned_names <- reactive({
    out <- raw()
    if (input$snake) {
      names(out) <- janitor::make_clean_names(names(out))
    }

    out
  })

  removed_empty <- reactive({
    out <- cleaned_names()
    if (input$empty) {
      out <- janitor::remove_empty(out, "cols")
    }
    out
  })

  removed_constant <- reactive({
    out <- removed_empty()
    if (input$constant) {
      out <- janitor::remove_constant(out)
    }

    out
  })

  output$preview2 <- renderTable(head(removed_constant(), input$rows))

  output$download <- downloadHandler(
    filename = function() {
      paste0(tools::file_path_sans_ext(input$file$name), ".tsv")
    },
    content = function(file) {
      vroom::vroom_write(removed_constant(), file)
    }
  )
}

shinyApp(ui, server)
