# Health Insurance Classifier

This project is a machine learning application designed to predict whether an individual is likely to file a health insurance claim based on various features. The model is trained using historical insurance data and is deployed as a web service that allows users to input their information and receive predictions in real time.

## Project Structure

- **data/**: Contains the raw insurance data used for training the model.
  - `insurance.csv`: The dataset with features such as age, sex, bmi, children, smoker, region, and charges.

- **models/**: Stores the trained machine learning model.
  - `trained_model.joblib`: The serialized model ready for deployment.

- **src/**: Contains the source code for data processing, model training, and the web API.
  - **preprocessing/**: Includes scripts for data preprocessing.
    - `data_processor.py`: Functions for cleaning, normalization, and feature encoding.
  - **training/**: Responsible for training the machine learning model.
    - `model_trainer.py`: Contains model selection, training, and evaluation metrics.
  - **api/**: Implements the web service.
    - `app.py`: Provides endpoints for user input and model predictions.

- **static/**: Contains static files for the frontend.
  - **css/**: Styles for the user interface.
    - `style.css`: CSS styles for the application.
  - **js/**: JavaScript code for frontend functionality.
    - `main.js`: Handles user input and API requests.

- **templates/**: Contains HTML templates for the frontend.
  - `index.html`: The main user interface for data input.

- **requirements.txt**: Lists the dependencies required for the project.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/solus-tzm/HealthInsuranceMachine.git
   cd health-insurance-classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the web service:
   ```
   uvicorn src.api.app:app --reload --host 0.0.0.0 --port 8000
   ```

4. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

- Input your details (age, sex, bmi, children, smoker, region) in the provided fields.
- Click on the submit button to receive a prediction on whether you are likely to file a claim (1 for yes, 0 for no).

## Model Information

The model is trained using various machine learning algorithms and evaluated based on accuracy, precision, recall, F1-score, and ROC-AUC metrics. The best-performing model is saved and used for predictions in the web service.

## API Endpoints

- **POST /predict**: Accepts user input and returns the prediction result.

## License

The project was made by `1tzme`