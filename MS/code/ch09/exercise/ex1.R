################################################################
# File         : ex1
# Author(s)    : Stephen CUI
# LastEditor(s): Stephen CUI
# CreatedTime  : 2023-11-07 22:12:50
# Description  : 使用Thomas Lin Pedersen 的 ambient 包生成 worley 噪声并下载它的 PNG。
################################################################
library(shiny)
library(ambient)

ui <- fluidPage(
  downloadButton("download", class = "btn-block"),
  plotOutput("plot")
)

server <- function(input, output, session) {
  # 我不知道如何产生噪声
  # data <- reactive({
  #     df <- ambient::noise_worley()
  # })
}

shinyApp(ui, server)
