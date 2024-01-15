# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:52:53 2023

@author: LuPerez
"""


class FirmaDigital:
    
    def getFirma(self, imagen_base64):
        return """
        <br><br><br>
        <table cellpadding="0" cellspacing="0" border="0" style="font-family: Calibri, sans-serif;">
            <tr>
                <td style="font-weight: bold; color: green;">Lucia Perez Moron</td>
            </tr>
            <tr>
                <td>Analista de Inteligencia de Negocios</td>
            </tr>
            <tr>
                <td>Tel. - Int. 2025</td>
            </tr>
            <tr>
                <td>Oficina Nacional – Santa Cruz</td>
            </tr>
            <tr>
                <td colspan="2" style="font-size: 8px; padding-top: 10px;">
                    El contenido de este correo electrónico es confidencial y está dirigido únicamente al destinatario especificado en el mensaje. Está estrictamente prohibido compartir cualquier parte de este mensaje con terceros, sin el consentimiento por escrito del remitente. Si usted ha recibido este mensaje por error, por favor contáctese con el remitente y elimine este correo electrónico así como cualquier copia que hubiera podido obtener.<br><br>
                    The content of this email is confidential and is addressed only to the recipient specified in the message. It is strictly forbidden to share any part of this message with third parties, without the written consent of the sender. If you have received this message in error, please contact the sender and delete this email as well as any copy you could have obtained.
                </td>
            </tr>
        </table>
            """