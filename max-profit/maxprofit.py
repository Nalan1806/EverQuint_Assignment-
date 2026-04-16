def maxprofit(n):
    max_profit=0

    #to find the best combination of t,p and c via brute force
    best_t=0
    best_p=0
    best_c=0
     
    for t in range (n//5+1):
        for p in range(n//4+1):
            for c in range(n//10+1):

                total_build_time=5*t+4*p+10*c
                

                if total_build_time <=n :
                    current_time=0
                    profit=0

                    #we simulate a build order T->P->c

                    for _ in range(t):
                        current_time+=5
                        if current_time<=n:
                            profit +=1500 *(n-current_time)
                    for _ in range(p):
                        current_time+=4
                        if current_time<=n:
                            profit +=1000 *(n-current_time)
                        
                    for _ in range(c):
                        current_time+=10
                        if current_time<=n:
                            profit +=2000 *(n-current_time)

                    if profit>max_profit:
                     max_profit=profit
                     best_t,best_p,best_c=t,p,c

    return best_t,best_p,best_c,max_profit


n=int(input("enter value of n: "))
t,p,c,profit = maxprofit(n)

print(f"T:{t}, P:{p}, C:{c}")
print(f"Earnings: ${profit}")
