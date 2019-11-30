num=int(input("Enter a number"))
k=0
for i in range(1,num+1):
        if(num%i==0):
          k=k+1
          if(k>2):
            break
if(k>2):
    print("Not a prime")
else:
    print("Prime")