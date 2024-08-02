import numpy as np
import time

'''
Aqui, veremos a comparação de tempo de processamento de operações python puro e python com numpy.
'''

my_arr = np.arange(1000000)

my_list = list(range(1000000))

start = time.time()

for _ in range(10):
    my_arr2 = my_arr*2
end = time.time()

print(f'Tempo de CPU: {end - start:.2f} s ')

st2 = time.time()
for _ in range(10):
    my_list2 = my_list*2
en2 = time.time()

print(f'{en2 - st2:.2f}')