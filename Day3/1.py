ls=[(10,20,40),(40,50,60),(70,80,90)]
ls2=[]
for i in range(len(ls)):
   a=ls[i][0]
   b=ls[i][1]
   c=100
   new_tuple=(a,b,c)
   ls2.append(new_tuple)
print(ls2)