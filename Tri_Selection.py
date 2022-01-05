def saisie():
    while True:
        n=int(input("Entrez la taille de tableau: "))
        if n>0:
            break
    return n

def remplir(t,n):
    for i in range(n):
        t[i] =int(input("Entrez un entier: "))

def affichage(t,n):
    for i in range(n):
        print(t[i],end=" ")

def PremPosMin(t,n,d):
    Pm=d
    for i in range(d+1,n):
        if t[i]<t[Pm]:
            Pm=i
    return Pm

def TriSelect(t,n):
    for i in range(n-1):
        PPM=PremPosMin(t,n,i)
        if PPM!=i:
            x=t[i]
            t[i]=t[PPM]
            t[PPM]=x


n=saisie()
t=[0]*n
remplir(t,n)
print("Ici votre tableau non trieé :")
affichage(t,n)
TriSelect(t,n)
print("Ici votre tableau trieé :")
affichage(t,n)

