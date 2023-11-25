library(shiny)
library(testthat)
test_that("can find dataset", {
  testServer(datasetServer, {
    dataset <- session$getReturned()

    session$setInputs(dataset = "mtcars")
    expect_equal(dataset(), mtcars)

    session$setInputs(dataset = "iris")
    expect_equal(dataset(), iris)
  })
})
