library(shiny)

ui <- fluidPage(
  
)

server <- function(input, output, session) {
  data <- reactive({
    id <- showNotification("Reading data...",
                           duration = NULL,
                           closeButton = FALSE)
    on.exit(removeNotification(id), add = TRUE)
  })
}

shinyApp(ui, server)