CC= 184
CT= 65
TT= 7
Total= CC+CT+TT
Fcc= CC/Total
Fct= CT/Total
Ftt= TT/Total
Pc=((2*CC)+CT)/(2*Total)
Pt= 1-Pc
#Estimate genotype frequencies
Pcc= (Pc)**2
print("Pcc=", Pcc)
Ptt= (Pt)**2
print("Ptt=", Ptt)
Pct= 2 *(Pc * Pt)
print ("Pct=", Pct)