import mysql.connector
import os

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                port=int(os.getenv("DB_PORT", 3306)),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "root"),
                database=os.getenv("DB_NAME", "smd_db")
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Erro ao conectar no banco: {err}")
            self.conn = None
            self.cursor = None

    def fetch_alertas(self):
        if not self.cursor:
            return []
        self.cursor.execute("SELECT * FROM ALERTAS_DISPARADOS")
        return self.cursor.fetchall()

    def insert_alerta(self, id_area, timestamp, pessoas, efetividade, acao):
        if not self.cursor:
            return False
        query = """
            INSERT INTO ALERTAS_DISPARADOS 
                (id_area_monitorada1, timestamp_alerta, pessoas_alertadas, efetividade_alerta, acao_alerta)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (id_area, timestamp, pessoas, efetividade, acao)
        self.cursor.execute(query, values)
        self.conn.commit()
        return True

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.close()
