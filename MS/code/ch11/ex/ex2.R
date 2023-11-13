library(shiny)

ui <- function(request) {
  fluidPage(
    sidebarLayout(
      sidebarPanel(
        bookmarkButton(),
        fileInput("file", "Choose CSV file", multiple = TRUE, accept = ".csv")
      ),
      mainPanel(
        tableOutput("contents")
      )
    )
  )
}

server <- function(input, output, session) {
  data <- reactive({
    req(input$file)
    read.csv(input$file$datapath)
  })

  output$contents <- renderTable(head(data()))

  onBookmark(function(state) {
    state$values$data <- data()
  })

  onRestore(function(state) {
    data <- reactive(state$values$data)
  })

  enableBookmarking(store = "server")
}

shinyApp(ui, server)
