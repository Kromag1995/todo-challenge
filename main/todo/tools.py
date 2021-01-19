from datetime import date
from datetime import datetime

def from_date_To_datetime (date):
    if date == "":
        return date
    dt = datetime.strptime(date+ " 00:00", '%Y-%m-%d %H:%M')
    return dt

def filtar_segun_fechas(GET,Todos):
    desde = from_date_To_datetime(GET["desde"])
    hasta = from_date_To_datetime(GET["hasta"])
    if desde != "" and hasta != "":
        Todos = Todos.filter(timestamp__range=[desde,hasta])
    elif desde != "":
        Todos = Todos.filter(timestamp__gte=desde)
    elif hasta != "":
        Todos = Todos.filter(timestamp__lt=hasta)
    return Todos