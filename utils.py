
import sys

# la foncction qui chiffrer le texte.
def Vchiffrer(m,k,dic,v):
    # print("Input String (m):", repr(m))
    # print("Key String (k):", repr(k))
    k=sup_espace(k)
    d=sup_espace(m)
    c='' 
    s=len(k) 
    try:
        for i in range(len(d)):
            a= (dic[d[i]] + dic[k[i % s]]) % 26
            c= c + v[a] 
            if((i+1)%5==0):
                c=c+' '
            # print(c)
        return c   
    except Exception as e:
        # print(f'Error details: {e}')
        return 'There is an error: ' + str(e)

# la foncction qui déchiffrer le texte.
def Vdechiffrer(c,k,dic,v):
    k=sup_espace(k)
    m=''
    d=sup_espace(c)
    s=len(k)    
    for i in range(len(d)):
        a= (dic[d[i]] - dic[k[i % s]])
        if(a<0):
            a = a+26    
        m= m + v[a]
        if((i+1)%4==0):
            m=m+' '
    return m  

#La Cryptanalyse en utilisant l'indice de coincidence
def cle_coincidence(c,dic,v,lb,ub):
    T=[]
    d=sup_espace(c)
    IC,tab=Cle_size(c,dic,lb,ub)
    
    for i in tab:
        key=''
        for j in range (i):
            N=26*[0]
            for k in range (j,len(d),i):
                N[dic[d[k]]]+=1
            key=key+v[(N.index(max(N))-4)%26]
        T.append(key)
    return T,tab,IC  

#La Cryptanalyse en utilisant la longueur des répétition
def cle_repetition(c,dic,v):
    T=[]
    d=''
    s,compt=Compteur(c)
    for i in c:
        if(i!=' '):
            d=d+i
    for i in s:
        key=''
        for j in range (i):
            N=26*[0]
            for k in range (j,len(d),i):
                N[dic[d[k]]]+=1
            key=key+v[(N.index(max(N))-4)%26]
        T.append(key)
    return T,s  
def sup_espace(m):
    d = ''
    CH = ',;:!?/.+-*)]\\_`)([}{#~\'<>/’,»1234567890|@=¨œ' + '"' + '╔' + "^"
    
    for i in m:
        if i not in CH and i != ' ' and i != '\n' :
            d = d + i
    
    return d


def Indice_Coincidance(c,dic):  
    d=sup_espace(c)
    N=26*[0]
    for i in d:
        N[dic[i]]+=1
    ic=0
    for i in N:
        ic = ic + i*(i-1)
    ic=ic/(len(d)*(len(d)-1) )  
    
    return ic

def permutation(a,b):
    c=a;a=b;b=c
    return a,b


def tri(IC,tab):
    icf=0.074
    for i in range(len(IC)-1):
        for j in range(i+1,len(IC)):
            if(abs(IC[i]-icf)>abs(IC[j]-icf)):
                IC[i],IC[j]=permutation(IC[i],IC[j])
                tab[i],tab[j]=permutation(tab[i],tab[j])
    return IC,tab


def Cle_size(c,dic,lb,ub):
    tab=[]
    IC=[]
    d=''
    for i in c:
        if(i!=' '):
            d=d+i
    for j in range (len(d)-1):
        c_dec=''
        for i in range (0,len(d),j+1):
            c_dec=c_dec + d[i]
        ic=Indice_Coincidance(c_dec,dic)
        #print(ic)
        if (ic>=lb and ic<=ub):
            IC.append (round(ic,4))
            tab.append (j+1)
    IC,tab=tri(IC,tab)            
    return IC,tab


#les fonction de premiere methode


def MinMax(facteur):
    a=1000
    b=0
    for i in range (len(facteur)):
        if(a>min(facteur[i])):
            a=min(facteur[i])
        
        if(b<max(facteur[i])):
            b=max(facteur[i])
    return a,b

def repetition(c):
    c=sup_espace(c)
    chaine=[]
    rep=[]
    pos=[]
    for i in range(3,10):
        for j in range (len(c)-i):
            r=c[j:i+j]
            for k in range(j+i,len(c)-i):
                if(r==c[k:k+i]):
                    chaine.append(r)
                    rep.append(k-j)
                    pos.append(k)
    return   chaine,rep,pos

def decomposition(c):
    chaine,rep,pos=repetition(c)
    facteur=[]
    for n in (rep):
        fact=[]
        d=2
        while n>1:
            while n%d==0:
                if(d not in fact):
                    fact.append(d)
                n=n//d   
            d=d+1
        facteur.append(fact)    
    return facteur   


def FactCom(c):
    facteur=decomposition(c)
    a,b=MinMax(facteur)
    v=[]
    for i in range(a,b):
        for j in range(len(facteur)):
            if(i in facteur[j]):
                if (i not in v):
                    v.append(i)
    return v   
def Tri(IC,tab):
    icf=0.074
    for i in range(len(IC)-1):
        for j in range(i+1,len(IC)):
            if(abs(IC[i]-icf)>abs(IC[j]-icf)):
                IC[i],IC[j]=permutation(IC[i],IC[j])
                tab[i],tab[j]=permutation(tab[i],tab[j])
    return IC,tab

def permutation(a,b):
    c=a;a=b;b=c
    return a,b


def Tri(s,compt): 
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if(compt[i]<compt[j]):
                compt[i],compt[j]=permutation(compt[i],compt[j])
                s[i],s[j]=permutation(s[i],s[j])
    return s,compt


def Compteur(c):
    facteur=decomposition(c)
    s=FactCom(c)
    compt=[]
    for i in s:
        cpt=0
        for j in range(len(facteur)):
            if (i in facteur[j]):
                cpt=cpt+1
        compt.append(cpt)
    Tri(s,compt)  
    try :
        a=[s[0],2*s[0],3*s[0],4*s[0],5*s[0],6*s[0],7*s[0],8*s[0],9*s[0],10*s[0],11*s[0],12*s[0]]
        b=compt[0]
    except:
        a=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
        b=39
    return a,b
