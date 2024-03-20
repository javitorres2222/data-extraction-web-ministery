from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

#Variables
teclea = input ("Poner Provincia: ")
#tramite1 = input(" 1.TRÁMITES OFICINAS DE EXTRANJERÍA: REGISTRO")


# Crear una instancia del controlador del navegador 
driver = webdriver.Chrome()

# Esperar un tiempo  para que la página cargue completamente 
driver.implicitly_wait(10)

# Navegar a la página web
driver.get("https://icp.administracionelectronica.gob.es/icpplus/index.html")

# Encontrar el desplegable provincias
desplegable = driver.find_element(By.ID, "form")
desplegable.click()

select = Select(desplegable)

# Recorrer todas las opciones del desplegable
for opcion in select.options:
    # Imprimir el texto de la opción
    print(opcion.text)
    
    
    # Si el texto de la opción coincide con el que deseas seleccionar, seleccionar esa opción
    if opcion.text == teclea:
        select.select_by_visible_text(opcion.text)
        break  # Terminar el bucle después de seleccionar la opción
time.sleep(1)
aceptar =  driver.find_element(By.ID, "btnAceptar")
aceptar.click()  
time.sleep(3)

desplegable2 = driver.find_element(By.ID, "tramiteGrupo[0]")
desplegable2.click()
select2 = Select(desplegable2)



time.sleep(3)
#pasamos a la siguiente pantalla de elegir trámite 
#aceptar2 =  driver.find_element(By.ID, "btnAceptar")
#aceptar2.click()  
#time.sleep(5)
#Cerrar el navegador al finalizar
#driver.quit()