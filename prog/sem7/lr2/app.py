from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

# Статические курсы валют для демонстрации
EXCHANGE_RATES = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 110.0,
    'CAD': 1.25,
    'AUD': 1.35,
    'CHF': 0.92,
    'CNY': 6.45,
}


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/v1/currencies', methods=['GET'])
def get_currencies():
    currencies = {
        code: name for code, name in [
            ('USD', 'United States Dollar'),
            ('EUR', 'Euro'),
            ('GBP', 'British Pound'),
            ('JPY', 'Japanese Yen'),
            ('CAD', 'Canadian Dollar'),
            ('AUD', 'Australian Dollar'),
        ]
    }
    return jsonify({
        'success': True,
        'data': currencies
    })


@app.route('/api/v1/convert', methods=['POST'])
def convert_currency():
    try:
        data = request.get_json()

        amount = float(data.get('amount', 0))
        from_currency = data.get('from', 'USD').upper()
        to_currency = data.get('to', 'EUR').upper()

        if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
            return jsonify({
                'success': False,
                'error': 'Unsupported currency'
            }), 400

        # Простая конвертация
        from_rate = EXCHANGE_RATES[from_currency]
        to_rate = EXCHANGE_RATES[to_currency]
        converted_amount = (amount / from_rate) * to_rate

        return jsonify({
            'success': True,
            'data': {
                'from_amount': amount,
                'from_currency': from_currency,
                'to_amount': round(converted_amount, 2),
                'to_currency': to_currency,
                'exchange_rate': round(to_rate / from_rate, 4),
                'timestamp': datetime.now().isoformat()
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/api/v1/rates', methods=['GET'])
def get_rates():
    base = request.args.get('base', 'USD').upper()

    if base not in EXCHANGE_RATES:
        return jsonify({
            'success': False,
            'error': 'Unsupported base currency'
        }), 400

    base_rate = EXCHANGE_RATES[base]
    rates = {
        currency: round(rate / base_rate, 4)
        for currency, rate in EXCHANGE_RATES.items()
    }

    return jsonify({
        'success': True,
        'data': {
            'base': base,
            'rates': rates
        }
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)