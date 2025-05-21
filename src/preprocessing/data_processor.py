import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Create the 'claim' target variable
    threshold = 10000
    data['claim'] = (data['charges'] > threshold).astype(int)
    
    # Drop the 'charges' column as it's no longer needed
    data = data.drop(columns=['charges'])
    
    # Normalize 'bmi'
    data['bmi'] = (data['bmi'] - data['bmi'].mean()) / data['bmi'].std()
    
    # Encode categorical features
    data = pd.get_dummies(data, columns=['sex', 'smoker', 'region'], drop_first=True)
    
    return data

def split_data(data):
    from sklearn.model_selection import train_test_split
    X = data.drop(columns=['claim'])
    y = data['claim']
    return train_test_split(X, y, test_size=0.2, random_state=42)