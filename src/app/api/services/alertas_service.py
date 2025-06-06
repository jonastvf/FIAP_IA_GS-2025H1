from services.area_monitorada_service import getAreaMonitoradaName
from services.mock_service import areas_monitoradas, alertas_disparados

def get_alertas_formatados():
    alertas_formatados = []
    for alerta in alertas_disparados:
        nome_area = getAreaMonitoradaName(alerta["id_area_monitorada1"], areas_monitoradas)
        alertas_formatados.append({
            "data": alerta["timestamp_alerta"].isoformat(),
            "area_monitorada": nome_area,
            "pessoas_alertadas": alerta["pessoas_alertadas"],
            "efetividade": alerta["efetividade_alerta"],
            "acao_alerta": alerta["acao_alerta"]
        })
    return alertas_formatados
