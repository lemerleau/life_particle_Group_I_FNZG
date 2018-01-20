'''
@Author :: NONO Saha Cyrille Merleau 

@email : csaha@aims.edu.gh

Implentation of the approximated value of pi

'''

import random as r 
import numpy as np
from ROOT import *
import StandardDeviation as sd



def uniform(a,b) : 
        return (b-a)*r.random() + a 

def f(x,R) : 
        return np.sqrt(abs(x*x-R*R))

def pi_value(N) : 
        Ninf = 0 
        R = 1.0
        
        list_x = [] 
        list_y = []
        
        for i in range(N) : 
                list_x.append(uniform(0,R))
                list_y.append(uniform(0,R))
        
        list_accepted_x = []
        
        for i in range(N) : 
                if (list_y[i]< f(list_x[i],R)) : 
                        list_accepted_x.append(list_x[i])
                        
        
        
        Ninf = len(list_accepted_x)
        #print Ninf, len(list_x)
        fin = Ninf/float(N)
        pi = 4*fin
        
        #print "pi = ", pi
        
        return pi
        

def main () : 
       
        M = 100
        N = 100
        
        #liste that will contain all values of pi computed
        list_pi = []
        
        #perform pi computation M time
        list_mu_pi = []
        list_sigma_pi = []
        
        
        for i in range(50) : 
                for j in range(M) : 
                        list_pi.append(pi_value(N))
                list_mu_pi.append(sum(list_pi)/len(list_pi))
                list_sigma_pi.append(sd.MySigma(list_pi))
                N = N+200
                print i
        c = TCanvas("c","c",200,200)
        
        h1 = TH1F("h1","h1",100,3.,3.2)
         
        for x in list_mu_pi: 
                h1.Fill(x)
        
        h1.SetMinimum(0)
        h1.Draw("hist")
       
        c.SaveAs("pi-histogram_v1.eps")   
        
        
        
if __name__ =="__main__" : 
        main()
        
        
        
        
        
        
