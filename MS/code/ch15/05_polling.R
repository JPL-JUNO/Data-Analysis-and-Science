library(shiny)



# 我们使用 file.mtime()，它返回上次修改文件的时间，作为一种廉价的检查来查看是否需要重新加载文件
server <- function(input, output, session) {
  # 这将变化的数据连接到 Shiny 的反应式图表中，
  # 但它有一个严重的缺点：
  # 当你使反应无效时，你也会使所有下游消费者无效，
  # 所以即使数据相同，所有下游工作都必须重做。
  data <- reactive({
    on.exit(invalidateLater(1000))
    read.csv("data.csv")
  })
  data <- reactivePoll(
    1000, session,
    function() file.mtime("data.csv"),
    function() read.csv("data.csv")
  )
  # 当文件发生变化时读取文件是一项常见任务，
  #  因此 Shiny 提供了一个更具体的帮助器，只需要文件名和读取器函数：
  data <- reactiveFileReader(1000, session, "data.csv", read.csv())
}
