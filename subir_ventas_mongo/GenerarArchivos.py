# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:58:22 2024

@author: LENOVO10
"""

import pandas as pd
import seaborn as s
import matplotlib.pyplot as plt
import os
import logging

ciclo = input("Por favor, ingresa el ciclo actual: ")
CICLO28= pd.read_excel("VENTAS_SISTEMA.csv")

#SEPARAR SOLO LAS COLUMNAS QUE SE USARAN EN MONGO

columnas_a_conservar= [
    "CREATED_AT", "ADVISER_EMAIL", "ADVISER_FULLNAME", "CUSTOMER_NAME", 
    "CUSTOMER_LASTNAME", "CUSTOMER_PHONE", "PAY_DATE", "PAY_AMOUNT", 
    "SELL_PAYMENT_PARTS", "PAY_METHOD", "TICKET_ID", "PRODUCT_TITLE", 
    "CUSTOMER_SPECIALITY", "NOTES", "VOUCHER", "TICKET_TYPE", 
    "CUSTOMER_DNI", "SELL_FINAL_PRICE", "SELL_NEXT_PAYMENT", "ADVISER_CODE"
]

CICLO28 = CICLO28[columnas_a_conservar]
CICLO28.columns = CICLO28.columns.str.strip()

#AGREGAR LAS 4 COLUMNAS INICIALES DEL ESQUEMA DE MONGO
CICLO28["Cycle"] = None
CICLO28["Month"] = None
CICLO28["Year"] = None
CICLO28["Group"] = None

nuevas_columnas = ["Cycle", "Month", "Year", "Group"] + [col for col in CICLO28.columns if col not in ["Cycle", "Month", "Year", "Group"]]
CICLO28 = CICLO28[nuevas_columnas]

#AGREAGAR COLUMNAS INTERMEDIAS 

# 1. Insertar "Course_Duration" después de "CUSTOMER_SPECIALITY"
if "Course_Duration" not in CICLO28.columns:
    pos = CICLO28.columns.get_loc("CUSTOMER_SPECIALITY") + 1  # Obtiene la posición de "CUSTOMER_SPECIALITY"
    CICLO28.insert(pos, 'Course_Duration', None)  # Inserta la columna "Course_Duration" en la posición

# 2. Insertar "Sales_Origin" después de "VOUCHER"
if "Sales_Origin" not in CICLO28.columns:
    pos = CICLO28.columns.get_loc("VOUCHER") + 1  # Obtiene la posición de "VOUCHER"
    CICLO28.insert(pos, 'Sales_Origin', None)  # Inserta la columna "Sales_Origin" en la posición

# 3. Insertar "Referred_Number" después de "TICKET_TYPE"
if "Referred_Number" not in CICLO28.columns:
    pos = CICLO28.columns.get_loc("TICKET_TYPE") + 1  # Obtiene la posición de "TICKET_TYPE"
    CICLO28.insert(pos, 'Referred_Number', None)  # Inserta la columna "Referred_Number" en la posición

# 4. Insertar "Full_Name", "State", "Continuity" después de "SELL_FINAL_PRICE"
if "Full_Name" not in CICLO28.columns:
    pos = CICLO28.columns.get_loc("SELL_FINAL_PRICE") + 1  # Obtiene la posición de "SELL_FINAL_PRICE"
    CICLO28.insert(pos, 'Full_Name', None)  # Inserta la columna "Full_Name" en la posición
    CICLO28.insert(pos + 1, 'State', None)  # Inserta la columna "State" después de "Full_Name"
    CICLO28.insert(pos + 2, 'Continuity', None)  # Inserta la columna "Continuity" después de "State"

# 5. Insertar "Review_Date" después de "SELL_NEXT_PAYMENT"
if "Review_Date" not in CICLO28.columns:
    pos = CICLO28.columns.get_loc("SELL_NEXT_PAYMENT") + 1  # Obtiene la posición de "SELL_NEXT_PAYMENT"
    CICLO28.insert(pos, 'Review_Date', None)  # Insert

# EMPEZAR A LLENAR LOS DATOS
# Asegúrate de que la columna tiene el formato adecuado
CICLO28["CREATED_AT"] = pd.to_datetime(CICLO28["CREATED_AT"],dayfirst=True)

CICLO28["Cycle"]=ciclo
CICLO28["Month"] = CICLO28["CREATED_AT"].dt.month
CICLO28["Year"]=CICLO28["CREATED_AT"].dt.year

codigo_valores = {
    "A216": "A216_JUNIOR QUEZADA",
    "A613": "A613_KATIA AGREDA",
    "A501": "A501_ROYER CHAVEZ",
    "A570": "A570_ARIAN REYES",
    "G530": "G530_CESAR GARCIA",
    "A654": "A654_JHONATAN LUJAN",
    "A858": "A858_DAYANA SERNAQUE",
    "A587": "A587_DIANA AGUILERA",
    "G205": "G205_DANIEL ÁVILA",
    "G117": "G117_ALESKA BALCAZAR",
    "G575": "G575_FLAVIO ALFARO",
    "G574": "G574_DIEGO MEDINA",
    "G106": "G106_ANTHONELLA CALDERÓN",
    "G149": "G149_ARAIZA BALCAZAR",
    "G107": "G107_MASSIEL RODRIGUEZ",
    "G155": "G155_GUSTAVO LLANOS",
    "G573": "G573_KEVIN LOPEZ",
    "G124": "G124_ROSAURA ARANDA",
    "G108": "G108_MAURICIO RONDO",
    "G214": "G214_ORLAIDY OCANDO",
    "G143": "G143_ISMAEL GONZALES",
    "G142": "G142_KARLA ARELLANO",
    "G302": "G302_DAYANNA CAYETANO",
    "G369": "G369_HECTOR SANCHEZ",
    "G309": "G309_CRISTINA VERGARA",
    "G129": "G129_DIANA HUAMAN",
    "G260": "G260_ANA GOMEZ",
    "G325": "G325_GRETA NOVOA",
    "G304": "G304_GUIDO NOVOA",
    "G222": "G222_LORENLEY BARRETO",
    "G281": "G281_KARLA ALIAGA",
    "G282": "G282_JAEL GOMEZ",
    "G571": "G571_ELIZABETH CEDANO",
    "G286": "G286_HELEN GOMEZ",
    "G189": "G189_GENESIS GOMEZ",
    "G391": "G391_ESTEFANY GRADOS",
    "G150": "G150_ISABEL PELAEZ",
    "A231": "A231_ANTHONY LOAYZA",
    "G263": "G263_ASTRID HUAMAN",
    "A592": "A592_GARY GIL",
    "A596": "A596_ ANDY ARANDA",
    "A595": "A595_SHEYLA CARDENAS",
    "A597": "A597_JOYCE",
    "G102": "G102_KIARA VITAL",
    "A597": "A597_JOYCE",
    "G193": "G193_ALEJANDRA CACHAY"
}

CICLO28["ADVISER_FULLNAME"] = CICLO28["ADVISER_CODE"].map(codigo_valores)


CICLO28["Group"] = CICLO28["ADVISER_CODE"].str[:2]


CICLO28.loc[CICLO28["PRODUCT_TITLE"].str.contains("ASCENSO", na=False), "PRODUCT_TITLE"] = "ASCENSO 2024 II"
CICLO28.loc[CICLO28["PRODUCT_TITLE"].str.contains("SIMULACRO", na=False), "PRODUCT_TITLE"] = "SIMULACRO ASCENSO 2024"


#REEMPLAZAR LOS HEADER PARA MONGO 
nuevos_nombres = [
    "Cycle", "Month", "Year", "Group", "Temporary_Stamp", "Email", "Promoter", 
    "Teacher_First_Name", "Teacher_First_Surn", "Phone_Number", 
    "Current_Payment_Date", "Modality", "Amount_Deposited", "Bank_Account", 
    "Operation_Number", "Academic_Product_Purchased", "Teacher_Speciality", 
    "Course_Duration", "Observations", "Receipt_Image", "Sales_Origin", 
    "Voucher_Type", "Referred_Number", "Teacher_Dni", "Total_Price", 
    "Full_Name", "State", "Continuity", "Payment_Date", "Review_Date", "code"
]
if len(nuevos_nombres) == len(CICLO28.columns):
    CICLO28.columns = nuevos_nombres
    
CICLO28 = CICLO28.astype(str)

CICLO28.to_json("SUBIR ESTE ARCHIVO A MONGO.json", orient="records", force_ascii=False, indent=4)

#header para google sheets
nuevo_encabezado = [
    "CICLO", "MES", "AÑO", "GRUPO", "MARCA TEMPORAL", "DIRECCION DE CORREO", "PROMOTOR", 
    "DOCENTE NOMBRES", "DOCENTE APELLIDOS", "NUMERO DE CELULAR", "FECHA DE PAGO", "MODALIDAD", 
    "MONTO DEPOSITADO", "CUENTA BANCARIA", "NUMERO DE OPERACION", "PRODUCTO ACADEMICO", 
    "ESPECIALIDAD", "DURACION DEL CURSO", "OBSERVACIONES", "VOUCHER", "ORIGEN DE LA VENTA", 
    "TIPO DE VOUCHER", "DNI DEL QUE REFIERE", "DNI DEL DOCENTE", "MONTO TOTAL", 
    "MONTO TOTAL", "ESTADO", "CONTINUIDAD", "FECHA DEL SIGUENTE PAGO", "FECHA DE REVISION", 
    "CODIGO"
]

if len(nuevo_encabezado) == len(CICLO28.columns):
    CICLO28.columns = nuevo_encabezado

CICLO28.to_excel("SUBIR ESTE ARCHIVO A GOOGLE SHEETS.xlsx", index=False)
