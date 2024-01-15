# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:04:50 2023

@author: LuPerez
"""

import pandas as pd
import base64
from PIL import Image
from CargarImagen import CargarImagen


imagenes = CargarImagen()


class tablaHTMLproductividad:
    
    colorGris="#f2f2f2"
    colorLila="#694780"
    cargarImagen = CargarImagen()
    
    
    def getColumnas_con_pendientes(self):
        estilo_comun = 'style="width: 150px; font-family: Calibri;"'

        encabezados = [
            "Subgerente",
            "Agencia",
            "Productividad Desembolsos",
            "Puntualidad Desembolsos",
            "Puntualidad Pendientes"
            "Pendientes $us"
            ]

        columnas = f"""<tr style="background-color: {self.colorLila}; color: white;">"""
        columnas += ''.join([f'<th {estilo_comun}>{encabezado}</th>' for encabezado in encabezados])
        columnas += """</tr>"""
        return columnas
    

    
    def getColumnas(self):
        estilo_comun = f'style="width: 150px; font-family: Calibri;"'

        encabezados = [
            "Subgerente",
            "Agencia",
            "Productividad Desembolsos",
            "Puntualidad Desembolsos",
            "Puntualidad Pendientes"
            ]

        columnas = f"""<tr style="background-color: {self.colorLila}; color: white;">"""
        columnas += ''.join([f'<th {estilo_comun}>{encabezado}</th>' for encabezado in encabezados])
        columnas += """</tr>"""
        return columnas


   
    def cargarCampoImagen__(self, codigoImagen):
        imagen_base64 = self.cargarImagen.obtenerImagenBase64(codigoImagen)
        estilo_comun = f'style="background-color: {self.colorGris}; text-align: center;"'
        #img_tag = f'<img src="data:image/png;base64,{imagen_base64}" alt="Imagen">'
        
        width = 30  # Ancho deseado
        height = 30  # Altura deseada

        img_tag = f'<img src="data:image/png;base64,{imagen_base64}" alt="Imagen" style="width:{width}px; height:{height}px;">'


        campo_imagen = f'<td {estilo_comun}>{img_tag}</td>'
        return campo_imagen
    

    def crearCampoProductividad(self, dato, meta_produc):
        estilo_comun_float = f'style="background-color: {self.colorGris}; font-family: Calibri;display:flex; align-items:center"'
        imagen_base64=""
        if dato<meta_produc:
            imagen_base64 = self.cargarImagen.cargarImagenMal()
        else:
            imagen_base64= self.cargarImagen.cargarImagenBien()
        img_tag = f'<img src="data:image/png;base64,{imagen_base64}" alt="Imagen" style="margin-right: 5px;">'
        
        return f'<td {estilo_comun_float}>{img_tag}{int(dato)}%</td>'
        

    def crearCampoTabla(self, df_subgerentes, dato, rango):
        if rango == 0:
            codigo_empleado_sub = self.obtener_codigo_empleado(dato, df_subgerentes)
            campo_img = self.cargarCampoImagen__(codigo_empleado_sub)
            return campo_img

        estilo_comun = f'style="background-color: {self.colorGris}; font-family: Calibri;"'

        if isinstance(dato, float):
            return self.crear_numero_con_imagen(dato)

        estilo_general = estilo_comun
        return f'<td {estilo_general}>{dato}</td>'
    
    def crear_numero_con_imagen(self, dato):
        estilo_comun_float = f'style="background-color: {self.colorGris}; font-family: Calibri;display:flex; align-items:center"'
        imagen_base64 = self.cargar_icono_prod(dato)
        img_tag = f'<img src="data:image/png;base64,{imagen_base64}" alt="Imagen" style="margin-right: 5px;">'
        
        return f'<td {estilo_comun_float}>{img_tag}{int(dato)}%</td>'

    
    def cargar_icono_prod(self, dato):
        if dato < 71:
            return self.cargarImagen.cargarImagenMal()
        elif 70 < dato < 89:
            return self.cargarImagen.cargarImagenAdmiracion()
        else:
            return self.cargarImagen.cargarImagenBien()

    
    
    def obtener_codigo_empleado(self, id_agencia, dataframe):
        # Filtra el DataFrame por IdAgencia
        filtro = dataframe['IdAgencia'] == id_agencia
    
        if filtro.any():
        # Si hay coincidencia, obtén el CodigoEmpleado
            codigo_empleado = dataframe.loc[filtro, 'CodigoEmpleado'].iloc[0]
            return codigo_empleado
        else:
        # Si no hay coincidencia, devuelve 0
            return 0
    
    
    
    def crearTable(self, df, df_subgerentes,meta_produc ):
        
        tablaExcel="""<table style="border: black 1px solid">"""
        tablaExcel=tablaExcel+self.getColumnas()
        
        df = df.fillna('')
        
        df=df.sort_values('productividad',ascending=False)
        
        for i in range(len(df)):
            
            tablaExcel=tablaExcel+"""<tr >"""
            for j in range (len(df.iloc[i])):
                dato=df.iloc[i][j]
                if j==2:
                    tablaExcel=tablaExcel+self.crearCampoProductividad(dato, meta_produc)
                else:
                    tablaExcel=tablaExcel+self.crearCampoTabla(df_subgerentes,dato, j)
                
            tablaExcel=tablaExcel+"""</tr >"""
        
        
        tablaExcel=tablaExcel+"""</table>  <br>"""
        return tablaExcel
    
    
    
