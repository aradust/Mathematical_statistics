import scipy as sc
import numpy as np
from mpmath import mp
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
def func_1():
    data = np.loadtxt("sample_3_1.csv", delimiter='\t', dtype=float)
    return data
def func_2():
    data = np.loadtxt("sample_3_2.csv", delimiter='\t', dtype=float)
    return data
data_1=func_1()
data_2=func_2()
def func_3(data_1,data_2,eps):
    print("Эпсилон", eps)
    n = 50
    m = 100
    d = np.var(data_1, ddof=1) / np.var(data_2, ddof=1)
    t_1 = sc.stats.f.ppf(eps / 2, n - 1, m - 1)
    t_2 = sc.stats.f.ppf(1 - (eps / 2), n - 1, m - 1)
    print("Отношение несмещенных выборочных дисперсий", d)
    print("Интервал", [t_1, t_2])
    if d<1:
        d=1/d
        n, m = m, n
    print("p-value ",2*(1-sc.stats.f.cdf(d,n-1,m-1)))
print("Искусственные данные с одинаковой дисперсией")
data_3=sc.stats.norm(loc=0,scale=1).rvs(size=50)
data_4=sc.stats.norm(loc=0,scale=1).rvs(size=100)
data_5=sc.stats.norm(loc=0,scale=10).rvs(size=100)
func_3(data_3,data_4,0.2)
print("Искусственные данные с разной дисперсией")
func_3(data_3,data_5,0.2)
print("Наша выборка")
func_3(data_1,data_2,0.2)
print("Теперь меняем эпсилон ")
func_3(data_1,data_2,0.1)
func_3(data_1,data_2,0.05)
func_3(data_1,data_2,0.025)
func_3(data_1,data_2,0.005)
SR=0
S=0
n=50
for i in range(0,n):
    SR += data_1[i]
SR = SR / n
for i in range(0,n):
    S += (data_1[i] - SR) ** 2
S = S / (n-1)
#print(S,np.var(data_1, ddof=1))