#### Classes - Didática Tech
# https://www.youtube.com/watch?v=RhtsCbKyYoA 

def teste(v,i):
    valor = v
    incremento = i
    resultado = valor + incremento
    return resultado

a = teste(10,1)
print(f"o resultado da função é: {a}")
# print(resultado) # Vai dar erro, pois resultado está dentro da função

# Classes e métodos
# funcoes normalmente são escritas usando bva_teste

class BvaTeste:  #a boa prática é utilizar nomes de Classe iniciando com letras maiusculas em cada Palavra;
    def incrementa(self, v, i):  # self: 
        valor = v
        incremento = 1
        resultado = valor + incremento
        return resultado

a = BvaTeste()

b = a.incrementa(10,1)
print(f"o resultado da classe com os valores é: {b}")

# Quando temos uma função dentro de uma classe, isso é chamado de método
# self = a variavel toma o valor da função

class BvaTeste:
    def incrementa(self, v, i):
        self.valor = v
        self.incremento = 1
        self.resultado = self.valor + self.incremento
        return self.resultado

a = BvaTeste()

b = a.incrementa(10,1)
print(f"Resultado usando o parametro self dentro do método: {b}")
#print(f"Resultado da classe: {a.valor}")

# usar parametros dentro da classe para outras funções
class BvaTeste:
    def __init__(self, v: int, i: int):     # __init__ é chamado de método construtor, porque ele define os valores iniciais dos nossos atributos
        self.valor = v
        self.incremento = i
    def incrementa(self):
        # self.valor = self.valor + self.incremento
        self.valor += self.incremento   #forma mais "bonita" de usar incremento

a = BvaTeste(10, 1)
a.incrementa()
a.valor
print(f"Valor de a após rodar a classe é: {a.valor}")
a.incrementa()
a.valor
print(f"Agora após rodar mais uma vez a função incrementa o valor de a é: {a.valor}")

b = BvaTeste(20,2)
b.incrementa()
b.valor
print(f"O valor de b, com valores diferentes de é a, é: {b.valor}")

class BvaTeste:
    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor += self.incremento

a = BvaTeste()
a.incrementa()
a.valor
print(f"O valor padrão passado na classe é: {a.valor}")

# Depois de instanciarmos a = BvaTest(), quando executarmos a.incremento()
# o que o interpretador está fazendo é:
# BvaTeste().incremento(a, 10, 1)

# Objeto > Métodos: *Compartilhados com todos os objetos criados a 
# partir da mesma classe

# Atributos: *Não compartilhados com outros objetos criados a partir
# da mesma classe

# Métodos representam o comportamento
# Atributos representam o estado

class BvaTest:
    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v
    def incrementa(self):
        self.valor = self.valor + self.incremento
    def verifica(self):
        if self.valor > 12:
            print("Ultrapassou 12")
        else:
            print("Não ultrapassou 12")
    def exponencial(self, e):
        self.valor_exponencial = self.valor**e
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)

a = BvaTest()
a.incrementa()
a.verifica()
a.exponencial(3)
a.valor_exponencial
a.incrementa_quadrado()
a.valor
print(f"O valor de a.valor é:{a.valor} e seu exponencial é: {a.valor_exponencial}")

# Heranca
class Calculos(BvaTest):
    pass

c = Calculos()
c.incrementa()

print(f"O valor de c é: {c.valor}")

class Calculos(BvaTest):
    def decrementa(self):
        self.valor -= self.incremento

c = Calculos()
c.incrementa()

c.decrementa()
print(f"o valor de c agora é: {c.valor}")

### Definir novos valores com uma nova classe;

class Calculos(BvaTest):
    def __init__(self, d=5): #por termos colocado esse init, ele está sobreescrevendo, então, não está trazendo lá da classe anterior;
        super().__init__() # Chamando o método init da sua classe BvaTest
        self.divisor = d
    def decrementa(self):
        self.valor -= self.incremento
    def divide(self):
        self.valor = self.valor/self.divisor

c = Calculos()
c.incrementa()
print(f"O valor de c, na nova classe, agora é:{c.valor}")
c.decrementa()
print(f"O valor de c, na nova classe, agora é:{c.valor}")
c.divide()
print(f"O valor de c, na nova classe, agora é:{c.valor}")

