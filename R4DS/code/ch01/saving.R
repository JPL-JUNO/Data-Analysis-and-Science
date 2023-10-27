library(ggplot2)
library(palmerpenguins)

ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
    geom_point()
ggsave(filename = "img/penguin-plot.png")
