import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = ['python', 'c++', 'Django']
y = [100,134,245]

plt.bar(x, y)
plt.savefig('scatter_plot2.png')
