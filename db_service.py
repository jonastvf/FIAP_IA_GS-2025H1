class FakeCursor:
    def __init__(self, db_storage):
        self.db_storage = db_storage
        self.last_query = None
    
    def execute(self, query, values=None):
        self.last_query = query.strip().upper()
        # Simular INSERTs
        if self.last_query.startswith("INSERT INTO AREA_MONITORADA"):
            nova = {
                'id': len(self.db_storage['AREA_MONITORADA']) + 1,
                'nome_area_monitorada': values[0],
                'declividade_encosta': values[1],
                'tipo_solo': values[2],
                'coordenadas_lat': values[3],
                'coordenadas_lng': values[4],
                'presenca_agua_subterranea': values[5],
                'nivel_agua_profundidade_mt': values[6],
                'pressao_media_poros_kpa': values[7],
                'condicoes_vegetacao': values[8],
            }
            self.db_storage['AREA_MONITORADA'].append(nova)
        
        elif self.last_query.startswith("INSERT INTO ALERTAS_DISPARADOS"):
            nova = {
                'id': len(self.db_storage['ALERTAS_DISPARADOS']) + 1,
                'id_area_monitorada1': values[0],
                'timestamp_alerta': values[1],
                'pessoas_alertadas': values[2],
                'efetividade_alerta': values[3],
                'acao_alerta': values[4],
            }
            self.db_storage['ALERTAS_DISPARADOS'].append(nova)
        
        elif self.last_query.startswith("INSERT INTO SENSOR_UMIDADE"):
            nova = {
                'id': len(self.db_storage['SENSOR_UMIDADE']) + 1,
                'id_area_monitorada': values[0],
                'timestamp_medicao': values[1],
                'umidade_percentual': values[2],
                'temperatura_celsius': values[3],
                'status_bateria_sensor': values[4],
                'lat_sensor': values[5],
                'lng_sensor': values[6],
            }
            self.db_storage['SENSOR_UMIDADE'].append(nova)

        elif self.last_query.startswith("INSERT INTO CLIMA_AREA"):
            nova = {
                'id': len(self.db_storage['CLIMA_AREA']) + 1,
                'id_area_monitorada': values[0],
                'tipo_microclima': values[1],
                'timestamp_previsao_climatica': values[2],
                'precipitacao_esperada': values[3],
                'temperatura_esperada': values[4],
                'condicoes_climaticas_esperadas': values[5],
            }
            self.db_storage['CLIMA_AREA'].append(nova)
        
        elif self.last_query.startswith("INSERT INTO DOMICILIOS_AREA"):
            nova = {
                'id': len(self.db_storage['DOMICILIOS_AREA']) + 1,
                'id_area_monitorada': values[0],
                'lat_domicilio': values[1],
                'lng_domicilio': values[2],
                'condicao_ocupacao': values[3],
                'material_edificacao': values[4],
                'grau_exposicao_risco': values[5],
                'tipo_risco_exposicao': values[6],
            }
            self.db_storage['DOMICILIOS_AREA'].append(nova)
        
        elif self.last_query.startswith("INSERT INTO PESSOA_DOMICILIO"):
            nova = {
                'id': len(self.db_storage['PESSOA_DOMICILIO']) + 1,
                'id_domicilio1': values[0],
                'id_area_monitorada': values[1],
                'cpf_pessoa': values[2],
                'nome_pessoa': values[3],
                'pessoa_pcd': values[4],
                'tipo_necessidade_especial': values[5],
                'user_login_app': values[6],
                'contato_primario': values[7],
                'telefone_celular': values[8],
            }
            self.db_storage['PESSOA_DOMICILIO'].append(nova)
        
        elif self.last_query.startswith("INSERT INTO INCIDENTES_REGISTRADOS"):
            nova = {
                'id': len(self.db_storage['INCIDENTES_REGISTRADOS']) + 1,
                'id_pessoa1': values[0],
                'timestamp_incidente': values[1],
                'tipo_incidente_reportado': values[2],
                'lat_local_incidente': values[3],
                'lng_local_incidente': values[4],
                'id_domicilio': values[5],
                'id_area_monitorada': values[6],
            }
            self.db_storage['INCIDENTES_REGISTRADOS'].append(nova)
        
        elif self.last_query.startswith("INSERT INTO SENSOR_VENTO"):
            nova = {
                'id': len(self.db_storage['SENSOR_VENTO']) + 1,
                'id_area_monitorada': values[0],
                'timestamp_medicao': values[1],
                'velocidade_ms': values[2],
                'direcao_vento_graus': values[3],
                'status_bateria_sensor': values[4],
                'lat_sensor': values[5],
                'lng_sensor': values[6],
            }
            self.db_storage['SENSOR_VENTO'].append(nova)
        
        elif self.last_query.startswith("INSERT INTO SENSOR_VIBRACAO"):
            nova = {
                'id': len(self.db_storage['SENSOR_VIBRACAO']) + 1,
                'id_area_monitorada': values[0],
                'timestamp_medicao': values[1],
                'aceleracao_vibracao_ms2': values[2],
                'frequencia_vibracao_hz': values[3],
                'status_bateria_sensor': values[4],
                'lat_sensor': values[5],
                'lng_sensor': values[6],
            }
            self.db_storage['SENSOR_VIBRACAO'].append(nova)
        
        elif self.last_query.startswith("INSERT INTO SENSOR_PLUVIOMETRICO"):
            nova = {
                'id': len(self.db_storage['SENSOR_PLUVIOMETRICO']) + 1,
                'id_area_monitorada': values[0],
                'timestamp_medicao': values[1],
                'precipitacao_mm': values[2],
                'status_bateria_sensor': values[3],
                'lat_sensor': values[4],
                'lng_sensor': values[5],
            }
            self.db_storage['SENSOR_PLUVIOMETRICO'].append(nova)
        
        else:
            # Pode ignorar outras queries ou lançar exceção se quiser
            pass

    def fetchall(self):
        if self.last_query.startswith("SELECT * FROM AREA_MONITORADA"):
            return self.db_storage['AREA_MONITORADA']
        elif self.last_query.startswith("SELECT * FROM ALERTAS_DISPARADOS"):
            return self.db_storage['ALERTAS_DISPARADOS']
        elif self.last_query.startswith("SELECT * FROM SENSOR_UMIDADE"):
            return self.db_storage['SENSOR_UMIDADE']
        elif self.last_query.startswith("SELECT * FROM CLIMA_AREA"):
            return self.db_storage['CLIMA_AREA']
        elif self.last_query.startswith("SELECT * FROM DOMICILIOS_AREA"):
            return self.db_storage['DOMICILIOS_AREA']
        elif self.last_query.startswith("SELECT * FROM PESSOA_DOMICILIO"):
            return self.db_storage['PESSOA_DOMICILIO']
        elif self.last_query.startswith("SELECT * FROM INCIDENTES_REGISTRADOS"):
            return self.db_storage['INCIDENTES_REGISTRADOS']
        elif self.last_query.startswith("SELECT * FROM SENSOR_VENTO"):
            return self.db_storage['SENSOR_VENTO']
        elif self.last_query.startswith("SELECT * FROM SENSOR_VIBRACAO"):
            return self.db_storage['SENSOR_VIBRACAO']
        elif self.last_query.startswith("SELECT * FROM SENSOR_PLUVIOMETRICO"):
            return self.db_storage['SENSOR_PLUVIOMETRICO']
        else:
            return []

class FakeConnection:
    def commit(self):
        pass  # Não faz nada porque é fake

class Database:
    def __init__(self):
        self.db_storage = {
            'AREA_MONITORADA': [],
            'ALERTAS_DISPARADOS': [],
            'SENSOR_UMIDADE': [],
            'CLIMA_AREA': [],
            'DOMICILIOS_AREA': [],
            'PESSOA_DOMICILIO': [],
            'INCIDENTES_REGISTRADOS': [],
            'SENSOR_VENTO': [],
            'SENSOR_VIBRACAO': [],
            'SENSOR_PLUVIOMETRICO': [],
        }
        self.cursor = FakeCursor(self.db_storage)
        self.conn = FakeConnection()
