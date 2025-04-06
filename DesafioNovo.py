"""Dados:
entrada01: 3:45
entrada02: 14:20
Saida: 6:05"""
hora01 = 3
minutos01 = 45
hora02 = 14
minutos02 = 20
minutoF = minutos01 + minutos02

if hora01 >12:
    valorH01 = hora01 - 12
else:
    valorH01 = hora01

if hora02 >12:
    valorH02 = hora02 - 12
else:
    valorH02 = hora02

horaF = valorH01 + valorH02

if minutoF >= 60:
    minutoF02 = minutoF - 60
    horaF02 = horaF + 1
    if horaF02 >12:
        horaF03 = horaF02 - 12
        print(f"{horaF03}:{minutoF02}")
    else:
        print(f"{horaF02}:{minutoF02}")
else:
        print(f"{horaF}:{minutoF}")