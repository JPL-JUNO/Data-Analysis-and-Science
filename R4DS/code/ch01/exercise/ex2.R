library(tidyverse)
library(palmerpenguins)

ggplot(penguins, aes(y = species)) +
  geom_bar()

# color 是 bar 的外边线颜色
ggplot(penguins, aes(y = species)) +
  geom_bar(color = "red")

# fill 是 bar 的内部填充颜色
ggplot(penguins, aes(y = species)) +
  geom_bar(fill = "red")


ggplot(penguins, aes(x = body_mass_g)) +
  geom_histogram(bins = 30)


ggplot(diamonds, aes(x = carat)) +
  geom_histogram(bins = 50)
