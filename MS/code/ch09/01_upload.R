library(shiny)

ui <- fluidPage(
  # 使用 multiple = TRUE 来允许用户上传多个文件。
  fileInput("upload", NULL, buttonLabel = "Upload...", multiple = TRUE),
  tableOutput("files")
)

server <- function(input, output, session) {
  output$files <- renderTable(input$upload)
}

shinyApp(ui, server)
