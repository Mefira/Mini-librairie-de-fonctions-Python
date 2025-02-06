# Importation des bibliothèques utiles
import calendar
from math import sqrt

# Fonction qui affiche le calendrier du moi d'une annee donnée

def calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    cal = calendar.month(year, month)
    print(cal)

# Fonction qui pour résoudre une équation du second degré
def quadratic():

    # Saisie des valeur
    print('Entrez le coefficient de degre 2')
    a=float(input("> "))
    while a==0:
        print("Le coefficient de degre 2 doit etre non nul")
        a=float(input("> "))
    print('Entrez le coefficient de degre 1')
    b=float(input("> "))
    print('Entrez le coefficient de degre 1')
    c=float(input("> "))
    
    # Calcul du discriminant
    delta=b**2-4*a*c

    # Deux solutions réelles
    if delta>0:
        sol1,sol2=(-b- sqrt(delta))/2*a,(-b+ sqrt(delta))/2*a
        print(f"L'equation admet deux solution x1={sol1} et x2={sol2}")

    # Une solution réelle double  
    elif delta==0:
        sol=-b/2*a
        print(f"L'equation admet une solution double, x0={sol}")
    
    #Deux solutions complexes
    else:
        im_part=sqrt(abs(delta))/2*a
        real_part=-b/2*a
        print(f"L'equation admet deux solutions complexes x1={real_part}+{im_part}i et x2={real_part}-{im_part}i")
        
# Fonction de permutation sans valeur tempon

def permutation(a,b):
    b,a=a,b
    print("Apres permutation")
    print(f"a={a}")
    print(f"b={b}")

#Fonction qui décide si un nombre est premier ou pas

def prime(n):
    divider=0           # valeur de décision
    # vérification de primalité
    if n == 1:                  # cas n=1
        print(f"{n} n'est pas un nombre premier")
    else:                       # cas n différent de 1
        for i in range(2, n//2+1):
            if n%i==0:
                divider=i
                break
        
        # Vérification de la valeur de décison après le test
        if divider:
            print(f"{n} n'est pas un nombre premier car {divider} est l'un de ses diviseurs")
        else:
            print(f"{n} est un nombre premier")

# Autre version
def chek_prime(n):
    divider=0           # valeur de décision

    # vérification de primalité
    if n == 1 or n==0:                  # cas n=1
        divider=1
    else:                       # cas n différent de 1
        for i in range(2, n//2+1):
            if n%i==0:
                divider=i
                return divider
    return divider

# Fonction qui affiche les n premiers nombres premiers

def first_prime(n):
    list = []
    i=1
    while len(list) < n:
        if chek_prime(i)==0:
            list.append(i)
        i = i+1
    print(f"Voici la liste des {n} premiers nombres premiers")
    print(list)

#The fibonacci function (version recursive)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    elif n > 1:
        return fibonacci(n-2)+fibonacci(n-1)

# nombre d'amstrong

def amstrong(n):
    number=str(n)
    number_digits=len(number)
    amstrong_number=0
    for i in number:
        amstrong_number+=int(i)**number_digits
    return amstrong_number == n

# Function qui affiche les n premier nombres d'amtrongs

def first_amstrong(n):
    list=[]
    i=0
    while len(list) < n:
        if amstrong(i):
            list.append(i)
        i+=1
    print(f"Voici la liste des {n} premiers nombres d'amstrong.")
    print(list)

#Fonction qui calcule le PPCM de deux entiers

def ppcm(a,b):
    i = 2
    multiples = []
    if a >= b:
        temp = b
        multiples.append(a)
    else:
        temp = a
        multiples.append(b)
    ppcm=temp
    while(True):
        for multiple in multiples:
            if multiple == ppcm:
                return ppcm
        multiples.append(multiples[0]*i)
        ppcm += temp
        i+=1

# Une autre version plus optimale
def ppcm_optimal(a , b):
    if a > b :
        greater=a
    else:
        greater=b
    tem=greater
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater+=tem

#PGCD de deux entiers

def pgcd(a,b):
    if a <= b :
        lower = a
    else:
        lower = b
    if a % lower == 0 and a % lower == 0:
        return lower
    i = lower//2+1
    while i:
        if a % i == 0 and b % i == 0:
            return i
        i-=1

# Function which convert decimal to binary

def binary(n):
    quotient = n
    number=''
    while quotient:
        number=str(quotient%2)+number
        quotient = quotient//2
    return int(number)

# Function which convert decimal to octal
def octal(n):
    quotient = n
    number=''
    while quotient:
        number=str(quotient % 8) + number
        quotient = quotient//8
    return int(number)

# Function which convert decimal to hexa
def hexa(n):
    quotient = n
    number=''
    while quotient:
        remainder=quotient%16
        if remainder < 10:
            number = str(remainder) + number
        else:
            match remainder:
                case 10:
                    number='A'+number
                case 11:
                    number="B"+number
                case 12:
                    number="C"+number
                case 13:
                    number='D'+number
                case 14:
                    number = 'E'+number
                case 15:
                    number = 'F'+number
        quotient = quotient//16
    return number

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]
sentence=[]

def affichage():
    for i in subjects:
        for j in verbs:
            for k in objects:
                print(f"{i} {j} {k}")


# Fonction de saisie d'un entier qui retourne l'entier saisie
def saisie_entier():
    print("Entrer un entier ")
    a=input("> ")
    while not a.isdigit():
        print("Veillez saisir une valeur entiere")
        a=input("> ")
    return int(a)


#Fonction qui calcule le factoriel d'un entier (Version recursive)
def factoriel(n):
    if n <= 1:
        return 1
    elif n > 1:
        return factoriel(n-1)*n

# Notion de recherche binaire
# Rechecherche optimisee dans un tableau (trié ou non) en utulisant la recherche binaire
def recherche(tableau, cible):
    tableau_tri=sorted(tableau)
    debut,fin = 0 , len(tableau)-1
    milieu=(debut+fin)//2
    while debut <= fin:
        milieu = (debut+fin) // 2
        if tableau_tri[milieu] == cible:
            return True
        elif tableau_tri[milieu] < cible:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return False        # La fonction renvoit True si l'element est dans le tableau et False sinon

# Recherche optimisée de l'indice d'un element dans une tableau trié
def recherche_indice(tableau, cible):
    debut,fin = 0 , len(tableau)-1
    milieu=(debut+fin)//2
    while debut <= fin:
        milieu = (debut+fin) // 2
        if tableau[milieu] == cible:
            return milieu
        elif tableau[milieu] < cible:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1