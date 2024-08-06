from django.shortcuts import render
import joblib
import pandas as pd

def predict_car_price(request):
    if request.method == 'POST':
        # Get user input
        year = int(request.POST['year'])
        mileage = int(request.POST['mileage'])
        
        # Load the model
        model = joblib.load('car_predictor/car_price_prediction_model.pkl')  # Adjust the path as needed
        
        # Create a DataFrame with user input
        input_data = pd.DataFrame({'Year': [year], 'Mileage': [mileage]})
        
        # Make prediction
        predicted_price = model.predict(input_data)
        
        # Display the prediction result
        return render(request, 'car_predictor/prediction_result.html', {'predicted_price': predicted_price[0]})
    
    return render(request, 'car_predictor/predict_car_price.html')
