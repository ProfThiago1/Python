'''
Aqui, estudaremos o objeto narray do numpy. O narray é um array multidimensional onde os dados devem ser homogêneos.
'''

import numpy as np

# Criando arrays

data1 = [6,7.5,8,0,1] 
arr1 = np.array(data1)

#print(f'{arr1} \n {type(arr1)}')

'''
O método array() do numpy recebe como argumento o objeto do tipo sequÊncia (lista) data1 e o transforma em um narray, cuja dimensão é 1.

Para sabermos a dimensão do array, usamos o print do atributo ndim do array e, se quisermos saber o tamanho do array, usamos o atributo shape.
'''

#print(f'{arr1.ndim} \n {arr1.shape}')

'''
O print anterior nos mostra que a dimensão do array é 1, e possui 5 elementos.

'''

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2) # Um array (2,4): Duas dimensões, com quatro elementos, equivalentemente, uma matriz 2x4.
#print(arr2)
#print(f'{arr2.shape}, dim:{arr2.ndim} and  data type:{arr2.dtype}')

# arange é a versão do np da função embutida range do py com valor de array

a = np.arange(15)
arr3 = np.array(a)
#print(a)
