import numpy as np  #for numerical operations
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier  # Import decision trees
from sklearn.utils import resample  # Import resample function for bootstrapping
from scipy.stats import mode  # Import mode function for majority voting in classification

class RandomForest:
    def __init__(self, n_estimators=10, max_features=None, task="regression"):
     
        self.n_estimators = n_estimators  # Store number of trees
        self.max_features = max_features  # Store max features for each tree
        self.task = task  # Store whether it's regression or classification
        self.trees = []  # List to hold decision trees

        # Decide which type of decision tree to use
        if task == "regression":
            self.Tree = DecisionTreeRegressor  # Use regression tree for continuous outputs
        elif task == "classification":
            self.Tree = DecisionTreeClassifier  # Use classification tree for categorical outputs
        else:
            raise ValueError("Task must be 'regression' or 'classification'")  # Error handling for incorrect input

    def fit(self, X, y):

        self.trees = []  # Reset the list of trees before training
        n_samples, n_features = X.shape  # Get number of samples (rows) and features (columns)

        # If max_features is not set, use the square root of total features (common practice)
        if self.max_features is None:
            self.max_features = int(np.sqrt(n_features))

        # Train multiple trees
        for _ in range(self.n_estimators):
            # Bootstrap Sampling - Randomly select data points with replacement
            X_sample, y_sample = resample(X, y, replace=True)

            #Train a Decision Tree on the sampled data
            tree = self.Tree(max_features=self.max_features)  # Create a new tree
            tree.fit(X_sample, y_sample)  # Train the tree on the sampled data
            self.trees.append(tree)  # Store the trained tree in the forest

    def predict(self, X):
        # Get predictions from all trees
        predictions = np.array([tree.predict(X) for tree in self.trees])

        # Combine predictions
        if self.task == "regression":
            return np.mean(predictions, axis=0)  # Average the predictions for regression
        else:
            return mode(predictions, axis=0).mode.squeeze()  # Majority vote for classification

if __name__ == "__main__":
    from sklearn.datasets import make_regression, make_classification  # Generate synthetic data
    from sklearn.model_selection import train_test_split  # Split data into training and testing sets
    from sklearn.metrics import mean_squared_error, accuracy_score  # Evaluate model performance

    # REGRESSION
    X_reg, y_reg = make_regression(n_samples=500, n_features=5, noise=0.2)  # Create synthetic regression dataset
    X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2)  # Split into train and test

    rf_reg = RandomForest(n_estimators=20, task="regression")  # Create Random Forest for regression
    rf_reg.fit(X_train, y_train)  # Train the model
    y_pred = rf_reg.predict(X_test)  # Predict on test data

    print("Regression MSE:", mean_squared_error(y_test, y_pred))  # Print Mean Squared Error

    # CLASSIFICATION
    X_clf, y_clf = make_classification(n_samples=500, n_features=5, n_classes=2)  # Create synthetic classification dataset
    X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, test_size=0.2)  # Split into train and test

    rf_clf = RandomForest(n_estimators=20, task="classification")  # Create Random Forest for classification
    rf_clf.fit(X_train, y_train)  # Train the model
    y_pred = rf_clf.predict(X_test)  # Predict on test data

    print("Classification Accuracy:", accuracy_score(y_test, y_pred))  #Print accuracy score
