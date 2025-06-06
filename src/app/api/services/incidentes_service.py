from services.mock_service import incidentes_registrados, pessoas_domicilio, areas_monitoradas
from services.pessoa_service import getPessoaName
from services.area_monitorada_service import getAreaMonitoradaName

def get_incidentes_formatados():
    incidentes_formatados = []
    for inc in incidentes_registrados:
        nome_pessoa = getPessoaName(inc["id_pessoa1"], pessoas_domicilio)
        nome_area = getAreaMonitoradaName(inc["id_area_monitorada"], areas_monitoradas)
        incidentes_formatados.append({
            "data": inc["timestamp_incidente"].isoformat(),
            "reportado_por": nome_pessoa,
            "tipo_incidente": inc["tipo_incidente_reportado"],
            "localizacao": {
                "lat": inc["lat_local_incidente"],
                "lng": inc["lng_local_incidente"]
            },
            "area_monitorada": nome_area
        })
    return incidentes_formatados
