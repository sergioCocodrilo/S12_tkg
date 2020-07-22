# Análisis automático de TKG

## Requerimientos
1. python3
2. pandas
3. acceso al S12

## Procedimiento a automatizar

1. Obtener la lista de TKGs en S12. Guardar resultado en archivo (log).
	DISPLAY-TKG:TKG=ALL.
	El archivo log debe contener un solo reporte de resultados.
	En caso de tener más, también funcionará pero la fecha del resultado será erroneo.

2. Procesar el resultado del paso 1.
	Desde la carpeta TrunkGroups, ejecutar:
		python3 /processing_files/all_tkg_states.py

3. Visualizar los resultados
