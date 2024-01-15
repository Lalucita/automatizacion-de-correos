# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:20:19 2023

@author: LuPerez
"""

import os
import base64
from PIL import Image

class CargarImagen:
    
    imagen_bien=""
    imagen_admiracion=""
    imagen_mal=""
    logo_bi=""
    logo_bnb=""
    logo_bnb_firma=""
    
   # """
    def copiarImagenes(self):
        input_images_path = "C:/Users/LuPerez/Desktop/subgerentes_que_falta"
        files_names = os.listdir(input_images_path)
        print(files_names)
        
        output_images_path="D:/Lucia/PYTHON/envioDeCorreos/Subgerentes_nuevo/"
        
       
        for file_name in files_names:
            if file_name.split(".")[-1] not in ["png"]:
                continue
            
            image_path = input_images_path + "/" + file_name
            print(image_path)
            print("IMAGEN "+file_name)
            print("--------------------------------")            
            imagen = Image.open(image_path)
            ancho, alto = imagen.size
            imagen = imagen.resize((70,70))
            imagen.save(output_images_path+file_name)
            
            
    def achicarImagen(self, image_path, ancho,alto):
        imagen = Image.open(image_path)
        ancho, alto = imagen.size
        #imagen = imagen.resize((ancho//2,alto//2))
        magen = imagen.resize(ancho,alto)
        imagen.save(image_path+"1")
        
    def achicarImagen_(self, image_path, ancho, alto):
        try:
            imagen = Image.open(image_path)
            imagen_achicada = imagen.resize((ancho, alto), Image.ANTIALIAS)
            imagen_achicada.save(image_path)
        except Exception as e:
            print(f"Error al achicar la imagen: {str(e)}")     


    def achicarImagen(self,image_path, ancho_deseado):
        try:
            imagen = Image.open(image_path)

            # Calcula el nuevo alto manteniendo la proporción original
            proporcion = ancho_deseado / float(imagen.size[0])
            alto_deseado = int(float(imagen.size[1]) * float(proporcion))

            # Redimensiona la imagen
            imagen_achicada = imagen.resize((ancho_deseado, alto_deseado), Image.ANTIALIAS)

            # Guarda la imagen achicada
            imagen_achicada.save(image_path)
        except Exception as e:
            print(f"Error al achicar la imagen: {str(e)}")        
        
    def obtenerImagenBase64(self, codigoImagen):
        image_path ="fotosSubjerentes/"+str(codigoImagen).strip()+".png"
        try:
            with open(image_path,"rb") as img_file:
                my_string=base64.b64encode(img_file.read())

            my_string=my_string.decode('utf-8')
            return my_string
        except Exception:
            print(image_path)
            image_path ="fotosSubjerentes/0.png"
            with open(image_path,"rb") as img_file:
                my_string=base64.b64encode(img_file.read())

            my_string=my_string.decode('utf-8')
            return my_string
    
    

    def achicarTodasLasImagenesEnCarpeta(self, carpeta, nuevo_ancho, nuevo_alto):
        try:
            for archivo in os.listdir(carpeta):
                if archivo.endswith((".jpg", ".png", ".jpeg")):
                    ruta_imagen = os.path.join(carpeta, archivo)
                    print(ruta_imagen+" esta imagen")
                    self.achicarImagen_(ruta_imagen, nuevo_ancho, nuevo_alto)
        except Exception as e:
            print(f"Error al achicar las imágenes en la carpeta: {str(e)}")


    def cargarImagen(self, image_path):
        with open(image_path,"rb") as img_file:
            my_string=base64.b64encode(img_file.read())

        my_string=my_string.decode('utf-8')
        return my_string

    def cargarImagenBien(self):
        if not self.imagen_bien:
            image_path ="iconos/bien.png"
            self.imagen_bien= self.cargarImagen(image_path)
        return self.imagen_bien

        
    
    def cargarImagenAdmiracion(self):
        if not self.imagen_admiracion:
            image_path ="iconos/admiracion.png"
            self.imagen_admiracion= self.cargarImagen(image_path)
        return self.imagen_admiracion
    
    
    def cargarImagenMal(self):
        if not self.imagen_mal:
            image_path ="iconos/iconX.png"
            self.imagen_mal= self.cargarImagen(image_path)
        return self.imagen_mal
    
    def cargarLogoBI(self):
        if not self.logo_bi:
            image_path ="iconos/FBI.png"
            self.logo_bi= self.cargarImagen(image_path)
        return self.logo_bi
    
    def cargarLogoBNB(self):
        if not self.logo_bnb:
            image_path ="iconos/bnbVerde.png"
            self.logo_bnb= self.cargarImagen(image_path)
        return self.logo_bnb
    
    def cargarLogoBNB_firma(self):
        if not self.logo_bnb_firma:
            image_path ="iconos/logo_bnb_firma.png"
            self.logo_bnb_firma= self.cargarImagen(image_path)
        return self.logo_bnb_firma

imagen=CargarImagen()
#imagen.copiarImagenes()
#imagen.achicarImagen_("D:/Lucia/PYTHON/envioDeCorreos/logo/cuadro_atras.png", 30,70)
imagen.achicarTodasLasImagenesEnCarpeta("D:/Lucia/PYTHON/envioDeCorreos/Subgerentes_nuevo", 70, 70)
#print(imagen.obtenerImagen("200573"))
#imagen.copiarImagenes()
#imagen.achicarImagen("C:/Users/LuPerez/Desktop/SubjerentesQueFaltan/CODIGOS/0.png")




    