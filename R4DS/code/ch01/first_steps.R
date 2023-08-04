library(tidyverse)
library(palmerpenguins)
library(ggthemes)

palmerpenguins::penguins

# For an alternative view, where you can see all
# variables and the first few observations of each variable, use glimpse().
glimpse(palmerpenguins::penguins)
# if you’re in RStudio, run View(penguins) to open an interactive data viewer.
View(palmerpenguins::penguins)

## Creating a ggplot
ggplot(data = penguins)


ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
)

# 似乎可以回答我们的问题了，确实有关系，而且是线性的
ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
) +
  geom_point()

# 如果你看到了简单的线性关系，那么谨慎，看看是否有其他的变量影响了这些
ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g, color = species)
) +
  geom_point()

ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g, color = species)
) +
  geom_point() +
  geom_smooth(method = "lm")

# ggplot() 中的 aes 是全局的美学映射，可以在几何对象中指定映射，否则继承全局
ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
) +
  geom_point(aes(color = species)) +
  geom_smooth(method = "lm")

ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
) +
  geom_point(aes(color = species, shape = species)) +
  geom_smooth(method = "lm")

ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
) +
  geom_point(aes(color = species, shape = species)) +
  geom_smooth(method = "lm") +
  labs(
    x = "Flipper length (mm)",
    y = "Body mass (g)", title = "Body mass ad flipper length",
    subtitle = "Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
    color = "Species", shape = "Species"
  ) + # color and shape 会修改图例的显示内容
  scale_color_colorblind() # 视觉障碍友好
