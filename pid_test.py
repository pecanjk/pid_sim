import numpy as np
# import matplotlib.pyplot as plt


N=100
#These three has different unit scale
K_p=0.1
K_I=0.2
K_D=0.2

x_init=0
x_target=10

x=x_init
x_err_cumsum=0
x_err=x_target-x_init#first error


x_list=[x]
x_err_list=[x_err]
for i in range(N):
    x_err_pre=x_err
    x_err=x_target-x
    x_err_diff=x_err-x_err_pre
    x_err_cumsum+=x_err

    x=K_p*x_err + K_I*x_err_cumsum+ K_D*x_err_diff
    print('===after PID, now x=',x)
    x_list.append(x)
    x_err_list.append(x_err)


