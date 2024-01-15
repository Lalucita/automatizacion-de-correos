# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:14:09 2023

@author: LuPerez
"""

import win32com.client as win32
import win32com.client


class SendMail:
    
    

    
    def save_Mail(self, content, subject, TO, CC):
        # Crear una instancia de Outlook
        olApp = win32.Dispatch('Outlook.Application')
        
        # Crear un nuevo correo
        mailItem = olApp.CreateItem(0)
        
        # Configurar el asunto y el contenido
        mailItem.Subject = subject
        mailItem.HTMLBody = content
        
        # Configurar destinatarios (TO y CC)
        mailItem.To = TO
        mailItem.Cc = CC
        
        # Guardar en borradores
        mailItem.Save()





    
    def sendingMail(self,content, subject):
        olApp = win32.Dispatch('Outlook.Application')
        #olNS=olApp.GetNameSpace('MAPI')

        mailItem= olApp.CreateItem(0)
        mailItem.Subject=subject
       
        #mailItem.BodyFormat=1

        #mailItem.To='LoCabrera@bnb.com.bo;RRojas@bnb.com.bo'

        mailItem.To="LuPerez@bnb.com.bo"
        mailItem.Cc="LuPerez@bnb.com.bo"
        mailItem.HTMLBody=content
        mailItem.Display()
        mailItem.Send()
        
        
    
    def sendMail(self,content,subject, destinatarios,destinatariosCC):
        
        olApp = win32.Dispatch('Outlook.Application')

        mailItem= olApp.CreateItem(0)
        mailItem.Subject=subject

        mailItem.To=destinatarios
        mailItem.Cc=destinatariosCC
        mailItem.HTMLBody=content
        mailItem.Display()
        mailItem.Send()
        
        
        
    def enviar_correo_con_firma(self, subject, content):
        try:
            olApp = win32com.client.Dispatch('Outlook.Application')
            mailItem = olApp.CreateItem(0)
            mailItem.Subject = subject
            mailItem.To = "LuPerez@bnb.com.bo"
            mailItem.Cc = "LuPerez@bnb.com.bo"
            mailItem.HTMLBody = content

        # Obtener la firma del usuario
            namespace = olApp.GetNamespace("MAPI")
            account = namespace.Accounts.Item(1)  # Si tienes varias cuentas configuradas, puedes ajustar el índice.
            firma = account.Signature

        # Agregar la firma al cuerpo del correo
            mailItem.HTMLBody += f"<br><br>{firma}"

            mailItem.Display()
        # Para enviar automáticamente el correo, descomenta la línea siguiente
        # mailItem.Send()
        except Exception as e:
            print(f"Error al enviar el correo: {str(e)}")
        
  