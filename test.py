# Napišite program, ki izpiše praštevila do 200
#for num in range(0, 200):
   #if num > 1:
       #for i in range(2, num):
           #if (num % i) == 0:
               #break
       #else:
           #print(num)
print(2)
print(3)

for j in range (4, 200):

    je_prastevilo = True


    for mozni_delitelj in range (2, j): #dovolj je, da gremo do korena
        if j % mozni_delitelj == 0:
            je_prastevilo = False
            break
    if je_prastevilo:
        print(j)
    
    