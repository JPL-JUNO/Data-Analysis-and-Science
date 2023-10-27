library(ggplot2)

# q1
# 先保存散点图，因为它是最近运行的图片
ggplot(mpg, aes(x = class)) +
  geom_bar()
ggplot(mpg, aes(x = cty, y = hwy)) +
  geom_point()
ggsave("img/mpg-plot.png")

# q2
ggsave("img/mpg-plot.pdf")
