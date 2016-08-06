import re

Str = open(r'E:\C\CMD\div_\div_\main.cpp', 'r').read()
id_reg_exp = r'[a-zA-Z_][a-zA-Z_0-9]*'
ID_reg = re.compile(id_reg_exp)
id_list = re.findall(ID_reg, Str)
for i, id_elem in enumerate(id_list):
    print(i, id_elem)
