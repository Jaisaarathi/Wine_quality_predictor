# Wine_quality_predictor


1.Setting Up the Flask App:

The app is initialized using Flask(__name__). This creates a Flask web application.
2.Loading the Wine Quality Dataset:

The wine quality dataset is loaded from the CSV file using pd.read_csv.
3.Training the Machine Learning Model:

A Decision Tree classifier is used for simplicity. The model is trained using the features (X) and the target variable (y) from the dataset.
4.Creating a Function to Scale Predicted Quality:

The scale_quality function takes a predicted quality value and scales it to a range of 0 to 100. This function is used to provide a more interpretable prediction for display.
5.Setting Up Routes:

The @app.route('/') decorator defines the behavior when the user accesses the root URL (/). In this case, it renders the index.html template.
6.Creating the HTML Form:

The index.html file contains an HTML form where users can input values for the wine features. It also displays the prediction result.
7.Styling with CSS:

The styling is enhanced using a separate CSS file (styles.css) linked in the HTML file. This improves the visual appeal of the form.
8.Handling Form Submission:

When the user submits the form, the entered values are sent to the server using the HTTP POST method.
9.Making Predictions:

The entered values are converted to a DataFrame and used to make predictions using the trained machine learning model.
10.Scaling Predictions:

The predicted quality is scaled using the scale_quality function to be more user-friendly.
 1.Displaying Results:

 The scaled prediction is then displayed on the web page.
 2.Running the Flask App:

 The app is run using app.run(debug=True) to start the development server. The debug=True option enables automatic 
reloading of the server when code changes are made.
 3.Accessing the App:

Users can access the app by opening a web browser and navigating to http://127.0.0.1:5000/.
 4.Interacting with the Form:

 Users can enter values into the form fields, click the "Predict" button, and see the predicted wine quality displayed on the page.
This Flask app combines web development with machine learning to provide a simple interface for predicting wine quality based on user input. Users interact with the web form, and the backend uses a machine learning model to make predictions, which are then presented to the user. The styling enhances the visual appeal of the application.




