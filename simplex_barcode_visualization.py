import numpy as np
import matplotlib.pyplot as plt


def plot_bar(p,q,c='b',linestyle='-'):
    plt.plot([p[0],q[0]],[p[1],q[1]], c=c,linestyle=linestyle, linewidth=1)

birth = np.load("simplex_bar/birth_time.npy")
death = np.load("simplex_bar/death_time.npy")


length = len(birth)
for i in range(+length):
    plot_bar([birth[i],i],[death[i],i])

plt.show()