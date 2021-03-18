# https://www.youtube.com/watch?v=5PusmXfZBKo
def soma_2_numeros(a,b):
    print(f"a soma dos dois numeros é: {a + b}")

def soma_3_numeros(a, b, c):
    print(f"a soma dos tres numeros é: {a + b + c}")

soma_2_numeros(41,1)
soma_3_numeros(39,1,2)

####
def soma(*numeros): #valores arbitrários #quem manda é o operador (*)
    print(sum(numeros))

soma(20, 22)
soma(39, 10, 25)
soma(10, 20, 31, 44)
soma(11, 25, 30, 41, 55)
soma(1, 2, 3, 4, 5, 6, 7, 8, 9 ,10)

#### 
def f(*args):
    print(f"\nargs = {args}") #armazena o conteudo da variavel args (cria uma tupla)
    for arg in args:
        print(arg)

f()
f(1)
f(1,2)
f(1, 2 , 3)
f("São Paulo", "Rio de Janeiro")

### 
def filmes_favoritos(*filmes):
    print("\n Meus Filmes Favoritos:")
    for i, filme in enumerate(filmes, start=1):
        print(f"\t{i}. {filme}")

filmes_favoritos("Velozes e Furiosos", "Carros", "Toy Story")
filmes_favoritos("Chamado da Floresta", "Star Wars")

### 
def filmes_favoritos(nome, *filmes):
    print(f"\nOs Filmes favoritos do(a) {nome}:")
    for i, filme in enumerate(filmes, start=1):
        print(f"\t{i}. {filme}")

filmes_favoritos("Brutus", "Jumanji", "Rambo", "Hora do Rush")
filmes_favoritos("Gertrudes", "Xuxa, na terra dos baixinhos", "Angry Birds", "Borat", "Matrix")

### Entendendo o ***Kwargs
def f(**kwargs):
    print(f"\nkwargs = {kwargs}") #kw = keyword
    for key, value in kwargs.items():
        print(key, value)
f()
f(nome="Bruno")
f(nome= "Bruno", idade=35)
f(nome= "Bruno", idade=35, area=["Devops", "Infra", "Python", "Segurança"])

### Usando o kwargs
def favoritos(nome, **kwargs):
    print(f"\nOs favoritos do(a) {nome}:")
    for key, value in kwargs.items():
        print(f"\t- {key.capitalize()}: {value}")

favoritos("Bruno", artista="Jeremy Camp", musica="I Still believe")
favoritos("Vanessa", filme="Mulan", artista="Pitty", comida="Frango com Quiabo"),
favoritos(
    "Abigail",
    Linguagem="Python",
    Filme="Sonic",
    comida="Batata Frita",
    bebida="Leitinho"
) 

## 
def f(x, *args, **kwargs):
    print(f"x = {x}\nargs = {args}\nkwargs = {kwargs}")

f(1, 2, 3, y=4, z=5)

### Dá para usar *args e **kwargs juntos
### Mas não dá para fazer de qualquer jeito # Tem a ordem certas, args antes de kwargs
perfil = { 
    "nome": "Bruno",
    "idade": 35
}
print(perfil)
def f(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
## unpacking
f(**perfil)

#####
filmes = ["Rocket Science", "Thumbsucker"]

print(*filmes)
#Na prática, é isso que acontece:print("Rocket Science", "Thumbsucker")

def f(*args):
    for arg in args:
        print(arg)
f(*filmes)

#####
lista = [1, 2, 3, 4]
primeiro, *o_que_sobrou = lista

print(primeiro)
print(o_que_sobrou)

####
lista = [1, 2, 3, 4]
primeiro, o_que_sobrou = lista[0], lista[1:]

print(primeiro)
print(o_que_sobrou)

######
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

primeiro, *elementos_do_meio, ultimo = lista

print(primeiro)
print(elementos_do_meio)
print(ultimo)

#### Assuntos próximos
def f(pos1, pos2, /, pos_or_kwd,*,kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)

f(1,2, pos_or_kwd=3, kwd1=4, kwd2=5)