from fastapi import FastAPI, HTTPException
import pickle

# Load model
filename = "logisitic_regression_model.pkl"
model = pickle.load(open(filename, 'rb'))

# Initialize an instance of FastAPI
app = FastAPI()

# Define the default route


@app.get('/')
def root():
    return {'message': 'Welcome to Your Sentiment Analysis Instagram Comment'}


@app.post('/predict_sentiment/')
def predict_sentiment(text_message):
    polarity = ""

    if (not (text_message)):
        raise HTTPException(
            status_code=400, detail="Please provide a valid text message")

    prediction = model.predict([text_message])

    if (prediction[0] == 0):
        polarity = "Negative Comment"
    elif (prediction[0] == 1):
        polarity = "Positive Comment"

    return {
        "text_message": text_message,
        "sentiment_polarity": polarity
    }
