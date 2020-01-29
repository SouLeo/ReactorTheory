import numpy as np
import matplotlib.pyplot as plt

def main():
    t = np.linspace(0, 5, num=100)

    N_0 = 10**20
    K = [0.5, 1.0, 1.5]
    l = [0.5, 1, 1.001]

    N_array = np.zeros((3,100))

    for k in range(0, len(K)):
        N = N_0*np.exp(((K[k]-1)/l[k])*t)
        N_array[k, :] = N

    plt.title('Study of k on Neutron Population')
    plt.plot(t, N_array[0], label="N for k=0.5")
    plt.plot(t, N_array[1], label="N for k=1.0")
    plt.plot(t, N_array[2], label="N for k=1.5")
    plt.xlabel('Time (s)')
    plt.ylabel('N population')
    plt.grid()
    plt.legend()


    plt.show()

if __name__ == '__main__':
    main()
