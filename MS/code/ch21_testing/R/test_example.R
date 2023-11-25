library(testthat)

complicated_object <- list(
  x = list(mtcars, iris),
  y = 10
)

expect_equal(complicated_object$y, 10)

f <- function(){
  stop("Calculation failed [location 1]")
}

expect_error(f(), "Calculation failed [location 1]")

expect_error(f(), "Calculation failed \\[location 1\\]")
