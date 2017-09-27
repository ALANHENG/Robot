# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:52:25 2017

@author: Alan
"""

S = float(input("Please enter the stock price :"))

K = float(input("Please enter the strike price :"))

r = float(input("Please enter the risk-free rate :"))

T = float(input("Please enter the maturing time in year :"))

t = float(input("Please enter the starting time in year :"))

D = float(input("Please enter the annual dividend yield :"))

sigma = float(input("Please enter the annualized volatility :"))

from math import exp,log,sqrt 
from scipy import stats
    
def BSM_Option_Greek():
    
    d1 = (log(S/K ,exp(1)) + ((r - D + (0.5*(sigma**2)))*(T-t))) / (sigma*sqrt(T-t))
    d2 = d1 - (sigma*sqrt(T-t))

    Nd1 = stats.norm.cdf(d1,0.0,1.0)
    N_d1 = stats.norm.cdf(-d1,0.0,1.0)
    Sd1 = stats.norm.pdf(d1)
    
    Nd2 = stats.norm.cdf(d2,0.0,1.0)
    N_d2 = stats.norm.cdf(-d2,0.0,1.0)
    
    Delta_Call = exp(-D*(T-t))*Nd1
    print("Delta_Call=",Delta_Call)
    
    Gamma_Call_Put = (exp(-D*(T-t))*Sd1)/(S*sigma*sqrt(T-t))
    print("Gamma_Call=",Gamma_Call_Put)
     
    Vega_Call_Put= S*exp(-D*(T-t))*sqrt(T-t)*Sd1
    print("Vega_Call=",Vega_Call_Put)
    
    Theta_Call = (S*D*exp(-D*(T-t))*Nd1) - (r*K*exp(-r*(T-t))*Nd2) 
    - ((S*exp(-D*(T-t))*Sd1*sigma)/(2*sqrt(T-t)))
    print("Theta_Call=",Theta_Call)
    
    Rho_Call = (T-t)*K*exp(-r*(T-t))*Nd2
    print("Rho_Call =",Rho_Call)
    
    Psi_Call = -(T-t)*S*exp(-D*(T-t))*Nd1
    print("Psi_Call =",Psi_Call)
    
    Delta_Put = exp(-D*(T-t))*N_d1
    print("Delta_Put =",Delta_Put)
    
    print("Gamma_Put =",Gamma_Call_Put)
    
    print("Vega_Put =",Vega_Call_Put)
    
    Theta_Put = (r*K*exp(-r*(T-t))*N_d2) - (S*D*exp(-D*(T-t))*N_d1) 
    - ((S*exp(-D*(T-t))*sigma)/(2*sqrt(T-t)))
    print("Theta_Put =",Theta_Put)
    
    Rho_Put = -(T-t)*K*exp(-r*(T-t))*N_d2
    print("Rho_Put =",Rho_Put)
    
    Psi_Put = (T-t)*exp(-D*(T-t))*N_d1
    print("Psi_Put =",Psi_Put)
    
BSM_Option_Greek()
    