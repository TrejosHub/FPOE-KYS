import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Hilo4(threading.Thread):
    def __init__(self, nombre_hilo, nombre_persona):
        threading.Thread.__init__(self, name=nombre_hilo, target=Hilo4.run)
        self.nombreHilo = nombre_hilo
        self.nombre_persona = nombre_persona

    def run(self):
        self.consultar(self.nombre_persona)

    def consultar(self, nombre_persona):
        logging.debug('Consultando' + nombre_persona)
        time.sleep(5)
        return