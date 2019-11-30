fib=int(input("Enter size of fibonacci series"))
fb=[0,1]
for i in range(2,fib):
    fb.append(fb[i-1]+fb[i-2])
    
print("Fibbonaci Series ",fb)