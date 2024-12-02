# PASOS PARA SUBIR VENTAS A MONGO DB

## 1. Ir al recurso

[https://backoffice.grupodocenteperu.com/admin/reports/r0002/](https://backoffice.grupodocenteperu.com/admin/reports/r0002/)  
Exportar la tabla "Detalles de pago".

___

> **NOTA:**  
> Aplicar filtros si es necesario. No es necesario descargar todo. Revisar en [Google Drive](https://drive.google.com/drive/u/0/folders/1yXPOGDgIhQsDUqIAibGnYVGhjV4jGUOy) y buscar "CICLO[ciclo actual]SUBIDO A MONGO" para verificar hasta qué fecha ya se ha subido.

___

## 2. Buscar métodos de transformación a CSV

Es necesario transformar el archivo en CSV, ya que el script solo trabaja con ese formato.  
**Método actual de transformación:** Subir a Google Sheets y luego descargarlo en formato CSV.

## 3. Buscar en la laptop el siguiente directorio

`C:\Users\LENOVO10\Desktop\subir_ventas_mongo`

Mover el archivo CSV a esta dirección y renombrarlo como `VENTAS_SISTEMA.csv`.

## 4. Ejecutar el script

Ejecutar el script `AUTOMATIZACION.py`. Este script generará dos archivos:  
- `SUBIR ESTE ARCHIVO A MONGO.json`  
- `SUBIR ESTE ARCHIVO A GOOGLE SHEETS.xlsx`

Estos archivos están destinados a ser cargados a MongoDB y Google Sheets.

## 5. Abrir el ejecutable de MONGO COMPASS

Conectarse a MongoDB (buscar tutoriales de cómo conectarse).  
**Nota:** Pedir credenciales al área de sistemas.

## 6. Buscar la base de datos

Buscar la base de datos "consultas gdp" y la colección "CLients", e importar el archivo `.json`.
