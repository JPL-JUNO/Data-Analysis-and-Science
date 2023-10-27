library(ggplot2)
library(palmerpenguins)

ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
) +
  geom_point()

# 通常，函数的前一个或两个参数非常重要，应该记住它们。
ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point()


penguins |>
  ggplot(aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point()
