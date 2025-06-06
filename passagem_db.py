import pandas as pd
import mysql.connector
from datetime import datetime

# Conexão com banco MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="smd_db"
)
cursor = conn.cursor()

# Carregar dados da planilha
df = pd.read_excel("dados.xlsx", sheet_name="Página1", skiprows=1)
df.columns = [
    "DataHora", "Hora_ESP32", "Temperatura", "Umidade", "Chuva", "Vento",
    "Vibracao_X", "Vibracao_Y", "Vibracao_Z"
]

# Limpeza de dados
df["DataHora"] = pd.to_datetime(df["DataHora"], errors='coerce')
df["Chuva"] = df["Chuva"].astype(str).str.lower().map({"true": 1, "false": 0})

# Remover linhas com dados essenciais ausentes
df = df.dropna(subset=["DataHora", "Umidade", "Chuva", "Vento", "Vibracao_X", "Vibracao_Y", "Vibracao_Z"])

# Inserção nas tabelas
for _, row in df.iterrows():
    timestamp = row["DataHora"].to_pydatetime()  # Preserva data e hora
    id_area = 1  # fixo conforme seu pedido
    lat, lng = -23.0000000, -46.0000000
    bateria = 3.7  # valor simulado

    # SENSOR_UMIDADE
    cursor.execute("""
        INSERT INTO SENSOR_UMIDADE (id_area_monitorada, timestamp_medicao, vwc_conteudo_volumetrico_agua_perc,
        status_bateria_sensor, profundidade_sensor_cm, lat_sensor, lng_sensor)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (id_area, timestamp, row["Umidade"], bateria, 10, lat, lng))

    # SENSOR_PLUVIOMETRICO
    cursor.execute("""
        INSERT INTO SENSOR_PLUVIOMETRICO (id_area_monitorada, timestamp_medicao, precipitacao_mm,
        status_bateria_sensor, lat_sensor, lng_sensor)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (id_area, timestamp, row["Chuva"], bateria, lat, lng))

    # SENSOR_VENTO
    cursor.execute("""
        INSERT INTO SENSOR_VENTO (id_area_monitorada, timestamp_medicao, velocidade_ms,
        direcao_vento_graus, status_bateria_sensor, lat_sensor, lng_sensor)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (id_area, timestamp, row["Vento"], 180, bateria, lat, lng))

    # SENSOR_VIBRACAO
    aceleracao_x = row["Vibracao_X"]
    aceleracao_y = row["Vibracao_Y"]
    aceleracao_z = row["Vibracao_Z"]
    forca_vetorial = (aceleracao_x**2 + aceleracao_y**2 + aceleracao_z**2)**0.5

    cursor.execute("""
        INSERT INTO SENSOR_VIBRACAO (id_area_monitorada, timestamp_medicao, aceleracao_eixo_x,
        aceleracao_eixo_y, aceleracao_eixo_z, forca_vetorial_vibracao, status_bateria_sensor, lat_sensor, lng_sensor)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (id_area, timestamp, aceleracao_x, aceleracao_y, aceleracao_z, forca_vetorial, bateria, lat, lng))

# Finalizar
conn.commit()
cursor.close()
conn.close()

print(f"{len(df)} registros inseridos com sucesso.")
