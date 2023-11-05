library(shiny)

ui <- fluidPage(
  selectInput("language", "Language", choices = c("", "English", "Chinese")),
  textInput("name", "Name"),
  textOutput("greeting")
)

server <- function(input, output, session) {
  greetings <- c(
    English = "Hello",
    Chinese = "你好"
  )
  
  output$greeting <-  renderText({
    # 如果 input$language 没有选择（默认是空字符串），那么将会出现下标出界的问题
    paste0(greetings[[input$language]], " ", input$name, "!")
  })
}
server_req <- function(input, output, session) {
  greetings <- c(
    English = "Hello",
    Chinese = "你好"
  )
  
  output$greeting <-  renderText({
    # 如果 input$language 没有选择（默认是空字符串），那么将会出现下标出界的问题
    req(input$language, input$name)
    paste0(greetings[[input$language]], " ", input$name, "!")
  })
}

shinyApp(ui, server_req)