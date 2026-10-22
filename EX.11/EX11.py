Step 1: Load libraries
library(e1071)       # For SVM
library(rpart)       # For Decision Tree
library(caret)       # For Data Splitting and Accuracy
library(ggplot2)

# Step 2: Simulate Big Data sample
data <- iris   # Example: Iris Dataset
set.seed(123)
index <- createDataPartition(data$Species, p=0.7, list=FALSE)
train <- data[index,]
test <- data[-index,]

# Step 3: Linear Regression (Prediction: Petal.Length ~ Sepal.Length)
lin_model <- lm(Petal.Length ~ Sepal.Length, data=train)
summary(lin_model)
pred_lin <- predict(lin_model, newdata=test)

# Step 4: SVM Classification
svm_model <- svm(Species ~ ., data=train)
pred_svm <- predict(svm_model, test)
confusionMatrix(pred_svm, test$Species)

# Step 5: Decision Tree Classification
tree_model <- rpart(Species ~ ., data=train, method="class")
pred_tree <- predict(tree_model, test, type="class")
confusionMatrix(pred_tree, test$Species)