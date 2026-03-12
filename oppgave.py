import numpy as np 
import matplotlib as plt

def g(x):
    return np.arctan(x) - 4(x**2 + 1) # definerer funksjonen

a = 1 # bruker biseksjonsmetoden, viser hvordan jeg kom fram til dette på lastet opp utrenging for hånd.
b = 2

for i in range(1000):
    m = (a + b) / 2 # midtpunktsformelen
    if g(a) * g(m) <= 0: # ny intervall hvis roten er mellom a og m
        b = m 
    else:
        a = m 

x = (a + b) / 2
print(x)