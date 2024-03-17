import numpy as np

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))  

def tahnFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

def reluFunction(soma):
    if (soma >= 0):
        return soma
    return 0

def linearFunction(soma):
    return soma

def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()


print(stepFunction(-1))
print(sigmoidFunction(-0.358))
print(tahnFunction(-0.358))
print(reluFunction(0.358))
print(linearFunction(-0.358))
valores = [5.0, 2.0, 1.3]
print(softmaxFunction(valores))