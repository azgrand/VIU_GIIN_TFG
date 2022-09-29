from datetime import datetime as dt
import os
from os import path
from pathlib import Path


class Config:
    # Nombres de los datos de la app
    APP_NAME = 'pNmap_Scan'
    __FYLE_NAME = dt.now().strftime('%Y') + dt.now().strftime('%m') + dt.now().strftime('%d') + dt.now().strftime('%H') + dt.now().strftime('%M') + dt.now().strftime('%S')

    # Rutas de volcado de ficheros
    __PATH_DEL = os.getcwd()
    __PATH = str(Path.home())
    PATH_CSV = __PATH_DEL + APP_NAME + '.csv'
    PATH_HTML = __PATH_DEL + APP_NAME + '.html'
    PATH_PDF = __PATH + '/' + APP_NAME + __FYLE_NAME + '.pdf'

    def clean(self):
        if path.exists(Config.PATH_CSV):
            os.remove(Config.PATH_CSV)
        if path.exists(Config.PATH_HTML):
            os.remove(Config.PATH_HTML)
