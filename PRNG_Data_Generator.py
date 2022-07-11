#####################
#This generates a biased random numbers
#####################
from numba import njit
import numpy as np
import pandas as pd

fact=4
@njit#(nopython=True)
def rand_gen(n):
    
    Out=[]
    for i in np.arange((fact*10**n)):
        random=np.random.random()
        if random>=0.5:
            Out.append(0)
        elif random<=0.5:
            Out.append(1)
    return(Out)

n_0=7
## Following will produce a file with fact*(10**(n_0)) zeroes and ones
Out1=rand_gen(n_0)

df=pd.DataFrame(Out1)
df.to_csv('Name_Of_Output_file.dat',index=False,header=False) ##One can also use .bin or .csv as output format