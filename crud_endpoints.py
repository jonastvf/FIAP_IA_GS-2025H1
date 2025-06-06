from flask import Flask, request, jsonify
from db_service import Database
from datetime import datetime

app = Flask(__name__)
db = Database()

@app.route('/')
def home():
    return "API de Alertas SMD"

@app.route('/test-db')
def test_db():
    return jsonify({"teste-db": True})

# ---------------------- CRUD: AREA_MONITORADA ----------------------
@app.route('/area_monitorada', methods=['POST'])
def create_area():
    data = request.get_json()
    query = """
        INSERT INTO AREA_MONITORADA 
        (nome_area_monitorada, declividade_encosta, tipo_solo, coordenadas_lat, coordenadas_lng, 
        presenca_agua_subterranea, nivel_agua_profundidade_mt, pressao_media_poros_kPa, condicoes_vegetacao)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['nome_area_monitorada'], data['declividade_encosta'], data['tipo_solo'],
        data['coordenadas_lat'], data['coordenadas_lng'], data['presenca_agua_subterranea'],
        data['nivel_agua_profundidade_mt'], data['pressao_media_poros_kPa'], data['condicoes_vegetacao']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Área monitorada inserida"})

@app.route('/area_monitorada', methods=['GET'])
def get_areas():
    db.cursor.execute("SELECT * FROM AREA_MONITORADA")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: ALERTAS_DISPARADOS ----------------------
@app.route('/alertas_disparados', methods=['POST'])
def create_alerta():
    data = request.get_json()
    query = """
        INSERT INTO ALERTAS_DISPARADOS 
        (id_area_monitorada1, timestamp_alerta, pessoas_alertadas, efetividade_alerta, acao_alerta)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        data['id_area_monitorada1'], data['timestamp_alerta'], data['pessoas_alertadas'],
        data['efetividade_alerta'], data['acao_alerta']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Alerta disparado inserido"})

@app.route('/alertas_disparados', methods=['GET'])
def get_alertas():
    db.cursor.execute("SELECT * FROM ALERTAS_DISPARADOS")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: SENSOR_UMIDADE ----------------------
@app.route('/sensor_umidade', methods=['POST'])
def create_sensor_umidade():
    data = request.get_json()
    query = """
        INSERT INTO SENSOR_UMIDADE 
        (id_area_monitorada, timestamp_medicao, umidade_percentual, temperatura_celsius, status_bateria_sensor, lat_sensor, lng_sensor)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_area_monitorada'], data['timestamp_medicao'], data['umidade_percentual'],
        data['temperatura_celsius'], data['status_bateria_sensor'], data['lat_sensor'], data['lng_sensor']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Sensor de umidade inserido"})

@app.route('/sensor_umidade', methods=['GET'])
def get_sensor_umidade():
    db.cursor.execute("SELECT * FROM SENSOR_UMIDADE")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: CLIMA_AREA ----------------------
@app.route('/clima_area', methods=['POST'])
def create_clima():
    data = request.get_json()
    query = """
        INSERT INTO CLIMA_AREA 
        (id_area_monitorada, tipo_microclima, timestamp_previsao_climatica, precipitacao_esperada,
        temperatura_esperada, condicoes_climaticas_esperadas)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_area_monitorada'], data['tipo_microclima'], data['timestamp_previsao_climatica'],
        data['precipitacao_esperada'], data['temperatura_esperada'], data['condicoes_climaticas_esperadas']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Clima inserido"})

@app.route('/clima_area', methods=['GET'])
def get_clima():
    db.cursor.execute("SELECT * FROM CLIMA_AREA")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: DOMICILIOS_AREA ----------------------
@app.route('/domicilios_area', methods=['POST'])
def create_domicilio():
    data = request.get_json()
    query = """
        INSERT INTO DOMICILIOS_AREA 
        (id_area_monitorada, lat_domicilio, lng_domicilio, condicao_ocupacao, material_edificacao,
        grau_exposicao_risco, tipo_risco_exposicao)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_area_monitorada'], data['lat_domicilio'], data['lng_domicilio'],
        data['condicao_ocupacao'], data['material_edificacao'], data['grau_exposicao_risco'],
        data['tipo_risco_exposicao']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Domicílio inserido"})

@app.route('/domicilios_area', methods=['GET'])
def get_domicilios():
    db.cursor.execute("SELECT * FROM DOMICILIOS_AREA")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: PESSOA_DOMICILIO ----------------------
@app.route('/pessoa_domicilio', methods=['POST'])
def create_pessoa():
    data = request.get_json()
    query = """
        INSERT INTO PESSOA_DOMICILIO 
        (id_domicilio1, id_area_monitorada, cpf_pessoa, nome_pessoa, pessoa_pcd,
        tipo_necessidade_especial, user_login_app, contato_primario, telefone_celular)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_domicilio1'], data['id_area_monitorada'], data['cpf_pessoa'], data['nome_pessoa'],
        data['pessoa_pcd'], data['tipo_necessidade_especial'], data['user_login_app'],
        data['contato_primario'], data['telefone_celular']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Pessoa inserida"})

@app.route('/pessoa_domicilio', methods=['GET'])
def get_pessoas():
    db.cursor.execute("SELECT * FROM PESSOA_DOMICILIO")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: INCIDENTES_REGISTRADOS ----------------------
@app.route('/incidentes_registrados', methods=['POST'])
def create_incidente():
    data = request.get_json()
    query = """
        INSERT INTO INCIDENTES_REGISTRADOS 
        (id_pessoa1, timestamp_incidente, tipo_incidente_reportado, lat_local_incidente, lng_local_incidente,
        id_domicilio, id_area_monitorada)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_pessoa1'], data['timestamp_incidente'], data['tipo_incidente_reportado'],
        data['lat_local_incidente'], data['lng_local_incidente'], data['id_domicilio'], data['id_area_monitorada']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Incidente registrado"})

@app.route('/incidentes_registrados', methods=['GET'])
def get_incidentes():
    db.cursor.execute("SELECT * FROM INCIDENTES_REGISTRADOS")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: SENSOR_VENTO ----------------------
@app.route('/sensor_vento', methods=['POST'])
def create_sensor_vento():
    data = request.get_json()
    query = """
        INSERT INTO SENSOR_VENTO 
        (id_area_monitorada, timestamp_medicao, velocidade_ms, direcao_vento_graus, status_bateria_sensor,
        lat_sensor, lng_sensor)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_area_monitorada'], data['timestamp_medicao'], data['velocidade_ms'],
        data['direcao_vento_graus'], data['status_bateria_sensor'], data['lat_sensor'], data['lng_sensor']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Sensor de vento inserido"})

@app.route('/sensor_vento', methods=['GET'])
def get_sensor_vento():
    db.cursor.execute("SELECT * FROM SENSOR_VENTO")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: SENSOR_VIBRACAO ----------------------
@app.route('/sensor_vibracao', methods=['POST'])
def create_sensor_vibracao():
    data = request.get_json()
    query = """
        INSERT INTO SENSOR_VIBRACAO 
        (id_area_monitorada, timestamp_medicao, aceleracao_vibracao_ms2, frequencia_vibracao_Hz,
        status_bateria_sensor, lat_sensor, lng_sensor)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_area_monitorada'], data['timestamp_medicao'], data['aceleracao_vibracao_ms2'],
        data['frequencia_vibracao_Hz'], data['status_bateria_sensor'], data['lat_sensor'], data['lng_sensor']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Sensor de vibração inserido"})

@app.route('/sensor_vibracao', methods=['GET'])
def get_sensor_vibracao():
    db.cursor.execute("SELECT * FROM SENSOR_VIBRACAO")
    return jsonify(db.cursor.fetchall())

# ---------------------- CRUD: SENSOR_PLUVIOMETRICO ----------------------
@app.route('/sensor_pluviometrico', methods=['POST'])
def create_sensor_pluviometrico():
    data = request.get_json()
    query = """
        INSERT INTO SENSOR_PLUVIOMETRICO 
        (id_area_monitorada, timestamp_medicao, precipitacao_mm, status_bateria_sensor, lat_sensor, lng_sensor)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_area_monitorada'], data['timestamp_medicao'], data['precipitacao_mm'],
        data['status_bateria_sensor'], data['lat_sensor'], data['lng_sensor']
    )
    db.cursor.execute(query, values)
    db.conn.commit()
    return jsonify({"status": "Sensor pluviométrico inserido"})

@app.route('/sensor_pluviometrico', methods=['GET'])
def get_sensor_pluviometrico():
    db.cursor.execute("SELECT * FROM SENSOR_PLUVIOMETRICO")
    return jsonify(db.cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')