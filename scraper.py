from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import requests

"""
    Descarga y guarda todas las imágenes de una página web en una carpeta de destino especificada.
    Args:
        url (str): La URL de la página web desde la cual se descargarán las imágenes.
        carpeta_destino (str): La ruta de la carpeta donde se guardarán las imágenes descargadas.
    Returns:
        None
    Raises:
        TimeoutException: Si el tiempo de espera para cargar las imágenes se agota.
    Nota:
        Este script utiliza Selenium para cargar la página web y BeautifulSoup para analizar el contenido HTML.
        Asegúrate de tener el controlador de Chrome (chromedriver) en la ruta especificada y las bibliotecas necesarias instaladas.
    """

# Función para capturar y guardar imágenes de una URL específica
def guardar_imagenes(url, carpeta_destino):

    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Configurar Selenium y abrir la página
    service = Service(r'C:\chromedriver-win64\chromedriver.exe')  # Usa una cadena sin procesar
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    
    # Esperar hasta que las imágenes se hayan cargado (por si se cargan con JavaScript dinámicamente)
    try:
        WebDriverWait(driver, 20).until(  # Aumenta el tiempo de espera si es necesario
            EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
        )
    except TimeoutException:
        print("Tiempo de espera agotado. No se encontraron imágenes.")
        driver.quit()
        return
    
    # Obtener el contenido de la página después de que se haya cargado JavaScript
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    
    # Imprimir el contenido HTML de la página (opcional, si no lo necesitas, puedes borrar esta línea)
    print(soup.prettify())
    
    # Encontrar todas las etiquetas <img> en el HTML
    imagenes = soup.find_all("img")
    print(f"Se encontraron {len(imagenes)} imágenes en la página.")
    
    # Descargar y guardar cada imagen
    for idx, img in enumerate(imagenes, start=1):
        # Obtener el enlace de la imagen
        img_url = img.get("src")
        if not img_url:
            print(f"Imagen {idx} no tiene URL.")
            continue
        
        # Convertir la URL relativa a absoluta
        img_url = urljoin(url, img_url)
        print(f"Descargando imagen {idx} desde {img_url}")
        
        # Descargar la imagen
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            # Guardar la imagen en el escritorio
            nombre_imagen = f"imagen_{idx}.jpg"
            ruta_imagen = os.path.join(carpeta_destino, nombre_imagen)
            with open(ruta_imagen, "wb") as f:
                f.write(img_response.content)
            print(f"Guardada: {nombre_imagen}")
        else:
            print(f"Error al descargar la imagen {idx}")

# Llamar a la función con los parámetros correctos
url = "tu_url"  # Reemplaza con la URL que deseas usar
carpeta_destino = r"Tu_carpeta_destino"  # Usa una cadena sin procesar para la ruta
guardar_imagenes(url, carpeta_destino)

