library(dplyr)
library(ggplot2)
library(Lahman)

batters <- Batting |>
  group_by(playerID) |>
  summarize(
    performance = sum(H, na.rm = TRUE) / sum(AB, na.rm = TRUE),
    n = sum(AB, na.rm = TRUE)
  )

batters |>
  filter(n > 100) |>
  ggplot(aes(x = n, y = performance)) +
  geom_point(alpha = 1 / 10) +
  geom_smooth(se = FALSE)
# 1.
# 击球数较少的球员之间的 performance 差异更大。
# 该图的形状非常有特点：
# 每当您绘制平均值（或其他汇总统计数据）与组大小的关系时，
# 您都会看到随着样本大小的增加，变化会减小。
# 2.
# 技能 performance 和击球机会 n 之间呈正相关，
# 因为球队希望为最好的击球手提供最多的击球机会
batters |>
  arrange(desc(performance))
# 这对于排名也有重要影响。
# 如果你天真地排序 desc(performance)，
# 击球率最高的人显然是那些很少尝试将球投入比赛并碰巧击中的人，
# 他们不一定是最熟练的球员
batters |>
  ggplot(aes(x = n, y = performance)) +
  geom_point(alpha=1/10)+
  geom_smooth(se = FALSE)
