#WAP to print only IP address from the given string
str = '["127.0.0.1","234.93.3","243.1.1"]'

for i in str.split("'"):
    for j in i.split('['):    
        for k in j.split('"'):
                for l in k.split(']'):
                    for m in l.split(','):
                        print(m , end=" ")
                    
   

