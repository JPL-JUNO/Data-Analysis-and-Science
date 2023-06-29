################################################################
# Description: 数字、运算、赋值和向量
# Author(s): Stephen CUI
# LastEditor(s): Stephen CUI
# CreatedTime: 2023-06-29 22:21:38
################################################################
options(prompt = "R> ")
2 + 3
14 / 6
14 / 6 + 5
14 / (6 + 5)
3^2
2^3
sqrt(x = 9)
sqrt(x = 5.311)
print(10^2 + 3 * 60 / 8 - 3)
print(5^3 * (6 - 2) / (61 - 3 + 4))
print(2^(2 + 1) - 4 + 64^((-2)^(2.25 - 1 / 4)))
# print(2^(2 + 1) - 4 + 64^(-2^(2.25 - 1 / 4))) # nolint
print((.44 * (1 - .44) / 34)^(1 / 2))

# 对数与指数
print(log(x = 243, base = 3))
print(exp(x = 3))
print(log(20.08554))

# 科学计数法
# 默认的7位有效位数
# 只是为了显示问题，没有任何的信息损失
print(2342151012900)
print(0.0000002533)


print((6 * 2.3 + 42) / (3^(4.2 - 3.62)))
print(sqrt((25.2 + 15 + 16.44 + 15.3 + 18.6) / 5 / 2))
print(log(.3))

# 2.2 分配对象
x <- -5
print(x)

x <- x + 1
print(x)

my_number <- 45.2
print(my_number * x)

a <- 3^2 * 4^(1 / 8)
a <- a / 2.33
print(a)
d <- (-8.2) * 10^(-13)
print(d * a)

# 2.3 向量
my_vec <- c(1, 3, 1, 42)
print(my_vec)

foo <- 32.1
my_vec2 <- c(3, -3, 3.45, 1e03, 64^.5, 2 + (3 - 1.1) / 9.44, foo)
print(my_vec2)

my_vec3 <- c(my_vec, my_vec2)
print(my_vec3)

print(3:7)
foo <- 5.3
print(foo:(-45 + 1.5))

print(seq(from = 3, to = 27, by = 3))
print(seq(from = 3, to = 27, length.out = 40))
my_seq <- seq(from = foo, to = (-47 + 1.5), by = -2.4)
print(my_seq)

my_seq2 <- seq(from = foo, to = (-47 + 1.5), length.out = 5)
print(my_seq2)

print(rep(x = 1, time = 4))
print(rep(x = c(3, 62, 8.3), times = 3))
print(rep(x = c(3, 62, 8.3), each = 2))
# times是重复几次x，each是在每次重复中每个元素重复几次
print(rep(x = c(3, 62, 8.3), times = 3, each = 2))
print(sort(x = c(2.5, -1, -10, 3.14), decreasing = FALSE))
print(sort(x = c(2.5, -1, -10, 3.14), decreasing = TRUE))
foo <- seq(from = 4.3, to = 5.5, length.out = 8)
print(foo)
bar <- sort(foo, decreasing = TRUE)
print(bar)
print(sort(c(foo, bar), decreasing = FALSE))

print(length(x = c(3, 2, 8, 1)))
print(length(5:13))
foo <- 4
bar <- c(3, 8, 3, rep(x = 32, times = foo), seq(from = -2, to = 1, length.out = foo + 1))
print(length(bar))

## exercises
s <- seq(from = 5, to = -11, by = -.3)
s <- sort(s, decreasing = FALSE)
s <- rep(x = c(-1, 3, -5, 7, -9), each = 10, times = 2)
print(sort(x = s, decreasing = FALSE))
d <- c(
  seq(6, 12),
  rep(5.3, times = 3),
  -3,
  seq(102, length(s), length.out = 9)
)
print(length(d))

## 子集和元素的提取
my_vec <- c(5, -2, 3, 4, 4, 6, 8, 10, 40221, -8)
print(length(x=my_vec))
print(my_vec[1])
foo <- my_vec[2]
print(foo)

print(my_vec[length(my_vec)])
print(my_vec[c(1, 2, 3)])
foo <- 1:4
print(my_vec[foo])

print(my_vec[length(foo):2])

indexes <- c(4, rep(x=2, times=3), 1, 1, 2, 3:1)
print(my_vec[indexes])

print(foo[-c(1, 3)])