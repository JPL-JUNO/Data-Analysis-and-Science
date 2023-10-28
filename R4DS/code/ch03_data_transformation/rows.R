library(tidyverse)
library(nycflights13)

flights |>
  filter(dep_delay > 120)


flights |>
  filter(month == 1 & day == 1)


flights |>
  filter(month == 1 | month == 2)


flights |>
  filter(month %in% c(1, 2))


flights |>
  arrange(year, month, day, dep_time)

flights |>
  arrange(desc(dep_delay), year)

flights |>
  distinct()

flights |>
  distinct(origin, dest)


# 同时保留其他字段（列）
flights |>
  distinct(origin, dest, .keep_all = TRUE)

# sort 默认就是降序
flights |>
  count(origin, dest, sort = TRUE)
