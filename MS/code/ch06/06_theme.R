# fluidPage(
#   theme = bslib::ba_theme(...)
# )

library(shiny)

theme <- bslib::bs_theme(
  # 自定义主题
  bg = "#0b3d91",
  fg = "white",
  base_font = "Source Sans Pro"
)

ui <- fluidPage(
  theme = bslib::bs_theme(bootswatch = "darkly"),
  sidebarLayout(
    sidebarPanel(
      textInput("txt", "Text input:", "text here"),
      sliderInput("slider", "Slier input:", 1, 100, 30)
    ),
    mainPanel(
      h1(paste0("Theme: darkly")),
      h2("Header 2"),
      p("Some text")
    )
  )
)

server <- function(input, output, session) {

}

shinyApp(ui, server)
