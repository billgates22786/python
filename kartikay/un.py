n=2
while n<=100:
  m=0
  j=2
  while j<=n:
    if n%j==0:
      m=m+1
      break
    j=j+1

  if m==0:
    print(n)
n=n+1