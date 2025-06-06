from services.mock_service import areas_monitoradas

def getAreaMonitoradaName(id_area, areas_monitoradas = areas_monitoradas):
    for area in areas_monitoradas:
        if area["id_area_monitorada"] == id_area:
            return area["nome_area_monitorada"]
    return "Área desconhecida"