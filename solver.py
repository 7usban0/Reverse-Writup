def next_higher(n):
    c=bin(n)[2:] #101
    c=list(c)
    m=""
    for i in range(len(c)): #i=0
        if(c[-1-i] =="1" and c[-2-i]=="0"):
            c[-2-i]="1"
            c[-1-i]="0"
            for i in c:
                m+=i
            return m
    return -1


print(next_higher(127))
    