import numpy as np
import matplotlib.pyplot as plt

def main():
    t = np.linspace(0, 1, num=100)
    
    S = 10**6 # neutron source in n/s
    N_0 = 0 # initial neutron population in n

    k = 0.99 # initial multipliaction factor
    l = 10**-4 # initial neutron lifetime in seconds

    c = (k-1)/l
    N = -(S/c)*(1-np.exp(c*t)+N_0*np.exp(c*t))

    plt.title('N(t) with Source=10^6 n/s')
    plt.plot(t, N)
    plt.xlabel('Time (s)')
    plt.ylabel('N population')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
