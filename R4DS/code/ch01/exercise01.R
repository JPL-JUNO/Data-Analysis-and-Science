library(palmerpenguins)
library(tidyverse)

glimpse(penguins)

nrow(penguins)
ncol(penguins)
dim(penguins)

?penguins

ggplot(
  data = penguins,
  mapping = aes(x = bill_depth_mm, y = bill_length_mm)
) +
  geom_point()

ggplot(
  data = penguins,
  mapping = aes(x = species, y = bill_length_mm)
) +
  geom_point()
# 对于离散变量和连续变量，密度图可能更合适，并且将离散值进行 aes
ggplot(
  data = penguins,
  mapping = aes(x = bill_length_mm, color = species)
) +
  geom_density(linewidth = 2)
# 箱线图也是不错的选择
ggplot(
  data = penguins,
  mapping = aes(x = bill_length_mm, color = species)
) +
  geom_boxplot()

# T5
# 报错，因为没有添加任何的美学映射
# ggplot(data = penguins) + geom_point()
penguins |>
  ggplot(mapping = aes(x = bill_depth_mm, y = body_mass_g)) +
  geom_point()

# T6 移除缺失值的按钮
penguins |>
  ggplot(mapping = aes(x = bill_depth_mm, y = body_mass_g)) +
  geom_point(na.rm = TRUE)

# T7 增加一个图例
penguins |>
  ggplot(mapping = aes(x = bill_depth_mm, y = body_mass_g)) +
  geom_point(na.rm = TRUE) +
  labs(caption = "Data come from the palmerpenguins package")

# T8
penguins |>
  ggplot(mapping = aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(aes(color = bill_depth_mm), na.rm = TRUE) +
  geom_smooth(na.rm = TRUE)

# T9
ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g, color = island)
) +
  geom_point() +
  geom_smooth(se = FALSE)

# T10 没有什么不同的地方，因为都是继承过去的
ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
) +
  geom_point() +
  geom_smooth()

ggplot() +
  geom_point(
    data = penguins, mapping = aes(x = flipper_length_mm, y = body_mass_g)
  ) +
  geom_smooth(
    data = penguins,
    mapping = aes(x = flipper_length_mm, y = body_mass_g)
  )
