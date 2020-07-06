import numpy as np
import matplotlib.pyplot as plt







if __name__ == '__main__':

   a = 0
   t = 0
   n = 0
   X = 0
   P = 0
   w = 0
   VarMe = 4**2
   varM = 0.3
   Yb = np.zeros(1000)
   Yc = np.zeros(1000)
   tt = np.zeros(1000)
   we = np.zeros(1000)
  
   while t<=9.99:
   
    Ma = -8.57*np.cos(3*t)+8.57
     
    a = Ma +np.random.randn(1)*2  
    Xp = X
    Pp = P + varM
    K =  VarMe + Pp
    K = K**-1
    K = Pp* K
    P = K*Pp
    P = Pp - P
    X = a - Xp
    X = K * X
    X = Xp + X
    Yb[n] = X
    Yc[n] = a
    tt[n] = t
    we[n] = Ma
    n += 1
    t += 0.01


 
   
   plt.plot(tt,Yc)
   plt.plot(tt,Yb)
   plt.plot(tt,we)
   
   plt.grid()
   plt.show()

   
