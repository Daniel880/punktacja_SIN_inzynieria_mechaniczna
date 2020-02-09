# -*- coding: utf-8 -*-

import os
import _thread
import time


lista_komend = ['python pozyskiwanie_danych.py 2019',
                'python obrabianie_danych.py 2019',
                'python pozyskiwanie_danych.py 2018',
                'python obrabianie_danych.py 2018',
                ]




for c in lista_komend:
    os.system(c)


