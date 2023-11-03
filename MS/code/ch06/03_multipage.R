library(shiny)

ui <- fluidPage(
  tabsetPanel(
    tabPanel(
      "Import Data",
      fileInput("file", "Data", buttonLabel = "Upload..."),
      textInput("delim", "Delimiter (leave blank to guess)", ""),
      numericInput("skip", "Rows to skip", 0, min = 0),
      numericInput("rows", "Rows to preview", 10, min = 1)
    ),
    tabPanel("Set parameters"),
    tabPanel("Visualize results")
  )
)

ui2 <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      textOutput("panel")
    ),
    mainPanel(
      tabsetPanel(
        id = "tabset",
        tabPanel("panel 1", "如果您想知道用户选择了哪个选项卡，您可以提供参数 id，它将成为 tabsetPanel() 的输入"),
        tabPanel("panel 2", "tabsetPanel() 可以在应用程序中的任何位置使用"),
        tabPanel("panel 3", "如果需要的话，将选项卡集嵌套在其他组件（包括选项卡集！）中是完全可以的。"),
      )
    )
  )
)

ui3 <- fluidPage(
  navlistPanel(
    id = "tabset",
    "Heading 1",
    tabPanel("panel 1_1", "Panel one contents"),
    tabPanel("panel 1_2", "Panel one contents"),
    "Heading 2",
    tabPanel("panel 2", "Panel two contents"),
    "Heading 3",
    tabPanel("Panel 3", "Panel three contents")
  )
)

ui_navbar <- navbarPage(
  "Page title",
  tabPanel("panel 1", "one"),
  tabPanel("panel 2", "two"),
  tabPanel("panel 3", "three"),
  navbarMenu(
    "subpanels",
    tabPanel("panel 4a", "four-a"),
    tabPanel("panel 4b", "four-b"),
    tabPanel("panel 4c", "four-c"),
  )
)
server <- function(input, output, session) {
  output$panel <- renderText({
    paste("Current panel: ", input$tabset)
  })
}

shinyApp(ui_navbar, server)
