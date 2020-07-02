# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:59:49 2020

@authors: magrini and baroni
"""

"""
[IMPORTANTE] LEIA ATENTAMENTE
    
Este arquivo contém todas as funções implementadas na investigação  dos proble-
mas apresentados no artigo "Investigações Numérico-Computacionais em Teoria dos
Números: Construindo e Refutando Conjecturas" publicado na Revista do Professor
de Matemática (RPM) número XX e é de uso livre a todos os leitores e interessa-
dos desde que se faça a referência e citação completa do referido artigo.

Apesar de autorizados o uso e a  reprodução das funções aqui implementadas gra-
tuitamente isto não implica que os autores cedem os direitos de propriedade aos
usuários em qualquer hipótese ou o uso para fins que não educativos ou  com ob-
jetivos comerciais/financeiros.

Ao usar ou distribuir este código o usuário concorda explicitamente com os ter-
mos acima.

Contate-nos caso necessário ou existam dúvidas:
a) magrini@ifsp.edu.br
b) mariana.baroni@ifsp.edu.br
    
Obrigado.
    
"""

# Importação de módulos do Python 
# São necessários para o funcionamento do código. Não os altere.
import numpy as np
import math

# Implementação computacional do teste de primalidade.
# Seja "n" um número natural qualquer. Então esta função:
# a) Retorna 0 se o numero nao for primo.
# b) Retorna 1 se o numero for primo.
def teste_de_primalidade(n):
    # Verificando inicialmente se o numero é inteiro.
    # Se não for imprime mensagem de erro e encerra o programa.
    if int(n) != n:
       print('O número digitado não é inteiro. Verifique.')
       return ()
    else:
       # Verifica se, sendo inteiro, é não negativo.
       # Se for negativo, imprime mensagem de erro e encerra o programa.
       if n <= 0:
          print('O número digitado é negativo. Verifique.')           
          return ()
       # Caso trivial: 0 nao é primo.
       elif n == 0:
          return 0
       # Caso trivial: 1 nao é primo.      
       elif n == 1:
          return 0
       # Caso trivial: 2 é primo.      
       elif n == 2:
          return 1
       # Caso trivial: 3 é primo.      
       elif n == 3:
          return 1
       # Aqui o teste de fato é aplicado.
       # Inicialmente descarta qualquer numero par maio que dois.
       else:
          if n%2 == 0:
             return 0
       # Se for ímpar verifica se o numero n é divisivel por algum natural
       # menor ou igual à raiz de n.
       # Se for encontrado algum divisor menor ou igual à raiz de n, o progra-
       # ma se encerra.
          else:
             i = int(3.0)
             cont = 0
             while i <= math.sqrt(n):
                   if n%i == 0:
                      cont = cont + 1
                      break
                   i = i+2
    if cont == 0:
       return 1
    else:
       return 0  

# Implementacao computacional dos numeros de Fermat Fn = 2^2^n + 1
# Esta funcao retorna os n primeiros numeros de Fermat
def numeros_de_fermat(n):
    # Verificando inicialmente se o numero é inteiro.
    # Se não for imprime mensagem de erro e encerra o programa.
    if int(n) != n:
       print('O número digitado não é inteiro. Verifique.')
       return ()   
    # Verifica se, sendo inteiro, é não negativo.
    # Se for negativo, imprime mensagem de erro e encerra o programa.   
    if n < 0:
       print('O número digitado é negativo. Verifique.')           
       return ()   
    # Considerando n um número maior ou igual a zero gera-se os Fn's
    # Cria uma sequencia vazia de inteiros para armanezar os números de Fermat
    Fn = np.array([], dtype = 'float64')
    for i in range(n):
        fermat = (2**(2**i))+1
        Fn = np.append(Fn,fermat)
    return Fn


# Implementação computacional da contagem de números primos até um certo n.
# Esta funcao retorna a quantidade de numeros primos entre 1 e o numero n.
# Imprime uma mensagem na tela com a resposta.
def quantidade_de_primos(n):
    # Verificando inicialmente se o numero é inteiro.
    # Se não for imprime mensagem de erro e encerra o programa.
    if int(n) != n:
       print('O número digitado não é inteiro. Verifique.')
       return ()   
    # Verifica se, sendo inteiro, é não negativo.
    # Se for negativo, imprime mensagem de erro e encerra o programa.   
    if n <= 0:
       print('O número digitado não é positivo. Verifique.')           
       return ()   
    # Inicializa a quantidade de primos até o número n como sendo zero.
    quantidade_de_primos = 0
    # Para cada número natural entre 2 e o n desejado verifica se é primo usan-
    # do a função teste_de_primalidade.
    for i in range(1,n+1):
        if teste_de_primalidade(i) == 1:
           # a cada resultado positivo se aumenta em 1 a quantidade de primos.
           quantidade_de_primos = quantidade_de_primos + 1
    # Imprime na tela a quantidade de primos:
    string = 'Existem ' + str(quantidade_de_primos) + ' números primos até ' + str(n)
    print(string)
        



