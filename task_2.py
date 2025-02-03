import scipy as sc
import numpy as np
from mpmath import mp
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
mp.dps=16
def func_1():
    data = np.loadtxt("sample_2.csv", delimiter='\t', dtype=float)
    return data
data=func_1()
A=[]
B=[]
C=[]
for i in range(0,50):
    A.append(data[i])
for i in range(0,100):
    B.append(data[i])
for i in range(0, 1000):
    C.append(data[i])
F_1=ECDF(A)
F_2=ECDF(B)
F_3=ECDF(C)
x_1=A
x_2=B
x_3=C
for i in range(len(x_1)):
    for j in range(i + 1, len(x_1)):

        if x_1[i] > x_1[j]:
           x_1[i], x_1[j] = x_1[j], x_1[i]
for i in range(len(x_2)):
    for j in range(i + 1, len(x_2)):

        if x_2[i] > x_2[j]:
           x_2[i], x_2[j] = x_2[j], x_2[i]
for i in range(len(x_3)):
    for j in range(i + 1, len(x_3)):

        if x_3[i] > x_3[j]:
           x_3[i], x_3[j] = x_3[j], x_3[i]
y_1=F_1(x_1)
y_2=F_2(x_2)
y_3=F_3(x_3)
#plt.step(x_3,y_3)
#.xlabel('Значение')
#plt.ylabel('Вероятность')
#plt.title('Эмпирическая функция распределения при n=1000')
#plt.show()
print("Для критерия Колмогорова")
m=0
m_max=0
m_1=0
m_max_1=0
for i in range(0,49):
    m=np.abs(y_1[i+1]-x_1[i])
    if(m>=m_max):
        m_max=m
for i in range(0,50):
    m_1=np.abs(y_1[i]-x_1[i])
    if(m_1>=m_max_1):
        m_max_1=m_1
if m_max_1>=m_max:
    m_max=m_max_1
m=np.sqrt(50)*m_max
p=1-sc.stats.kstwobign.cdf(m)
print("при n",50,"p-value",p)
m=0
m_max=0
m_1=0
m_max_1=0
for i in range(0,99):
    m=np.abs(y_2[i+1]-x_2[i])
    if(m>=m_max):
        m_max=m
for i in range(0,100):
    m_1=np.abs(y_2[i]-x_2[i])
    if(m_1>=m_max_1):
        m_max_1=m_1
if m_max_1>=m_max:
    m_max=m_max_1
m=np.sqrt(100)*m_max
p=1-sc.stats.kstwobign.cdf(m)
print("при n",100,"p-value",p)
m=0
m_max=0
m_1=0
m_max_1=0
for i in range(0,999):
    m=np.abs(y_3[i+1]-x_3[i])
    if(m>=m_max):
        m_max=m
for i in range(0,1000):
    m_1=np.abs(y_3[i]-x_3[i])
    if(m_1>=m_max_1):
        m_max_1=m_1
if m_max_1>=m_max:
    m_max=m_max_1
m=np.sqrt(1000)*m_max
p=1-sc.stats.kstwobign.cdf(m)
print("при n",1000,"p-value",p)
print("Для критерия ХИ-квадрат")
p=0.2
S=0
v=np.zeros(5)
for i in range(0,5):
    for j in range(0,50):
        if x_1[j]<=p*(i+1) and x_1[j]>p*i:
            v[i]=v[i]+1
for i in range(0,5):
    S=S+((v[i]-50*p)**2)/(50*p)
p=1-sc.stats.chi2.cdf(S,4)
print("при n",50,"p-value",p)
p=0.1
S=0
v=np.zeros(10)
for i in range(0,10):
    for j in range(0,100):
        if x_2[j]<=p*(i+1) and x_2[j]>p*i:
            v[i]=v[i]+1
for i in range(0,10):
    S=S+((v[i]-100*p)**2)/(100*p)
p=1-sc.stats.chi2.cdf(S,9)
print("при n",100,"p-value",p)
p=0.01
S=0
v=np.zeros(100)
for i in range(0,100):
    for j in range(0,1000):
        if x_3[j]<=p*(i+1) and x_3[j]>p*i:
            v[i]=v[i]+1
for i in range(0,100):
    S=S+((v[i]-1000*p)**2)/(1000*p)
p=1-sc.stats.chi2.cdf(S,99)
print("при n",1000,"p-value",p)
def func_2(data,n):
    A=[]
    for i in range(0,n):
        A.append(data[i])
    p = 10/n
    S = 0
    a=n//10
    v = np.zeros(a)
    for i in range(0, a):
        for j in range(0, n):
            if A[j] <= p * (i + 1) and A[j] > p * i:
                v[i] = v[i] + 1
    for i in range(0, a):
        S = S + ((v[i] - n * p) ** 2) / (n * p)
    p = 1 - sc.stats.chi2.cdf(S, (n/10)-1)
    print("при n", n, "p-value", p)
    return p
A=[]
B=[]
for i in range(20,1010,10):
    A.append(func_2(data,i))
    B.append(i)
plt.show()
plt.xlabel('n')
plt.ylabel('p-value')
plt.title('Зависимость p-value от n')
plt.plot(B,A)
plt.show()