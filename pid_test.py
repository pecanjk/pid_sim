import numpy as np
import matplotlib.pyplot as plt


N=100
#These three has different unit scale
K_P=0.2
K_I=0.2
K_D=0.0

x_init=0
x_target=10

x=x_init
x_err_cumsum=0
x_err=x_target-x_init#first error


x_list=[x]
x_err_list=[x_err]
''' 
position_pid
    u(k)=K_p * e(k) + K_I * SUM_n=02k(e(n)) + K_d * (e(k)-e(k-1))
'''
for i in range(1,N):
    x_err_pre=x_err
    x_err=x_target-x
    x_err_diff=x_err-x_err_pre
    x_err_cumsum+=x_err

    x=K_P*x_err + K_I*x_err_cumsum+ K_D*x_err_diff
    # print('===after PID, now x=',x)
    x_list.append(x)
    x_err_list.append(x_err)

print('x_err_list=\n',x_err_list)
print('x_list=\n',x_list)

plt.figure(0)
plt.plot(range(N),x_list)

plt.figure(1)
plt.plot(range(N),x_err_list)

plt.show()


''' 
incremental_pid
    u(k-1)=K_P * e(k-1) + K_I * SUM_n=02k-1(e(n)) + K_d * (e(k-1)-e(k-2))
    u(k)=K_P * e(k) + K_I * SUM_n=02k(e(n)) + K_d * (e(k)-e(k-1))
===>>>==
    e(k)=u_target-u(k-1)
    du(k)=K_P * (e(k)-e(k-1)) + K_I * e(k) + K_d * (e(k)-2*e(k-1)+e(k-2))  #here no need to cummulated sum all err
    u(k)=u(k-1)+du(k)

'''

e_init=0
u_init=0
u_target=10

e=[0]*N
u=[0]*N
du=[0]*N

e[0]=e_init
u[0]=u_init
du[0]=0

e[1]=u_target-u[0]
u[1]=K_P * e[1] + K_I * (e[0]+e[1])+K_D*(e[1]-e[0])
du[1]=u[1]-u[0]


for k in range(2,N):
    e[k]=u_target-u[k-1]
    du[k]=K_P * (e[k]-e[k-1]) + K_I * e[k] + K_D * (e[k]-2*e[k-1]+e[k-2])
    u[k]=u[k-1]+du[k]

print('err list= \n',e)
print('du list= \n',du)
print('u list= \n',u)
