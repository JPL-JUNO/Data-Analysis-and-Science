library(dplyr)
library(nycflights13)

# q1
flights |>
  group_by(carrier) |>
  summarize(avg_delay = mean(dep_delay, na.rm = TRUE))


flights |>
  group_by(carrier, dest) |>
  summarize(avg_delap = mean(dep_delay, na.rm = TRUE))

# q2
flights |>
  group_by(dest) |>
  slice_max(dep_delay, n = 1)

# q3
flights |>
  group_by(hour) |>
  summarise(avg_deplay = mean(dep_delay, na.rm = TRUE)) |>
  ggplot(aes(x = hour, y = avg_deplay)) +
  geom_line()

# q4
# 似乎没有任何的选择，表示全部
flights |>
  group_by(hour) |>
  slice_max(dep_delay, n = -1)

# q5
# 按照统计结果排序，
flights |>
  group_by(month) |>
  count(sort = TRUE)

# q6
df <- tibble(
  x = 1:5,
  y = c("a", "b", "a", "a", "b"),
  z = c("K", "K", "L", "L", "K")
)

# 6a
df |>
  group_by(y)
# 6b
df |>
  arrange(y)
# 6c
df |>
  group_by(y) |>
  summarize(mean_x = mean(x))
# 6d
df |>
  group_by(y, z) |>
  summarize(mean_x = mean(x))

# 6e
df |>
  group_by(y, z) |>
  summarize(mean_x = mean(x), .groups = "drop")

# 6f
df |>
  group_by(y, z) |>
  summarize(mean_x = mean(x))
df |>
  group_by(y, z) |>
  mutate(mean_x = mean(x))
