freqpoly <- function(x1, x2, binwidth = .1, xlim = c(-3, 3)) {
  df <- data.frame(
    x = c(x1, x2),
    g = c(rep("x1", length(x1)), rep("x2", length(x2)))
  )
  
  ggplot(df, aes(x, color=g))+
    geom_freqpoly(binwidth=binwidth, linewidth=1)+
    coord_cartesian(xlim=xlim)
}

t_test <- function(x1, x2){
  test <- t.test(x1, x2)
  sprintf(
    "p value: %0.3f\n[%0.2f, %0.2f]",
    test$p.value, test$conf.int[1], test$conf.int[2]
  )
}
