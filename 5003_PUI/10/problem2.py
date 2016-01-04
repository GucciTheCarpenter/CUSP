import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']

np.random.seed(500)
random_names = [names[np.random.randint(low=0, high=len(names))] for i in range(1000)]

births = [np.random.randint(low=0, high=1000) for i in range(1000)]

BabyDataSet = zip(random_names, births)

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])

df.groupby('Names').sum().sort(columns='Births', ascending=True).plot(kind='bar')

plt.title('Baby names in 1880')
plt.ylabel('Births')
plt.xlabel('Names')
plt.show()
