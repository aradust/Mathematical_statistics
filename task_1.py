import scipy as sc
import numpy as np
def func_1():
    data = []
    with open("sample_1.csv") as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    f.close()
    return data
data=func_1()
def func_2(data,eps):
 print("Для эпсилон",eps)
 k=1-(eps/2)
 E=-0.45154895915072096
 sgm=np.sqrt(1.0032229992035606)
 n=50
 SR=0
 A=[]
 for i in range(0,n):
     A.append(data[i])
 for i in A:
     SR+=sum(i)
 SR=SR/n
 tau=sc.stats.norm.ppf(k, 0, 1)
 print("Квантиль",tau)
 len_1=SR-(sgm*tau)/np.sqrt(n)
 len_2=SR+(sgm*tau)/np.sqrt(n)
 interv=[len_1,len_2]
 print("Доверительный интервал для",n,interv)
 n=100
 SR=0
 A=[]
 for i in range(0,n):
     A.append(data[i])
 for i in A:
     SR+=sum(i)
 SR=SR/n
 tau=sc.stats.norm.ppf(k, 0, 1)
 len_1=SR-(sgm*tau)/np.sqrt(n)
 len_2=SR+(sgm*tau)/np.sqrt(n)
 interv=[len_1,len_2]
 print("Доверительный интервал для",n,interv)
 n = 500
 SR = 0
 A = []
 for i in range(0, n):
     A.append(data[i])
 for i in A:
     SR += sum(i)
 SR = SR / n
 tau = sc.stats.norm.ppf(k, 0, 1)
 len_1 = SR - (sgm * tau) / np.sqrt(n)
 len_2 = SR + (sgm * tau) / np.sqrt(n)
 interv = [len_1, len_2]
 print("Доверительный интервал для", n, interv)
 n = 1000
 SR = 0
 A = []
 for i in range(0, n):
     A.append(data[i])
 for i in A:
     SR += sum(i)
 SR = SR / n
 tau = sc.stats.norm.ppf(k, 0, 1)
 len_1 = SR - (sgm * tau) / np.sqrt(n)
 len_2 = SR + (sgm * tau) / np.sqrt(n)
 interv = [len_1, len_2]
 print("Доверительный интервал для", n, interv)
 n = 5000
 SR = 0
 A = []
 for i in range(0, n):
     A.append(data[i])
 for i in A:
     SR += sum(i)
 SR = SR / n
 tau = sc.stats.norm.ppf(k, 0, 1)
 len_1 = SR - (sgm * tau) / np.sqrt(n)
 len_2 = SR + (sgm * tau) / np.sqrt(n)
 interv = [len_1, len_2]
 print("Доверительный интервал для", n, interv)
 n = 10000
 SR = 0
 A = []
 for i in range(0, n):
     A.append(data[i])
 for i in A:
     SR += sum(i)
 SR = SR / n
 tau = sc.stats.norm.ppf(k, 0, 1)
 len_1 = SR - (sgm * tau) / np.sqrt(n)
 len_2 = SR + (sgm * tau) / np.sqrt(n)
 interv = [len_1, len_2]
 print("Доверительный интервал для", n, interv)
def func_3(data,eps):
    print("Для эпсилон", eps)
    k = 1 - (eps / 2)
    E = -0.45154895915072096
    sgm = np.sqrt(1.0032229992035606)
    n = 50
    SR = 0
    S=0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
         S+=(sum(i)-SR)**2
    S=(1/(n-1))*S
    S=np.sqrt(S)
    tau = sc.stats.t.ppf(k,n-1)
    print("Квантиль", tau)
    len_1 = SR - (S * tau) / np.sqrt(n)
    len_2 = SR + (S * tau) / np.sqrt(n)
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 100
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = (1 / (n - 1)) * S
    S = np.sqrt(S)
    tau = sc.stats.t.ppf(k, n - 1)
    len_1 = SR - (S * tau) / np.sqrt(n)
    len_2 = SR + (S * tau) / np.sqrt(n)
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 500
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = (1 / (n - 1)) * S
    S = np.sqrt(S)
    tau = sc.stats.t.ppf(k, n - 1)
    len_1 = SR - (S * tau) / np.sqrt(n)
    len_2 = SR + (S * tau) / np.sqrt(n)
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 1000
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = (1 / (n - 1)) * S
    S = np.sqrt(S)
    tau = sc.stats.t.ppf(k, n - 1)
    len_1 = SR - (S * tau) / np.sqrt(n)
    len_2 = SR + (S * tau) / np.sqrt(n)
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 5000
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = (1 / (n - 1)) * S
    S = np.sqrt(S)
    tau = sc.stats.t.ppf(k, n - 1)
    len_1 = SR - (S * tau) / np.sqrt(n)
    len_2 = SR + (S * tau) / np.sqrt(n)
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 10000
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = (1 / (n - 1)) * S
    S = np.sqrt(S)
    tau = sc.stats.t.ppf(k, n - 1)
    len_1 = SR - (S * tau) / np.sqrt(n)
    len_2 = SR + (S * tau) / np.sqrt(n)
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
def func_4(data,eps):
    print("Для эпсилон", eps)
    k = 1 - (eps / 2)
    E = -0.45154895915072096
    sgm = np.sqrt(1.0032229992035606)
    n = 50
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        S += (sum(i) - E) ** 2
    tau_1 = sc.stats.chi2.ppf(eps / 2, n)
    tau_2 = sc.stats.chi2.ppf(k, n)
    print("Квантили", tau_1, tau_2)
    len_1 = S / tau_2
    len_2 = S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n =100
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        S += (sum(i) -E)**2
    tau_1 = sc.stats.chi2.ppf(eps / 2, n)
    tau_2 = sc.stats.chi2.ppf(k, n )
    len_1 = S / tau_2
    len_2 = S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 500
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        S += (sum(i) - E) ** 2
    tau_1 = sc.stats.chi2.ppf(eps / 2, n)
    tau_2 = sc.stats.chi2.ppf(k, n)
    len_1 = S / tau_2
    len_2 = S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 1000
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        S += (sum(i) - E) ** 2
    tau_1 = sc.stats.chi2.ppf(eps / 2, n)
    tau_2 = sc.stats.chi2.ppf(k, n)
    len_1 = S / tau_2
    len_2 = S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 5000
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        S += (sum(i) - E) ** 2
    tau_1 = sc.stats.chi2.ppf(eps / 2, n)
    tau_2 = sc.stats.chi2.ppf(k, n)
    len_1 = S / tau_2
    len_2 = S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n =10000
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        S += (sum(i) - E) ** 2
    tau_1 = sc.stats.chi2.ppf(eps / 2, n)
    tau_2 = sc.stats.chi2.ppf(k, n)
    len_1 = S / tau_2
    len_2 = S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
def func_5(data,eps):
    print("Для эпсилон", eps)
    k = 1 - (eps / 2)
    E = -0.45154895915072096
    sgm = np.sqrt(1.0032229992035606)
    n = 50
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S=S/n
    tau_1 = sc.stats.chi2.ppf(eps/2, n - 1)
    tau_2 = sc.stats.chi2.ppf(k, n - 1)
    print("Квантили", tau_1,tau_2)
    len_1 = n*S/tau_2
    len_2 = n*S/tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 100
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = S / n
    tau_1 = sc.stats.chi2.ppf(eps / 2, n - 1)
    tau_2 = sc.stats.chi2.ppf(k, n - 1)
    len_1 = n * S / tau_2
    len_2 = n * S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 500
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = S / n
    tau_1 = sc.stats.chi2.ppf(eps / 2, n - 1)
    tau_2 = sc.stats.chi2.ppf(k, n - 1)
    len_1 = n * S / tau_2
    len_2 = n * S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 1000
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = S / n
    tau_1 = sc.stats.chi2.ppf(eps / 2, n - 1)
    tau_2 = sc.stats.chi2.ppf(k, n - 1)
    len_1 = n * S / tau_2
    len_2 = n * S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 5000
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = S / n
    tau_1 = sc.stats.chi2.ppf(eps / 2, n - 1)
    tau_2 = sc.stats.chi2.ppf(k, n - 1)
    len_1 = n * S / tau_2
    len_2 = n * S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
    n = 10000
    SR = 0
    S = 0
    A = []
    for i in range(0, n):
        A.append(data[i])
    for i in A:
        SR += sum(i)
    SR = SR / n
    for i in A:
        S += (sum(i) - SR) ** 2
    S = S / n
    tau_1 = sc.stats.chi2.ppf(eps / 2, n - 1)
    tau_2 = sc.stats.chi2.ppf(k, n - 1)
    len_1 = n * S / tau_2
    len_2 = n * S / tau_1
    interv = [len_1, len_2]
    print("Доверительный интервал для", n, interv)
print("Параметры:")
print("E:", -0.45154895915072096)
print("D:", 1.0032229992035606 )
print("Случай для математического ожидания, когда дисперсия известна")
func_2(data,0.2)
func_2(data,0.1)
func_2(data,0.05)
func_2(data,0.025)
print("Параметры:")
print("E:", -0.45154895915072096)
print("D:", 1.0032229992035606 )
print("Случай для математического ожидания, когда дисперсия неизвестна")
func_3(data,0.2)
func_3(data,0.1)
func_3(data,0.05)
func_3(data,0.025)
print("Параметры:")
print("E:", -0.45154895915072096)
print("D:", 1.0032229992035606 )
print("Случай для дисперсии, когда математическое ожидание известно")
func_4(data,0.2)
func_4(data,0.1)
func_4(data,0.05)
func_4(data,0.025)
print("Параметры:")
print("E:", -0.45154895915072096)
print("D:", 1.0032229992035606 )
print("Случай для дисперсии, когда математическое ожидание неизвестно")
func_5(data,0.2)
func_5(data,0.1)
func_5(data,0.05)
func_5(data,0.025 )
