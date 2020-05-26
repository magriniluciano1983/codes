# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:10:50 2020

@author: magri
"""

# Funcoes do Modulo Daubechies
# Sendo dado o numero de momentos nulos gera os fitros das funcoes escala e wa-
# velet associadas. Adicionamente permite gerar visualizacoes das funcoes esca-
# la e wavelet.

# Referencia princial:
# Daubechies, I. Ten lectures on Wavelets. SIAM. 1992.


# Escrito por Magrini, l. A.
# Ultima Versao em Abril/2020.

###############################################################################

# Modulos
import scipy.linalg as linalg
import scipy.signal as signal
import sympy as sym
import numpy as np
import math

###############################################################################

# Zero da Maquina e variaveis para manipulacao simbolica
eps = np.finfo(float).eps
# Variaveis de manipulacao simbolica
y = sym.symbols('y')
z = sym.symbols('z')
phi = sym.symbols('phi')

###############################################################################

# Funcao Auxiliar 1: 
# Gera numeros binomiais
def binomial(n,p):
    return math.factorial(n)/(math.factorial(p)*math.factorial(n-p))

###############################################################################

# Funcao Auxiliar 2: Retorna o polinomio Pn.
# Pn = sum_{0 to n-1} combination (n-1+k)(k)*y^k
# Obs: variavel "n/2" corresponde ao numero de momentos nulos da wavelet ou ao
# comprimento do filtro associado.
def pol_pn(n,variable):
    n = int(n)
    coefs = np.zeros([n,1])
    string = '0+'
    for k in range(n):
        coefs[k] = binomial(n-1+k,k)
        string_aux = f'{int(coefs[k])}*{variable}**{k}+'
        string = string + string_aux
    string = string[:-1]
    Pn = sym.sympify(string)
    return string, Pn

###############################################################################
    
# Funcao Auxliar 3: polinomio de Daubechies
# Construcao depende da funcao auxiliar 2
# Pd = sum_{0 to n/2} Pn(1/2 - 1/(4z) - z/4)) em que Pn corresponde ao polino-
# mio gerado pela funcao auxiliar 2.
def pol_db(n):
    if np.mod(n,2) == 1:
       print('ERROR: The input value must be even value!')
       return -1
    else:
       string, Pd = pol_pn(n/2, '(1/2 - 1/(4*z) - z/4)')
       return string, Pd

###############################################################################
   
# Funcao Auxiliar 4: raizes complexas do polinomio Pd de Daubechies
# Mantem-se somente as raizes complexas dentro da bola fechada de raio r = 1.
# Pd tem construcao via funcao auxiliar 3.
def roots_less_one(pol, variable):
    roots_output = np.array([], dtype='complex')
    string_1 = 'sym.sympify(' + pol + ')'
    string_2 = 'sym.solveset(' + string_1 + ')' 
    roots = eval(string_2)
    roots = np.array([i for i in roots])
    for i in range(len(roots)):
        aux = roots[i]
        if abs(aux) <= 1.0:
           roots_output = np.append(roots_output, aux) 
    return roots_output

###############################################################################
    
# Funcao Auxiliar 5: gera o filtro da funcao escala utilizando as raizes calcu-
# ladas via funcao auxiliar 4.
def scale_filter_dbN(n):    
    pol_string, pol_aux = pol_db(n)
    roots_less_1 = roots_less_one(pol_string, 'z')   
    string = f'(z+1)**({n}/2)*'
    for root in roots_less_1:
        string_aux = f'(z-{root})*'
        string = string + string_aux
    string = string[:-1]
    pol1 = sym.sympify(string)  
    pol1 = sym.Poly(pol1, z)
    coefs1 = pol1.coeffs()
    string = '0+'
    for k in range(n):
        string_aux = f'z**({n}-{k}-1)+'
        string = string + string_aux
    string = string[:-1]
    pol2 = sym.sympify(string)
    pol2 = sym.Poly(pol2, z)
    coefs2 = pol2.coeffs()
    ck = [i/j for i,j in zip(coefs1, coefs2)]
    ck_real = np.array([sym.re(i) for i in ck])
    sum_ck = np.dot(ck_real,ck_real)
    norm = math.sqrt(sum_ck)    
    ck_norm = [i/norm for i in ck_real]
    ck_norm = ck_norm[::-1]
    return np.array(ck_norm)

###############################################################################

# Funcao Auxiliar 6: padding em series temporais com comprimentos diferentes.
def padding(x,y):
    len_x = len(x)
    len_y = len(y)
    if len_x > len_y:
       dif = len_x - len_y
       for i in range(dif):
           y = np.append(y,0)
    if len_y > len_x:
       dif = len_y - len_x
       for i in range(dif):
           x = np.append(x,0)
    return x,y

###############################################################################

# Funcao Auxiliar 7: downsampling
def downsampling(x):
    x_dn = x[::2]
    return x_dn

###############################################################################

# Funcao Auxiliar 8: upsampling
def upsampling(x,rate):
    x_up = np.zeros(rate*len(x)-1)
    x_up[::rate] = x
    while x_up[-1] == 0:
       x_up = np.delete(x_up,[len(x_up)-1])
    return x_up

###############################################################################
             
# Funcao Auxiliar 9: "entrelacamento" de dois vetores
def merge(x,y):
    len_x = len(x)
    len_y = len(y)
    if len_x > len_y:  
       dif = len_x - len_y
       aux = [0 for i in range(dif)]
       y = np.append(y,aux)
       len_y = len(y)
    if len_x < len_y:
       dif = len_y - len_x
       aux = [0 for i in range(dif)]
       x = np.append(x,aux)        
       len_x = len(x)
    vector = np.zeros([2*len_x,1])
    for i in range(2*len_x):
        if i%2 == 0:
           vector[i] = x[int(i/2)]
        else:
           vector[i] = y[int((i-1)/2)]
    while vector[-1] == 0:
        vector = np.delete(vector,[len(vector)-1])
    return vector

###############################################################################

# Funcao Auxiliar 10: funcao escala associada a um filtro
# Calculo via convolucoes em frequencia.
def scale_function(h):
    kk = 15
    len_aux = len(h)
    # normalizacao do filtro
    h_norm = h*2/np.sum(h)
    h_reverse = h_norm[::-1]  
    # matrizes
    matrix_t = np.zeros([len_aux, 3*len_aux-2])  
    b = np.zeros([len_aux,1]) 
    b[-1]=1
    for i in range(len_aux):
        matrix_t[i,2*i:2*i+len_aux] = h_reverse
    matrix0 = matrix_t[:,len_aux-1:2*len_aux-1]
    matrix_initial = matrix0 - np.identity(len_aux)
    matrix_j = matrix_initial
    matrix_j[len_aux-1,:] = np.ones([1,len_aux])   
    matrix_sol = linalg.solve(matrix_j,b)
    p = matrix_sol
    p = np.delete(p,[0,len_aux-1])
    p = np.convolve(h_norm,p)   
    y = np.convolve(h_norm,downsampling(p))
    p = merge(y,p)
    h_aux = h_norm
    for k in range(kk):
        h_aux = upsampling(h_aux,2)
        y = signal.convolve(h_aux,y,method='fft')
        p = merge(y,p)
    p = p[::-1]
    return p

###############################################################################

# Funcao Auxiliar 11: funcao wavelet associada ao filtro h. 
# Computa via "reconstrucao" sinal pulso com convolucoes em frequencia.
def wavelet_function(h):
    kk = 15
    g_rec = math.sqrt(2)*np.array([(-1)**i*h[i] for i in range(len(h))])
    h_rec = math.sqrt(2)*h[::-1]
    psi = signal.convolve(np.ones(1),g_rec,method='fft')
    psi = upsampling(psi,2)
    for i in range(kk):
        if i != (kk-1):
           psi = signal.convolve(psi,h_rec,method='fft')
           psi = upsampling(psi,2)
        if i == kk-1:
           psi = signal.convolve(psi,h_rec,method='fft')            
    return psi

###############################################################################


#plt.figure()
#xwave = np.linspace(0,len(h)-1,len(wave),endpoint='True')    
#plt.plot(xwave,wave)
#plt.show()
#
#plt.figure()
#xphi = np.linspace(0,len(h)-1,len(phi),endpoint='True')    
#plt.plot(xphi,phi)
#plt.show()

            
           
           
        
        
   
    








    
