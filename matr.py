import numpy as np
import matplotlib.pyplot as plt
 

if __name__ == '__main__':

   t = 0
   lol = 0
   
   Bias = np.zeros(1000)
   n =0
   tt = np.zeros(1000)
   ya = np.zeros(1000)
   yva = np.zeros(1000)
   bi = np.zeros(1000)
   Ybb = np.zeros(1000)
   Yb = np.zeros(1000)
   Vec = np.zeros((2,1))
   VecAS = np.zeros(1000)
   VecA = np.zeros(1000)
   Lo = np.zeros(1000)
   b1 = np.pi*2*np.pi*1 * 0.03
   b2 = np.pi*2 * 0.1
   X = np.array([[0],[0],[0]])
   H = np.array([[1,0,1],[0,1,0]])
   R = np.array([[b1**2,0],[0,b2**2]])
   A = np.array([[1,0,0],[0.01,1,0],[0,0,1]])
   Q = np.array([[30,0,0],[0,0,0],[0,0,0.5]])
   P = np.array([[0,0,0],[0,0,0],[0,0,0]])
    
   
    
   
   while t<=9.99:

    Xp = np.dot(A,X)
    Pp = np.dot(A,P)
    Pp = np.dot(Pp,A.T)
    Pp = Pp+Q
    
    K = np.dot(Pp,H.T)
    Iv = np.dot(H,Pp)
    Iv = np.dot(Iv,H.T)
    Iv = Iv + R
    Iv = np.linalg.inv(Iv)  
    K = np.dot(K,Iv)
    
    P = np.dot(K,H)
    P = np.dot(P,Pp)
    P = Pp-P

    

    X = np.dot(H,Xp)
    X =  Vec - X
    F = np.dot(K,X)
    X = Xp+F
    VecAS[n]= X[0,0]
    VecA[n]= X[1,0]
    Bias[n] = X[2,0]
     
     
     
     
     
    Mva =  60*np.sin(7*t)
    
     
    Ma = -8.57*np.cos(7*t)+8.57
    biais = 5*t+20*np.sin( 0.50*t) 
    Mvabb = Mva +biais+ np.random.randn(1)*b1
    
    Mab = Ma + np.random.randn(1)*b2
     
    

     
    Vec[0,0] = Mvabb
    Vec[1,0] = Mab
    Ybb[n] = Mvabb
    Yb[n] = Mab
    yva[n] = Mva
    ya[n] = Ma
    bi[n] = biais
    tt[n] = t
    t += 0.01
    n += 1


   
   
   ax=plt.subplot(111)
   ax.plot(tt, ya, label='Angle reelle')
   ax.plot(tt, VecA, label='Pred Angle')
   ax.plot(tt, Yb, label='Mesure bruitee')
   plt.xlabel('Temps')
   plt.ylabel('Angle')
   plt.title('Pos-Angulaire')
   ax.legend()
   plt.savefig('A.png')
   plt.show()
   ax=plt.subplot(111)
   ax.plot(tt, yva, label='V-Angulaire reelle')
   ax.plot(tt, VecAS, label='Pred V-Angulaire')
   ax.plot(tt, Ybb, label='V-Angulaire bruitee & biaise')
   plt.xlabel('Temps')
   plt.ylabel('A/S')
   plt.title('V-Angulaire')
   ax.legend()
   plt.savefig('AS.png')
   plt.show()
   ax=plt.subplot(111)
   ax.plot(tt, bi, label='Biais reelle')
   ax.plot(tt, Bias, label='Pred biais')
   plt.xlabel('Temps')
   plt.ylabel('Angle')
   plt.title('Biais')
   ax.legend()
   plt.savefig(' Bi.png')
   plt.show()
   



     

    

     
    	
     
  

   
     
     
     
    

   



   
  
  
   
    
   	 