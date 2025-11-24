kwh=int(input())
S=0
if kwh <= 50:
    S=kwh*1800
elif kwh > 50 and kwh <= 100:
    S=50*1800+(kwh-50)*2000
elif kwh > 100:
    S=50*1800+(kwh-50)*2000+(kwh-100)*2500
print(S)