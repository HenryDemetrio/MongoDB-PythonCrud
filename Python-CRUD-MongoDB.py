#pip install pymongo no terminal

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.Contatos

def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('|21960562  -  Izabelle Vitoria dos Santos                     |')
    print('|22010597  -  Henry Demetrio                                  |')
    print('|21943063  -  Maria Helena Siqueira dos Santos                |')
    print('|                                                             |')
    print('|                                                             |')
    print('| versão 2.0 de 12/06/2022                                    |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')


def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)

        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True

    return txt


def opcaoEscolhida(mnu):
    print()

    nroDaOpc = 1
    for opc in mnu:
        print(nroDaOpc, ') ', opc, sep='')
        nroDaOpc += 1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', [str(opc) for opc in range(1, len(mnu) + 1)])


def incluir(agd):
    digitouDireito = False
    while not digitouDireito:
        nome = input('Digite o nome da pessoa que deseja incluir nesta agenda.  ')
        pessoa = db.pessoas.find_one({'name': nome})
        if pessoa != None:
            print('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito = True

    aniversario = input('Aniversário: ')
    endereco = input('Endereço...: ')
    telefone = input('Telefone...: ')
    celular = input('Celular....: ')
    email = input('e-mail.....: ')

# Inserindo no banco UMA pessoa
    db.pessoas.insert_one({"name": nome, "birthday": aniversario,  "address": endereco, "phone": telefone,  "phone_n": celular, "email": email })


def procurar(agd):
    digitouDireito = False
    while not digitouDireito:
        nome = input('Qual a pessoa que esta procurando? :  ')
        procurado = db.pessoas.find_one({'name': nome})
    # Se procurado esta vazio, significa que esta pessoa nao esta banco
        if procurado == None:
            print('Pessoa não encontrada, favor redigitar...')
        else:
            digitouDireito = True
   # Caso contrario, imprime as informacoes do procurado
    print('\nNome:', procurado['name'])
    print('\nAniversário:', procurado['birthday'])
    print('\nEndereço:', procurado['address'])
    print('\nTelefone:', procurado['phone'])
    print('\nCelular: ', procurado['phone_n'])
    print('\ne-mail:', procurado['email'])



def atualizar(agd):
    digitouDireito = False
    while not digitouDireito:
        nome = input('\nDigite o nome da pessoa que deseja atualizar o cadastro:  ')
        procurado = db.pessoas.find_one({'name': nome}, {'_id':0})
        if procurado == None:
            print('Pessoa não encontrada, favor redigitar...')
        else:
            digitouDireito = True
  # imprimindo as informacoes do procurado
    print('\nNome:', procurado['name'])
    print('\nAniversário:', procurado['birthday'])
    print('\nEndereço:', procurado['address'])
    print('\nTelefone:', procurado['phone'])
    print('\nCelular: ', procurado['phone_n'])
    print('\ne-mail:', procurado['email'])

    menu = ['Atualizar Nome',
            'Atualizar Aniversário',
            'Atualizar Endereço',
            'Atualizar Telefone',
            'Atualizar Celular',
            'Atualizar e-mail',
            'Finalizar']
    opcao = None
    while opcao != 7:
        opcao = int(opcaoEscolhida(menu))
    # Atualizando cada opcao escolhida
        
        if opcao == 1:
            nom = input("Digite um novo nome ")
            db.pessoas.update_one({'name': nome}, {"$set": {'name': nom}})
        elif opcao == 2:
            anv = input("Digite a nova data de aniversario ")
            db.pessoas.update_one({'name': nome}, {"$set": {'birthday': anv}})
        elif opcao == 3:
            end = input("Digite o novo endereço: ")
            db.pessoas.update_one({'name': nome}, {"$set": {'address': end}})
        elif opcao == 4:
            tel = input("Digite o novo numero de telefone: ")
            db.pessoas.update_one({'name': nome}, {"$set": {'phone': tel}})
        elif opcao == 5:
            cel = input("Digite o novo numero de celular: ")
            db.pessoas.update_one({'name': nome}, {"$set": {'phone_n': cel}})
        elif opcao == 6:
            email = input("Digite o novo e-mail: ")
            db.pessoas.update_one({'name': nome}, {"$set": {'email': email}})
    print('Contato atualizado!')

def listar(agd):
    # alocando pessoas do banco na variavel people
    people = db.pessoas.find({}, {'_id': 0})
    if people != None:
        # para cada pessoa em people, listar
        for pessoas in people:
            print(pessoas)

    else:
        print('Nenhuma pessoa cadastrada.')


def excluir(agd):
    digitouDireito = False
    while not digitouDireito:
        nome = input('\nDigite o nome da pessoa que deseja excluir: ')
        procurado = db.pessoas.find_one({'name': nome}, {'_id': 0})
        if procurado == None:
            print('Pessoa não encontrada, favor redigitar...')
        else:
            digitouDireito = True
    print('\nNome: ', procurado['name'])
    print('\nAniversário: ', procurado['birthday'])
    print('\nEndereço: ', procurado['address'])
    print('\nTelefone: ', procurado['phone'])
    print('\nCelular: ', procurado['phone_n'])
    print('\ne-mail: ', procurado['email'])

    resposta = umTexto('Deseja realmente excluir? ', 'Você deve digitar S ou N', ['s', 'S', 'n', 'N'])

    if resposta in ['s', 'S']:
        # atribuindo o nome para a varivel excluido
        excluido = nome
        # removendo o dado desejado
        db.pessoas.delete_one({'name': excluido})
        print("Contato excluido com sucesso!")
    else:
        print("Nao foi possivel fazer a excluir!")


apresenteSe()

agenda = []

menu = ['Incluir Contato',
        'Procurar Contato',
        'Atualizar Contato',
        'Listar Contatos',
        'Excluir Contato',
        'Sair do Programa']

opcao = None
while opcao != 6:
    opcao = int(opcaoEscolhida(menu))

    if opcao == 1:
        incluir(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)

print('OBRIGADO POR USAR ESTE PROGRAMA!')