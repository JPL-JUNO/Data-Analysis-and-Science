library(shiny)
reactiveConsole(TRUE)

temp_c <- reactiveVal(10)
temp_c()
# 像函数调用(单参数函数)一样来 set value
temp_c(20)
# 像函数调用(无参数函数)一样来 get value
temp_c()

temp_f <- reactive({
  message("Converting")
  (temp_c() * 9 / 5) + 32
})
temp_f()

# 响应式表达式会自动跟踪其所有依赖项。
# 这样以后如果 temp_c 有变化，temp_f 会自动更新：
temp_c(-3)
temp_c(-10)
temp_f()

# 如果 temp_c() 没有改变，
# 则 temp_f() 不需要重新计算，只需从缓存中检索即可：
temp_f()