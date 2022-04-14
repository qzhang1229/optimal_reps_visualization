import numpy as np
import matplotlib.pyplot as plt
import sys

def plot_bar(p,q,c='b',linestyle='-'):
    plt.plot([p[0],q[0]],[p[1],q[1]], c=c,linestyle=linestyle, linewidth=1)


birth_file = sys.argv[1]
death_file = sys.argv[2]

birth = np.load(birth_file)
death = np.load(death_file)

length = len(birth)
for i in range(+length):
    plot_bar([birth[i],i],[death[i],i])

plt.show()