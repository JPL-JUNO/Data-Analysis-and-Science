################################################################
# File         : 02_downloading_data
# Author(s)    : Stephen CUI
# LastEditor(s): Stephen CUI
# CreatedTime  : 2023-11-06 21:58:03
# Description  :
################################################################
library(shiny)
# 建议使用.tsv（制表符分隔值）而不是.csv（逗号分隔值），因为许多欧洲国家使用逗号来分隔数字的整数部分和小数部分（例如 1,23vs 1.23）
ui <- fluidPage(
  selectInput("dataset", "Pick a dataset", ls("package:datasets")),
  tableOutput("preview"),
  downloadButton("download", "Download .tsv")
)

server <- function(input, output, session) {
  data <- reactive({
    out <- get(input$dataset, "package:datasets")
    if (!is.data.frame(out)) {
      # 只可以下载 TSV 文件
      validate(paste0("'", input$dataset, "' is not a data frame"))
    }
    out
  })

  output$preview <- renderTable({
    head(data())
  })

  output$download <- downloadHandler(
    filename = function() {
      paste0(input$dataset, ".tsv")
    },
    content = function(file) {
      vroom::vroom_write(data(), file)
    }
  )
}

shinyApp(ui, server)
