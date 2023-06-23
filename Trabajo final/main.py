# Seguimiento de los usuarios que se han conectado días feriados y no laborables (sábados y domingos). 
# Debe incluir la posibilidad de ingresar un rango de fechas. 
# input (Fecha 1) -> 1/7/2023
# input (Fecha 2) -> 1/8/2023
# ----------------------------------------------------------------
# Usuario | Fecha de conexión | Fecha de finalizacion
# matias  | 15/7/2023         | 16/7/2023
# matias  | 23/7/2023         | 24/7/2023
# igna    | 3/7/2023          | 4/8/2023
# ----------------------------------------------------------------
# Extra:
#     filtrar celdas vacías.
#     obterner datos desde una api.
#     incluir cuarentena
#     buscar en todos los registros si ambas fechas son vacias
#     Guardar fechas de fin de semana y feriadas precargadas en un archivo para agilizar la comparacion.
#     https://www.youtube.com/watch?v=DMYK-58U0Tk
#{'Input_Octects', 'ID_Conexión_unico', 'FIN_de_Conexión_Dia', 'Unnamed: 17', 'Usuario', 'MAC_Cliente', 'Tipo__conexión', 'ID', 'Session_Time', 'Unnamed: 16', 'ID_Sesion', 'IP_NAS_AP', #'Razon_de_Terminación_de_Sesión', 'MAC_AP', 'Inicio_de_Conexión_Dia', 'Inicio_de_Conexión_Hora', 'Output_Octects', 'FIN_de_Conexión_Hora'}
import datetime
import pandas as pd
import numpy as np
import time
from dask import dataframe as df1
def is_weekend(date):
    return date.weekday() >= 5  # 5 representa el sábado, 6 representa el domingo

if __name__ == '__main__':
    dask_df = df1.read_csv('Trabajo final/archivo.csv', dtype={'Input_Octects': 'object',
                                                            'Output_Octects': 'object',
                                                            'Session_Time': 'object',
                                                            'Unnamed: 16': 'object',
                                                            'Unnamed: 17': 'object'})
    usuarios = dask_df['Usuario']
    mac_usuarios = dask_df['MAC_Cliente']
    mac_AP = dask_df['MAC_AP']
    inicio_conexion = dask_df['Inicio_de_Conexión_Dia']
    fin_conexion = dask_df['FIN_de_Conexión_Dia']
    fecha_inicio = '2023-01-28'
    fecha_fin = '2023-01-29'
    date_filter = (inicio_conexion >= fecha_inicio) & (fin_conexion <= fecha_fin)
    usuarios_filtrados = usuarios[date_filter].compute()
    usuarios_unicos = set(usuarios_filtrados)
    conteo_usuarios = usuarios_filtrados.value_counts()
print(usuarios_unicos)
