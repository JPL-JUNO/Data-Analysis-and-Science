library(shiny)

ui <- fluidPage(
  textInput("name", "Name"),
  actionButton("add", "Add"),
  actionButton("del", "Delete"),
  textOutput("names")
)

server <- function(input, output, session) {
  r <- reactiveValues(names = character())
  observeEvent(input$add, {
    r$names <- c(input$name, r$names)
    updateTextInput(session, "name", value = "")
  })

  observeEvent(input$del, {
    r$names <- setdiff(r$names, input$name)
    updateTextInput(session, "name", value = "")
  })
  output$names <- renderText(r$names)
}

shinyApp(ui, server)
