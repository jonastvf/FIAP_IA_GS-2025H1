
-- Script de Criação de Tabelas baseado no XMLA

DROP TABLE IF EXISTS SENSOR_VIBRACAO;
DROP TABLE IF EXISTS SENSOR_VENTO;
DROP TABLE IF EXISTS SENSOR_UMIDADE;
DROP TABLE IF EXISTS SENSOR_PLUVIOMETRICO;
DROP TABLE IF EXISTS INCIDENTES_REGISTRADOS;
DROP TABLE IF EXISTS PESSOA_DOMICILIO;
DROP TABLE IF EXISTS DOMICILIOS_AREA;
DROP TABLE IF EXISTS CLIMA_AREA;
DROP TABLE IF EXISTS ALERTAS_DISPARADOS;
DROP TABLE IF EXISTS AREA_MONITORADA;

CREATE TABLE AREA_MONITORADA (
    id_area_monitorada INT PRIMARY KEY AUTO_INCREMENT,
    declividade_encosta DOUBLE,
    tipo_solo VARCHAR(10),
    coordenadas_gps INT,
    presenca_agua_subterranea VARCHAR(12),
    nivel_agua_profundidade_mt DOUBLE,
    pressao_media_poros_kPa DOUBLE,
    condicoes_vegetacao TEXT
);

CREATE TABLE ALERTAS_DISPARADOS (
    id_alerta INT PRIMARY KEY AUTO_INCREMENT,
    id_area_monitorada1 INT,
    timestamp_alerta DATE,
    pessoas_alertadas DOUBLE,
    efetividade_alerta VARCHAR(15),
    acao_alerta VARCHAR(12),
    FOREIGN KEY (id_area_monitorada1) REFERENCES AREA_MONITORADA(id_area_monitorada)
);

CREATE TABLE CLIMA_AREA (
    id_clima INT PRIMARY KEY AUTO_INCREMENT,
    id_area_monitorada INT,
    tipo_microclima DOUBLE,
    timestamp_previsao_climatica DATE,
    precipitacao_esperada DOUBLE,
    temperatura_esperada DOUBLE,
    condicoes_climaticas_esperadas VARCHAR(10),
    FOREIGN KEY (id_area_monitorada) REFERENCES AREA_MONITORADA(id_area_monitorada)
);

CREATE TABLE DOMICILIOS_AREA (
    id_domicilio INT PRIMARY KEY AUTO_INCREMENT,
    id_area_monitorada INT,
    coordenadas_gps INT,
    condicao_ocupacao VARCHAR(255),
    material_edificacao VARCHAR(255),
    grau_exposicao_risco INT,
    tipo_risco_exposicao VARCHAR(15),
    FOREIGN KEY (id_area_monitorada) REFERENCES AREA_MONITORADA(id_area_monitorada)
);

CREATE TABLE PESSOA_DOMICILIO (
    id_pessoa INT PRIMARY KEY AUTO_INCREMENT,
    id_domicilio1 INT,
    id_area_monitorada INT,
    cpf_pessoa INT,
    nome_pessoa VARCHAR(10),
    pessoa_pcd VARCHAR(12),
    tipo_necessidade_especial VARCHAR(15),
    user_login_app VARCHAR(15),
    contato_primario VARCHAR(15),
    telefone_celular VARCHAR(15),
    FOREIGN KEY (id_domicilio1) REFERENCES DOMICILIOS_AREA(id_domicilio),
    FOREIGN KEY (id_area_monitorada) REFERENCES AREA_MONITORADA(id_area_monitorada)
);

CREATE TABLE INCIDENTES_REGISTRADOS (
    id_incidente_reportado INT PRIMARY KEY AUTO_INCREMENT,
    id_pessoa1 INT,
    timestamp_incidente DATE,
    tipo_incidente_reportado VARCHAR(12),
    coordenadas_local_incidente INT,
    id_domicilio INT,
    id_area_monitorada INT,
    FOREIGN KEY (id_pessoa1) REFERENCES PESSOA_DOMICILIO(id_pessoa),
    FOREIGN KEY (id_domicilio) REFERENCES DOMICILIOS_AREA(id_domicilio),
    FOREIGN KEY (id_area_monitorada) REFERENCES AREA_MONITORADA(id_area_monitorada)
);

CREATE TABLE SENSOR_PLUVIOMETRICO (
    id_sensor_pluviometrico INT PRIMARY KEY AUTO_INCREMENT,
    id_area_monitorada INT,
    timestamp_medicao DATE,
    precipitacao_mm FLOAT,
    status_bateria_sensor DOUBLE,
    coordenadas_sensor INT,
    FOREIGN KEY (id_area_monitorada) REFERENCES AREA_MONITORADA(id_area_monitorada)
);

CREATE TABLE SENSOR_UMIDADE (
    id_sensor_umidade INT PRIMARY KEY AUTO_INCREMENT,
    id_area_monitorada INT,
    timestamp_medicao DATE,
    vwc_conteudo_volumetrico_agua_perc DOUBLE,
    status_bateria_sensor DOUBLE,
    profundidade_sensor_cm DOUBLE,
    coordenadas_sensor INT,
    FOREIGN KEY (id_area_monitorada) REFERENCES AREA_MONITORADA(id_area_monitorada)
);

CREATE TABLE SENSOR_VENTO (
    id_sensor_vento INT PRIMARY KEY AUTO_INCREMENT,
    id_area_monitorada INT,
    timestamp_medicao DATE,
    velocidade_ms FLOAT,
    direcao_vento_graus INT,
    status_bateria_sensor DOUBLE,
    coordenadas_sensor INT,
    FOREIGN KEY (id_area_monitorada) REFERENCES AREA_MONITORADA(id_area_monitorada)
);

CREATE TABLE SENSOR_VIBRACAO (
    id_sensor_vibracao INT PRIMARY KEY AUTO_INCREMENT,
    id_area_monitorada INT,
    timestamp_medicao DATE,
    aceleracao_eixo_x DOUBLE,
    aceleracao_eixo_y DOUBLE,
    aceleracao_eixo_z DOUBLE,
    forca_vetorial_vibracao DOUBLE,
    status_bateria_sensor DOUBLE,
    coordenadas_sensor INT,
    FOREIGN KEY (id_area_monitorada) REFERENCES AREA_MONITORADA(id_area_monitorada)
);
