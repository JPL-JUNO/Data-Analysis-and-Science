library(dplyr)
library(nycflights13)


flights |>
  group_by(month)


# 发生这种情况是因为一些观察到的航班在延误列中缺少数据，
# 因此当我们计算包括这些值的平均值时，我们得到了结果NA。
flights |>
  group_by(month) |>
  summarise(avg_delay = mean(dep_delay))

flights |>
  group_by(month) |>
  summarise(
    avg_delay = mean(dep_delay, na.rm = TRUE)
  )

flights |>
  group_by(month) |>
  summarise(
    avg_delay = mean(dep_delay, na.rm = TRUE),
    n = n()
  )

# 会选出所有满足最大值的行（如果有多个相同的最大值）
flights |>
  group_by(dest) |>
  slice_max(arr_delay, n = 1) |>
  relocate(dest)

daily <- flights |>
  group_by(year, month, day)

daily_flights <- daily |>
  summarise(n = n())

daily_flights <- daily |>
  summarise(
    n = n(),
    .groups = "keep"
  )

# 取消分组
daily |>
  ungroup()

daily |>
  ungroup() |>
  summarize(
    avg_daily = mean(dep_delay, na.rm = TRUE),
    flights = n()
  )


# .by 操作
flights |>
  summarize(
    delay = mean(dep_delay, na.rm = TRUE),
    n = n(),
    .by = month
  )
flights |>
  summarize(
    delay = mean(dep_delay, na.rm = TRUE),
    n = n(),
    .by = c(month, dest)
  )
