library(dplyr)
library(nycflights13)

# q3
flights |>
  select(year, year)

# q4
variables <- c("year", "month", "day", "dep_delay", "arr_delay")
flights |>
  select(any_of(variables))
# q5
flights |>
  select(contains("TIME"))

flights |>
  rename(air_time_min = air_time) |>
  relocate(air_time_min)
