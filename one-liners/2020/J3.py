a,x,y = int(input()),[],[];l= [input().split(",") for i in range(a)];[[x.append(int(u[0])),y.append(int(u[1]))]for u in l];print(f"{min(x)-1},{min(y)-1}"+'\n'+f"{max(x)+1},{max(y)+1}")