
lungcap <- read.table(file = "E:/Larning/hadoop/Data Science/03_Linear Regression/lungcapdata.csv", header = T, sep=",")


summary(lungcap)

attach(lungcap)

plot(factor(Age))

names(lungcap)

cor(Age,LungCap)


plot(Age,LungCap)

fit1 <- lm(LungCap~Age+Height+Smoke)


abline(fit1)

summary(fit1)
# Age          Estimate -- 0.54485 # thsis is the Slope values for Age
#(Intercept)  1.14686

# Residual standard error: 1.526 on 723 degrees of freedom
# This give the size ot Avg of error for residuals

plot(fit1)
mean(fit1$residuals)

# resuials(e-error term) vs Fitted 
# Q-Q Qualtile Qualtile Plot
# Non Linearty an Non Constant values

par(mfrow = c(2,2))

gvlma::gvlma(fit1)







