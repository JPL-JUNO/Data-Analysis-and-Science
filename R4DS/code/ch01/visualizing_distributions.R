library(tidyverse)
library(palmerpenguins)

ggplot(penguins, aes(x = species)) +
  geom_bar()

# 降序
ggplot(penguins, aes(x = fct_infreq(species))) +
  geom_bar()


ggplot(penguins, aes(x = body_mass_g)) +
  geom_histogram(binwidth = 200)

# binwidth 参数是需要不断尝试的
ggplot(penguins, aes(x = body_mass_g)) +
  geom_histogram(binwidth = 20)
ggplot(penguins, aes(x = body_mass_g)) +
  geom_histogram(binwidth = 2000)

ggplot(penguins, aes(x = body_mass_g)) +
  geom_density()
