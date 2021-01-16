
# Read in the "NEW" LungCapData2...
# (this data has a 'nice' non-linearity to work with)
LungCapData2 <- read.table(file="E:/Larning/hadoop/Data Science/03_Linear Regression/lungcapdata.csv", sep=",", header=T)
# and attach the data
attach(LungCapData2)
# ask for a summary of the data
summary(LungCapData2)


# make a plot of LungCap vs. Height
plot(Height, LungCap, main="Regression", las=1)

# now, let's fit a linear regression
model1 <- lm(LungCap ~ Height)
summary(model1)



trainingRowIndex <- sample(1:nrow(LungCapData2), 0.85*nrow(LungCapData2))  # row indices for training data
trainingData <- LungCapData2[trainingRowIndex, ]  # model training data
testData  <- LungCapData2[-trainingRowIndex, ]   # test data

model1 <- lm(LungCap ~ Height,data=trainingData)
summary(model1)
LungCapPred <- predict(model1, testData[,c(2:6)])  # predict distance

View(LungCapPred)
actuals_preds <- data.frame(cbind(actuals=testData$LungCap, predicteds=LungCapPred))  # make actuals_predicteds dataframe.

head(actuals_preds)



# and add the line to the plot...make it thick and red...
abline(model1, lwd=3, col="red")
??lwd

#_____________


trainingRowIndex <- sample(1:nrow(LungCapData2), 0.5*nrow(LungCapData2))  # row indices for training data
trainingData <- LungCapData2[trainingRowIndex, ]  # model training data
testData  <- LungCapData2[-trainingRowIndex, ]   # test data

# now, let's fit a linear regression
# Build the model on training data -
model2 <- lm(LungCap ~ Height + Age + Smoke, data =trainingData )
summary(model2)

head(testData[,c(2:6)])

LungCapPred <- predict(model2, testData[,c(2:6)])  # predict distance
View(LungCapPred)

actuals_preds <- data.frame(cbind(actuals=testData$LungCap, predicteds=LungCapPred))  # make actuals_predicteds dataframe.

head(actuals_preds)


min_max_accuracy <- mean(apply(actuals_preds, 1, min) / apply(actuals_preds, 1, max)) 

mean(model2$residuals)

par(mfrow=c(2,2))
plot(model2)

library("gvlma")
gvlma::gvlma(model1)



#_____________


trainingRowIndex <- sample(1:nrow(LungCapData2), 0.8*nrow(LungCapData2))  # row indices for training data
trainingData <- LungCapData2[trainingRowIndex, ]  # model training data
testData  <- LungCapData2[-trainingRowIndex, ]   # test data

head(trainingData)
# now, let's fit a linear regression
# Build the model on training data -
model3 <- lm(LungCap ~ Height + Age + Smoke + Gender + Caesarean , data =trainingData )
summary(model3)



LungCapPred <- predict(model3, testData)  # predict distance

actuals_preds <- data.frame(cbind(actuals=testData$LungCap, predicteds=LungCapPred))  # make actuals_predicteds dataframe.

head(actuals_preds)


min_max_accuracy <- mean(apply(actuals_preds, 1, min) / apply(actuals_preds, 1, max)) 


par(mfrow=c(2,2))
plot(model3)

library("gvlma")
gvlma::gvlma(model2)

