# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:57:40 2020
@author: magri
"""

""" 
Este é o script básico onde você poderá testar as funções que estão no arquivo 
"aritmetica.py".

Para usá-lo, salve este script básico em uma mesma pasta que o arquivo módulo
"aritmética.py". Caso não estejam na mesma pasta você não conseguirá usá-lo!

IMPORTANTE: Não faça alterações no arquivo "aritmética.py". Ele é um conjunto
de funções testadas (chamado em Python de módulo) que é importado automatica-
mente quando se declara abaixo "import aritmetica as arimetica" (linha 29).

Atente-se para as condições de uso livre descritas no arquivo "aritmetica.py". 
Leia-o de modo a não infringir as regras de uso.

Ao usar as funções, não esqueça de citar corretamente o artigo da Revista do 
Professor de Matemática (RPM) nas normas ABNT vigentes.

Questões? Dúvidas?
Escreva para (a) magrini@ifsp.edu.br ou (b) mariana.baroni@ifsp.edu.br

"""

# Antes de usar qualquer funcao neste arquivo para teste, selecione as linhas
# 32 e 33 e clicando com o botão direito do mouse escolha "executar seleção".

import aritmetica as aritmetica
import numpy as np

# Numeros de Fermat: Gera os primeiros 25 deles.
# Atencao: Um desktop "comum" não tem capacidade de ir muito além disso.
fn = aritmetica.numeros_de_fermat(25)   

# Calcula o numero de dígitos de cada um dos 25 números de Fermat gerados.
# Valores registrados em "Numeros_de_Fermat_Qtde_de_Digitos.txt".
numero_de_digitos = np.array([], dtype = 'int64')
for i in range(len(fn)):
    digitos = len(str(fn[i]))
    numero_de_digitos = np.append(numero_de_digitos, digitos)


# Quantidade de primos entre 1 e n para n escolhido.
# Mude à vontade o valor de n (natural) na linha 48.
# Para executar, selecione as linhas 48 e 49, clique com o botão direito do 
# mouse e escolha "executar seleção".
n = 10000
aritmetica.quantidade_de_primos(n)
   

