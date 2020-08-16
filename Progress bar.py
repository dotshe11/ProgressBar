import time

scale = 10

print('------------开始执行------------\n')

for i in range(scale+1):
    a = '***' * i
    b = '...' * (scale - i)
    c = (i/scale) * 100
    print("\r%{:^3.0f} [{}>{}]".format(c,a,b),end="",flush=True)
    time.sleep(0.2)

print('\n\n-------- ---执行结束------------')