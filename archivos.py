import os
# import cv2
# import numpy as np
from PIL import Image
from skimage import io

# carpeta_imagenes = './imagenes'
carpeta_imagenes = '/home/jono/Escritorio/unahur/python-buscador-imagenes-JhonCavalera13/imagenes'

def armar_ruta(nombre):
  return os.path.join(carpeta_imagenes, nombre)

def leer_imagen(nombre):
  return Image.open(armar_ruta(nombre))

def escribir_imagen(nombre, imagen):
  Image.fromarray(imagen).save(armar_ruta(nombre))

def leer_imagen2(nombre):
  return io.imread(armar_ruta(nombre))

def escribir_imagen2(nombre, imagen):
  io.imsave(armar_ruta(nombre),imagen)
