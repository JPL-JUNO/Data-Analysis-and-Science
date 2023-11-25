library(testthat)
library(usethis)
library(shiny)
test_that("returns other value when primary is other", {
  testServer(server, {
    session$setInputs(fruit = "apple")
    expect_equal(output$value, "apple")

    session$setInputs(fruit = "other", other = "orange")
    expect_equal(output$value, "orange")
  })
})

test_that("returns other value when primary is other", {
  testServer(server, {
    session$setInputs(fruit = "apple", other = "orange")
    expect_equal(output$value, "orange")
  })
})

test_that("automatically switches to other", {
  app <- ShinyDriver$new(shinyApp(ui, server))
  app$setInputs(other = "orange")
  expect_equal(app$getValue("fruit"), "other")
  expect_equal(app$getValue("value"), "orange")
})
