from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "API de Alertas SMD"

@app.route('/test-db')
def test_db():
        return jsonify({"teste-db": True})