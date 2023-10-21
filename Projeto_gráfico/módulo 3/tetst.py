from funcionalidades import *

tv = Televisor('Samsung','SM-084')

controle = ControleRemoto(tv)

controle.sintcanal('SBT')
controle.trocadecanal('SBT')



print(tv.canal_atual)
print(tv.list_canal)

