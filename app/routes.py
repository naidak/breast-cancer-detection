# from flask import Blueprint, render_template

# main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return render_template('index.html')

from flask import Blueprint, request, jsonify, render_template
import pickle
import numpy as np

main = Blueprint('main', __name__)

# Učitavanje modela
with open('app\model.pkl', 'rb') as f:
    model = pickle.load(f)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    try:
        # Dobijanje JSON podataka iz zahtjeva
        data = request.get_json()
        
        # Redoslijed parametara treba odgovarati redoslijedu kojim je model treniran
        required_features = [
            "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
            "compactness_mean", "concavity_mean", "concave_points_mean", "symmetry_mean",
            "fractal_dimension_mean", "radius_se", "texture_se", "perimeter_se", "area_se",
            "smoothness_se", "compactness_se", "concavity_se", "concave_points_se", "symmetry_se",
            "fractal_dimension_se", "radius_worst", "texture_worst", "perimeter_worst", "area_worst",
            "smoothness_worst", "compactness_worst", "concavity_worst", "concave_points_worst",
            "symmetry_worst", "fractal_dimension_worst"
        ]
        
        # Izvlačenje vrijednosti i kreiranje ulaznog vektora
        input_data = [data[feature] for feature in required_features]
        
        # Predikcija modela
        prediction = model.predict([input_data])
        prediction_label = 'Malignant' if prediction[0] == 1 else 'Benign'
        
        # Slanje odgovora
        return jsonify({'prediction': prediction_label})
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
