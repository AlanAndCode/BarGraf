import matplotlib.pyplot as plt

dados = [1,3,5,7,9,11]
nomes = ['RJ', 'SP', 'RS', 'MG', 'MA', 'CE']
plt.bar(nomes, dados, label = 'Histograma')
plt.legend()