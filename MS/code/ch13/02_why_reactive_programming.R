temp_c <- 10
temp_f <- (temp_c * 9 / 5) + 32
print(temp_f)

temp_c <- 30

temp_f <- function() {
  message("Converting")
  (temp_c * 9) / 5 + 32
}
temp_f()

# 事件驱动编程
DynamicValue <- R6::R6Class("DynamicValue", list(
  value = NULL, on_update = NULL,
  get = function() self$value,
  set = function(value) {
    self$value <- value
    if (!is.null(self$on_update)) {
      self$on_update(value)
    }
    invisible(self)
  },
  onUpdate = function(on_update) {
    self$on_update <- on_update
    invisible(self)
  }
))

temp_c <- DynamicValue$new()
temp_c$onUpdate(function(value) {
  message("Converting")
  temp_f <<- (value * 9 / 5) + 32
})

temp_c$set(10)
temp_f
