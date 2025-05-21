from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
import pathlib
import sys

app = FastAPI()

# Add CORS middleware
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the absolute paths and set up paths
current_dir = pathlib.Path(__file__).resolve().parent
root_dir = current_dir.parent.parent
model_path = root_dir / 'models' / 'trained_model.joblib'
static_dir = root_dir / 'static'
templates_dir = root_dir / 'templates'

# Print debug information
print(f"Starting server with:")
print(f"- Current directory: {current_dir}")
print(f"- Root directory: {root_dir}")
print(f"- Templates directory: {templates_dir}")
print(f"- Static directory: {static_dir}")

# Verify directories and files
for path, name in [
    (templates_dir, "Templates directory"),
    (static_dir, "Static directory"),
    (model_path, "Model file"),
    (templates_dir / "index.html", "Index template")
]:
    if not path.exists():
        raise RuntimeError(f"{name} not found: {path}")
    print(f"Found {name}: {path}")

# Load the trained model
try:
    model = joblib.load(model_path)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    raise

# Initialize FastAPI app
app = FastAPI(
    title="Health Insurance Claim Predictor",
    description="Predict health insurance claims using machine learning",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "https://health-insurance-classifier.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Mount static files
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Setup templates
templates = Jinja2Templates(directory=str(templates_dir))

class InputData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

@app.post("/predict")
async def predict(data: InputData):
    try:
        # Create region encoding
        regions = ['northeast', 'northwest', 'southeast', 'southwest']
        region_encoded = [1 if data.region == r else 0 for r in regions[1:]]  # One-hot encoding, drop first category
        
        # Prepare the input data for prediction
        input_data = [[
            data.age,
            1 if data.sex == 'male' else 0,  # Encode sex
            data.bmi,
            data.children,
            1 if data.smoker == 'yes' else 0,  # Encode smoker
            *region_encoded  # Unpack encoded region values
        ]]
        
        # Make prediction
        prediction = model.predict(input_data)
        return {"claim": int(prediction[0])}
    except Exception as e:
        import traceback
        print(f"Prediction error: {str(e)}")
        print(traceback.format_exc())
        raise

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        return templates.TemplateResponse(
            "index.html",
            {"request": request}
        )
    except Exception as e:
        import traceback
        print(f"Error rendering template: {str(e)}")
        print(traceback.format_exc())
        return HTMLResponse(
            content=f"""
            <html>
                <body>
                    <h1>Debug Information</h1>
                    <pre>
                    Current directory: {current_dir}
                    Template directory: {templates_dir}
                    Template exists: {(templates_dir / "index.html").exists()}
                    Error: {str(e)}
                    </pre>
                </body>
            </html>
            """,
            status_code=500
        )
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Setup templates
templates = Jinja2Templates(directory=str(templates_dir))

class InputData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

@app.post("/predict")
async def predict(data: InputData):
    try:
        # Create region encoding
        regions = ['northeast', 'northwest', 'southeast', 'southwest']
        region_encoded = [1 if data.region == r else 0 for r in regions[1:]]  # One-hot encoding, drop first category
        
        # Prepare the input data for prediction
        input_data = [[
            data.age,
            1 if data.sex == 'male' else 0,  # Encode sex
            data.bmi,
            data.children,
            1 if data.smoker == 'yes' else 0,  # Encode smoker
            *region_encoded  # Unpack encoded region values
        ]]
        
        # Make prediction
        prediction = model.predict(input_data)
        return {"claim": int(prediction[0])}  # Return 1 for claim, 0 for no claim
    except Exception as e:
        import traceback
        print(f"Prediction error: {str(e)}")
        print(traceback.format_exc())
        raise

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        print("Attempting to render index.html template")
        template_path = templates_dir / "index.html"
        print(f"Template exists: {template_path.exists()}")
        
        response = templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "debug": {
                    "template_dir": str(templates_dir),
                    "static_dir": str(static_dir)
                }
            }
        )
        print("Template rendered successfully")
        return response
    except Exception as e:
        import traceback
        print(f"Error rendering template: {str(e)}")
        print(traceback.format_exc())
        return HTMLResponse(
            content=f"""
            <html>
                <body>
                    <h1>Debug Information</h1>
                    <pre>
                    Current directory: {current_dir}
                    Template directory: {templates_dir}
                    Template exists: {(templates_dir / "index.html").exists()}
                    Error: {str(e)}
                    </pre>
                </body>
            </html>
            """,
            status_code=500
        )