from collections import namedtuple

struct_pessoa = namedtuple('struct_pessoa', ['nome', 'idade'])

def pedestruct():
    nome = input("Introduza o nome: ")
    idade = input("Intoduza a idade: ")
    return struct_pessoa(nome=nome, idade=idade)

pessoa = pedestruct()

print("Nome: " + pessoa.nome + ".")
print("Idade: " + pessoa.idade + ".")

exit