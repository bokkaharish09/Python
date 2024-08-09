target=int(input("Enter your desired target number"))

sum=0

for x in range (2,target+1,2):
   sum+=x
print(sum)

asum=0
for x in range (2,target+1):
  if(x%2==0):
      asum+=x
  else:  #else is not necessary
      pass
print(sum)