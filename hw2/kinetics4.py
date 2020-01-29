import numpy as np
import matplotlib.pyplot as plt

def main():
    time = np.linspace(0, 0.0015, num=100)
    
    S = 10**6 # neutron source in n/s
    N_0 = 0 # initial neutron population in n

    k = 0.99 # initial multipliaction factor
    l = 10**-4 # initial neutron lifetime in seconds

    #Loss = 1 # assume constant neutron loss?
    N_array = np.zeros(100)

    # Update for t=0
    c = (k-1)/l
    N = -(S/c)*(1-np.exp(c*time[1])+N_0*np.exp(c*time[1]))
    N_array[1] = N
    N_prev = N

    print(N_prev)

    # Updates for t>0
    for t in range(2, len(time)): 
        c = (k-1)/l
        N = -(S/c)*(1-np.exp(c*time[t])+N_0*np.exp(c*time[t]))
        # Update for k and l
        k = N/N_prev
        #l = Loss #N/l
        N_array[t] = N
        N_prev = N

    plt.title('N(t) with Source=10^6 n/s')
    plt.plot(time, N_array)
    plt.xlabel('Time (s)')
    plt.ylabel('N population')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
