import scipy as sc
import numpy as np
from mpmath import mp
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
def func_1():
    data = np.loadtxt("sample_4_1.csv", delimiter='\t', dtype=float)
    return data
def func_2():
    data = np.loadtxt("sample_4_2.csv", delimiter='\t', dtype=float)
    return data
def func_3(data_1,data_2,eps):
 print("Эпсилон",eps)
 n=50
 m=100
 S_1=0
 S_2=0
 s_1=0
 s_2=0
 SR_1=0
 SR_2=0
 S=0
 for i in range(0,n):
     SR_1 =SR_1+data_1[i]
 SR_1 = SR_1 / n
 for i in range(0,m):
     SR_2 =SR_2+ data_2[i]
 SR_2 = SR_2 / m
 s_1=np.var(data_1, ddof=1)*(n-1)/n
 s_2=np.var(data_2, ddof=1)*(m-1)/m
 a=np.abs(SR_1-SR_2)
 b=np.sqrt((n*s_1)+(m*s_2))
 k=np.sqrt((n+m-2)/((1/n)+(1/m)))
 d=a*k/b
 c=sc.stats.t.ppf(1-(eps/2),n+m-2)
 p=1-sc.stats.t.cdf(d,n+m-2)+sc.stats.t.cdf(-d,n+m-2)
 print("Расстояние Стьюдента",d,"Квантиль уровня 1-eps/2",c,"p-value",p)
data_1=func_1()
data_2=func_2()
#a,b=sc.stats.ttest_ind(data_1,data_2)
#print(a,b)
func_3(data_1,data_2,0.2)
func_3(data_1,data_2,0.1)
func_3(data_1,data_2,0.05)
func_3(data_1,data_2,0.025)
func_3(data_1,data_2,0.005)
