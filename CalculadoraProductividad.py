import calendar
from datetime import date, timedelta

class Calculadora_Productividad:
    

    
    def __init__(self,mi_fecha ):
        self.year = mi_fecha.year
        self.month = mi_fecha.month
        self.day=mi_fecha.day

    def cantidad_dias_lunes_a_viernes_en_mes(self):
        _, last_day = calendar.monthrange(self.year, self.month)
        primer_dia = date(self.year, self.month, 1)
        ultimo_dia = date(self.year, self.month, last_day)

        dias_mes = [primer_dia + timedelta(days=i) for i in range((ultimo_dia - primer_dia).days + 1)]

        # Filtrar solo los días de lunes a viernes
        dias_lunes_a_viernes = [dia for dia in dias_mes if dia.weekday() < 5]

        return len(dias_lunes_a_viernes)

    def cantidad_dias_lunes_a_viernes_hasta_fecha(self):
        fecha_hasta = date(self.year, self.month, self.day)
        primer_dia = date(self.year, self.month, 1)

        dias_hasta_fecha = [primer_dia + timedelta(days=i) for i in range((fecha_hasta - primer_dia).days + 1)]

        # Filtrar solo los días de lunes a viernes
        dias_lunes_a_viernes_hasta_fecha = [dia for dia in dias_hasta_fecha if dia.weekday() < 5]

        return len(dias_lunes_a_viernes_hasta_fecha)
    
    def getProductividad(self):
        q_dias_mes=self.cantidad_dias_lunes_a_viernes_en_mes()
        q_dias_hasta_fecha=self.cantidad_dias_lunes_a_viernes_hasta_fecha()
        return int((q_dias_hasta_fecha/q_dias_mes)*100)
    

# Ejemplo de uso
