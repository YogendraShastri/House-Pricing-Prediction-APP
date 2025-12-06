# 🏠 House Price Prediction System

A machine learning-powered house price prediction system built with **FastAPI** backend and **Streamlit** frontend. The system uses a pre-trained Random Forest model (saved as a PKL file) to predict house prices based on various property features.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Pydantic Features Used](#pydantic-features-used)
- [Usage Examples](#usage-examples)
- [Project Architecture](#project-architecture)

## 🎯 Project Overview

This project provides a complete end-to-end solution for house price prediction:

- **Backend (FastAPI)**: RESTful API with data validation, error handling, and CORS support
- **Frontend (Streamlit)**: Interactive web interface for easy price prediction
- **Model**: Pre-trained Random Forest model loaded from PKL file
- **Data Validation**: Comprehensive input validation using Pydantic

## 📁 Project Structure

```
House_Pricing_LLM/
├── app.py                      # FastAPI application (backend)
├── ui_app.py                   # Streamlit UI application (frontend)
├── core/
│   ├── __init__.py
│   ├── config.py              # Configuration settings
│   └── utility.py             # Utility functions (model loading)
├── schemas/
│   ├── __init__.py
│   └── house.py               # Pydantic models for data validation
├── models/
│   └── house_price_model.pkl  # Pre-trained Random Forest model
├── TrainingData/
│   └── Housing.csv            # Training dataset
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## ✨ Features

- 🎯 **Single House Prediction**: Predict price for one house at a time
- 📊 **Batch Prediction**: Predict prices for multiple houses in one request
- ✅ **Input Validation**: Comprehensive validation using Pydantic
- 🔒 **Type Safety**: Strong typing with Pydantic models
- 🌐 **CORS Support**: Configured for Streamlit frontend integration
- 🎨 **Interactive UI**: User-friendly Streamlit interface
- 📝 **API Documentation**: Auto-generated OpenAPI/Swagger docs

## 🛠 Technology Stack

- **Backend Framework**: FastAPI
- **Frontend Framework**: Streamlit
- **Data Validation**: Pydantic v2
- **Machine Learning**: scikit-learn, joblib
- **Data Processing**: pandas, numpy
- **HTTP Client**: requests
- **Server**: Uvicorn

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Navigate to Project Directory

```bash
cd House_Pricing_LLM
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:
- `fastapi` - Web framework for building APIs
- `uvicorn` - ASGI server for FastAPI
- `pydantic` - Data validation using Python type annotations
- `streamlit` - Frontend framework
- `pandas`, `numpy` - Data processing
- `scikit-learn`, `joblib` - Machine learning model handling
- `requests` - HTTP library for API calls

## 🚀 Running the Application

The application consists of two separate services that need to run simultaneously:

### Option 1: Using Two Terminal Windows/Tabs (Recommended)

#### Terminal 1: Start FastAPI Backend

```bash
# Make sure you're in the project directory
cd House_Pricing_LLM

# Activate virtual environment (if using one)
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Run FastAPI application
python app.py
```

The FastAPI server will start on **http://localhost:8000**

You should see output like:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

#### Terminal 2: Start Streamlit Frontend

Open a **new terminal window/tab** and run:

```bash
# Navigate to project directory
cd House_Pricing_LLM

# Activate virtual environment (if using one)
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Run Streamlit application
streamlit run ui_app.py
```

The Streamlit UI will automatically open in your browser at **http://localhost:8501**

### Option 2: Using Background Process (Linux/macOS)

You can run FastAPI in the background:

```bash
# Start FastAPI in background
python app.py &

# Start Streamlit
streamlit run ui_app.py
```

### Option 3: Using Screen/Tmux (Linux/macOS)

```bash
# Create a new screen session
screen -S house_price

# Start FastAPI
python app.py

# Press Ctrl+A then D to detach

# In another terminal, start Streamlit
streamlit run ui_app.py
```

## 📚 API Documentation

Once the FastAPI server is running, you can access:

- **Interactive API Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc
- **Root Endpoint**: http://localhost:8000/

### API Endpoints

#### 1. `GET /`
Root endpoint that returns API status and information.

**Response:**
```json
{
  "status_code": 200,
  "message": "House Price Prediction API. POST /predict with JSON body to get prediction."
}
```

#### 2. `POST /predict`
Predict house price for a single house.

**Request Body:**
```json
{
  "area": 5000.0,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 1,
  "parking": 2,
  "mainroad": "yes",
  "guestroom": "no",
  "basement": "no",
  "hotwaterheating": "no",
  "airconditioning": "yes",
  "prefarea": "yes",
  "furnishingstatus": "semi-furnished"
}
```

**Response:**
```json
{
  "status_code": 200,
  "predicted_price": 9876543.21
}
```

#### 3. `POST /predict_batch`
Predict house prices for multiple houses.

**Request Body:**
```json
{
  "items": [
    {
      "area": 5000.0,
      "bedrooms": 3,
      "bathrooms": 2,
      "stories": 1,
      "parking": 2,
      "mainroad": "yes",
      "guestroom": "no",
      "basement": "no",
      "hotwaterheating": "no",
      "airconditioning": "yes",
      "prefarea": "yes",
      "furnishingstatus": "semi-furnished"
    },
    {
      "area": 6000.0,
      "bedrooms": 4,
      "bathrooms": 3,
      "stories": 2,
      "parking": 2,
      "mainroad": "yes",
      "guestroom": "yes",
      "basement": "yes",
      "hotwaterheating": "no",
      "airconditioning": "yes",
      "prefarea": "yes",
      "furnishingstatus": "furnished"
    }
  ]
}
```

**Response:**
```json
{
  "status_code": 200,
  "predicted_price": [9876543.21, 12345678.90]
}
```

## 🔍 Pydantic Features Used

This project extensively uses **Pydantic v2** for data validation and serialization. Here's a detailed explanation of the Pydantic features implemented:

### 1. **BaseModel**
The foundation of all Pydantic models. All data models inherit from `BaseModel`:

```python
from pydantic import BaseModel

class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    # ... other fields
```

**Benefits:**
- Automatic data validation
- Type conversion
- JSON serialization/deserialization
- IDE support with type hints

### 2. **Field() - Field Definitions**
Used to add metadata, constraints, and examples to model fields:

```python
from pydantic import Field

class HouseFeatures(BaseModel):
    area: float = Field(..., examples=[1000])
    bedrooms: int = Field(..., examples=[3], ge=0)
    bathrooms: int = Field(..., examples=[2], ge=0)
```

**Field Parameters Used:**
- `...` (Ellipsis): Required field (cannot be None)
- `examples=[value]`: Example values for API documentation
- `ge=0`: Greater than or equal to 0 (minimum value constraint)
- `le=value`: Less than or equal to value (maximum value constraint)
- `gt=value`: Greater than value
- `lt=value`: Less than value
- `description="text"`: Field description for documentation

**Other Available Field Parameters:**
- `default=value`: Default value if field is not provided
- `alias="name"`: Alternative field name for serialization
- `title="Title"`: Field title for documentation
- `min_length=value`: Minimum string length
- `max_length=value`: Maximum string length
- `pattern="regex"`: Regex pattern for string validation

### 3. **field_validator() - Field-Level Validation**
Validates individual fields with custom logic:

```python
from pydantic import field_validator

@field_validator("mainroad", "guestroom", "basement", "hotwaterheating", 
                 "airconditioning", "prefarea", mode="before")
@classmethod
def yes_no_validator(cls, v: str) -> str:
    if v.lower() not in {"yes", "no"}:
        raise ValueError("must be yes/no")
    return v.lower()
```

**Key Features:**
- `mode="before"`: Validates before type conversion
- `mode="after"`: Validates after type conversion (default)
- Can validate multiple fields at once
- Must be a `@classmethod`
- Returns the validated/transformed value

**Validation Modes:**
- `mode="before"`: Runs before Pydantic's internal validation
- `mode="after"`: Runs after type conversion (default)
- `mode="wrap"`: Wraps the validator with error handling

### 4. **Other Pydantic Features (Available but not used in this project)**

#### **model_validator() - Model-Level Validation**
Validates the entire model or multiple fields together:

```python
from pydantic import model_validator

@model_validator(mode='after')
def validate_model(self):
    if self.bedrooms > self.stories * 2:
        raise ValueError("Too many bedrooms for the number of stories")
    return self
```

#### **computed_field() - Computed/Derived Fields**
Create fields that are computed from other fields:

```python
from pydantic import computed_field

class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    
    @computed_field
    @property
    def price_per_sqft(self) -> float:
        return self.price / self.area if self.area > 0 else 0.0
```

#### **Field Serialization**
Control how fields are serialized:

```python
from pydantic import field_serializer

class HouseFeatures(BaseModel):
    price: float
    
    @field_serializer('price')
    def serialize_price(self, value: float) -> str:
        return f"${value:,.2f}"
```

#### **ConfigDict (Pydantic v2)**
Model configuration:

```python
from pydantic import ConfigDict

class HouseFeatures(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,  # Strip whitespace from strings
        validate_assignment=True,    # Validate on assignment
        use_enum_values=True,        # Use enum values
        extra='forbid'              # Forbid extra fields
    )
```

#### **Generic Models**
Create reusable model patterns:

```python
from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class Response(BaseModel, Generic[T]):
    status_code: int
    data: T
```

#### **Nested Models**
Models within models:

```python
class Address(BaseModel):
    street: str
    city: str

class HouseFeatures(BaseModel):
    area: float
    address: Address  # Nested model
```

## 💡 Usage Examples

### Using the Streamlit UI

1. Start both FastAPI and Streamlit (as described in [Running the Application](#running-the-application))
2. Open the Streamlit UI in your browser (usually http://localhost:8501)
3. Fill in the house details:
   - Area, bedrooms, bathrooms, stories, parking
   - Select options for amenities (main road, guest room, etc.)
   - Choose furnishing status
4. Click "Predict price"
5. View the predicted price

### Using the API Directly

#### Using curl

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "area": 5000.0,
    "bedrooms": 3,
    "bathrooms": 2,
    "stories": 1,
    "parking": 2,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "no",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "prefarea": "yes",
    "furnishingstatus": "semi-furnished"
  }'
```

#### Using Python requests

```python
import requests

url = "http://localhost:8000/predict"
payload = {
    "area": 5000.0,
    "bedrooms": 3,
    "bathrooms": 2,
    "stories": 1,
    "parking": 2,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "no",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "prefarea": "yes",
    "furnishingstatus": "semi-furnished"
}

response = requests.post(url, json=payload)
print(response.json())
```

#### Using the Interactive API Docs

1. Start FastAPI server
2. Navigate to http://localhost:8000/docs
3. Click on `/predict` endpoint
4. Click "Try it out"
5. Fill in the request body
6. Click "Execute"
7. View the response

## 🏗 Project Architecture

```
┌─────────────────┐
│  Streamlit UI   │  (Frontend - Port 8501)
│   (ui_app.py)   │
└────────┬────────┘
         │ HTTP POST
         │ requests
         ▼
┌─────────────────┐
│  FastAPI App    │  (Backend - Port 8000)
│    (app.py)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Pydantic       │  (Data Validation)
│  Schemas        │
│ (schemas/house) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Model Loader   │  (core/utility.py)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PKL Model      │  (models/house_price_model.pkl)
│  (Random Forest)│
└─────────────────┘
```

## 🔧 Configuration

### Changing API Port

Edit `app.py`:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Change port here
```

### Changing Streamlit Port

```bash
streamlit run ui_app.py --server.port 8502
```

### Changing API URL in Streamlit

Edit `ui_app.py`:

```python
API_URL = "http://localhost:8000"  # Change this
```

## 🐛 Troubleshooting

### Issue: Model file not found
**Error**: `Model does not found`

**Solution**: Ensure `models/house_price_model.pkl` exists in the project directory.

### Issue: Connection refused
**Error**: `Connection refused` or `Cannot connect to API`

**Solution**: 
1. Make sure FastAPI server is running on port 8000
2. Check if the port is already in use: `lsof -i :8000` (macOS/Linux) or `netstat -ano | findstr :8000` (Windows)
3. Verify the API URL in `ui_app.py` matches the FastAPI server URL

### Issue: CORS errors
**Error**: CORS policy errors in browser console

**Solution**: The CORS middleware is already configured in `app.py`. Ensure `http://localhost:8501` is in the allowed origins.

### Issue: Validation errors
**Error**: Pydantic validation errors

**Solution**: 
- Check that all required fields are provided
- Ensure field types match (e.g., `area` is a float, not a string)
- Verify categorical fields use correct values ("yes"/"no" for binary fields)

## 📝 Notes

- The model expects specific feature order and encoding. The Pydantic validators ensure data is in the correct format.
- All categorical fields are automatically normalized to lowercase by validators.
- The model file (`house_price_model.pkl`) should be trained with the same feature engineering pipeline used during training.

## 🚀 Future Enhancements

- [ ] Add authentication/authorization
- [ ] Implement model versioning
- [ ] Add prediction history/logging
- [ ] Create Docker containerization
- [ ] Add unit tests
- [ ] Implement caching for predictions
- [ ] Add model retraining capabilities
- [ ] Create batch prediction UI

## 📄 License

This project is for educational purposes.

## 👨‍💻 Author

Professional Coder - House Price Prediction System

---

**Happy Predicting! 🏠💰**

