# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:25:38 2024

@author: LENOVO10
"""

import pandas as pd
ciclo = input("Por favor, ingresa el ciclo actual para los certificados: ")
VENTAS123 = pd.read_csv("consolidado_ventas_123.csv")
CURSOS_CICLO28=pd.read_csv("cursos_ciclo28.csv")
CERTIFICADOS_CICLO28=pd.read_csv("certificado_ciclo_28.csv")

def procesar_columnas(df, columnas_a_string, columnas_a_fillna=None):
    for col in columnas_a_string:
        df[col] = df[col].astype(str)
    
    if columnas_a_fillna:
        for col, fill_value in columnas_a_fillna.items():
            df[col] = df[col].fillna(fill_value).astype(str)

# Aplicar la función a los DataFrames
procesar_columnas(
    VENTAS123,
    columnas_a_string=["NUMERO DE CELULAR", "DNI DEL DOCENTE", "DOCENTE APELLIDOS"],
    columnas_a_fillna={"DOCENTE APELLIDOS": ""}
)

procesar_columnas(
    CURSOS_CICLO28,
    columnas_a_string=["NUMERO DE CELULAR", "DNI DEL DOCENTE", "DOCENTE APELLIDOS"],
    columnas_a_fillna={"DOCENTE APELLIDOS": ""}
)

procesar_columnas(
    CERTIFICADOS_CICLO28,
    columnas_a_string=["NÚMERO DE CELULAR - DOCENTE", "DNI DEL DOCENTE", "NOMBRE"]
)


"""
reemplazos = {
    'ALESKA NAYELI BALCAZAR RONDO': 'G117_ALESKA BALCAZAR',
    'ARAIZA DE LOS ANGELES BALCAZAR RONDO': 'G149_ARAIZA BALCAZAR',
    'SHEYLA PATRYCIA CARDENAS GUEVARA': 'A595_SHEYLA CARDENAS',
    'ROSAURA ELIZABETH ARANDA NAMAY': 'G124_ROSAURA ARANDA',
    'ORLAIDY ELINA OCANDO GONZALES': 'G214_ORLAIDY OCANDO',
    'MAURICIO NICOLAS RONDO ROBLES': 'G108_MAURICIO RONDO',
    'MASSIEL AIRA RODRIGUEZ REYES': 'G107_MASSIEL RODRIGUEZ',
    'MARIA ISABEL PELAEZ HUAMAN': 'G150_ISABEL PELAEZ',
    'MARIA ALEJANDRA CACHAY TERRONES': 'G193_ALEJANDRA CACHAY',
    'LORENLEY NELLYSABEL BARRETO CASTAÑEDA': 'G222_LORENLEY BARRETO',
    'KIARA ABIGAIL Vital Garcia': 'G102_KIARA VITAL',
    'G2 (PRUEBA)_KIARA VITAL': 'G102_KIARA VITAL',
    'KEVIN ANTONIO LOPEZ LUIS': 'G573_KEVIN LOPEZ',
    'KARLA ANGELINA ALIAGA MORI': 'G281_KARLA ALIAGA',
    'JHONATAN DAVID LUJAN DIAZ': 'A654_JHONATAN LUJAN',
    'JAEL ROSMERI GOMEZ QUINTOS': 'G282_JAEL GOMEZ',
    'G2(PRUEBA) - ASTRID_H': 'G263_ASTRID HUAMAN',
    'ASTRID BRIJHIT HUAMAN COLLAVE': 'G263_ASTRID HUAMAN',
    'G4(PRUEBA) - RENZO_T': 'G464_RENZO TERAN',
    'G129_DIANA HUAMÁN': 'G129_DIANA HUAMAN',
    "G3(PRUEBA) - D'ALEXANDRO CHICCHON": "G333_D'ALEXANDRO CHICCHON",
    'ANTONELLA MILAGROS CALDERON RONDO': 'G2 - MILAGROS_RONDO',
    'HECTOR MANUEL SANCHEZ ASMAT': 'G369_HECTOR SANCHEZ',
    'DAYANNA YAMELY CAYETANO LEON': 'G302_DAYANNA CAYETANO',
    'ESTEFANY VALERIA GRADOS OLIVARES': 'G391_ESTEFANY GRADOS',
    'FLAVIO DENILSON ALFARO VERA': 'G575_FLAVIO ALFARO',
    'GUIDO ANDRES NOVOA LLERENA': 'G304_GUIDO NOVOA',
    'DIEGO ALONSO MEDINA SANCHEZ': 'G574_DIEGO MEDINA',
    'GUSTAVO ALEJANDRO LLANOS MARINO': 'G155_GUSTAVO LLANOS',
    'ELIZABETH NATHALY CEDANO QUEZADA': 'G571_ELIZABETH CEDANO',
    'GRETA LAURA NOVOA SEMINARIO': 'G325_GRETA NOVOA',
    'DIANA DEL ROSARIO AGUILERA BAZAN': 'A587_DIANA AGUILERA',
    'DIANA JAQUELINE HUAMAN CENIZARIO': 'G129_DIANA HUAMAN',
    'GENESIS SCARLETT GOMEZ SERNAQUE': 'G189_GENESIS GOMEZ',
    'HELEN STHEFANY GOMEZ QUINTOS': 'G286_HELEN GOMEZ',
    'G4(PRUEBA) - ORIANA_F': 'G465_ORIANA FLORIAN',
    'ALFREDO JHOASID ISMAEL GONZALES RODRIGUEZ': 'G143_ISMAEL GONZALES',
    'G2(PRUEBA) - KARLA_A': 'G281_KARLA ALIAGA',
    'ANA CRISTINA GOMEZ QUINTOS': 'G260_ANA GOMEZ',
    'G263_ASTRID  HUAMAN': 'G263_ASTRID HUAMAN',
    'A530_CESAR GARCIA': 'G530_CESAR GARCIA'
}

VENTAS123['PROMOTOR'] = VENTAS123['PROMOTOR'].replace(reemplazos)
"""

promotores_especificos = [
    "G530_CESAR GARCIA",
    "A587_DIANA AGUILERA",
    "A595_SHEYLA CARDENAS",
    "A654_JHONATAN LUJAN",
    "G102_KIARA VITAL",
    "G106_ANTHONELLA CALDERÓN",
    "G107_MASSIEL RODRIGUEZ",
    "G108_MAURICIO RONDO",
    "G117_ALESKA BALCAZAR",
    "G124_ROSAURA ARANDA",
    "G129_DIANA HUAMAN",
    "G142_KARLA ARELLANO",
    "G143_ISMAEL GONZALES",
    "G149_ARAIZA BALCAZAR",
    "G150_ISABEL PELAEZ",
    "G155_GUSTAVO LLANOS",
    "G189_GENESIS GOMEZ",
    "G193_ALEJANDRA CACHAY",
    "G205_DANIEL ÁVILA",
    "G214_ORLAIDY OCANDO",
    "G222_LORENLEY BARRETO",
    "G260_ANA GOMEZ",
    "G263_ASTRID HUAMAN",
    "G281_KARLA ALIAGA",
    "G282_JAEL GOMEZ",
    "G286_HELEN GOMEZ",
    "G302_DAYANNA CAYETANO",
    "G304_GUIDO NOVOA",
    "G309_CRISTINA VERGARA",
    "G325_GRETA NOVOA",
    "G369_HECTOR SANCHEZ",
    "G391_ESTEFANY GRADOS",
    "G571_ELIZABETH CEDANO",
    "G573_KEVIN LOPEZ",
    "G574_DIEGO MEDINA",
    "G575_FLAVIO ALFARO"
]
#CONVERTIR LA MARCA TEMPORAR A FECHA 

CERTIFICADOS_CICLO28["Marca temporal"] = pd.to_datetime(CERTIFICADOS_CICLO28["Marca temporal"],dayfirst=True)
CURSOS_CICLO28["MARCA TEMPORAL"] = pd.to_datetime(CURSOS_CICLO28["MARCA TEMPORAL"])
VENTAS123["MARCA TEMPORAL"] = pd.to_datetime(VENTAS123["MARCA TEMPORAL"])

#QUITAR CICLO 28 POR QUE YA LO TENEMOS POR SEPARADO

VENTAS123=VENTAS123[VENTAS123['CICLO'] != 'CICLO 28']

#AGREGAR LA COLUMNA CICLO A CERTIFICADOSS
CERTIFICADOS_CICLO28['CICLO'] = ciclo

def seleccionar_columnas(df, columnas):
    return df[columnas]

def calcular_nombres_completos(df, col_nombres, col_apellidos, nueva_columna):
    df[nueva_columna] = df[col_nombres] + ' ' + df[col_apellidos]
    return df

# Aplicar funciones a los DataFrames
VENTAS123 = seleccionar_columnas(
    VENTAS123, 
    ["CICLO", "PROMOTOR", "NOMBRES_COMPLETOS", "NUMERO DE CELULAR", "DNI DEL DOCENTE", "PRODUCTO ACADEMICO", "ESPECIALIDAD","MARCA TEMPORAL"]
)

CURSOS_CICLO28 = calcular_nombres_completos(
    CURSOS_CICLO28, 
    col_nombres="DOCENTE NOMBRES", 
    col_apellidos="DOCENTE APELLIDOS", 
    nueva_columna="NOMBRES_COMPLETOS"
)

CURSOS_CICLO28 = seleccionar_columnas(
    CURSOS_CICLO28, 
    ["CICLO", "PROMOTOR", "NOMBRES_COMPLETOS", "NUMERO DE CELULAR", "DNI DEL DOCENTE", "PRODUCTO ACADEMICO", "ESPECIALIDAD","MARCA TEMPORAL"]
)

CERTIFICADOS_CICLO28 = seleccionar_columnas(
    CERTIFICADOS_CICLO28, 
    ["CICLO", "PROMOTOR", "NOMBRE", "NÚMERO DE CELULAR - DOCENTE", "DNI DEL DOCENTE", "PERIODO", "ESPECIALIDAD","Marca temporal"]
)

CERTIFICADOS_CICLO28.columns = ["CICLO", "PROMOTOR", "NOMBRES_COMPLETOS", "NUMERO DE CELULAR", "DNI DEL DOCENTE", "PRODUCTO ACADEMICO", "ESPECIALIDAD","MARCA TEMPORAL"]

CONCATENADO = pd.concat([VENTAS123, CURSOS_CICLO28, CERTIFICADOS_CICLO28], ignore_index=True)

#categorizar para verificar si son asesores activos
CONCATENADO["ES_ACTIVO"] = CONCATENADO["PROMOTOR"].apply(lambda x: 1 if x in promotores_especificos else 0)



USUARIOS=CONCATENADO[CONCATENADO["NUMERO DE CELULAR"] != "0"][["DNI DEL DOCENTE", "NUMERO DE CELULAR"]]


USUARIOS["CLAVE_UNICA"] = USUARIOS["DNI DEL DOCENTE"].where(USUARIOS["DNI DEL DOCENTE"] != "0", USUARIOS["NUMERO DE CELULAR"])


def procesar_por_clave_unica(usuarios, ventas):
    # Crear un DataFrame vacío para almacenar los resultados
    resultado_df = pd.DataFrame(columns=["CLAVE_UNICA","CICLO", "PROMOTOR", "DOCENTE_NOMBRES", "NUMERO_DE_CELULAR", "DNI_DEL_DOCENTE","PRODUCTO","ESPECIALIDAD"])
    
    # Iterar sobre cada clave única
    claves_unicas = usuarios["CLAVE_UNICA"].unique()
    print(f"Total de claves únicas a procesar: {len(claves_unicas)}")

    for i, clave in enumerate(claves_unicas, 1):
        print(f"\nProcesando clave {i}/{len(claves_unicas)}: {clave}")
        
        # Filtrar registros coincidentes en el DataFrame VENTAS123 (por DNI o Número de Celular)
        coincidencias = ventas[
            (ventas["DNI DEL DOCENTE"] == clave) | 
            (ventas["NUMERO DE CELULAR"] == clave)
        ]
        print(f"Coincidencias encontradas: {len(coincidencias)}")
        
        if coincidencias.empty:
            print(f"No se encontraron coincidencias para la clave {clave}.")
            continue  # Si no hay coincidencias, pasar al siguiente
        
        # Si hay un único registro
        if len(coincidencias) == 1:
            print("Solo una coincidencia encontrada.")
            registro = coincidencias.iloc[0]
            nuevo_registro = {
                "CLAVE_UNICA": clave,
                "PROMOTOR": registro["PROMOTOR"] if registro["ES_ACTIVO"] == 1 else "LIBRE",
                "DOCENTE_NOMBRES": registro["NOMBRES_COMPLETOS"],
                "NUMERO_DE_CELULAR": registro["NUMERO DE CELULAR"],
                "DNI_DEL_DOCENTE": registro["DNI DEL DOCENTE"],
                "PRODUCTO":registro["PRODUCTO ACADEMICO"],
                "ESPECIALIDAD":registro["ESPECIALIDAD"],
                "CICLO":registro["CICLO"]
            }
            print(f"Registro agregado: {nuevo_registro}")
            resultado_df = pd.concat([resultado_df, pd.DataFrame([nuevo_registro])], ignore_index=True)
        
        # Si hay múltiples registros
        else:
            print(f"Se encontraron múltiples coincidencias ({len(coincidencias)}). Ordenando por 'MARCA TEMPORAL'.")
            registros_ordenados = coincidencias.sort_values(by="MARCA TEMPORAL", ascending=False)
            
            for j, (_, registro) in enumerate(registros_ordenados.iterrows(), 1):
                print(f"Evaluando registro {j}/{len(registros_ordenados)}: {registro['MARCA TEMPORAL']}")
                if registro["ES_ACTIVO"] == 1:
                    if "SIMULACRO" not in registro["PRODUCTO ACADEMICO"] and "REPASO" not in registro["PRODUCTO ACADEMICO"] and "TICS" not in registro["PRODUCTO ACADEMICO"] and "PLANIFICACION" not in registro["PRODUCTO ACADEMICO"]:
                        nuevo_registro = {
                            "CLAVE_UNICA": clave,
                            "PROMOTOR": registro["PROMOTOR"],
                            "DOCENTE_NOMBRES": registro["NOMBRES_COMPLETOS"],
                            "NUMERO_DE_CELULAR": registro["NUMERO DE CELULAR"],
                            "DNI_DEL_DOCENTE": registro["DNI DEL DOCENTE"],
                            "PRODUCTO":registro["PRODUCTO ACADEMICO"],
                            "ESPECIALIDAD":registro["ESPECIALIDAD"],
                            "CICLO":registro["CICLO"]
                        }
                        print(f"Registro agregado tras validar condiciones: {nuevo_registro}")
                        resultado_df = pd.concat([resultado_df, pd.DataFrame([nuevo_registro])], ignore_index=True)
                        break  # Terminar el ciclo para esta clave única
                    else:
                        print(f"Registro descartado por contener 'SIMULACRO' o 'REPASO' en 'PRODUCTO ACADEMICO'.")
                else:
                    print(f"Registro descartado porque 'ES_ACTIVO' es 0.")
            print(f"Terminado procesamiento de múltiples registros para la clave {clave}.")

    print("\nProcesamiento completo.")
    print(f"Total de registros generados: {len(resultado_df)}")
    return resultado_df

resultado = procesar_por_clave_unica(USUARIOS, CONCATENADO)
print("\nResultados finales:")
print(resultado)

resultado.to_csv("LISTA DE CLIENTES POR CADA ASESOR.csv",index=False)