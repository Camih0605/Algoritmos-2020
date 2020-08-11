import time

def caso1(n):

    if n < 2:
        return n
    else:
        return caso1(n-1) + caso1(n-2)
    
def caso2(n):
  if n < 2:
        return n
  else:
    a=0
    b=1
    for c in range(2,n+1):
      c=a+b
      a=b
      b=c
    return(c)

inicio = time.time()
tiempo_caso1 = inicio-time.time()
inicio = time.time()
tiempo_caso2 = inicio-time.time()

if tiempo_caso1>tiempo_caso2:
    print("Es mejor el caso 2")
else:
    print("Es mejor el caso 1")
