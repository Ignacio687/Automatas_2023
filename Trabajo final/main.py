from datetime import datetime
numero_dia = dt.weekday()
# numero_dia >= 5

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
