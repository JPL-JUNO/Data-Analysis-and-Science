library(vroom)
dir.create("neiss")

# maybe have no way to download
download <- function(name) {
  url <- "https://github.com/hadley/mastering-shiny/tree/main/neiss/"
  download.file(paste0(url, name), paste0("neiss/", name), quiet = TRUE)
}
download("injuries.tsv.gz")
download("population.tsv")
download("products.tsv")

injuries <- vroom::vroom("neiss/injuries.tsv.gz")
products <- vroom::vroom("neiss/products.tsv")
population <- vroom::vroom("neiss/population.tsv")

