from fastapi import  FastAPI, HTTPException
import pandas as pd
from core.utility import load_model
from schemas.house import HouseFeatures, BatchRequest

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware


origins = [
        "http://localhost:8501",  # Streamlit's default port
        # Add other origins if your Streamlit app is deployed elsewhere
    ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
def read_root():
    return {
        "status_code" : 200,
        "message": "House Price Prediction API. POST /predict with JSON body to get prediction."
    }


@app.post('/predict')
def predict_price(payload: HouseFeatures):
    # check for model
    model = load_model()
    if model is None:
        raise HTTPException(status_code=500, detail="Model does not found")

    # check if data present
    house_data = payload.model_dump()
    df = pd.DataFrame([house_data])

    try:
        prediction = model.predict(df)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {e}")

    return {
        "status_code" : 200,
        "predicted_price": float(prediction[0])
    }

@app.post('/predict_batch')
def predict_batch(req : BatchRequest):
    model = load_model()
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded on server.")

    house_data = [item.model_dump() for item in req.items]

    try:
        result = []
        for data in house_data:
            df = pd.DataFrame([data])
            prediction = model.predict(df)
            result.append(float(prediction[0]))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {e}")

    return {
        "status_code": 200,
        "predicted_price": result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)






