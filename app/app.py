# from flask import Flask, request, jsonify, render_template
# import pickle
# import numpy as np
# import os
# app = Flask(__name__)

# # Učitaj model
# if os.path.exists('app\model.pkl'):
#     with open('app\model.pkl', 'rb') as f:
#         model = pickle.load(f)
# else:
#     print("model.pkl not found.")

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.json
#         input_data = np.array([data['parameters']])
#         prediction = model.predict(input_data)
#         result = "Malignant (M)" if prediction[0] == 1 else "Benign (B)"
#         return jsonify({'diagnosis': result})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from app.routes import main  # Importovanje ruta

def create_app():
    app = Flask(__name__)

    # Registracija blueprinta
    app.register_blueprint(main)

    # Mogu se dodati dodatne konfiguracije ovdje
    return app

# Pokretanje aplikacije samo ako se direktno pokreće `app.py`
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
