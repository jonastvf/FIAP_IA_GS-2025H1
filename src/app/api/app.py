from flask import Flask, jsonify, render_template
from flask_cors import CORS
from services.alertas_service import get_alertas_formatados
from services.incidentes_service import get_incidentes_formatados

app = Flask(__name__)
CORS(app)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/mapa-de-risco')
def mapa_risco():
    return render_template('mapa_de_risco.html')

@app.route('/api/alertas')
def get_alertas():
    return jsonify(get_alertas_formatados())

@app.route('/api/incidentes')
def get_incidentes():
    return jsonify(get_incidentes_formatados())