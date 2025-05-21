# Insurance Claim Prediction Project

This project is a machine learning application that predicts insurance claims using a Random Forest classifier. It includes both the model training pipeline and a web interface for making predictions.

## Features

- Data preprocessing pipeline
- Machine learning model training using Random Forest
- Web interface for making predictions
- REST API endpoints for programmatic access

## Project Structure

```
├── data/                    # Data directory
│   └── insurance.csv        # Insurance dataset
├── models/                  # Trained model storage
│   └── trained_model.joblib # Saved model
├── src/                     # Source code
│   ├── api/                # FastAPI web application
│   ├── preprocessing/      # Data preprocessing modules
│   └── training/          # Model training scripts
├── static/                 # Static web assets
├── templates/              # HTML templates
└── requirements.txt        # Python dependencies
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python -m src.training.model_trainer
   ```
4. Run the web application:
   ```bash
   uvicorn src.api.app:app --reload
   ```

## Usage

Access the web interface at `http://localhost:8000` after starting the server.

## Model Performance

The current model achieves:
- Accuracy: 96%
- Precision: 97%
- Recall: 92%
- F1 Score: 95%
- ROC AUC: 95%

## License

MIT License