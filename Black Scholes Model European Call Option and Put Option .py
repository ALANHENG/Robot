# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:22:01 2017

@author: Alan Heng Hua Tat
"""

#Black Scholes Model
###############
S = float()
K = float()
r = float()
T = float()
t = float() 
D = float() 
sigma = float()

def BS_Call_Value():
    """ 
    Parameter
    S: Stock price
    K: Strike price
    r: annual risk-free rate
    T: Maturity date(in year)
    t: starting time
    D: annual dividend yield
    sigma: annualized volatility
    
    """
    
    from math import exp,log,sqrt 
    from scipy import stats
    
    #Calculate the d1 
    d1 = (log(S/K ,exp(1)) + ((r - D + (0.5*(sigma**2)))*(T-t))) / (sigma*sqrt(T-t))
    print("d1 =",d1)
    #Calculate the d2
    d2 = d1 - (sigma*sqrt(T-t))
    print("d2 =",d2)
    
    #Compute the probability of cumulative standard normal distribution in d1 and d2
    Nd1 = stats.norm.cdf(d1, 0.0 ,1.0)
    print("N(d1) =",Nd1)
    Nd2 = stats.norm.cdf(d2, 0.0 ,1.0)
    print("N(d2) =",Nd2)
    
    call_value = float((S*exp(-D*(T-t))*Nd1)- (K*exp(-r*(T-t))*Nd2))
    return call_value 

European_Call_Option = BS_Call_Value()
print("Theoretical value of European_Call_Option =",European_Call_Option)

def BS_Put_Value():
    """ 
    Parameter
    S: Stock price
    K: Strike price
    r: annual risk-free rate
    T: Maturity date(in year)
    t: starting time
    D: annual dividend yield
    sigma: annualized volatility
    
    """
    
    from math import exp,log,sqrt 
    from scipy import stats
   
    d1 = (log(S/K ,exp(1)) + ((r - D + (0.5*(sigma**2)))*(T-t))) / (sigma*sqrt(T-t))
    print("d1 =",d1)
    d2 = d1 - (sigma*sqrt(T-t))
    print("d2=",d2)
    
    N_d1 = stats.norm.cdf(-d1, 0.0 ,1.0)
    print("N(-d1) =",N_d1)
    N_d2 = stats.norm.cdf(-d2, 0.0 ,1.0)
    print("N(-d2) =",N_d2)
    
    Put_value = float((K*exp(-r*(T-t))*N_d2)-(S*exp(-D*(T-t))*N_d1))
    return Put_value

European_Put_Option = BS_Put_Value()
print("Theoretical value of European_Put_Option =",European_Put_Option)

###################
#Put Call Parity under Black Scholes Model
################### 
Put_Call_Parity = round(European_Call_Option - European_Put_Option,2)
print("Put Call Parity =",Put_Call_Parity)

###################
#Put Call Parity, proof C-P = PV(S-K)
#PV(S) = S*exp(-dividend yield*(T-t))
#PV(K) = K*exp(-risk-free rate*(T-t))
def P_C_Parity():
    
     from math import exp
     
     PV_S = S*exp(-D*(T-t))
     print("Present Value of Stock Price =",PV_S)
     PV_K = K*exp(-r*(T-t))
     print("Present Value of Strike Price in Dollar =",PV_K)
     P_C = round(PV_S - PV_K , 2)
     return P_C
 
Put_Call_Parity = P_C_Parity()
print("Put Call Parity =", Put_Call_Parity)
     

