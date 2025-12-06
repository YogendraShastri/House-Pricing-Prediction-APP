
import joblib

from .config import MODEL_DIR, HOUSE_MODEL_NAME

def load_model():
    try:
        model = joblib.load(str(MODEL_DIR) + f'/{HOUSE_MODEL_NAME}')
    except Exception as e:
        model = None
        print(f"model load failed : {e}")
    return model