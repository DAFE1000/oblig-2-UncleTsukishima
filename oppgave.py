import numpy as np 
import matplotlib.pyplot as plt

def f(x): 
    return np.exp(-x/4) * np.arctan(x) # definerer funksjonen (originalfunksjonen)

def g(x):
    return np.arctan(x) - 4 / (x**2 + 1) # definerer funksjonen (den deriverte)

a = 1 # bruker biseksjonsmetoden, viser hvordan jeg kom fram til dette på lastet opp utrenging for hånd.
b = 2

for i in range(1000):
    m = (a + b) / 2 # midtpunktsformelen med 1000 interasjoner
    if g(a) * g(m) <= 0: # ny intervall hvis roten er mellom a og m
        b = m 
    else:
        a = m 

x = (a + b) / 2
y = f(x)

X = np.linspace(0, 5, 400)
Y = f(X)

print(f"Toppunkt: {x:.4f}")
print(f"f(x) = {y:.4f}")
plt.plot(X, Y, label="f(x)") # plotter funksjonen
plt.scatter([x], [f(x)], color="blue", label="Maksimalpunkt") # markerer toppunktet.
plt.title("f(x) = e^(-x/4) * arctan(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

