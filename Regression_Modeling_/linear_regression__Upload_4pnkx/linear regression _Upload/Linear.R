# Load the data into R
library(MASS)
data("Boston")
View(Boston)


#For data description
?Boston


#To view the correlation of variables
plot(Boston$crim,Boston$medv,cex = 0.5,xlab = "Crime rate" , ylab = "Price")
cr<- cor(Boston)

#We can use corrplot to visualize
library(corrplot)

corrplot(cr,type = "lower")


#We will split the data into training and testing sets
set.seed(2)
library(caTools) #sample.split function is present in this package

split<-sample.split(Boston$medv,SplitRatio = 0.7) 
#we divided the data with the ratio 0.7
split

training_data<-subset(Boston,split=="TRUE")
testing_data<-subset(Boston,split=="FALSE")



#Linear regression Model

colnames(training_data)

#Now to create the model we will use all columns

model<-lm(medv~.,data = training_data)
#or
model<-lm(medv~ crim + zn + indus + chas + nox + rm + age + dis + rad + 
            tax + ptratio + black + lstat,data = training_data)


#for descripion of the model
summary(model)


#Now we can use this model to predict the output of test set
predic<-predict(model,testing_data)
predic
str(predic)

#To compare predicted values and actual values ,we can use plots
plot(testing_data$medv,type = "l",lty = 1.8,col = "green")
lines(predic,type = "l",col = "blue")

cbind(predic,testing_data$medv)





