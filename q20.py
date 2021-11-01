x,a1,a2,a3 = map(int,input().split())

y = a1*15+a2*20+a3*30
z = x-y

b = z//50
c = (z%50)//5
d = (z%50)%5

print(f"{d}\n{c}\n{b}")

    
    
        
    