"""Finite-K delta, plus, Mellin, regular and convolution measurement matrices."""
import numpy as np

def measurements(K,n):
    x=(np.arange(n,dtype=float)+1.0)/(n+1.0) # support strictly below endpoint
    endpoint=np.zeros(n); endpoint[-1]=1.0
    phi=x**2+0.3*x
    regular=phi/n
    plus=(phi-phi[-1])/(1-x+1/(K+1)); plus-=plus.mean() # constant-test cancellation convention
    logplus=np.log(1-x+1/(K+1))*(phi-phi[-1])/(1-x+1/(K+1)); logplus-=logplus.mean()
    mellin=np.vstack([x**p/n for p in (0,1,2)])
    kernel=np.exp(-2*np.abs(x[:,None]-x[None,:]))/n
    return {"regular":regular[None,:],"delta":endpoint[None,:],"plus":plus[None,:],"logplus":logplus[None,:],"mellin":mellin,"convolution":kernel,"x":x}

def direct_action(row,f): return sum(float(a)*complex(b) for a,b in zip(row,np.asarray(f)))
