'''
This code tries to answer to the question : Where is the particle inside the box ? 

@Author : Funmilayo, Nono, Zarcharia, and Gilles  

'''

from ROOT import *
import numpy as np 
import random as r 

#Definition of probability distribution function A 
def pA(x,c1,c2) :
        a = c1*c1*(np.sin(np.pi*x))**2
        b = c2*c2*(np.sin(2*np.pi*x))**2
         
        return a + b  
        
#Definition of probability distribution function B
def pB(x,c1,c2) :
        a = c1*(np.sin(np.pi*x))
        b = c2*(np.sin(2*np.pi*x))
         
        return pA(x,c1,c2) + 2*a*b


def main() : 

        
        N = 600000
        list_x = [] 
        list_u = []
        list_accepted_x = []
        
        #Canvas for drawin
        c = TCanvas("c","c",200,200)
        
        
        #Load the observed data and plot the histogram of data
        f = open("particle_in_a_box_v0_PerfectDetector_N10000.txt")
        lines = f.readlines()
        observed_val = []
        for line in lines : 
                val = float(line.split()[1])
                observed_val.append(val)
        hdata = TH1F("hdata","hdata",100,0,1)
        
        #Fill the data on the histogram 
         
        for val in observed_val : 
                hdata.Fill(val)

        #Draw the histogram                
        hdata.Draw("hist")
        
        #Save the histogram as a picture
        c.SaveAs("check_data.eps")
        
        
        #genrating of N random numbers between 0 and 1 and 0 and 4
        for i in range(N): 
                list_x.append(r.uniform(0,1))
                list_u.append(r.uniform(0,4))
        
        
        ############################################################################
        ##                                                                        ##
        ##                                                                        ##
        ## This Section tries to predict the set of data following probability A
        ## and check the result with the given data observed and compute the Chisquart##                           
        ##                                                                            ##
        ################################################################################
        #Chosen the value of c1 and c2 
        c1 = 0.75
        c2 = 0.64
        
        
        #Selecting the first 10000 values respected to probalility B
        for i in range(N): 
                if list_u[i] < pA(list_x[i],c1,c2) :
                        list_accepted_x.append(list_x[i])  
                if len(list_accepted_x) == 10000: 
                        break    
                        
        
        hpa = TH1F("Hist P_A","Observation P_A",100,0,1)
        
        
        print len(list_accepted_x)
        
        for i in range(10000): 
                hpa.Fill(list_accepted_x[i])
         
        
        print "Mean observed Vs Pa === ", hdata.GetMean()
        print "Mean predicted using PA === ", hpa.GetMean()
        
        print  "Chisquare observed Pa ===", hdata.Chi2Test(hpa,"UUCHI2")
        print  "Chisquare predicted Pa ===", hpa.Chi2Test(hdata,"UUCHI2")
        hdata.SetMinimum(0)
        hdata.SetLineColor(1)  
        hdata.SetMarkerSize(0.3)
        hdata.SetMarkerStyle(22)
        hdata.SetMarkerColor(2)
        
        
        hpa.SetMinimum(0)
        hpa.SetLineColor(1)  
        hpa.SetMarkerColor(4)
        hpa.SetMarkerSize(0.3)
        hpa.SetMarkerStyle(20)
        
        
        hdata.Draw("pe")
        hpa.Draw("pesame")
        c.SaveAs("vA_hist_test1.eps")
        
        
        
        
        #Clean list_accepted_x
        list_accepted_x = []
        
        ############################################################################
        ##                                                                        ##
        ##                                                                        ##
        ## This Section tries to predict the set of data following probability B
        ## and check the result with the given data observed and compute the Chisquart##                           
        ##                                                                            ##
        ################################################################################
        #Chosen the value of c1 and c2 
        c1 = 0.75
        c2 = 0.64
        
        
        
        #Selecting the first 10000 values respected to probalility B
        for i in range(N): 
                if list_u[i] < pB(list_x[i],c1,c2) :
                        list_accepted_x.append(list_x[i])  
                if len(list_accepted_x) == 10000: 
                        break    
                        
        
        hpb = TH1F("Hist P_B Vs Obs","Observation P_B",100,0,1)
        
        
        print len(list_accepted_x)
        
        for i in range(10000): 
                hpb.Fill(list_accepted_x[i])
         
        
        print "Mean observed === ", hdata.GetMean()
        print "Mean experience === ", hpb.GetMean()
        
        print  "Chisquare observed Pb ===", hdata.Chi2Test(hpb,"UUCHI2")
        print  "Chisquare predicted Pb ===", hpb.Chi2Test(hdata,"UUCHI2")
        hdata.SetMinimum(0)
        hdata.SetLineColor(1)  
        hdata.SetMarkerSize(0.3)
        hdata.SetMarkerStyle(22)
        hdata.SetMarkerColor(2)
        
        
        hpb.SetMinimum(0)
        hpb.SetLineColor(1)  
        hpb.SetMarkerColor(4)
        hpb.SetMarkerSize(0.3)
        hpb.SetMarkerStyle(20)
        
        
        
        
        hpb.Draw("pe")
        hdata.Draw("pesame")
        c.SaveAs("vB_hist_test1.eps")
        
        
        


if __name__ == "__main__" : 
        main() 
                
                
