import bs4
import requests


#Usamos requests y bs4 para extraer datos y lo ponemos en una lista llamada tabla
def extraer_tabla():
	url_b = 'https://www.buenasalud.net/2010/05/30/tabla-de-peso-y-estatura.html'
	
	respuesta = requests.get(url_b)
	html  = respuesta.text
	
	soupe = bs4.BeautifulSoup(html, 'html.parser')
	tabla = soupe.find_all('td')
	return tabla

#agrupamos las alturas de las mujeres extraidas de tabla en una lista llamada tabla_alt_mujer
def altura_mujer():
	tabla_alt_mujer = extraer_tabla()
	tabla_alt_mujer = tabla_alt_mujer[13:223]
	
	aturas_m_sucias = [] 
	alturas_m_limpias = []
	
	for i in range(0,210,7):
		aturas_m_sucias.append(tabla_alt_mujer[i:i+1])
	
	#Limpiamos los datos de las alturas de las mujeres y lo ponemos en una lista llamada alturas_m_limpias
	for alturas_m in aturas_m_sucias:
		item_alt_m = str(alturas_m)
		item_alt_m = item_alt_m[45:-15]
		item_alt_m = float(item_alt_m)
		alturas_m_limpias.append(item_alt_m)

	return alturas_m_limpias

#agrupamos los pesos de las mujeres extraidas de tabla en una lista llamada tabla_peso_mujer
def peso_mujer():
	tabla_peso_mujer = extraer_tabla()
	tabla_peso_mujer = tabla_peso_mujer[13:223]

	pesos_m_sucio = []
	pesos_m_limpio = []

	for i in range(1,209,7):
		pesos_m_sucio.append(tabla_peso_mujer[i:i+1])
		pesos_m_sucio.append(tabla_peso_mujer[i+1:i+2])

	#Limpiamos los datos de los pesos de las mujeres y lo ponemos en una lista llamada pesos_m_limpios
	for pesos_m in pesos_m_sucio:
		item_pes_m = str(pesos_m)
		item_pes_m = item_pes_m[37:-6]
		item_pes_m = float(item_pes_m)
		pesos_m_limpio.append(item_pes_m)

	return pesos_m_limpio

		

#agrupamos las alturas de los hombres extraidas de tabla en una lista llamada tabla_alt_hombre
def altura_hombre():
	tabla_alt_hombre = extraer_tabla()
	tabla_alt_hombre = tabla_alt_hombre[236:446]

	alturas_h_sucias = []
	alturas_h_limpias = []

	for j in range(0,210,7):
		alturas_h_sucias.append(tabla_alt_hombre[j:j+1])

	#Limpiamos los datos de las alturas de los hombres y le ponemos en una tabla llamada alturas_h_limpias
	for alturas_h in alturas_h_sucias:
		item_alt_h = str(alturas_h)
		item_alt_h = item_alt_h[61:-15]
		item_alt_h = float(item_alt_h)
		alturas_h_limpias.append(item_alt_h)

	return alturas_h_limpias


#agrupamos los pesos de los hombres en una lista llamada tabla_peso_hombre
def peso_hombre():
	tabla_peso_hombre = extraer_tabla()
	tabla_peso_hombre = tabla_peso_hombre[236:446]

	pesos_h_sucios = []
	pesos_h_limpio = []

	for i in range(1,209,7):
		pesos_h_sucios.append(tabla_peso_hombre[i:i+1])
		pesos_h_sucios.append(tabla_peso_hombre[i+1:i+2])

	#Limpiamos los datos de pesos de los hombres y le ponemos en una lista llamada pesos_h_limpio
	for pesos_h in pesos_h_sucios:
		item_pes_h = str(pesos_h)
		item_pes_h = item_pes_h[37:-6]
		item_pes_h = float(item_pes_h)
		pesos_h_limpio.append(item_pes_h)

	return pesos_h_limpio


#Esta funcion agrupa los datos de las mujeres en una lista de listas [[peso minimo,peso maximo,segun su altura]]
def final_lista_mujer():

	lista_esp_mujer = []

	lista_altura_mujer = altura_mujer()
	lista_peso_mujer   = peso_mujer()

	for i in range(0,59,2):		
		lista_esp_mujer.append(lista_peso_mujer[i:i+2])

	for j in range(0,30,1):		
		lista_esp_mujer[j].append(lista_altura_mujer[j])

	
	return lista_esp_mujer

#Esta funcion agrupa los datos de los hombres en una lista de listas [[peso minimo,peso maximo,segun su altura]]
def final_lista_hombre():

	lista_esp_homre = []
	lista_altura_hombre = altura_hombre()
	lista_peso_hombre   = peso_hombre()

	for i in range(0,59,2):		
		lista_esp_homre.append(lista_peso_hombre[i:i+2])

	for j in range(0,30,1):		
		lista_esp_homre[j].append(lista_altura_hombre[j])

	
	return lista_esp_homre


#Añadimos en una lista de lista datos de mujeres y hombre
def lista_X():

	lista_X_mujeres = final_lista_mujer()
	lista_X_hombres = final_lista_hombre()
	lista_mh = [] 
	for i in range(0,30,1):
		lista_mh.append(lista_X_mujeres[i])
		lista_mh.append(lista_X_hombres[i])

	return lista_mh

#creamos una lista que asignara a cada dato de la lista_X() si es 'Mujer' o 'Hombre' segun sus medidas
def lista_Y():
	lista_y_mh = []
	for i in range(0,30):
		lista_y_mh.append('Mujer')
		lista_y_mh.append('Hombre')

	return lista_y_mh

#solo si se ejecuta este scrip directamente...
if __name__ == '__main__':
	print('You not import me--WORKING!!')
	