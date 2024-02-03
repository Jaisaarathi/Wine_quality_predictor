from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Load the dataset from the CSV file
file_path = "Wine_quality_predictor/winequality-white.csv"
data = pd.read_csv(file_path, sep=';')

# Assume 'quality' is the target variable, and other columns are features
X = data.drop('quality', axis=1)
y = data['quality']

# Initialize the Decision Tree classifier
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

def scale_quality(quality):
    return int((quality - 3) / 6 * 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = {
            'fixed acidity': float(request.form['fixed_acidity']),
            'volatile acidity': float(request.form['volatile_acidity']),
            'citric acid': float(request.form['citric_acid']),
            'residual sugar': float(request.form['residual_sugar']),
            'chlorides': float(request.form['chlorides']),
            'free sulfur dioxide': float(request.form['free_sulfur_dioxide']),
            'total sulfur dioxide': float(request.form['total_sulfur_dioxide']),
            'density': float(request.form['density']),
            'pH': float(request.form['pH']),
            'sulphates': float(request.form['sulphates']),
            'alcohol': float(request.form['alcohol'])
        }

        user_df = pd.DataFrame([user_input])
        predicted_quality = model.predict(user_df)
        predicted_quality_scaled = scale_quality(predicted_quality[0])

        return render_template('index.html', prediction=predicted_quality_scaled)

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
