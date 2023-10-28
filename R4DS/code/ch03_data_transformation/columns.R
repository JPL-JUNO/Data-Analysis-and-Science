library(ggplot2)
library(nycflights13)

flights |>
  mutate(
    gain = dep_delay - arr_delay,
    speed = distance / air_time * 60
  )


flights |>
  mutate(
    gain = dep_delay - arr_delay,
    speed = distance / air_time * 60,
    .before = 1
  )

flights |>
  mutate(
    gain = dep_delay - arr_delay,
    speed = distance / air_time * 60,
    .before = day
  )

flights |>
  mutate(
    gain = dep_delay - arr_delay,
    hours = air_time / 60,
    gain_per_hour = gain / hours,
    .keep = "used"
  )


flights |>
  select(year, month, day)

# 闭区间
flights |>
  select(year:day)

# 闭区间
flights |>
  select(!year:day)

flights |>
  select(where(is.character))

flights |>
  select(starts_with("c"))

flights |>
  select(ends_with("t"))

flights |>
  select(contains("t"))

flights |>
  select(num_range("x", 1:3))


flights |>
  select(tail_num = tailnum)

flights |>
  rename(tail_num = tailnum)

flights |>
  relocate(time_hour, air_time)

flights |>
  relocate(year:dep_time, .after = time_hour)

flights |>
  relocate(starts_with("arr"), .before = dep_time)
