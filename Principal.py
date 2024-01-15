# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:29:12 2023
 
@author: LuPerez
"""

import pandas as pd

from SendMail import SendMail

from Sql import SqlConexion
from tablaHTMLproductividad import tablaHTMLproductividad
from SendMail import SendMail
from Sucursales import sucursales
from CalculadoraProductividad import Calculadora_Productividad
from ConstructorCuerpoCorreo import construir_cuerpo_correo,obtener_analisis,get_firma,TITULO

from datetime import datetime


conexionBd = SqlConexion()
tablaHTML = tablaHTMLproductividad()
enviadorCorreo = SendMail()
sucursales = sucursales()
engine = conexionBd.crearEngine()
fecha_data = conexionBd.obtenerUltimaFechaData_Creditos_ejecutivos(engine)
print(fecha_data)
calculadoraP = Calculadora_Productividad(fecha_data)
META_PRODUCTIVIDAD =calculadoraP.getProductividad()

fecha = conexionBd.obtenerUltimaFechaData_Creditos_ejecutivos(engine)
print(fecha)

df_subgerentes = conexionBd.ObtenerSubjerentesBancaPErsonas(engine)
df_sucursales = sucursales.getSucursalesPersonas()

correo_Resumen=""



def quitar_agencias(df_sucursales, ciudad):
    if ciudad=='COCHABAMBA':
        df_filtrado = df_sucursales[~df_sucursales['agencia'].isin(["CB - BLANCO GALINDO", "CB - OF CENTRAL"])]
        return df_filtrado
    else:
        return df_sucursales


def obtener_saludo():
    hora_actual = datetime.now().hour
    saludo=""
    if 6 <= hora_actual < 12:
        saludo="Buenos días"
    elif 12 <= hora_actual < 18:
        saludo="Buenas tardes"
    else:
        saludo="Buenas noches"
        
   # return "<br>"+saludo+"<br>"
    return "<br><span style='font-family: Calibri, sans-serif; font-size: 12pt;'>"+saludo+"</span><br>"



for index, row in df_sucursales.iterrows():
    ciudad = row['Ciudad']
    destinatarios = row['Destinatarios']
    destinatarios_en_cc = row['Destinatarios_en_CC']
    
    df_sucursal = conexionBd.ejecutarSP(engine, ciudad)
    df=quitar_agencias(df_sucursal, ciudad)
    
    
    texto_correo=construir_cuerpo_correo(df, META_PRODUCTIVIDAD)
    tabla = tablaHTML.crearTable(df, df_subgerentes,META_PRODUCTIVIDAD)
    subject="Gestión Comercial Banca Personas _ " + ciudad
    enviadorCorreo.save_Mail(texto_correo + tabla+get_firma(), subject,destinatarios, destinatarios_en_cc)
    
    ##correo resumen para Don Rolando
    df_pendientesUSD=conexionBd.get_pendientes_USD_mes_actual(ciudad, engine)
    analisis_sucursal=obtener_analisis(df, df_pendientesUSD, META_PRODUCTIVIDAD,ciudad)
    correo_Resumen=correo_Resumen+analisis_sucursal
    correo_Resumen=correo_Resumen+tabla


correo_Resumen=TITULO+obtener_saludo()+correo_Resumen+get_firma()
enviadorCorreo.save_Mail(correo_Resumen, "Indicadores Gestión Comercial Banca Personas","LuPerez@bnb.com.bo", "LuPerez@bnb.com.bo")
correo_Resumen=""


###------- envío a banca MICROCRÉDITOS------------ 


df_subgerentes_micros = conexionBd.ObtenerSubjerentesBancaMicrocreditos(engine)
df_sucursales = sucursales.getSucursalesMicrocreditos()


for index, row in df_sucursales.iterrows():
    ciudad = row['Ciudad']
    destinatarios = row['Destinatarios']
    destinatarios_en_cc = row['Destinatarios_en_CC']
    
    df_sucursal = conexionBd.ejecutar_sp_indicadores_microcreditos(engine, ciudad)
   
    
    texto_correo=construir_cuerpo_correo(df_sucursal, META_PRODUCTIVIDAD)
    tabla = tablaHTML.crearTable(df_sucursal, df_subgerentes_micros, META_PRODUCTIVIDAD)
    subject="Gestión Comercial Banca Mircrocréditos _ " + ciudad
    enviadorCorreo.save_Mail(texto_correo + tabla+get_firma(), subject,destinatarios, destinatarios_en_cc)
    
    
    ##correo resumen para Don Rolando
    df_pendientesUSD=conexionBd.get_pendientes_USD_mes_actual(ciudad, engine)
    analisis_sucursal=obtener_analisis(df_sucursal, df_pendientesUSD, META_PRODUCTIVIDAD,ciudad)
    correo_Resumen=correo_Resumen+analisis_sucursal
    correo_Resumen=correo_Resumen+tabla
    
    
correo_Resumen=TITULO+obtener_saludo()+correo_Resumen+get_firma()
enviadorCorreo.save_Mail(correo_Resumen, "Indicadores Gestión Comercial Banca Microcréditos","LuPerez@bnb.com.bo", "LuPerez@bnb.com.bo")
    