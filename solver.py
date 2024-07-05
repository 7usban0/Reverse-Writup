c = "9,4,6,8.6.2,9.2,;.2,9.9,2,2,7.3,4,7.2,2,9.4,7.3,3.7,9.1,9,4.0,9.8."
n = ""
result = ""

for j in range(0, len(c), 2):
    for i in range(97, 127):
        if c[j] == str(chr(i // 2)):
            if(c[j+1]=="." and  i%2==0):
                result+=chr(i)
                n+=chr(i//2)
                n+="."
            else:
                result+=chr(i+1)
                n+=chr((i+1)//2)
                n+=","
            break
print(result, n)
"""
"simplereverseengineeringforcsharp" just change the b to a in before r    string
"""
