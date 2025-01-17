import numpy as np
def incertitude(liste):
    u=[]
    for i in range(len(liste)):
        u.append(np.sqrt((b_R0[i]/f_R0[i] uf0[i])2+(1/f_R0[i] *ub0[i])*2))
    return u

f_R0 = [5.1, 10, 16, 20.7, 20.6, 30.4]
uf0=[0.6,0.4,0.5,0.4,0.6,0.5]
b_R0 = [160, 291, 460, 621, 750, 976]
ub0=[2.1,1.4,1.1,0.9,0.4,0.2]
v_R0 = [187, 305, 465, 624, 751, 976]

# Division élément par élément
f_R0 = [x * 2*np.pi for x in f_R0]
sous = [x - y for x, y in zip( f_R0,b_R0)]
g_R0 = [x / y for x, y in zip(sous, f_R0)]
b_R0=[x * (2*np.pi/60) for x in b_R0]
v_R0=[x * (2*np.pi/60) for x in v_R0]
# R=200W
f_R200 = [6.5, 9.9, 15.4, 18.9, 21.6, 29.6]
b_R200 = [215.2, 309.2, 470.9, 565.3, 705, 873.1]
v_R200 = [211.3, 306.2, 468.8, 564.4, 706, 873.9]
f_R0 = [x * 2*np.pi for x in f_R200]
b_R200=[x * (2*np.pi/60) for x in b_R200]
v_R200=[x * (2*np.pi/60) for x in v_R200]
sous = [x - y for x, y in zip( f_R200,b_R200)]
g_R200 = [x / y for x, y in zip(sous, f_R200)]
# R=800W
f_R800 = [6.3, 11, 17.9, 22.2, 26.3, 30.6]
b_R800 = [200.5, 304.9, 493.6, 635.8, 762.8, 916.6]
v_R800 = [201.3, 303, 492.3, 634.8, 762.6, 916.4]
f_R80 = [x * 2*np.pi for x in f_R800]
b_R800=[x * (2*np.pi/60) for x in b_R800]
v_R800=[x * (2*np.pi/60) for x in v_R800]
sous = [x - y for x, y in zip( f_R800,b_R800)]
g_R800 = [x / y for x, y in zip(sous, f_R800)]

y=g_R0
deltay=incertitude(y)# Delta x donnant l'intervalle de confiance à 95% pour 
x=b_R0
deltax = ub0

