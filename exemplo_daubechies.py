# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:42:59 2020
@author: magrini
"""
# Exemplo da geracao dos filtros 
# Daubechies 4
# Escrito por Magrini, l. A.

# Modulos
import matplotlib.pyplot as plt
import scipy.linalg as linalg
import scipy.signal as signal
import sympy as sym
import numpy as np
import math
import daubechies

# Comprimento do filtro
n = 4

# Geracao do filtro passa baixa h_0
h0 = daubechies.scale_filter_dbN(n)

# Geracao das funcoes escala e wavelet associadas
phi = daubechies.scale_function(h0)
psi = daubechies.wavelet_function(h0)

# Graficos das funcoes phi e psi
plt.figure()
xpsi = np.linspace(0,len(h0)-1,len(psi),endpoint='True')    
plt.plot(xpsi, psi)
plt.rc('xtick', labelsize=15)    
plt.rc('ytick', labelsize=15)   
plt.xlabel("Tempo", fontsize=15, fontweight='bold')
plt.title("Funcao Escala", fontsize=15, fontweight='bold')
plt.show()
#
plt.figure()
xphi = np.linspace(0,len(h0)-1,len(phi),endpoint='True')    
plt.plot(xphi,phi)
plt.rc('xtick', labelsize=15)    
plt.rc('ytick', labelsize=15)   
plt.show()
plt.xlabel("Tempo", fontsize=15, fontweight='bold')
plt.title("Funcao Wavelet", fontsize=15, fontweight='bold')
\end{python}
