library(ggplot2)
library(palmerpenguins)

ggplot(mpg, aes(x = hwy, y = displ)) +
  geom_point(aes(color = cty))

ggplot(mpg, aes(x = hwy, y = displ)) +
  geom_point(aes(size = cty))

ggplot(mpg, aes(x = hwy, y = displ)) +
  geom_point(aes(size = cty, color = cty))


# q3
ggplot(mpg, aes(x = hwy, y = displ)) +
  geom_point(aes(linewidth = cty))


# q5
ggplot(penguins, aes(x = bill_depth_mm, y = bill_length_mm, color = species)) +
  geom_point()
ggplot(penguins, aes(x = bill_depth_mm, y = bill_length_mm)) +
  geom_point() +
  facet_wrap(~species)

# q6
ggplot(penguins, aes(x = bill_depth_mm, y = bill_length_mm, color = species, shape = species)) +
  geom_point() +
  labs(color = "Species", shape = "Species")

# q7
# 回答每个岛屿上物种的分布
ggplot(penguins, aes(x = island, fill = species)) +
  geom_bar(position = "fill")
# 回答物种在岛屿分布
ggplot(penguins, aes(x = species, fill = island)) +
  geom_bar(position = "fill")
