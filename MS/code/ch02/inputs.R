animals <- c("dog", "cat", "mouse", "bird", "other", "I hate animals")
ui <- fluidPage(
  # 文本输入
  # 收集少量文本
  textInput("name", "What's your name?"),
  # 收集密码
  passwordInput("password", "What's your password?"),
  # 收集文本段落
  textAreaInput("story", "Tell me about yourself", rows = 3),

  # 数值输入
  # 创建带有约束文本框（约束数值）
  numericInput("num", "Number one", value = 0, min = 0, max = 100),
  # 滑块
  sliderInput("num2", "Number two", value = 50, min = 0, max = 100),
  sliderInput("rng", "Range", value = c(10, 20), min = 0, max = 100),

  # 收集日期
  dateInput("dob", "When were you born?"),
  dateRangeInput("holiday", "When do you want to go on vacation next?"),

  # 有限项
  selectInput("state", "What's your favorite state?", state.name),
  radioButtons("animal", "What's your favourite animal?", animals),
  radioButtons("rb", "Choose one:", choiceNames = list(
    icon("angry"), icon("smile"), icon("sad-tear")
  ), choiceValues = list("angry", "happy", "sad")),
  selectInput("state", "What's your favourite state?", state.name, multiple = TRUE),
  checkboxGroupInput("animal", "What animals do you like?", animals),
  
  
  # 单选框，value = TRUE 表示默认选中
  checkboxInput("cleanup", "Clean up", value = TRUE),
  checkboxInput("shutdown", "Shutdown?"),
  
  # 文件上传
  # fileInput 在服务端需要特殊的处理
  fileInput("upload", NULL),
  
  # 操作按钮
  actionButton("click", "Click me!"),
  actionButton("drink", "Drink me!", icon=icon("cocktail")),
  
  fluidRow(
    actionButton("click", "Click me!", class="btn-danger"),
    actionButton("drink", "Drink me!", class = "btn-lg btn-class")
  ),
  fluidRow(
    actionButton("eat", "Eat me!", class="btn-block")
  )
)
server <- function(input, output, session) {}
shinyApp(ui, server)
