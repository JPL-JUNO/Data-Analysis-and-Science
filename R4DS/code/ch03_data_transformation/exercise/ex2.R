library(dplyr)
library(nycflights13)
# q1
flights |>
  filter(arr_delay >= 120)

flights |>
  filter(dest %in% c("IAU", "HOU"))

flights |>
  filter(carrier %in% c("UA", "AM", "DL"))

flights |>
  filter(month %in% c(7, 8, 9))

flights |>
  filter(dep_delay <= 0 & arr_delay > 120)

flights |>
  filter(dep_delay > 60 & arr_delay < 30)

# q2
flights |>
  arrange(desc(dep_delay))

# q3

flights |>
  arrange(desc(distance / air_time))

# q4
flights |>
  distinct(month, day) |>
  count()

# q5
flights |>
  arrange(desc(distance))

flights |>
  arrange(distance)

# q7
flights |>
  filter(month == 7) |>
  arrange(dep_delay)

flights |>
  arrange(dep_delay) |>
  filter(month == 7)
