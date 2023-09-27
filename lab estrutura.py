from numpy import sin
from numpy import pi

def minpdec(g,m):
    m = m/60
    g = g+m
    return g

def decpmin(g):
    a = int(g)
    b = (g-int(g))*60
    return [a,int(b)]

def minpdec1(g):
    g = g.split('º')
    g[0] = int(g[0])
    g[1] = g[1].replace("'",'')
    g[1] = int(g[1])
    g[1] = g[1]/60
    num = g[0]+g[1]
    return num

def emrad(g):
    x = g*pi/180
    return x


d = 3.33e-6 #metros

p = ' ' 
nomes = []
graus = []
print('O nome das cores:')
p = input()
while p != '':
    nomes.append(p)
    p = input() # lembre-se q quando acabar os nomes, só clicar Enter
print('Agora as medidas:')
for i in range(len(nomes)):
    p = input()
    graus.append(minpdec1(p))

print()
print('Medidas:')
for i in range(len(nomes)):
    print(nomes[i],graus[i])

print()
print('Agora, as respectivas cores menos os brancos:')
for i in range(len(nomes)):
    print(nomes[i],'menos o branco é:',graus[i]-graus[0])

print()
print('Agora, as respectivas medias das cores:')

lmbs = []
tam = len(nomes)
metade = int((tam-1)/2)
media = [0]*(metade+1)
medias = []
for i in range(1,metade+1):
    media = (abs(graus[i]-graus[0]) + abs(graus[i+metade]-graus[0]))/2
    print('A média entre',nomes[i],'e',nomes[i+metade],'é:',media)
    senom = sin(emrad(media))
    lmb = d*senom/1
    print('O valor de lambda para',nomes[i],'é então:',lmb)
    lmbs.append(lmb) #note q o valor de lambda de nomes[i] vai ser lmbs[i-1]
    medias.append(media)

print()
print('Agora o 1/λ:')
umslmb = []
umsns = []
for i in range(len(lmbs)):
    print('Para',nomes[len(lmbs)-i],'temos 1/λ:',1/lmbs[len(lmbs)-i-1],'n =',i+3,'e',1/(2**2)-1/((i+3)**2))
    umslmb.append(1/lmbs[len(lmbs)-i-1])
    umsns.append(1/(2**2)-1/((i+3)**2))

print('Então, a relação pra achar o R fica: x =',*umsns,', y =',*umslmb)

print('Para o grafico de λ(sen(o)), você usa: x =',*[sin(emrad(i)) for i in medias],', y =',*lmbs)



