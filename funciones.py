#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Comenzaremos importando las librerías:

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
import re
from sklearn.metrics import roc_auc_score, roc_curve


# In[2]:


def limpieza(texto):
    """
    Función para realizar una limpieza de carácteres de una variable de texto
    """
    contenido = texto
    #Eliminamos palabras que empiecen por https:
    contenido = re.sub('http\S+', ' ', contenido)
    #Eliminamos signos innecesarios:
    regex = '[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~]'
    contenido = re.sub(regex , ' ', contenido)
    #Separamos palabras:
    contenido = contenido.split(sep = ' ')
    #Eliminamos palabras con una longitus <2:
    contenido = [token for token in contenido if len(token) > 2]
    return(contenido)
# In[ ]:




