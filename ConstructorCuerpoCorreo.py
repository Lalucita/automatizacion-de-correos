import requests
import json
import pandas as pd
from datetime import datetime
from CargarImagen import CargarImagen
from FirmaDigital import FirmaDigital

# Configuración
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

API_KEY = "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"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "OpenAI-Python"
}
imagenes = CargarImagen()
imagenbi = imagenes.cargarLogoBI()
imagenBNB = imagenes.cargarLogoBNB()
imagenfirma = imagenes.cargarLogoBNB_firma()

firma=FirmaDigital()




def get_firma():
    return firma.getFirma(imagenfirma)

def generar_titulo(imagen_base64, imagen_base64_bnb):
    # Ruta de la imagen (debes reemplazar 'ruta_de_la_imagen' con la ruta real de tu imagen)
    img_tag = f'<img src="data:image/png;base64,{imagen_base64}">'
    img_tag_bnb = f'<img src="data:image/png;base64,{imagen_base64_bnb}">'
    # Código HTML para la tabla
    tabla_html = f'''
        <table border="0"   >
            <tr>
                <td >{img_tag}</td>
                <td style="text-align: center; font-weight: bold;width:700px">
                <h2 style="font-family: 'Calibri', sans-serif; margin: 0;">Productividad de las agencias</h2>
                </td>
                <td >{img_tag_bnb}</td>
                </tr>
        </table> <br><br>
    '''
    return tabla_html


TITULO = generar_titulo(imagenbi, imagenBNB)



def obtener_saludo():
    hora_actual = datetime.now().hour
    saludo=""
    if 6 <= hora_actual < 12:
        saludo="Buenos días"
    elif 12 <= hora_actual < 18:
        saludo="Buenas tardes"
    else:
        saludo="<br><br>Buenas noches<br>"
    
    return "<br>"+saludo+"<br>"


def generarTablaInvisible(texto):
    return f"""
        <table style="border-collapse: collapse; visibility: hidden;width: 900px; font-family: Calibri, sans-serif;">
            <tr>
                <td>{texto}</td>
            </tr>
        </table>
    """

def respuesta_positiva_una_agencia(valor):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Eres un analista de datos que esta evaluando a oficiales"},
            {"role": "user",
             "content": f"necesito un mensaje de felicitacion a la siguiente agencia que superó la meta de productividad de {valor}%. este mensaje tiene que ser en 30 palabras"}
        ]
    }

    # Realizar la solicitud a la API
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    response_data = response.json()

    # Extraer el resumen del contenido de respuesta
    summary = response_data['choices'][0]['message']['content']
    return summary + "<br><br>"


def generar_lista(lista_agencia):
    elementos_html = ['<ul>']
    for agencia in lista_agencia:
        elementos_html.append(f"    <li>{agencia}</li>")
    elementos_html.append('</ul>')
    return "\n".join(elementos_html)

def generar_negrilla(palabra):
    return f"<strong>{palabra}</strong>"
    

def construir_respuesta(mensaje, lista_agencia):
    return mensaje + "<br>" + lista_agencia + "<br>"



def respuesta_positiva(valor):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Eres un analista de datos que esta evaluando a oficiales"},
            {"role": "user",
             "content": f"necesito un mensaje de felicitacion a las agencias que superaron la meta de productividad de {valor}%. este mensaje tiene que ser en 30 palabras"}
        ]
    }

    # Realizar la solicitud a la API
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    response_data = response.json()

    # Extraer el resumen del contenido de respuesta
    summary = response_data['choices'][0]['message']['content']
    return summary + "<br>"


def respuesta_negativa(valor):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Eres un analista de datos que esta evaluando a oficiales"},
            {"role": "user",
             "content": f"necesito un mensaje de alerta para que presten atencion a las agencias que no llegaron a la meta de productividad. este mensaje tiene que ser en 30 palabras"}
        ]
    }

    # Realizar la solicitud a la API
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    response_data = response.json()

    # Extraer el resumen del contenido de respuesta
    summary = response_data['choices'][0]['message']['content']
    return summary + "<br><br>"

def respuesta_negativa_una_agencia(valor):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Eres un analista de datos que esta evaluando a oficiales"},
            {"role": "user",
             "content": f"necesito un mensaje de alerta para que presten atencion a la  agencia que no llegó a la meta de productividad. este mensaje tiene que ser en 30 palabras"}
        ]
    }

    # Realizar la solicitud a la API
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    response_data = response.json()

    # Extraer el resumen del contenido de respuesta
    summary = response_data['choices'][0]['message']['content']
    return summary + "<br>"





def hacer_consulta(pregunta):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "experto analista de gestion comercial del banco"},
            {"role": "user",
             "content": pregunta}
        ],"temperature": 0.8
    }

    # Realizar la solicitud a la API
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    response_data = response.json()

    # Extraer el resumen del contenido de respuesta
    summary = response_data['choices'][0]['message']['content']
    return summary






def construir_cuerpo_correo(df_sucursal, META_PRODUCTIVIDAD):
    texto_correo=""
    df_negativo = df_sucursal[df_sucursal['productividad'] < META_PRODUCTIVIDAD]
    df_positivo = df_sucursal[df_sucursal['productividad'] >= META_PRODUCTIVIDAD]
    name_agencias_positiva = df_positivo['agencia'].to_list()
    name_agencias_negativa = df_negativo['agencia'].to_list()
    if len(name_agencias_positiva) == 1:
        texto_correo = respuesta_positiva_una_agencia(META_PRODUCTIVIDAD)
        lista_agencias_pos = generar_lista(name_agencias_positiva)
        texto_correo = construir_respuesta(texto_correo, lista_agencias_pos)
    if len(name_agencias_positiva)>1:
        texto_correo=respuesta_positiva(META_PRODUCTIVIDAD)
        lista_agencias_pos = generar_lista(name_agencias_positiva)
        texto_correo = construir_respuesta(texto_correo, lista_agencias_pos)
   
    if len(name_agencias_negativa)==1:
        texto_negativas=respuesta_negativa_una_agencia(META_PRODUCTIVIDAD)
        lista_agencias = generar_lista(name_agencias_negativa)
        texto_correo=texto_correo+construir_respuesta(texto_negativas, lista_agencias)
    if len(name_agencias_negativa)>1:
        texto_negativas=respuesta_negativa(META_PRODUCTIVIDAD)
        lista_agencias = generar_lista(name_agencias_negativa)
        texto_negativas=construir_respuesta(texto_negativas, lista_agencias)
        texto_correo=texto_correo+texto_negativas
    saludo=obtener_saludo()
    texto_correo=generarTablaInvisible(saludo+texto_correo)
    return TITULO+texto_correo



def obtener_analisis(df_agencias_debajo,df_pendientes_USD,meta_produc, sucursal):
    if len(df_agencias_debajo)==0:
        return ""
    prompt=generarPrompt(df_agencias_debajo, df_pendientes_USD, meta_produc)
    respuesta=generar_negrilla(sucursal+": ")+hacer_consulta(prompt)
    respuesta=generarTablaInvisible(respuesta)
    return "<br>"+respuesta+"<br>"


def generarPrompt(df_agencias_debajo, df_pendientes_USD,meta_produc):
    df_agencias_debajo = pd.merge(df_agencias_debajo, df_pendientes_USD[['Cod_Agencia', 'pendientesUSD']],
                               left_on='cod_agencia', right_on='Cod_Agencia', how='left')
    cant_palabras=70#len(df_agencias_debajo)*17
    
    prompt=f""" eres un experto financiero. necesito un analisis de exactamnte {cant_palabras} palabras.
                La meta de productividad es de ({meta_produc}%), 
                felicite a las agencias que lo lograron, sin ser muy salamero; 
                luego indique donde deben mejorar las demás agecias, donde ajustar. 
    """
    for index, row in df_agencias_debajo.iterrows():
        agencia = row['agencia']
        productividad=int(row['productividad']) if pd.notna(row['productividad']) else 0
        puntualidad_desembolso=row['PuntualidadDesembolsos']
        puntualidad_desembolso=int(puntualidad_desembolso) if pd.notna(puntualidad_desembolso) else 0
        puntualidad_pendiente=row['PuntualidadPendientes']
        puntualidad_pendiente=int(puntualidad_pendiente) if pd.notna(puntualidad_pendiente) else 0
        #pendientesUSD=row['pendientesUSD']
        #pendientesUSD=int(pendientesUSD) if pd.notna(pendientesUSD) else 0
        
        agencias=f"""La agencia {agencia} con productividad del {productividad}%, 
                    una puntualidad de desembolsos del {puntualidad_desembolso}%, 
                    puntualidad de pendientes del {puntualidad_pendiente}%"""
                    #y {pendientesUSD}$us en creditos pendientes para desembolso."""
        prompt=prompt+agencias
    prompt=prompt+"""solo dame tu opinion, no menciones que eres un experto financiero,
    directo dame solo el texto, por favor"""
    return prompt


        

preguntaScz ="""eres un experto analista de gestion comercial del banco, y tienes que analizar 
            todas las agencias que no cumplieron con la meta de productividad (21%), 
            mencionando todos los indicadores con las agencias que deben mejorar; da tu opinion como experto 
            financiero en  un total de 69 palabras. La agencia Patio Design con productividad del 15%, 
            una puntualidad de desembolsos del 100%, puntualidad de pendientes del 92% y 408000$us 
            en creditos pendientes para desembolso. 
            La agencia Central con productividad del 10%, una puntualidad de desembolsos del 91%, 
            puntualidad de pendientes del 71% y 2236000$us en creditos pendientes para desembolso.  
            La agencia Norte autobanco con productividad del 9%, una puntualidad de desembolsos del 83%, 
            puntualidad de pendientes del 79% y 550000$us en creditos pendientes para desembolso. 
            La agencia Ventura Mall con productividad del 5%, una puntualidad de desembolsos del 100%, 
            puntualidad de pendientes del 38% y 359000$us en creditos pendientes para desembolso. 
            solo dame tu opinion, no menciones que eres un experto analista, ni digas en mi opinion, 
            directo dame el texto, por favor.
            """
            


            
preguntaLPZ="""eres un experto analista de gestion comercial del banco, y tienes que analizar 
            todas las agencias que no cumplieron con la meta de productividad (21%), 
            mencionando todos los indicadores con las agencias qué deben mejorar; da tu opinion como experto 
            financiero en menos de 100 palabras.  La agencia miraflores con productividad del 16%, 
            una puntualidad de desembolsos del 100%, puntualidad de pendientes del 0% y 50000$us 
            en creditos pendientes para desembolso. La agencia san miguel con productividad del 12%,
            una puntualidad de desembolsos del 33%, puntualidad de pendientes del 90% y 732000 $us
            en creditos pendientes para desembolso.  La agencia achumani con productividad del 7%,
            una puntualidad de desembolsos del 100%, puntualidad de pendientes del 50% y 377000$us en 
            creditos pendientes para desembolso. La agencia central con productividad del 5%, una 
            puntualidad de desembolsos del 83%, puntualidad de pendientes del 55% y 777000$us en creditos 
            pendientes para desembolso. La agencia irpavi con productividad del 4%, una puntualidad de 
            desembolsos del 100%, puntualidad de pendientes del 60% y 777000$us en creditos pendientes 
            para desembolso.La agencia 20 de octubre con productividad del 3%, una puntualidad de desembolsos 
            del 100%, puntualidad de pendientes del 57% y 579000$us en creditos pendientes para desembolso.
            La agencia Torres del poeta con productividad del 3%, una puntualidad de desembolsos del 100%, 
            puntualidad de pendientes del 22% y 279000$us en creditos pendientes para desembolso.solo dame 
            tu opinion, no menciones que eres un experto analista, ni digas en mi opinion, directo dame el 
            texto, por favor"""
            
otra_pregunta="""'Es necesario realizar ajustes en las agencias mutualista y mype plan 3000. En la agencia mutualista, se deben mejorar la puntualidad en desembolsos y reducir los créditos pendientes para desembolso. En la agencia mype plan 3000, se deben trabajar temas de puntualidad en desembolsos y pendientes, así como reducir la cantidad de créditos pendientes. Estos factores contribuirán a mejorar la productividad y el desempeño financiero de las agencias.
                    
                '"""




respuesta =hacer_consulta(preguntaScz)
respuesta1=hacer_consulta(preguntaLPZ)
print(respuesta)
