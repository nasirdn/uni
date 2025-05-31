from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Загрузка модели и скейлера
model = joblib.load('wine_quality_model.pkl')
scaler = joblib.load('scaler.pkl')
imputer = joblib.load('imputer.pkl')

# Ожидаемые признаки в правильном порядке
EXPECTED_FEATURES = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol'
]


@app.route('/')
def home():
    return render_template('index.html', features=EXPECTED_FEATURES)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получаем данные из формы
        data = request.form.to_dict()

        # Создаем DataFrame с правильным порядком признаков
        input_data = pd.DataFrame({feat: [float(data.get(feat, 0))] for feat in EXPECTED_FEATURES})

        # Предобработка данных
        input_data = imputer.transform(input_data)
        input_data = scaler.transform(input_data)

        # Предсказание
        prediction = model.predict(input_data)

        return render_template('index.html',
                               prediction_text=f'Предсказанное качество вина: {prediction[0]}',
                               features=EXPECTED_FEATURES)

    except Exception as e:
        return render_template('index.html',
                               prediction_text=f'Ошибка: {str(e)}',
                               features=EXPECTED_FEATURES)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')