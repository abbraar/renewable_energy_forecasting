from fastapi import FastAPI
import pickle

app = FastAPI()

# Load your model
with open('app/Solar_Prophet.pkl', 'rb') as P:
    model = pickle.load(P)

@app.get('/')
def pred_endpoint(d: int):
    future = model.make_future_dataframe(periods=d)
    forecast = model.predict(future)
    return forecast.to_json()
