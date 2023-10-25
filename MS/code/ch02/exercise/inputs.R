ui <- fluidPage(
  # ex1
  textInput("name", label = NULL, placeholder = "Your name"),

  # ex2
  sliderInput("date", "When should we deliver?",
    value = as.Date("2020-09-17", "%Y-%m-%d"),
    min = as.Date("2020-09-16", "%Y-%m-%d"), max = as.Date("2020-09-22", "%Y-%m-%d")
  ),

  # ex3
  sliderInput("value", "Which value you choose?",
    value = 0, min = 0, max = 100, step = 5, animate = TRUE
  ),

  # ex4
  # 使用 named list
  selectInput(
    "text", "which value you choose?",
    list(
      `East Coast` = list("NY", "NJ", "CT"),
      `West Coast` = list("WA", "OR", "CA"),
      `Midwest` = list("MN", "WI", "IA")
    )
  )
)
server <- function(input, output, session) {}

shinyApp(ui, server)
