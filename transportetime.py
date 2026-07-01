from datetime import datetime, timedelta

class TrayectoTransporte:
    ESTACIONES_METRO_LÍNEA1= {
        "Talleres": 1,
        "San Bernabé": 2,
        "Unidad Modelo": 3,
        "Aztlán": 4,
        "Penitenciaría": 5,
        "Alfonso reyes": 6,
        "Mitras": 7,
        "Simón Bolívar": 8,
        "Hospital": 9,
        "Edison": 10,
        "Central": 11,
        "Cuahutémoc":12,
        "Del Golfo": 13,
        "Félix U. Gómez": 14, 
        "Parque Fundidora": 15,
        "Y Griega": 16,
        "Eloy Cavazos": 17,
        "Lerdo de Tejada": 18,
        "Exposición": 19
    }
    
    ESTACIONES_METRO_LÍNEA2={
        "Sendero": 1,
        "Tapia": 2,
        "SAN NICOLAS": 3,
        "ANAHUAC": 4,
        "UNIVERSIDAD": 5,
        "NIÑOS HEROES": 6,
        "REGINA": 7,
        "GENERAL ANAYA": 8,
        "CUAHUTÉMOC": 9, 
        "ALAMEDA": 10,
        "FUNDADORES": 11,
        "PADRE MIER": 12,
        "GENERAL I ZARAGOZA": 13
    }
    
    ESTACIONES_METRO_LÍNEA3={
        "HOSPITAL METROPOLITANO": 1,
        "LOS ANGELES": 2,
        "RUIZ CORTINES": 3,
        "COL. MODERNA": 4,
        "METALURGIA": 5,
        "FÉLIX U. GÓMEZ": 6,
        "COL OBRERA": 7, 
        "SANTA LUCIA": 8,
        "GENERAL I ZARAGOZA": 9
    }
    
    
    
    
    def __init__(self, lugar, estaciones, hay_transbordo: bool, tray_extra: int, hora_llegada: str):
        self.lugar=lugar
        self.base_estacion="Mitras"
        self.estacion_destino=estaciones
        self.estaciones=self.cant_estaciones(estaciones)
        self.hay_transbordo=hay_transbordo
        self.tray_extra=tray_extra
        self.hora_llegada=hora_llegada
        self.hora_llegada_hour=datetime.strptime(hora_llegada, "%I:%M %p")
  
       #Uber
        self.asignar=5
        self.llegar=10
        self.ecovia=10
        self.total_u=self.asignar+self.llegar+self.ecovia

    #ecovia
        self.esperar=10
        self.trayecto=30
        self.total_e=self.esperar+self.trayecto
        
    
   
        
    #metro call
        self.metro(self.estaciones)
        
     #transbordo call
        self.transbordar(hay_transbordo)
        
        
    #extra call
        self.extras(self.tray_extra)

    def normalizar(self, texto):
        return texto.strip().lower()

    #verificar estación
    
    def cant_estaciones(self,estaciones):
        if isinstance(estaciones, int):
            return estaciones
        
        est_norm = self.normalizar(estaciones)
        
        l1 = {self.normalizar(k): v for k, v in self.ESTACIONES_METRO_LÍNEA1.items()}
        l2 = {self.normalizar(k): v for k, v in self.ESTACIONES_METRO_LÍNEA2.items()}
        l3 = {self.normalizar(k): v for k, v in self.ESTACIONES_METRO_LÍNEA3.items()}
        
        if est_norm not in l1 and est_norm not in l2 and est_norm not in l3:
            raise ValueError(f"Estación desconocida: {estaciones}")
        
        if est_norm in l1:
            base_num=l1[self.normalizar("Mitras")]
            dest_num=l1[est_norm]
            return abs(dest_num - base_num)
        
        elif est_norm in l2:
            base_num=l2[self.normalizar("CUAHUTÉMOC")]
            dest_num=l2[est_norm]
            return abs(dest_num - base_num)
        
        elif est_norm in l3:
            base_num=l3[self.normalizar("FÉLIX U. GÓMEZ")]
            dest_num=l3[est_norm]
            return abs(dest_num - base_num)
       
   
    #metro
    def metro(self,estaciones):
        subir=5
        esperar=5
        if isinstance(estaciones, int):
            self.total_m=(estaciones*2)+subir+esperar
       
    
    def transbordar(self, hay_transbordo):
        if not hay_transbordo:
            return
        else:
            espera_transbordo=10
            dest=self.normalizar(self.estacion_destino)
            l2 = {self.normalizar(k): v for k, v in self.ESTACIONES_METRO_LÍNEA2.items()}
            l3 = {self.normalizar(k): v for k, v in self.ESTACIONES_METRO_LÍNEA3.items()}
            if dest in l2 or dest in l3:
                self.total_m += espera_transbordo
            
    #extras
    def extras(self, tray_extra):
        
        ##self.tray_extra = min caminata o uber
        
        if not tray_extra:
            total_minutes= self.total_u + self.total_e + self.total_m
        else:
            total_minutes= self.total_u + self.total_e + self.total_m + tray_extra
        self.total_hours = timedelta(minutes=total_minutes)


    def hora_salida(self):
        salida=(self.hora_llegada_hour - self.total_hours)
        return salida.strftime("%I:%M %p")
    
    def __str__(self):
        llegada = self.hora_llegada_hour.strftime("%I:%M %p")
        return f"{self.lugar} | Salida: {self.hora_salida()} | Llegada: {llegada}"
        
    
        

## {variable_nombre lugar} = (lugar: str, número de estaciones de metro o nombre de la estación de metro, true or false si voy a transbordar, hora de llegada: str)

FashDi = TrayectoTransporte("Fashion Drive", "hospital", True, 10, "11:30 AM")
CM  = TrayectoTransporte("Fundi", "Y Griega", False, 0, "11:00 AM")
MG     = TrayectoTransporte("Matcha Garden", "Hospital", False, 15, "1:00 PM")
ver_kss_ctro=TrayectoTransporte("Mala Hierba", "Edison", False, 0, "2:10 PM")
LT= TrayectoTransporte("Lucky Tattoos", "Hospital", False, 10, "12:45 PM")
Mn= TrayectoTransporte("Espacio Monono", "Hospital", False, 0, "2:15 PM")
PB= TrayectoTransporte("Plum Blossom", "Padre Mier", True, 5, "6:00 PM")
NS= TrayectoTransporte("Nuevo Sur", "Parque Fundidora", False, 10, "2:00 PM")

Fd= TrayectoTransporte("Parque Fundidora", "Eloy Cavazos", False, 0, "3:00 PM")

ok=TrayectoTransporte("Omg K-dogs", "Col Obrera", True, 10, "2:00 PM")

print(ok)
print (Fd)


    
