def gcd(a, b):  
    if a == 0 : 
        return b  
      
    return gcd(b%a, a) 

print(gcd(10, 12))