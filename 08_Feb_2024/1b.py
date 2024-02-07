CC= 184
CT= 65
TT= 7
Total= CC+CT+TT
Fcc= CC/Total
Fct= CT/Total
Ftt= TT/Total
#Estimate allele freq
Pc=((2*CC)+CT)/(2*Total)
print("Pc=", Pc)
Pt= 1-Pc
print("Pt=", Pt)
