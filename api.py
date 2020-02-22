import requests
import json
import os

class PixabayAPI:
  def __init__(self, key, carpeta_imagenes):
    self.key = key
    self.carpeta_imagenes = carpeta_imagenes
    self.lista_rutas = []
    
  def buscar_imagenes(self, query, cantidad):
    # URL de búsqueda. Ver la documentación en https://pixabay.com/api/docs/#api_search_images
    url = f'https://pixabay.com/api/?key={self.key}&per_page={cantidad}&q={query}&image_type=photo&lang=es'

    # Hago la request y parseo el JSON que viene como respuesta
    response = requests.get(url)
    jsonResponse = json.loads(response.text)

    # La respuesta tiene esta pinta:
    # {
    # 	"total": 4692,
    # 	"totalHits": 500,
    # 	"hits": [{
    # 			"id": 195893,
    # 			"pageURL": "https://pixabay.com/en/blossom-bloom-flower-195893/",
    # 			"type": "photo",
    # 			"tags": "blossom, bloom, flower",
    # 			"largeImageURL": "https://pixabay.com/get/ed6a99fd0a76647_1280.jpg",
    #       ... más campos que no interesan
    # 		}, {
    #       ...otra imagen
    #     }
    # 	]
    # }
    #
    # Pero solo nos interesa el campo "largeImageURL" que está dentro de la lista de "hits".
    # Para que la función devuelva eso usamos un map, que en Wollok sería algo así:
    #
    # jsonResponse.hits.map { x => x.largeImageURL }
    #
    # Pero en Python las funciones de listas son funciones globales y no métodos, así que queda así:
    return map(lambda h: h['largeImageURL'], jsonResponse['hits'])

  def descargar_imagen(self,url,lista):
    bytes_imagen = requests.get(url)
    nombre_imagen = url.split('/')[-1]
    ruta_archivo = os.path.join(self.carpeta_imagenes, nombre_imagen)
    ruta_archivo_split = ruta_archivo.split('/')[-1]
    lista.append(ruta_archivo_split)
    print(ruta_archivo_split)
  
    with open(ruta_archivo, 'wb') as archivo:
      archivo.write(bytes_imagen.content)

  def getListaRutas(self):
    return self.lista_rutas
  
  def appendRuta(self, ruta):
    self.lista_rutas.append(ruta)


