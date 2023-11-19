# File         : 04_case_study
# Author(s)    : Stephen CUI
# LastEditor(s): Stephen CUI
# CreatedTime  : 2023-11-18 17:05:58
# Description  :
library(shiny)

next_page <- function(id, i) {
  actionButton(NS(id, paste0("go_", i, "_", i + 1)), "next")
}

prev_page <- function(id, i) {
  actionButton(NS(id, paste0("go_", i, "_", i - 1)), "prev")
}

wrap_page <- function(title, page,
                      button_left = NULL,
                      button_right = NULL) {
  tabPanel(
    title = title,
    fluidRow(
      column(12, page)
    ),
    fluidRow(
      column(6, button_left),
      column(6, button_right)
    )
  )
}


wizard_ui <- function(id, pages, done_button = NULL) {
  stopifnot(is.list(pages))
  n <- length(pages)

  wrapped <- vector("list", n)
  for (i in seq_along(pages)) {
    lhs <- if (i > 1) prev_page(id, i)
    rhs <- if (i < n) next_page(id, i) else done_button
    wrapped[[i]] <- wrap_page(paste0("page_", i), pages[[i]], lhs, rhs)
  }

  wrapped$id <- NS(id, "wizard")
  wrapped$type <- "hidden"
  do.call("tabsetPanel", wrapped)
}

wizard_server <- function(id, n) {
  moduleServer(id, function(input, output, session) {
    change_page <- function(from, to) {
      observeEvent(input[[paste0("go_", from, "_", to)]], {
        updateTabsetPanel(session, "wizard", selected = paste0("page_", to))
      })
    }

    ids <- seq_along(n)
    lapply(ids[-1], function(i) change_page(i, i - 1))
    lapply(ids[-n], function(i) change_page(i, i + 1))
  })
}


wizard_app <- function(...) {
  page1 <- tagList(
    textInput("name", "What's your name?")
  )
  page2 <- tagList(
    numericInput("age", "How old are you?", 20)
  )
  page3 <- tagList(
    "Is this data correct?",
    verbatimTextOutput("info")
  )

  ui <- fluidPage(
    wizard_ui(
      id = "demographics",
      pages = list(page1, page2, page3),
      done_button = actionButton("done", "Submit")
    )
  )
  server <- function(input, output, session) {
    wizard_server("demographics", 3)

    observeEvent(input$done, showModal(
      modalDialog("Thank you!", footer = NULL)
    ))

    output$info <- renderText(paste0(
      "Age: ", input$age, "\n",
      "Name: ", input$name, "\n"
    ))
  }

  shinyApp(ui, server)
}

wizard_app()
