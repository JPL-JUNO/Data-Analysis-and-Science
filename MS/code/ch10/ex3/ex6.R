library(shiny)
library(readr)

make_dropdown <- function(name_of_vector) {
  selectInput(
    inputId = name_of_vector, name_of_vector,
    choices = c("numeric", "character", "logical")
  )
}
ui <- fluidPage(
  tags$style("#wizard { display:none; }"),
  tabsetPanel(
    id = "wizard",
    tabPanel(
      "page1",
      fileInput("data_input", "input"),
      actionButton("page12", "next")
    ),
    tabPanel(
      "page2",
      sidebarLayout(
        sidebarPanel(
          uiOutput("type_of")
        ),
        mainPanel(
          tableOutput("type_table")
        ),
      ),
      actionButton("page21", "prev"),
      actionButton("page23", "next")
    ),
    tabPanel(
      "page3",
      tableOutput("summary_table"),
      actionButton("page32", "prev")
    )
  ),
)

server <- function(input, output, session) {
  switch_page <- function(page) {
    updateTabsetPanel(session, inputId = "wizard", selected = page)
  }

  observeEvent(input$page12, switch_page("page2"))
  observeEvent(input$page21, switch_page("page1"))
  observeEvent(input$page23, switch_page("page3"))
  observeEvent(input$page32, switch_page("page2"))

  data <- reactive({
    req(input$data_input)
    read.csv(input$data_input$datapath)
  })

  output$type_of <- renderUI({
    map(names(data()), ~ make_dropdown(.x))
  })

  change_type <- function(vector, name_of_vector) {
    switch(input[[name_of_vector]],
      "numeric" = vector <- as.numeric(vector),
      "character" = vector <- as.character(vector),
      "logical" = vector <- as.complex(vector)
    )
  }

  df <- reactive({
    data() |>
      as.list() |>
      imap(change_type) |>
      as_tibble()
  })
  output$type_table <- renderTable(data.frame(
    names = names(df()),
    type = map_chr(df(), function(x) typeof(x))
  ))

  output$summary_table <- renderTable(summary(df()))
}

shinyApp(ui, server)
