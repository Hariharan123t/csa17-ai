import numpy as np

class TreeNode:
    def __init__(self, depth=0, max_depth=None):
        self.depth = depth
        self.max_depth = max_depth
        self.left = None
        self.right = None
        self.feature_index = None
        self.threshold = None
        self.label = None
    
    def fit(self, X, y):
        unique_classes = np.unique(y)
        
        # Base case: all samples belong to the same class
        if len(unique_classes) == 1:
            self.label = unique_classes[0]
            return
        
        # Base case: reached max depth
        if self.max_depth is not None and self.depth == self.max_depth:
            self.label = np.argmax(np.bincount(y))  # Majority voting
            return
        
        n_samples, n_features = X.shape
        best_gini = float('inf')
        best_feature_idx = None
        best_threshold = None
        
        # Calculate Gini impurity for current node
        gini_parent = self.calculate_gini(y)
        
        # Try splitting on each feature
        for feature_idx in range(n_features):
            thresholds, unique_thresholds = self.generate_thresholds(X[:, feature_idx])
            for threshold in thresholds:
                left_indices = np.where(X[:, feature_idx] <= threshold)[0]
                right_indices = np.where(X[:, feature_idx] > threshold)[0]
                
                if len(left_indices) == 0 or len(right_indices) == 0:
                    continue
                
                gini_left = self.calculate_gini(y[left_indices])
                gini_right = self.calculate_gini(y[right_indices])
                
                weighted_gini = (len(left_indices) / n_samples) * gini_left + (len(right_indices) / n_samples) * gini_right
                
                if weighted_gini < best_gini:
                    best_gini = weighted_gini
                    best_feature_idx = feature_idx
                    best_threshold = threshold
        
        if best_gini == float('inf'):
            self.label = np.argmax(np.bincount(y))  # Majority voting
            return
        
        self.feature_index = best_feature_idx
        self.threshold = best_threshold
        
        # Split data
        left_indices = np.where(X[:, best_feature_idx] <= best_threshold)[0]
        right_indices = np.where(X[:, best_feature_idx] > best_threshold)[0]
        
        # Recursive call to build left and right subtrees
        self.left = TreeNode(depth=self.depth + 1, max_depth=self.max_depth)
        self.left.fit(X[left_indices], y[left_indices])
        
        self.right = TreeNode(depth=self.depth + 1, max_depth=self.max_depth)
        self.right.fit(X[right_indices], y[right_indices])
    
    def calculate_gini(self, y):
        classes, class_counts = np.unique(y, return_counts=True)
        gini = 1.0
        for class_count in class_counts:
            gini -= (class_count / len(y)) ** 2
        return gini
    
    def generate_thresholds(self, feature):
        unique_thresholds = np.unique(feature)
        thresholds = (unique_thresholds[:-1] + unique_thresholds[1:]) / 2
        return thresholds, unique_thresholds

    def predict(self, X):
        if self.label is not None:
            return np.array([self.label] * len(X))
        
        predictions = np.zeros(len(X), dtype=int)
        left_indices = np.where(X[:, self.feature_index] <= self.threshold)[0]
        right_indices = np.where(X[:, self.feature_index] > self.threshold)[0]
        
        predictions[left_indices] = self.left.predict(X[left_indices])
        predictions[right_indices] = self.right.predict(X[right_indices])
        
        return predictions

class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.root = None
    
    def fit(self, X, y):
        self.root = TreeNode(max_depth=self.max_depth)
        self.root.fit(X, y)
    
    def predict(self, X):
        return self.root.predict(X)

# Example usage:
if __name__ == "__main__":
    # Sample dataset (binary classification)
    X = np.array([[2.771244718,1.784783929],
                  [1.728571309,1.169761413],
                  [3.678319846,2.81281357],
                  [3.961043357,2.61995032],
                  [2.999208922,2.209014212],
                  [7.497545867,3.162953546],
                  [9.00220326,3.339047188],
                  [7.444542326,0.476683375],
                  [10.12493903,3.234550982],
                  [6.642287351,3.319983761]])
    
    y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])  # Labels: 0 and 1
    
    # Create decision tree classifier
    dt = DecisionTreeClassifier(max_depth=3)
    dt.fit(X, y)
    
    # Predictions
    y_pred = dt.predict(X)
    print("Predictions:", y_pred)
