-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2025-06-05 17:49:39 BRT
--   site:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE ALERTAS_DISPARADOS 
    ( 
     id_alerta          INTEGER  NOT NULL , 
     id_area            INTEGER  NOT NULL , 
     timestamp_alerta   TIMESTAMP WITH LOCAL TIME ZONE  NOT NULL , 
     pessoas_alertadas  NUMBER , 
     efetividade_alerta VARCHAR2 (15) , 
     acao_alerta        VARCHAR2 (12 CHAR) 
    ) 
    LOGGING 
;

COMMENT ON COLUMN ALERTAS_DISPARADOS.efetividade_alerta IS 'Se o alerta foi:
- Real
- Falso Positivo
- Outro' 
;

COMMENT ON COLUMN ALERTAS_DISPARADOS.acao_alerta IS 'Ação realizada com alerta:
- Evacuação
- Contenção
- Outra' 
;

ALTER TABLE ALERTAS_DISPARADOS 
    ADD CONSTRAINT PK_ALERTAS_DISPARADOS PRIMARY KEY ( id_alerta, id_area ) ;

CREATE TABLE AREA_MONITORADA 
    ( 
     id_area                    INTEGER  NOT NULL , 
     declividade_encosta        NUMBER , 
     tipo_solo                  VARCHAR2 (10 CHAR) , 
     coordenadas_gps            NUMBER , 
     presenca_agua_subterranea  VARCHAR2 (12 CHAR) , 
     nivel_agua_profundidade_mt NUMBER , 
     pressao_media_poros_kPa    NUMBER , 
     condicoes_vegetacao        UNKNOWN 
--  ERROR: Datatype UNKNOWN is not allowed 
                    
    ) 
    LOGGING 
;

COMMENT ON COLUMN AREA_MONITORADA.condicoes_vegetacao IS 'Descreve as condições da vegetação local como fator de risco ou proteção.' 
;

ALTER TABLE AREA_MONITORADA 
    ADD CONSTRAINT PK_AREA_MONITORADA PRIMARY KEY ( id_area ) ;

CREATE TABLE CLIMA_AREA 
    ( 
     id_clima                       INTEGER  NOT NULL , 
     id_area                        INTEGER  NOT NULL , 
     tipo_microclima                NUMBER (6) , 
     timestamp_previsao_climatica   TIMESTAMP WITH LOCAL TIME ZONE  NOT NULL , 
     precipitacao_esperada          NUMBER (6) , 
     temperatura_esperada           NUMBER (6) , 
     condicoes_climaticas_esperadas VARCHAR2 (10) 
    ) 
    LOGGING 
;

COMMENT ON COLUMN CLIMA_AREA.condicoes_climaticas_esperadas IS 'Neblina, Sol aberto, etc. ' 
;

ALTER TABLE CLIMA_AREA 
    ADD CONSTRAINT PK_CLIMA_AREA PRIMARY KEY ( id_clima ) ;

CREATE TABLE DOMICILIOS_AREA 
    ( 
     id_domicilio         INTEGER  NOT NULL , 
     id_area              INTEGER  NOT NULL , 
     coordenadas_gps      NUMBER , 
     condicao_ocupacao    VARCHAR2 
--  ERROR: VARCHAR2 size not specified 
                    , 
     material_edificacao  VARCHAR2 
--  ERROR: VARCHAR2 size not specified 
                    , 
     grau_exposicao_risco INTEGER , 
     tipo_risco_exposicao VARCHAR2 (15 CHAR) 
    ) 
    LOGGING 
;

COMMENT ON COLUMN DOMICILIOS_AREA.condicao_ocupacao IS 'Condição de ocupação do terreno:
- Regular
- Em processo de reconhecimento de usucapião
- Irregular' 
;

COMMENT ON COLUMN DOMICILIOS_AREA.material_edificacao IS 'Material no qual domicilio foi edificado:
- Alvenaria
- Madeira
- Misto
- Etc.' 
;

COMMENT ON COLUMN DOMICILIOS_AREA.grau_exposicao_risco IS 'Em uma escala de risco, qual grau medido de exposição.
' 
;

ALTER TABLE DOMICILIOS_AREA 
    ADD CONSTRAINT PK_DOMICILIOS_AREA PRIMARY KEY ( id_domicilio, id_area ) ;

CREATE TABLE INCIDENTES_REGISTRADOS 
    ( 
     id_incidente_reportado      INTEGER  NOT NULL , 
     id_pessoa                   INTEGER  NOT NULL , 
     timestamp_incidente         TIMESTAMP WITH LOCAL TIME ZONE  NOT NULL , 
     tipo_incidente_reportado    VARCHAR2 (12) , 
     coordenadas_local_incidente NUMBER , 
     id_domicilio                INTEGER  NOT NULL , 
     id_area                     INTEGER  NOT NULL , 
     id_alerta                   INTEGER  NOT NULL , 
     id_area2                    INTEGER  NOT NULL 
    ) 
    LOGGING 
;

ALTER TABLE INCIDENTES_REGISTRADOS 
    ADD CONSTRAINT PK_INCIDENTES_REGISTRADOS PRIMARY KEY ( id_incidente_reportado ) ;

CREATE TABLE PESSOA_DOMICILIO 
    ( 
     id_pessoa                 INTEGER  NOT NULL , 
     id_domicilio              INTEGER  NOT NULL , 
     id_area                   INTEGER  NOT NULL , 
     cpf_pessoa                INTEGER  NOT NULL , 
     nome_pessoa               VARCHAR2 (10 CHAR)  NOT NULL , 
     pessoa_pcd                VARCHAR2 (12) , 
     tipo_necessidade_especial VARCHAR2 (15 CHAR) , 
     user_login_app            VARCHAR2 (15 CHAR) , 
     contato_primario          VARCHAR2 (15) , 
     telefone_celular          VARCHAR2 (15) 
    ) 
    LOGGING 
;

ALTER TABLE PESSOA_DOMICILIO 
    ADD CONSTRAINT PK_PESSOA_DOMICILIO PRIMARY KEY ( id_pessoa, id_domicilio, id_area ) ;

CREATE TABLE SENSOR_PLUVIOMETRICO 
    ( 
     id_sensor_pluviometrico INTEGER  NOT NULL , 
     id_area                 INTEGER  NOT NULL , 
     timestamp_medicao       TIMESTAMP WITH LOCAL TIME ZONE  NOT NULL , 
     precipitacao_mm         FLOAT , 
     status_bateria_sensor   NUMBER , 
     coordenadas_sensor      NUMBER , 
     latitude_sensor         NUMBER , 
     longiitude_sensor       NUMBER 
    ) 
    LOGGING 
;

ALTER TABLE SENSOR_PLUVIOMETRICO 
    ADD CONSTRAINT PK_SENSOR_PLUVIOMETRICO PRIMARY KEY ( id_sensor_pluviometrico ) ;

CREATE TABLE SENSOR_UMIDADE 
    ( 
     id_sensor_umidade                  INTEGER  NOT NULL , 
     id_area                            INTEGER , 
     timestamp_medicao                  TIMESTAMP WITH LOCAL TIME ZONE  NOT NULL , 
     vwc_conteudo_volumetrico_agua_perc NUMBER , 
     status_bateria_sensor              NUMBER , 
     profundidade_sensor_cm             NUMBER , 
     latitude_sensor                    NUMBER , 
     longitude_sensor                   NUMBER 
    ) 
    LOGGING 
;

COMMENT ON COLUMN SENSOR_UMIDADE.profundidade_sensor_cm IS 'Profundidade de instalação do sensor em centimetros' 
;

ALTER TABLE SENSOR_UMIDADE 
    ADD CONSTRAINT PK_SENSOR_UMIDADE PRIMARY KEY ( id_sensor_umidade ) ;

CREATE TABLE SENSOR_VENTO 
    ( 
     id_sensor_vento       INTEGER  NOT NULL , 
     id_area               INTEGER , 
     timestamp_medicao     TIMESTAMP WITH LOCAL TIME ZONE  NOT NULL , 
     velocidade_ms         FLOAT , 
     direcao_vento_graus   INTEGER , 
     status_bateria_sensor NUMBER , 
     coordenadas_sensor    NUMBER , 
     latitude_sensor       NUMBER , 
     longiitude_sensor     NUMBER 
    ) 
    LOGGING 
;

ALTER TABLE SENSOR_VENTO 
    ADD CONSTRAINT PK_SENSOR_VENTO PRIMARY KEY ( id_sensor_vento ) ;

CREATE TABLE SENSOR_VIBRACAO 
    ( 
     id_sensor_vibracao      INTEGER  NOT NULL , 
     id_area                 INTEGER , 
     timestamp_medicao       TIMESTAMP WITH LOCAL TIME ZONE  NOT NULL , 
     aceleracao_eixo_x       NUMBER , 
     aceleracao_eixo_y       NUMBER , 
     aceleracao_eixo_z       NUMBER , 
     forca_vetorial_vibracao NUMBER , 
     status_bateria_sensor   NUMBER , 
     coordenadas_sensor      NUMBER , 
     latitude_sensor         NUMBER , 
     longiitude_sensor       NUMBER 
    ) 
    LOGGING 
;

COMMENT ON COLUMN SENSOR_VIBRACAO.aceleracao_eixo_x IS 'O sensor funciona com um acelerometro. ' 
;

ALTER TABLE SENSOR_VIBRACAO 
    ADD CONSTRAINT PK_SENSOR_VIBRACAO PRIMARY KEY ( id_sensor_vibracao ) ;

ALTER TABLE ALERTAS_DISPARADOS 
    ADD CONSTRAINT FK_ALERTAS_DISPARADOS_AREA_MONITORADA FOREIGN KEY 
    ( 
     id_area
    ) 
    REFERENCES AREA_MONITORADA 
    ( 
     id_area
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE CLIMA_AREA 
    ADD CONSTRAINT FK_CLIMA_AREA_AREA_MONITORADA FOREIGN KEY 
    ( 
     id_area
    ) 
    REFERENCES AREA_MONITORADA 
    ( 
     id_area
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE DOMICILIOS_AREA 
    ADD CONSTRAINT FK_DOMICILIOS_AREA_AREA_MONITORADA FOREIGN KEY 
    ( 
     id_area
    ) 
    REFERENCES AREA_MONITORADA 
    ( 
     id_area
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE INCIDENTES_REGISTRADOS 
    ADD CONSTRAINT FK_INCIDENTES_REGISTRADOS_ALERTAS_DISPARADOS FOREIGN KEY 
    ( 
     id_alerta,
     id_area2
    ) 
    REFERENCES ALERTAS_DISPARADOS 
    ( 
     id_alerta,
     id_area
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE PESSOA_DOMICILIO 
    ADD CONSTRAINT FK_PESSOA_DOMICILIO_DOMICILIOS_AREA FOREIGN KEY 
    ( 
     id_domicilio,
     id_area
    ) 
    REFERENCES DOMICILIOS_AREA 
    ( 
     id_domicilio,
     id_area
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE SENSOR_PLUVIOMETRICO 
    ADD CONSTRAINT FK_SENSOR_PLUVIOMETRICO_AREA_MONITORADA FOREIGN KEY 
    ( 
     id_area
    ) 
    REFERENCES AREA_MONITORADA 
    ( 
     id_area
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE SENSOR_UMIDADE 
    ADD CONSTRAINT FK_SENSOR_UMIDADE_AREA_MONITORADA FOREIGN KEY 
    ( 
     id_area
    ) 
    REFERENCES AREA_MONITORADA 
    ( 
     id_area
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE SENSOR_VENTO 
    ADD CONSTRAINT FK_SENSOR_VENTO_AREA_MONITORADA FOREIGN KEY 
    ( 
     id_area
    ) 
    REFERENCES AREA_MONITORADA 
    ( 
     id_area
    ) 
    NOT DEFERRABLE 
;

ALTER TABLE SENSOR_VIBRACAO 
    ADD CONSTRAINT FK_SENSOR_VIBRACAO_AREA_MONITORADA FOREIGN KEY 
    ( 
     id_area
    ) 
    REFERENCES AREA_MONITORADA 
    ( 
     id_area
    ) 
    NOT DEFERRABLE 
;



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            10
-- CREATE INDEX                             0
-- ALTER TABLE                             19
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   3
-- WARNINGS                                 0
