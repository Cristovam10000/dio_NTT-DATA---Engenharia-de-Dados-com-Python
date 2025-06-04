def exibir_mensagem():
    print("olá mundo")

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}")

def exibir_mensagem_3(nome="cris"):
    print(f"seja bem vindo {nome}")    

exibir_mensagem()

exibir_mensagem_2(nome="cris")
# ou
exibir_mensagem_2("cris")

# se eu não passo nada
exibir_mensagem_3()

# se eu passo alguma coisa
exibir_mensagem_3("bitrick")

# ///////////////////////////////////////////////////////////////////////

def  calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor,sucessor

print(calcular_total([10, 20, 34]))
print(retornar_antecessor_e_sucessor(10))

# ///////////////////////////////////////////////////////////////////////

def func_3():
    print("olá mundo")

print(func_3())

# ///////////////////////////////////////////////////////////////////////

def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

salvar_carro("fiat", "palio", "1999", "ABC-1234")
salvar_carro(marca="fiat", modelo="palio", ano="1999", placa="ABC-1234")
salvar_carro(**{'marca': "fiat", 'modelo':"palio", 'ano':"1999", 'placa':"ABC-1234"})
# ///////////////////////////////////////////////////////////////////////

# *args
# os valores vem em uma tubpla
# **keargs
# valores vão ser recebidos por meio de um dicionario

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados ="\n".join([f'{chave.title()}: {valor}' for chave, valor  in kwargs.items()]) 
    mensagem = f'{data_extenso} \n\n {texto}\n\n{meta_dados}'
    print(mensagem)

# valor serparado por virgula é tupla 
exibir_poema('zen of python', 'beatifullis better than ugly.', autor='tim Peters', ano=1999) 

# ///////////////////////////////////////////////////////////////////////

# depois da "/" pode definir o nome ou so posição
def salvar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

salvar_carro("palio", "1999", "ABC-1234", marca="fiat", motor="1.0", combustivel="gasolina" )

def criar_carro (*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="fiat", ano=1990, placa="ABC-1234", marca= "fiat", motor="1.0", combustivel="gasolina")

# ///////////////////////////////////////////////////////////////////////

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'p resultado da operação {a} + {b} = {resultado}')

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

op = somar 

print(op(1, 23))

# ///////////////////////////////////////////////////////////////////////

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))