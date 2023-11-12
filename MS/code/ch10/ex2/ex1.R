library(shiny)
# 通过点击复选框来显示面板
ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      checkboxInput("more_controls", "高级", value = FALSE)
    ),
    mainPanel(
      tabsetPanel(
        id = "basic",
        type = "hidden",
        tabPanelBody(
          "panel1",
          numericInput("basicControl", "Basic:", 0)
        )
      ),
      tabsetPanel(
        id = "advanced",
        type = "hidden",
        # 这个是用来占位的吗？
        tabPanelBody("emptyPanel", style = "display:none"),
        tabPanelBody(
          "panel2",
          numericInput("advancedControl", "Advanced:", 1)
        )
      ),
    )
  )
)

server <- function(input, output, session) {
  observeEvent(input$more_controls, {
    if (input$more_controls) {
      updateTabsetPanel(session, inputId = "advanced", selected = "panel2")
    } else {
      updateTabsetPanel(session, inputId = "advanced", selected = "emptyPanel")
    }
  })
}

shinyApp(ui, server)
