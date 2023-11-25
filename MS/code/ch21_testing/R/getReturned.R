library(shiny)
library(testthat)

datasetServer <- function(id) {
  moduleServer(id, function(input, output, session) {
    reactive(get(input$dataset, "package:datasets"))
  })
}

test_that("can find dataset", {
  testServer(datasetServer, {
    dataset <- session$getReturned()

    session$setInputs(dataset = "mtcars")
    expect_equal(dataset(), mtcars)

    session$setInputs(dataset = "iris")
    expect_equal(dataset(), iris)
  })
})
