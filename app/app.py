from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "test CI/CD"


@app.route('/health')
def health_check():
    """Эндпоинт для проверки здоровья сервиса (health check)."""
    return jsonify(status="OK"), 200


@app.route('/metrics')
def metrics():
    metrics_data = (
        "# HELP fake_metric A fake metric for demonstration\n"
        "# TYPE fake_metric gauge\n"
        "fake_metric 100\n"
    )
    return metrics_data, 200, {'Content-Type': 'text/plain; version=0.0.4'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
