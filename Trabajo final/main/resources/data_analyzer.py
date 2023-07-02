import pathlib,csv, json
from datetime import datetime, timedelta, date

class IncorrectFileFormat(Exception):
    pass

class DataAnalyzer():
    def __init__(self, filePath: str) -> None:
        """Class capable of validating a specific format csv file and 
        returning filtered data.\n
        filePath: Absolute path of the file"""
        self.filePath = filePath
        startDate = datetime.strptime("2003-01-01", "%Y-%m-%d")
        endDate = datetime.strptime("2023-06-30", "%Y-%m-%d")
        self.filterUsers(startDate=startDate, endDate=endDate)

    def validate(self) -> dict[int, str|int]:
        """Method capable of validating the file format and all data within the lines. 
        Returns a dictionary with all the found errors '{line_index:[errors_list]}'."""
        pass

    def generateFile(self, path: str, lines: tuple[int]|None = None) -> str:
        """Method designed to copy the original file, with or without removing lines, 
        into a new directory. Returns the new file absolute path.\n
        path: Absolute path where the new file will be.\n
        lines: Indexes of lines willing to remove."""
        pass

    def filterUsers(self, 
                    filter: bool = True, 
                    startDate = None, 
                    endDate = None
                    ):
        """Method designed to filter the users that have accessed the system on Non-working days. 
        Returns a dictionary {user_name: [total_session_time, most_used_MAC_NWD, most_used_MAC_WD, 
            , total_output_octects]}  *NWD = Non-working days * WD = Working days\n
        filter: if set to False method returns complete list of users\n
        startDate/endDate: if either of them is set to None, the method will take the most old or 
        new date available respectively."""
        """
        ID,ID_Sesion,ID_Conexión_unico,Usuario,IP_NAS_AP,Tipo__conexión,Inicio_de_Conexión_Dia,Inicio_de_Conexión_Hora,FIN_de_Conexión_Dia,FIN_de_Conexión_Hora,
        Session_Time,Input_Octects,Output_Octects,MAC_AP,MAC_Cliente,Razon_de_Terminación_de_Sesión,,
        603877,5AA0184E-000001CA,d6104707df0cd315,invitado-deca,192.168.247.11,Wireless-802.11,2019-02-07,19:46:08,2019-03-13,11:27:57,25,39517,505219,DC-9F-DB-12-F3-EA:HCDD,DC-BF-E9-1A-B5-D0,User-Request,,
        """
        fecha_inicio = date(2019, 3, 26) ## Argumentos
        fecha_fin = date(2019, 3, 28)
        if fecha_inicio == None:
            fecha_inicio = date(2000, 3, 27) # Fecha antigua para incluir todos los resultados
        if fecha_fin == None:
            fecha_fin = date.today()
        if fecha_fin < fecha_inicio:
            fecha_fin, fecha_inicio = fecha_inicio, fecha_fin

        def is_holyday(date):
            #main/data/2019.json
            with open(f"main/data/{date.year}.json") as json_file:
                data = json.load(json_file)
                month = date.month-1
                day = my_date.strftime("%d")
                if day in [i for i in data[month]]:
                    return True
        
        def is_weekend(fecha_inicio, fecha_fin):
            delta = timedelta(days=1)
            if (fecha_fin - fecha_inicio).days > 5:
                return True
            fecha_actual = fecha_inicio
            while fecha_actual <= fecha_fin:
                dia_semana = fecha_actual.weekday()
                if dia_semana in [5, 6] :  # 5 representa sábado y 6 representa or is_holyday(fecha_actual)
                    return True
                fecha_actual += delta
            return False

        def print_data():
            for key in user_data.keys():
                print(f"\n{'-'*30} MOSTRANDO DATOS DESDE {fecha_inicio} HASTA {fecha_fin} {'-'*30}\n")
                print(f"{key}:")
                print(f"\tUsername: {user_data[key]['username']} ")
                print(f"\tMac adress: {user_data[key]['mac_cliente']}")
                print(f"\tConexiones:")
                for i in user_data[key]['conexiones']:
                    print(f"\t\t{i}")
                    
        user_data = {}
        with open(self.filePath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                inicio_conexion = datetime.strptime(row['Inicio_de_Conexión_Dia'], "%Y-%m-%d").date()
                fin_conexion = datetime.strptime(row['FIN_de_Conexión_Dia'], "%Y-%m-%d").date()
                session_time = row['Session_Time']
                username = row['Usuario']
                mac_cliente = row['MAC_Cliente']
                input_octets = row['Input_Octects']
                output_octects = row['Output_Octects']
                if not(inicio_conexion > fecha_fin or fin_conexion < fecha_inicio) and is_weekend(inicio_conexion, fin_conexion): 
                    if not user_data.get(username):
                        user_data[username] = {'username': username, 'mac_cliente': [mac_cliente], 'conexiones': [] } 
                #if user_data.get(username) : # and len(user_data.get(username)['conexiones'])
                    if mac_cliente not in user_data[username]['mac_cliente']:
                        user_data[username]['mac_cliente'].append(mac_cliente)
                    user_data[username]['conexiones'].append(f"{row['Inicio_de_Conexión_Dia']} -> {row['FIN_de_Conexión_Dia']} => Total time: {row['Session_Time']+' hs':<8} | input_octets: {row['Input_Octects']:<10} | output_octects: {row['Output_Octects']:<10}")
        print_data()


def is_holyday(fecha_inicio, fecha_fin):
    with open(f"main/data/{fecha_inicio.year}.json") as json_file:
        delta = timedelta(days=1)
            # if (fecha_fin - fecha_inicio).days > 5:
            #     return True
        fecha_actual = fecha_inicio
        data = json.load(json_file)
        month = fecha_actual.month-1
        day = fecha_actual.strftime("%d")
        print(data[month])
        while fecha_actual <= fecha_fin:
            if day in [i for i in data[month]]:
                print(f"Fecha {fecha_actual} es feriado")
            print(f"Fecha {fecha_actual} no es feriado")
            fecha_actual += delta
                    
if __name__ == '__main__':
    #my_date = date(2020, 3, 2)
    # fecha_inicio = date(2020, 3, 1) ## Argumentos
    # fecha_fin = date(2020, 4, 1)
    # print(is_holyday(fecha_inicio, fecha_fin))
    d = DataAnalyzer('/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/main/data/test_files/test_mati.csv')
    # d = DataAnalyzer('/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/archivo.csv')