# Redes Neurais (II)

## Neurônio Artificial: Um neurônio tem uma representação muito parecida com esta imagem abaixo:


Ele tem as entradas que em um problema real por exemplo valor de um lote: seriam as características do lote como tamanho,localização,preço médio por metro quadrado. Os Pesos são parâmetros que são ajustáveis e que medem o desempenho e controlam o comportamento da nossa rede.
A função de soma é representada por 
soma = i=1nxi*wi
onde xi é a entrada e wi é o peso. 
O Step function é uma função que retorna 1 se a soma for  1 caso contrário ela retorna 0.
Usando esta rede neural de exemplo temos a soma sendo:

Logo nossa função Step function deve nos retornar 1.
Redes multicamadas(Multilayer perceptron)
Estas redes podem ter várias camadas escondidas entre os nossos pesos e a nossa saída, este tipo de rede é usado para modelos não linearmente separáveis.

## Sigmoid(função sigmóide)
Está função nos retorna um valor entre 0 e 1 sua fórmula é


Onde x é o valor que vamos encontrar na soma, se o valor for alto ele vai ficar perto de 1 e caso for baixo vai tender a 0.

Rede neural para fazer o operador XOR.


Temos nossa entradas como 0 e 0 e nossa saída esperada é 0
Aplicamos a soma dos pesos para cada neurônio logo após aplicamos na função de ativação, devemos fazer isso para todos os valores de x1 e x2.
Após descobrimos o valor da soma e da ativação passamos para o próximo neurônio 
Aqui vamos fazer a mesma coisa, encontrar o valor da duma e da ativação.

Cálculo do Erro
Fórmula: Erro = respostaCorreta − respostaCalculada
Comparando a nossa resposta correta com a resposta calculada temos este quadro abaixo:


A média absoluta do erro foi de 0.49 ou seja nossa rede neural acerta apenas 51% dos casos mostrando que nosso erro está muito alto.
Descida do Gradiente
A descida do gradiente é um algoritmo de otimização que nos ajude encontrar o mínimo de uma função de perda ou erro. A ideia por trás dele é ajustar iterativamente os pesos de uma rede neural na direção contrária ao gradiente.



Nossa função de custo vai calcular a derivada parcial para mover para a direção do gradiente, devemos encontrar a combinação de pesos que o erro é o menor possível o gradiente nos ajuda a saber quanto devemos ajustar nos pesos.

O gradiente vai nos ajudar a encontrar os mínimos globais e não os mínimos locais.Ele irá calcular o declive da curva com as derivadas parciais.

Y é o Sigmoid,  o D vai nos dizer se devemos aumentar o valor do nosso peso ou o diminuí- lo.


Cálculo do parâmetro delta
Fluxograma de tudo que precisamos para encontrar o gradiente

Já temos os valores de soma,ativação,erro e da derivada de ativação 

Fórmula para encontrarmos o erro:

aplicando os valores a esta fórmula temos o delta de saída como -0.098, agora repetimos este mesmo processo para todos os valores de x1 e x2.Após isso devemos calcular o delta da camada escondida, a fórmula é:

Nossa soma e a derivada:


aplicando este cálculo x1=0 e x2=0  teríamos:
0.25 *(-0.017)* (-0.098)  0.000
0.25 *(-0.893)* (-0.098) = 0.022
0.25 *0.148* (-0.098) = -0.004
x1 = 0 x2= 1
0.242 *(-0.017)* 0.139 =-0.001
0.230 *(-0.893)*0.139 = 0.029
0.236 *0.148* 0.139 = 0.005
x1 = 1 x2= 0
0.239 *(-0.017)*0.139= -0.001
0.219 *(-0.893)* 0.139= -0.027
0.200 *0.148* 0.139= -0.004
x1 = 1 x2= 1
0.250 *(-0.017)* (-0.114) = 0.000
0.167*(-0.893)* (-0.114) = 0.017
0.156 *0.148* (-0.114) = -0.003

Agora vamos usar o algoritmo de backpropagation sua fórmula é:

O parâmetro momento serve para acelerar a descida do gradiente
Este tipo de rede neural ele é chamado de feat forward ele faz o cálculo do erro e dps volta fazendo a atualização dos pesos.



Vamos fazer este cálculo para os 3 neurônios, este cálculo que foi feito acima foi apenas o cálculo do valor de entrada * o delta.
Agora vamos aplicá los na fórmula completa:
Adotamos uma taxa de aprendizagem = 3
Momento = 1
entrada x delta:
0.032
0.022
0.021
Antigos pesos:


Aplicando na fórmula temos
(-0.017*1) +0.032*0.3 = -0.007
(-0.893*1)*0.893* *0.3  = -0.886
(-0.148*1) *0.148*0.3 = 0.154

feita esta conta alteramos os pesos para estes novos valores, após isso faremos para os pesos de entrada 


calculamos a entrada * o delta e temos os resultados os 2 resultados dera -0.0000 isso quer dizer que os valores são um valor negativo muito próximo de 0.

Taxa de aprendizagem = 0.3
Momento = 1
Entrada x delta
-0.000 -0.010 0.001
-0.000 -0.012 0.002

Vamos aplicar na fórmula:
Peson+1  = (peson* momento)+(Entrada * delta * taxa de aprendizado)
(-0.434*1) +(-0.000)*0.3 = -0.424
(0.358*1) +(-0.000)*0.3 = 0.358
(-0.740*1) +(-0.010)*0.3 = -0.743
(-0.577*1) +(-0.012)*0.3 = -0.581
(-0.961*1) +(-0.001)*0.3 = -0.961
(-0.469*1) +(-0.002)*0.3 = -0.468

Temos aqui os pesos antigos e os novos pesos 


Assim concluímos a atualização dos valores, lembrando que fizemos apenas a primeira interação ou a primeira época.

## Bias
O bias atua como um ajuste fino, ele nos ajuda a ter uma maior precisão fazendo a rede aprender e se adaptar melhor aos dados do modelo.
ex: se nossa entrada for 0 nossa rede irá zerar,o bias evita que isso aconteça, ele  já está implementado nas bibliotecas de deep learning que você usará, como TensorFlow e PyTorch. Não é necessário configurá-lo manualmente.
Nesta imagem abaixo vemos que foram adicionados 2 novos neurônios com pesos estes neurônios foram adicionados pelo bias normalmente eles recebem o valor 1.




## Erro
Os algoritmos de erros servem para medir a diferença entre as saídas da rede e as saídas desejadas.Este valor do erro é usado para ajustar os pesos com o objetivo de melhorar o desempenho da rede.
Função simples para calcular o erro:
Existem várias funções para calcular o erro, anteriormente usamos uma função muito  simples que fazíamos uma subtração do valor da resposta certa pela resposta calculada


## Mean square error(MSE)
Sua fórmula é:

fi = saída esperada
yi= saída encontrada 
Lembrando que nesta subtração usamos o valor absoluto do fi e yi, após a soma elevarmos esta soma ao quadrado penaliza muito mais os erros ajudando a chegarmos em valores mais próximos do valor desejado.

Root mean square error(RMSE)
É muito parecido com o MSE, a sua única diferença é que ele faz a raiz quadrada do erro.


## Gradient Descent

Batch Gradient Descent (BGD):
Serve para calcular os pesos e ajustá-los conforme vai calculando, ele utiliza MSE ou RMSE para medir as discrepâncias entre as previsões e os valores reais.Ele é muito bom pois aumenta a precisão, é ideal para pequenos datasets.

Stochastic Gradient Descent (SGD):
É muito parecido com o BGD mas tem suas particularidades uma é que ele é mais rápido que o BGD para datasets grandes.Ele também tem uma menor probabilidade de cair em mínimos locais, devido à natureza aleatória da atualização.
Mini-Batch Gradient Descent (MBGD):
É o mais completo de todos pois combina as vantagens do BGD e do SGD,equilíbrio entre precisão e velocidade, processando dados em blocos.




## Funções de Ativação 
Step function(Função degrau)
Esta função nos devolve um número 0 ou 1,ela é usada apenas para problemas linear mentes separáveis 


## Sigmoide

A função sigmoide mapeia qualquer número real para um valor entre 0 e 1. Isso a torna útil para problemas de classificação binária em machine learning, onde estamos tentando prever se uma entrada pertence a uma de duas classes possíveis.

## Hyperbolic tanget

Retorna um número entre 1 e -1, também é muito boa para problemas de classificação binária.

## ReLU


ReLU mapeia qualquer número negativo para 0 e mantém qualquer número positivo como está.


## Linear

Está função retorna o que recebe ex: se recebe 5 retorna 5.

