import numpy as np
import matplotlib.pyplot as plt

def main():
    t = np.linspace(0, 5, num=100)

    R = [0, 0.01, 1, 100]   # source values
    R_labels = ['R(t)=0', 'R(t)=0.01', 'R(t)=1', 'R(t)=100']
    N_0 = 10**20
    radiation_decay_constant = 1    # units in sec^-1, aka lambda

    N_array = np.zeros((4, 100))
    dNdt_array = np.zeros((4, 100))

    for r in range(0, len(R)):
        N = (R[r]/radiation_decay_constant)*(1-np.exp(-radiation_decay_constant*t))
        dNdt = -radiation_decay_constant*N+R[r]
        N_array[r, :] = N
        dNdt_array[r, :] = dNdt

    plt.subplot(2, 2, 1)
    plt.title('N population when R(t)=0')
    plt.plot(t, N_array[0], label="N")
    plt.plot(t, dNdt_array[0], label="dNdt")
    plt.xlabel('Time (s)')
    plt.ylabel('N population in nuclei/cm^3')
    plt.grid()

    plt.subplot(2, 2, 2)
    plt.title('N population when R(t)=0.01')
    plt.plot(t, N_array[1], label="N")
    plt.plot(t, dNdt_array[1], label="dNdt")
    plt.xlabel('Time (s)')
    plt.ylabel('N population in nuclei/cm^3')
    plt.grid()

    plt.subplot(2, 2, 3)
    plt.title('N population when R(t)=1')
    plt.plot(t, N_array[2], label="N")
    plt.plot(t, dNdt_array[2], label="dNdt")
    plt.xlabel('Time (s)')
    plt.ylabel('N population in nuclei/cm^3')
    plt.grid()

    plt.subplot(2, 2, 4)
    plt.title('N population when R(t)=100')
    plt.plot(t, N_array[3], label="N")
    plt.plot(t, dNdt_array[3], label="dNdt")
    plt.xlabel('Time (s)')
    plt.ylabel('N population in nuclei/cm^3')
    plt.grid()

    plt.show()

if __name__ == '__main__':
    main()