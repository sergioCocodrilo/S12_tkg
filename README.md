Análisis automático de TKG
=========================

Procedimiento
------------

1. Obtener la lista de TKGs en S12. Guardar resultado en archivo (log).
	DISPLAY-TKG:TKG=ALL.

2. Procesar el resultado del paso 1.
	Ejecutar: python3 /processing_files/all_tkg_states.py
