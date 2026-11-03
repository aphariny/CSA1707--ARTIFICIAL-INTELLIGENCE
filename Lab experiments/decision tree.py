from sklearn.tree import DecisionTreeClassifier

# Training data
# [Study Hours, Attendance]
X = [
    [1, 40],
    [2, 50],
    [3, 60],
    [4, 70],
    [5, 80],
    [6, 90]
]

# Output: 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

# Create decision tree
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Get input from user
hours = int(input("Enter study hours: "))
attendance = int(input("Enter attendance percentage: "))

# Predict result
result = model.predict([[hours, attendance]])

if result[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")
