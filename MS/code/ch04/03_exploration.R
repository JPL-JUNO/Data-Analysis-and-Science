library(vroom)
library(tidyverse)
# tidyverse must before vroom because some functions be masked by tidyverse
library(shiny)
injuries <- vroom::vroom("neiss/injuries.tsv")
products <- vroom::vroom("neiss/products.tsv")
population <- vroom::vroom("neiss/population.tsv")

# injuries <- read.csv("neiss/injuries.tsv", sep = "\t")

selected <- injuries %>% filter(prod_code == 649)

selected %>%
  count(location, wt = weight, sort = TRUE)

selected %>%
  count(body_part, wt = weight, sort = TRUE)

# 诊断
selected %>%
  count(diag, wt = weight, sort = TRUE)


summary <- selected |>
  count(age, sex, wt = weight)

summary |>
  ggplot(aes(age, n, color = sex)) +
  geom_line() +
  labs(y = "Estimated number of injuries")


summary <- selected |>
  count(age, sex, wt = weight) |>
  left_join(population, by = c("age", "sex")) |>
  mutate(rate = n / population * 1e4)

# 因为受伤的人中是有年龄的，但是 population 中没有统计全部
# 会出现一些 NA 值
summary |> 
  ggplot(aes(age, rate, color=sex))+
  geom_line(na.rm = TRUE)+
  labs(y = "Injuries per 10,000 people")

selected |> 
  sample_n(10) |> 
  pull(narrative)
