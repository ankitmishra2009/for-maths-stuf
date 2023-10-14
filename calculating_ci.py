p = int(input("input principal:"))
r = int(input("input rate of itrest:"))
t = int(input("input time:"))

ammount = p*(1+r/100)**t
ci = round(ammount) - p 

print("your ammount :",round(ammount))
print("your ci :", ci)