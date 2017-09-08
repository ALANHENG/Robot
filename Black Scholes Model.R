###################
#Black Scholes Model
###################
#S : Stock Price
#K : Strike Price
#D : Dividend Yield (continuous,annual)
#r : Risk Free Rate (annual)
#sigma : volatility (annual)
#T : Time to maturity (in year)
#t : current time

BSM<-function(S,K,D,r,sigma,t,T){
  T = T-t
  d1 = (log(S/K,exp(1)) + (r - D + (0.5*(sigma**2)))*T) / (sigma*sqrt(T))
  d2 = (d1 - (sigma*sqrt(T)))
  Nd1 = pnorm(d1, mean = 0,sd = 1)
  Nd2 = pnorm(d2, mean = 0,sd = 1)
  Call_value = (S*exp(-D*T)*Nd1)- (K*exp(-r*T)*Nd2)
  
  N_d1 = pnorm(-d1, mean = 0, sd = 1)
  N_d2 = pnorm(-d2, mean = 0, sd = 1)
  
  Put_Value = (K*exp(-r*T)*N_d2) - (S*exp(-D*T)*N_d1)
  
  BSM_c_p<-c(Call_value,Put_Value)
  names(BSM_c_p)<-c("European Call","European Put")
  return(BSM_c_p)}

print(BSM)
BSM(68.93,67.5,0.0226,0.1,0.23,0,1.5)