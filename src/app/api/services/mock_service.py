import datetime

areas_monitoradas = [
    {
        "id_area_monitorada": 1,
        "nome_area_monitorada": "Petrópolis - RJ",
        "declividade_encosta": 32.5,
        "tipo_solo": "argiloso",
        "coordenadas_lat": -22.5043,
        "coordenadas_lng": -43.1785,
        "presenca_agua_subterranea": "presente",
        "nivel_agua_profundidade_mt": 4.2,
        "pressao_media_poros_kPa": 120.7,
        "condicoes_vegetacao": "Vegetação densa com presença de mata atlântica nativa."
    },
    {
        "id_area_monitorada": 2,
        "nome_area_monitorada": "Chapada dos Guimarães - MT",
        "declividade_encosta": 18.0,
        "tipo_solo": "arenoso",
        "coordenadas_lat": -15.4542,
        "coordenadas_lng": -55.7499,
        "presenca_agua_subterranea": "ausente",
        "nivel_agua_profundidade_mt": 15.8,
        "pressao_media_poros_kPa": 65.2,
        "condicoes_vegetacao": "Cerrado típico com vegetação rasteira e arbustiva."
    },
    {
        "id_area_monitorada": 3,
        "nome_area_monitorada": "Blumenau - SC",
        "declividade_encosta": 22.4,
        "tipo_solo": "argiloso",
        "coordenadas_lat": -26.9154,
        "coordenadas_lng": -49.0704,
        "presenca_agua_subterranea": "presente",
        "nivel_agua_profundidade_mt": 6.3,
        "pressao_media_poros_kPa": 97.1,
        "condicoes_vegetacao": "Vegetação mista de áreas urbanizadas e mata secundária."
    },
    {
        "id_area_monitorada": 4,
        "nome_area_monitorada": "Juazeiro do Norte - CE",
        "declividade_encosta": 12.8,
        "tipo_solo": "arenoso",
        "coordenadas_lat": -7.2133,
        "coordenadas_lng": -39.3155,
        "presenca_agua_subterranea": "ausente",
        "nivel_agua_profundidade_mt": 20.5,
        "pressao_media_poros_kPa": 52.0,
        "condicoes_vegetacao": "Vegetação semiárida com predominância de caatinga."
    },
    {
        "id_area_monitorada": 5,
        "nome_area_monitorada": "Nova Friburgo - RJ",
        "declividade_encosta": 35.0,
        "tipo_solo": "argiloso",
        "coordenadas_lat": -22.2868,
        "coordenadas_lng": -42.5311,
        "presenca_agua_subterranea": "presente",
        "nivel_agua_profundidade_mt": 3.7,
        "pressao_media_poros_kPa": 110.3,
        "condicoes_vegetacao": "Encostas com vegetação densa e presença de plantações em áreas altas."
    },
    {
        "id_area_monitorada": 6,
        "nome_area_monitorada": "São Roque - SP",
        "declividade_encosta": 25.6,
        "tipo_solo": "misto",
        "coordenadas_lat": -23.5288,
        "coordenadas_lng": -47.1363,
        "presenca_agua_subterranea": "presente",
        "nivel_agua_profundidade_mt": 5.4,
        "pressao_media_poros_kPa": 102.5,
        "condicoes_vegetacao": "Mata ciliar e vegetação remanescente da mata atlântica."
    },
    {
        "id_area_monitorada": 7,
        "nome_area_monitorada": "Campos do Jordão - SP",
        "declividade_encosta": 40.0,
        "tipo_solo": "argiloso",
        "coordenadas_lat": -22.7383,
        "coordenadas_lng": -45.5923,
        "presenca_agua_subterranea": "presente",
        "nivel_agua_profundidade_mt": 2.9,
        "pressao_media_poros_kPa": 134.8,
        "condicoes_vegetacao": "Floresta de altitude com vegetação bem preservada."
    },
    {
        "id_area_monitorada": 8,
        "nome_area_monitorada": "Itabira - MG",
        "declividade_encosta": 28.5,
        "tipo_solo": "rochosos",
        "coordenadas_lat": -19.6245,
        "coordenadas_lng": -43.2318,
        "presenca_agua_subterranea": "ausente",
        "nivel_agua_profundidade_mt": 11.7,
        "pressao_media_poros_kPa": 78.3,
        "condicoes_vegetacao": "Vegetação impactada por mineração e reflorestamentos isolados."
    },
    {
        "id_area_monitorada": 9,
        "nome_area_monitorada": "Paraty - RJ",
        "declividade_encosta": 30.2,
        "tipo_solo": "misto",
        "coordenadas_lat": -23.2221,
        "coordenadas_lng": -44.7176,
        "presenca_agua_subterranea": "presente",
        "nivel_agua_profundidade_mt": 4.9,
        "pressao_media_poros_kPa": 106.2,
        "condicoes_vegetacao": "Mata atlântica preservada com áreas de mangue próximas."
    },
    {
        "id_area_monitorada": 10,
        "nome_area_monitorada": "São João del-Rei - MG",
        "declividade_encosta": 20.1,
        "tipo_solo": "argiloso",
        "coordenadas_lat": -21.1357,
        "coordenadas_lng": -44.2582,
        "presenca_agua_subterranea": "ausente",
        "nivel_agua_profundidade_mt": 9.2,
        "pressao_media_poros_kPa": 88.9,
        "condicoes_vegetacao": "Vegetação típica de cerrado de altitude, com campos limpos e cerradões."
    },
]

clima_areas = [
    {
        "id_clima": 1,
        "id_area_monitorada": 1,
        "tipo_microclima": 2.5,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 80.0,
        "temperatura_esperada": 21.4,
        "condicoes_climaticas_esperadas": "chuva"
    },
    {
        "id_clima": 2,
        "id_area_monitorada": 2,
        "tipo_microclima": 1.2,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 5.0,
        "temperatura_esperada": 32.1,
        "condicoes_climaticas_esperadas": "seco"
    },
    {
        "id_clima": 3,
        "id_area_monitorada": 3,
        "tipo_microclima": 2.1,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 40.5,
        "temperatura_esperada": 24.7,
        "condicoes_climaticas_esperadas": "nublado"
    },
    {
        "id_clima": 4,
        "id_area_monitorada": 4,
        "tipo_microclima": 1.0,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 0.0,
        "temperatura_esperada": 34.2,
        "condicoes_climaticas_esperadas": "seco"
    },
    {
        "id_clima": 5,
        "id_area_monitorada": 5,
        "tipo_microclima": 2.9,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 92.3,
        "temperatura_esperada": 20.1,
        "condicoes_climaticas_esperadas": "chuva"
    },
    {
        "id_clima": 6,
        "id_area_monitorada": 6,
        "tipo_microclima": 2.2,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 55.0,
        "temperatura_esperada": 23.5,
        "condicoes_climaticas_esperadas": "nublado"
    },
    {
        "id_clima": 7,
        "id_area_monitorada": 7,
        "tipo_microclima": 3.3,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 75.4,
        "temperatura_esperada": 17.8,
        "condicoes_climaticas_esperadas": "chuva"
    },
    {
        "id_clima": 8,
        "id_area_monitorada": 8,
        "tipo_microclima": 1.7,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 18.5,
        "temperatura_esperada": 28.6,
        "condicoes_climaticas_esperadas": "instável"
    },
    {
        "id_clima": 9,
        "id_area_monitorada": 9,
        "tipo_microclima": 3.1,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 90.0,
        "temperatura_esperada": 22.2,
        "condicoes_climaticas_esperadas": "chuva"
    },
    {
        "id_clima": 10,
        "id_area_monitorada": 10,
        "tipo_microclima": 2.0,
        "timestamp_previsao_climatica": "2025-06-06",
        "precipitacao_esperada": 25.0,
        "temperatura_esperada": 26.3,
        "condicoes_climaticas_esperadas": "nublado"
    },
]

domicilios_area = [
    {
        "id_domicilio": 1,
        "id_area_monitorada": 1,  # Petrópolis - RJ
        "lat_domicilio": -22.5040,
        "lng_domicilio": -43.1790,
        "condicao_ocupacao": "regular",
        "material_edificacao": "alvenaria",
        "grau_exposicao_risco": 3,
        "tipo_risco_exposicao": "deslizamento"
    },
    {
        "id_domicilio": 2,
        "id_area_monitorada": 2,  # Chapada dos Guimarães - MT
        "lat_domicilio": -15.4545,
        "lng_domicilio": -55.7490,
        "condicao_ocupacao": "regular",
        "material_edificacao": "madeira",
        "grau_exposicao_risco": 1,
        "tipo_risco_exposicao": "incêndio"
    },
    {
        "id_domicilio": 3,
        "id_area_monitorada": 3,  # Blumenau - SC
        "lat_domicilio": -26.9150,
        "lng_domicilio": -49.0701,
        "condicao_ocupacao": "irregular",
        "material_edificacao": "mista",
        "grau_exposicao_risco": 2,
        "tipo_risco_exposicao": "inundação"
    },
    {
        "id_domicilio": 4,
        "id_area_monitorada": 4,  # Juazeiro do Norte - CE
        "lat_domicilio": -7.2130,
        "lng_domicilio": -39.3150,
        "condicao_ocupacao": "regular",
        "material_edificacao": "taipa",
        "grau_exposicao_risco": 2,
        "tipo_risco_exposicao": "calor_extremo"
    },
    {
        "id_domicilio": 5,
        "id_area_monitorada": 5,  # Nova Friburgo - RJ
        "lat_domicilio": -22.2865,
        "lng_domicilio": -42.5310,
        "condicao_ocupacao": "irregular",
        "material_edificacao": "alvenaria",
        "grau_exposicao_risco": 4,
        "tipo_risco_exposicao": "deslizamento"
    },
    {
        "id_domicilio": 6,
        "id_area_monitorada": 6,  # São Roque - SP
        "lat_domicilio": -23.5285,
        "lng_domicilio": -47.1360,
        "condicao_ocupacao": "regular",
        "material_edificacao": "alvenaria",
        "grau_exposicao_risco": 2,
        "tipo_risco_exposicao": "erosão"
    },
    {
        "id_domicilio": 7,
        "id_area_monitorada": 7,  # Campos do Jordão - SP
        "lat_domicilio": -22.7380,
        "lng_domicilio": -45.5920,
        "condicao_ocupacao": "irregular",
        "material_edificacao": "mista",
        "grau_exposicao_risco": 3,
        "tipo_risco_exposicao": "deslizamento"
    },
    {
        "id_domicilio": 8,
        "id_area_monitorada": 8,  # Itabira - MG
        "lat_domicilio": -19.6248,
        "lng_domicilio": -43.2310,
        "condicao_ocupacao": "regular",
        "material_edificacao": "alvenaria",
        "grau_exposicao_risco": 1,
        "tipo_risco_exposicao": "vazamento_mineral"
    },
    {
        "id_domicilio": 9,
        "id_area_monitorada": 9,  # Paraty - RJ
        "lat_domicilio": -23.2220,
        "lng_domicilio": -44.7170,
        "condicao_ocupacao": "irregular",
        "material_edificacao": "taipa",
        "grau_exposicao_risco": 3,
        "tipo_risco_exposicao": "inundação"
    },
    {
        "id_domicilio": 10,
        "id_area_monitorada": 10,  # São João del-Rei - MG
        "lat_domicilio": -21.1355,
        "lng_domicilio": -44.2580,
        "condicao_ocupacao": "regular",
        "material_edificacao": "alvenaria",
        "grau_exposicao_risco": 2,
        "tipo_risco_exposicao": "erosão"
    },
]


pessoas_domicilio = [
    {
        "id_pessoa": 1,
        "id_domicilio1": 1,
        "id_area_monitorada": 1,
        "cpf_pessoa": 12345678901,
        "nome_pessoa": "Carlos",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "carlos01",
        "contato_primario": "carlos01",
        "telefone_celular": "21999990001"
    },
    {
        "id_pessoa": 2,
        "id_domicilio1": 1,
        "id_area_monitorada": 1,
        "cpf_pessoa": 12345678902,
        "nome_pessoa": "Ana",
        "pessoa_pcd": "sim",
        "tipo_necessidade_especial": "visual",
        "user_login_app": "ana_01",
        "contato_primario": "ana_01",
        "telefone_celular": "21999990002"
    },
    {
        "id_pessoa": 3,
        "id_domicilio1": 2,
        "id_area_monitorada": 2,
        "cpf_pessoa": 22345678901,
        "nome_pessoa": "Joao",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "joao02",
        "contato_primario": "joao02",
        "telefone_celular": "65999990001"
    },
    {
        "id_pessoa": 4,
        "id_domicilio1": 2,
        "id_area_monitorada": 2,
        "cpf_pessoa": 22345678902,
        "nome_pessoa": "Lia",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "lia02",
        "contato_primario": "lia02",
        "telefone_celular": "65999990002"
    },
    {
        "id_pessoa": 5,
        "id_domicilio1": 3,
        "id_area_monitorada": 3,
        "cpf_pessoa": 32345678901,
        "nome_pessoa": "Tadeu",
        "pessoa_pcd": "sim",
        "tipo_necessidade_especial": "motora",
        "user_login_app": "tadeu03",
        "contato_primario": "tadeu03",
        "telefone_celular": "47999990001"
    },
    {
        "id_pessoa": 6,
        "id_domicilio1": 3,
        "id_area_monitorada": 3,
        "cpf_pessoa": 32345678902,
        "nome_pessoa": "Marina",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "marina03",
        "contato_primario": "marina03",
        "telefone_celular": "47999990002"
    },
    {
        "id_pessoa": 7,
        "id_domicilio1": 3,
        "id_area_monitorada": 3,
        "cpf_pessoa": 32345678903,
        "nome_pessoa": "Nina",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "nina03",
        "contato_primario": "nina03",
        "telefone_celular": "47999990003"
    },
    {
        "id_pessoa": 8,
        "id_domicilio1": 4,
        "id_area_monitorada": 4,
        "cpf_pessoa": 42345678901,
        "nome_pessoa": "Rafa",
        "pessoa_pcd": "sim",
        "tipo_necessidade_especial": "auditiva",
        "user_login_app": "rafa04",
        "contato_primario": "rafa04",
        "telefone_celular": "88999990001"
    },
    {
        "id_pessoa": 9,
        "id_domicilio1": 5,
        "id_area_monitorada": 5,
        "cpf_pessoa": 52345678901,
        "nome_pessoa": "Lucas",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "lucas05",
        "contato_primario": "lucas05",
        "telefone_celular": "22999990001"
    },
    {
        "id_pessoa": 10,
        "id_domicilio1": 5,
        "id_area_monitorada": 5,
        "cpf_pessoa": 52345678902,
        "nome_pessoa": "Joana",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "joana05",
        "contato_primario": "joana05",
        "telefone_celular": "22999990002"
    },
    {
        "id_pessoa": 11,
        "id_domicilio1": 6,
        "id_area_monitorada": 6,
        "cpf_pessoa": 62345678901,
        "nome_pessoa": "Tiago",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "tiago06",
        "contato_primario": "tiago06",
        "telefone_celular": "11999990001"
    },
    {
        "id_pessoa": 12,
        "id_domicilio1": 7,
        "id_area_monitorada": 7,
        "cpf_pessoa": 72345678901,
        "nome_pessoa": "Duda",
        "pessoa_pcd": "sim",
        "tipo_necessidade_especial": "visual",
        "user_login_app": "duda07",
        "contato_primario": "duda07",
        "telefone_celular": "11999990002"
    },
    {
        "id_pessoa": 13,
        "id_domicilio1": 8,
        "id_area_monitorada": 8,
        "cpf_pessoa": 82345678901,
        "nome_pessoa": "Beto",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "beto08",
        "contato_primario": "beto08",
        "telefone_celular": "31999990001"
    },
    {
        "id_pessoa": 14,
        "id_domicilio1": 9,
        "id_area_monitorada": 9,
        "cpf_pessoa": 92345678901,
        "nome_pessoa": "Carol",
        "pessoa_pcd": "sim",
        "tipo_necessidade_especial": "motora",
        "user_login_app": "carol09",
        "contato_primario": "carol09",
        "telefone_celular": "24999990001"
    },
    {
        "id_pessoa": 15,
        "id_domicilio1": 10,
        "id_area_monitorada": 10,
        "cpf_pessoa": 10345678901,
        "nome_pessoa": "Enzo",
        "pessoa_pcd": "nao",
        "tipo_necessidade_especial": "",
        "user_login_app": "enzo10",
        "contato_primario": "enzo10",
        "telefone_celular": "32999990001"
    }
]

sensor_pluviometrico = [
    {'id_sensor_pluviometrico': 1, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.56, 'lat_sensor': -22.50386769525138, 'lng_sensor': -43.178550699341855},
    {'id_sensor_pluviometrico': 2, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.12, 'lat_sensor': -22.50416103441663, 'lng_sensor': -43.17826173278396},
    {'id_sensor_pluviometrico': 3, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 3.88, 'lat_sensor': -22.5040805526411, 'lng_sensor': -43.17880666164481},
    {'id_sensor_pluviometrico': 4, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.98, 'lat_sensor': -22.50394652083115, 'lng_sensor': -43.17835747056695},
    {'id_sensor_pluviometrico': 5, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.59, 'lat_sensor': -22.503865997074193, 'lng_sensor': -43.178505082843955},
    {'id_sensor_pluviometrico': 6, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.09, 'lat_sensor': -22.504697702790693, 'lng_sensor': -43.17883813123638},
    {'id_sensor_pluviometrico': 7, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.03, 'lat_sensor': -22.504503367723146, 'lng_sensor': -43.17820580091035},
    {'id_sensor_pluviometrico': 8, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 3.99, 'lat_sensor': -22.504764081064028, 'lng_sensor': -43.17869381481245},
    {'id_sensor_pluviometrico': 9, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 3.95, 'lat_sensor': -22.50448109314883, 'lng_sensor': -43.17829906004745},
    {'id_sensor_pluviometrico': 10, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.07, 'lat_sensor': -22.504405628389534, 'lng_sensor': -43.17824786063692},
    {'id_sensor_pluviometrico': 11, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 3.55, 'lat_sensor': -22.504095494033187, 'lng_sensor': -43.17889699323439},
    {'id_sensor_pluviometrico': 12, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.95, 'lat_sensor': -22.50449869686509, 'lng_sensor': -43.17806945626416},
    {'id_sensor_pluviometrico': 13, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.93, 'lat_sensor': -22.504758064846147, 'lng_sensor': -43.17817468923202},
    {'id_sensor_pluviometrico': 14, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.71, 'lat_sensor': -22.504131745036716, 'lng_sensor': -43.17880222038484},
    {'id_sensor_pluviometrico': 15, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.52, 'lat_sensor': -22.50394388194717, 'lng_sensor': -43.178397619385265},
    {'id_sensor_pluviometrico': 16, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 3.79, 'lat_sensor': -22.504368248986914, 'lng_sensor': -43.17882860136241},
    {'id_sensor_pluviometrico': 17, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.09, 'lat_sensor': -22.50461284347068, 'lng_sensor': -43.178657571587486},
    {'id_sensor_pluviometrico': 18, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.04, 'lat_sensor': -22.5046612192235, 'lng_sensor': -43.17831833721352},
    {'id_sensor_pluviometrico': 19, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.05, 'lat_sensor': -22.504496108971797, 'lng_sensor': -43.178813501323106},
    {'id_sensor_pluviometrico': 20, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.06, 'lat_sensor': -22.50419858334539, 'lng_sensor': -43.178750878452256},
    {'id_sensor_pluviometrico': 21, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.87, 'lat_sensor': -22.504204397855098, 'lng_sensor': -43.178165810990066},
    {'id_sensor_pluviometrico': 22, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.1, 'lat_sensor': -22.503984001239505, 'lng_sensor': -43.17822649540564},
    {'id_sensor_pluviometrico': 23, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 4.07, 'lat_sensor': -22.504203593517996, 'lng_sensor': -43.17868722051933},
    {'id_sensor_pluviometrico': 24, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 3.68, 'lat_sensor': -22.503979151891254, 'lng_sensor': -43.17821348885099},
    {'id_sensor_pluviometrico': 25, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 4.12, 'lat_sensor': -22.503938771826963, 'lng_sensor': -43.17879424290058},
    {'id_sensor_pluviometrico': 26, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 3.92, 'lat_sensor': -22.504135827967943, 'lng_sensor': -43.1780722994513},
    {'id_sensor_pluviometrico': 27, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.6, 'lat_sensor': -22.504463424516434, 'lng_sensor': -43.17839771250932},
    {'id_sensor_pluviometrico': 28, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 1.5, 'status_bateria_sensor': 3.94, 'lat_sensor': -22.504412074095775, 'lng_sensor': -43.178735782448335},
    {'id_sensor_pluviometrico': 29, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.72, 'lat_sensor': -22.50415031710174, 'lng_sensor': -43.17869843904692},
    {'id_sensor_pluviometrico': 30, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'precipitacao_mm': 0.0, 'status_bateria_sensor': 3.6, 'lat_sensor': -22.50408586501443, 'lng_sensor': -43.17899057278506},
]

sensor_umidade = [
    {'id_sensor_umidade': 1, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 30.5, 'status_bateria_sensor': 3.56, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50386769525138, 'lng_sensor': -43.178550699341855},
    {'id_sensor_umidade': 2, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 30.5, 'status_bateria_sensor': 4.12, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50416103441663, 'lng_sensor': -43.17826173278396},
    {'id_sensor_umidade': 3, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 56.5, 'status_bateria_sensor': 3.88, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.5040805526411, 'lng_sensor': -43.17880666164481},
    {'id_sensor_umidade': 4, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 27.5, 'status_bateria_sensor': 3.98, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50394652083115, 'lng_sensor': -43.17835747056695},
    {'id_sensor_umidade': 5, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 27.5, 'status_bateria_sensor': 3.59, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.503865997074193, 'lng_sensor': -43.178505082843955},
    {'id_sensor_umidade': 6, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 48.0, 'status_bateria_sensor': 4.09, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504697702790693, 'lng_sensor': -43.17883813123638},
    {'id_sensor_umidade': 7, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 67.5, 'status_bateria_sensor': 4.03, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504503367723146, 'lng_sensor': -43.17820580091035},
    {'id_sensor_umidade': 8, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 75.5, 'status_bateria_sensor': 3.99, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504764081064028, 'lng_sensor': -43.17869381481245},
    {'id_sensor_umidade': 9, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 75.5, 'status_bateria_sensor': 3.95, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50448109314883, 'lng_sensor': -43.17829906004745},
    {'id_sensor_umidade': 10, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 75.5, 'status_bateria_sensor': 4.07, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504405628389534, 'lng_sensor': -43.17824786063692},
    {'id_sensor_umidade': 11, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 100.0, 'status_bateria_sensor': 3.55, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504095494033187, 'lng_sensor': -43.17889699323439},
    {'id_sensor_umidade': 12, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 100.0, 'status_bateria_sensor': 3.95, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50449869686509, 'lng_sensor': -43.17806945626416},
    {'id_sensor_umidade': 13, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 77.0, 'status_bateria_sensor': 3.93, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504758064846147, 'lng_sensor': -43.17817468923202},
    {'id_sensor_umidade': 14, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 77.0, 'status_bateria_sensor': 3.71, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504131745036716, 'lng_sensor': -43.17880222038484},
    {'id_sensor_umidade': 15, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 77.0, 'status_bateria_sensor': 3.52, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50394388194717, 'lng_sensor': -43.178397619385265},
    {'id_sensor_umidade': 16, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 77.0, 'status_bateria_sensor': 3.79, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504368248986914, 'lng_sensor': -43.17882860136241},
    {'id_sensor_umidade': 17, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 77.0, 'status_bateria_sensor': 4.09, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50461284347068, 'lng_sensor': -43.178657571587486},
    {'id_sensor_umidade': 18, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 43.0, 'status_bateria_sensor': 4.04, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.5046612192235, 'lng_sensor': -43.17831833721352},
    {'id_sensor_umidade': 19, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 43.0, 'status_bateria_sensor': 4.05, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504496108971797, 'lng_sensor': -43.178813501323106},
    {'id_sensor_umidade': 20, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 79.5, 'status_bateria_sensor': 4.06, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50419858334539, 'lng_sensor': -43.178750878452256},
    {'id_sensor_umidade': 21, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 23.0, 'status_bateria_sensor': 3.87, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504204397855098, 'lng_sensor': -43.178165810990066},
    {'id_sensor_umidade': 22, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 23.0, 'status_bateria_sensor': 4.1, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.503984001239505, 'lng_sensor': -43.17822649540564},
    {'id_sensor_umidade': 23, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 38.5, 'status_bateria_sensor': 4.07, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504203593517996, 'lng_sensor': -43.17868722051933},
    {'id_sensor_umidade': 24, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 92.5, 'status_bateria_sensor': 3.68, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.503979151891254, 'lng_sensor': -43.17821348885099},
    {'id_sensor_umidade': 25, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 79.5, 'status_bateria_sensor': 4.12, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.503938771826963, 'lng_sensor': -43.17879424290058},
    {'id_sensor_umidade': 26, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 79.5, 'status_bateria_sensor': 3.92, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504135827967943, 'lng_sensor': -43.1780722994513},
    {'id_sensor_umidade': 27, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 77.5, 'status_bateria_sensor': 3.6, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504463424516434, 'lng_sensor': -43.17839771250932},
    {'id_sensor_umidade': 28, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 75.5, 'status_bateria_sensor': 3.94, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.504412074095775, 'lng_sensor': -43.178735782448335},
    {'id_sensor_umidade': 29, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 94.0, 'status_bateria_sensor': 3.72, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50415031710174, 'lng_sensor': -43.17869843904692},
    {'id_sensor_umidade': 30, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'vwc_conteudo_volumetrico_agua_perc': 13.5, 'status_bateria_sensor': 3.6, 'profundidade_sensor_cm': 50.0, 'lat_sensor': -22.50408586501443, 'lng_sensor': -43.17899057278506},
]

sensor_vento = [
    {'id_sensor_vento': 1, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1001, 'direcao_vento_graus': 339, 'status_bateria_sensor': 3.56, 'lat_sensor': -22.50386769525138, 'lng_sensor': -43.178550699341855},
    {'id_sensor_vento': 2, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1001, 'direcao_vento_graus': 150, 'status_bateria_sensor': 4.12, 'lat_sensor': -22.50416103441663, 'lng_sensor': -43.17826173278396},
    {'id_sensor_vento': 3, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 797, 'direcao_vento_graus': 159, 'status_bateria_sensor': 3.88, 'lat_sensor': -22.5040805526411, 'lng_sensor': -43.17880666164481},
    {'id_sensor_vento': 4, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 122, 'direcao_vento_graus': 185, 'status_bateria_sensor': 3.98, 'lat_sensor': -22.50394652083115, 'lng_sensor': -43.17835747056695},
    {'id_sensor_vento': 5, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 122, 'direcao_vento_graus': 217, 'status_bateria_sensor': 3.59, 'lat_sensor': -22.503865997074193, 'lng_sensor': -43.178505082843955},
    {'id_sensor_vento': 6, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 122, 'direcao_vento_graus': 178, 'status_bateria_sensor': 4.09, 'lat_sensor': -22.504697702790693, 'lng_sensor': -43.17883813123638},
    {'id_sensor_vento': 7, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 610, 'direcao_vento_graus': 190, 'status_bateria_sensor': 4.03, 'lat_sensor': -22.504503367723146, 'lng_sensor': -43.17820580091035},
    {'id_sensor_vento': 8, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 3717, 'direcao_vento_graus': 228, 'status_bateria_sensor': 3.99, 'lat_sensor': -22.504764081064028, 'lng_sensor': -43.17869381481245},
    {'id_sensor_vento': 9, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 3717, 'direcao_vento_graus': 229, 'status_bateria_sensor': 3.95, 'lat_sensor': -22.50448109314883, 'lng_sensor': -43.17829906004745},
    {'id_sensor_vento': 10, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 3717, 'direcao_vento_graus': 342, 'status_bateria_sensor': 4.07, 'lat_sensor': -22.504405628389534, 'lng_sensor': -43.17824786063692},
    {'id_sensor_vento': 11, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 2340, 'direcao_vento_graus': 276, 'status_bateria_sensor': 3.55, 'lat_sensor': -22.504095494033187, 'lng_sensor': -43.17889699323439},
    {'id_sensor_vento': 12, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1622, 'direcao_vento_graus': 353, 'status_bateria_sensor': 3.95, 'lat_sensor': -22.50449869686509, 'lng_sensor': -43.17806945626416},
    {'id_sensor_vento': 13, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1622, 'direcao_vento_graus': 208, 'status_bateria_sensor': 3.93, 'lat_sensor': -22.504758064846147, 'lng_sensor': -43.17817468923202},
    {'id_sensor_vento': 14, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1622, 'direcao_vento_graus': 182, 'status_bateria_sensor': 3.71, 'lat_sensor': -22.504131745036716, 'lng_sensor': -43.17880222038484},
    {'id_sensor_vento': 15, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1622, 'direcao_vento_graus': 4, 'status_bateria_sensor': 3.52, 'lat_sensor': -22.50394388194717, 'lng_sensor': -43.178397619385265},
    {'id_sensor_vento': 16, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1622, 'direcao_vento_graus': 89, 'status_bateria_sensor': 3.79, 'lat_sensor': -22.504368248986914, 'lng_sensor': -43.17882860136241},
    {'id_sensor_vento': 17, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1622, 'direcao_vento_graus': 216, 'status_bateria_sensor': 4.09, 'lat_sensor': -22.50461284347068, 'lng_sensor': -43.178657571587486},
    {'id_sensor_vento': 18, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 219, 'direcao_vento_graus': 315, 'status_bateria_sensor': 4.04, 'lat_sensor': -22.5046612192235, 'lng_sensor': -43.17831833721352},
    {'id_sensor_vento': 19, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 1654, 'direcao_vento_graus': 283, 'status_bateria_sensor': 4.05, 'lat_sensor': -22.504496108971797, 'lng_sensor': -43.178813501323106},
    {'id_sensor_vento': 20, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 2742, 'direcao_vento_graus': 358, 'status_bateria_sensor': 4.06, 'lat_sensor': -22.50419858334539, 'lng_sensor': -43.178750878452256},
    {'id_sensor_vento': 21, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 435, 'direcao_vento_graus': 104, 'status_bateria_sensor': 3.87, 'lat_sensor': -22.504204397855098, 'lng_sensor': -43.178165810990066},
    {'id_sensor_vento': 22, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 435, 'direcao_vento_graus': 86, 'status_bateria_sensor': 4.1, 'lat_sensor': -22.503984001239505, 'lng_sensor': -43.17822649540564},
    {'id_sensor_vento': 23, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 2242, 'direcao_vento_graus': 288, 'status_bateria_sensor': 4.07, 'lat_sensor': -22.504203593517996, 'lng_sensor': -43.17868722051933},
    {'id_sensor_vento': 24, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 3969, 'direcao_vento_graus': 327, 'status_bateria_sensor': 3.68, 'lat_sensor': -22.503979151891254, 'lng_sensor': -43.17821348885099},
    {'id_sensor_vento': 25, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 3728, 'direcao_vento_graus': 101, 'status_bateria_sensor': 4.12, 'lat_sensor': -22.503938771826963, 'lng_sensor': -43.17879424290058},
    {'id_sensor_vento': 26, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 3728, 'direcao_vento_graus': 116, 'status_bateria_sensor': 3.92, 'lat_sensor': -22.504135827967943, 'lng_sensor': -43.1780722994513},
    {'id_sensor_vento': 27, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 4028, 'direcao_vento_graus': 86, 'status_bateria_sensor': 3.6, 'lat_sensor': -22.504463424516434, 'lng_sensor': -43.17839771250932},
    {'id_sensor_vento': 28, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 3875, 'direcao_vento_graus': 11, 'status_bateria_sensor': 3.94, 'lat_sensor': -22.504412074095775, 'lng_sensor': -43.178735782448335},
    {'id_sensor_vento': 29, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 2593, 'direcao_vento_graus': 289, 'status_bateria_sensor': 3.72, 'lat_sensor': -22.50415031710174, 'lng_sensor': -43.17869843904692},
    {'id_sensor_vento': 30, 'id_area_monitorada': 1, 'timestamp_medicao': datetime.date(2025, 6, 4), 'velocidade_ms': 111, 'direcao_vento_graus': 42, 'status_bateria_sensor': 3.6, 'lat_sensor': -22.50408586501443, 'lng_sensor': -43.17899057278506},
]
alertas_disparados = [
    {
        "id_alerta": 1,
        "id_area_monitorada1": 1,
        "timestamp_alerta": datetime.date(2025, 6, 4),
        "pessoas_alertadas": 19.0,
        "efetividade_alerta": "baixa",
        "acao_alerta": "isolamento"
    },
    {
        "id_alerta": 2,
        "id_area_monitorada1": 1,
        "timestamp_alerta": datetime.date(2025, 6, 4),
        "pessoas_alertadas": 20.0,
        "efetividade_alerta": "média",
        "acao_alerta": "isolamento"
    },
    {
        "id_alerta": 3,
        "id_area_monitorada1": 1,
        "timestamp_alerta": datetime.date(2025, 6, 4),
        "pessoas_alertadas": 12.0,
        "efetividade_alerta": "média",
        "acao_alerta": "isolamento"
    },
    {
        "id_alerta": 4,
        "id_area_monitorada1": 1,
        "timestamp_alerta": datetime.date(2025, 6, 4),
        "pessoas_alertadas": 8.0,
        "efetividade_alerta": "alta",
        "acao_alerta": "evacuacao"
    },
    {
        "id_alerta": 5,
        "id_area_monitorada1": 1,
        "timestamp_alerta": datetime.date(2025, 6, 4),
        "pessoas_alertadas": 11.0,
        "efetividade_alerta": "média",
        "acao_alerta": "isolamento"
    }
]

incidentes_registrados = [
    {
        "id_incidente_reportado": 1,
        "id_pessoa1": 7,
        "timestamp_incidente": datetime.date(2025, 6, 4),
        "tipo_incidente_reportado": "erosao",
        "lat_local_incidente": -22.504862,
        "lng_local_incidente": -43.178132,
        "id_domicilio": 1,
        "id_area_monitorada": 1
    },
    {
        "id_incidente_reportado": 2,
        "id_pessoa1": 7,
        "timestamp_incidente": datetime.date(2025, 6, 4),
        "tipo_incidente_reportado": "inundacao",
        "lat_local_incidente": -22.504133,
        "lng_local_incidente": -43.178587,
        "id_domicilio": 1,
        "id_area_monitorada": 1
    },
    {
        "id_incidente_reportado": 3,
        "id_pessoa1": 15,
        "timestamp_incidente": datetime.date(2025, 6, 4),
        "tipo_incidente_reportado": "deslizamento",
        "lat_local_incidente": -22.503464,
        "lng_local_incidente": -43.178211,
        "id_domicilio": 1,
        "id_area_monitorada": 1
    },
]
