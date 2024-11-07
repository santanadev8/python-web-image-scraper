# Web Image Scraper

Este proyecto es un script en Python que descarga y guarda todas las imágenes de una página web en una carpeta de destino especificada. Utiliza Selenium para cargar la página web y BeautifulSoup para analizar el contenido HTML.

## Requisitos

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu_usuario/web-image-scraper.git
    cd web-image-scraper
    ```

2. Instala las dependencias:
    ```sh
    pip install selenium beautifulsoup4 requests
    ```

3. Descarga ChromeDriver y asegúrate de que esté en tu PATH o especifica su ubicación en el script (debes tener el navegador Chrome instalado).

## Uso

1. Abre el archivo `scraper.py` y reemplaza los valores de `url` y `carpeta_destino` con la URL de la página web que deseas usar y la ruta de la carpeta donde se guardarán las imágenes descargadas:
    ```python
    url = "tu_url"  # Reemplaza con la URL que deseas usar
    carpeta_destino = r"Tu_carpeta_destino"  # Usa una cadena sin procesar para la ruta
    ```

2. Ejecuta el script:
    ```sh
    python scraper.py
    ```

## Descripción del Script

El script `scraper.py` realiza las siguientes acciones:

1. Crea la carpeta de destino si no existe.
2. Configura Selenium y abre la página web especificada.
3. Espera hasta que todas las imágenes se hayan cargado.
4. Obtiene el contenido de la página después de que se haya cargado JavaScript.
5. Encuentra todas las etiquetas `<img>` en el HTML.
6. Descarga y guarda cada imagen en la carpeta de destino.

## Notas

- Asegúrate de tener el controlador de Chrome (ChromeDriver) en la ruta especificada y las bibliotecas necesarias instaladas.
- Puedes aumentar el tiempo de espera en `WebDriverWait` si la página tarda más en cargar las imágenes.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor haz un fork del repositorio y envía un pull request.
