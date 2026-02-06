#objetivo: Gerar um código que simula uma concessionária, com compra, aluguel e venda de veiculos

#primeiramente criei um dicionário de carros, com  marca dele, depois os modelos e preços
#esse é o dicionário de compra
carros = {
    "Porsche": {
        "911 GT3": 1700000.0,
        "Cayenne Turbo": 850000.0,
        "Panamera 4S": 900000.0,
        "Macan GTS": 600000.0,
        "718 Cayman": 500000.0,
        "Taycan Turbo": 1200000.0,
        "911 Carrera": 800000.0
    },
    "audi": {
        "A3 Sedan S-Line": 227383.0,
        "Q3 Prestige": 225084.0,
        "A4 Avant": 240000.0,
        "Q5 Black Edition": 270000.0,
        "A6 Sedan": 350000.0,
        "RS7 Performance": 800000.0,
        "e-tron GT": 650000.0
    },
    "nissan": {
        "GT-R": 700000.0,
        "Frontier Attack": 210000.0,
        "Kicks Exclusive": 120000.0,
        "Sentra SL": 130000.0,
        "Leaf": 180000.0,
        "Versa Advance": 95000.0,
        "X-Trail": 200000.0
    },
    "volkswagen": {
        "Golf GTI": 170000.0,
        "Tiguan R-Line": 220000.0,
        "Nivus Highline": 150000.0,
        "Virtus GTS": 145000.0,
        "T-Cross Comfortline": 135000.0,
        "Passat R-Line": 250000.0,
        "Polo GTS": 140000.0
    }
}
#esse aqui é outro dicionário dessa vez, de alugel, onde o client poderá escolher o carro a ser alugado, com o valor da diária
aluguel ={ 
    "porsche": {
        "718 Cayman S": 9500.0,
        "Macan S": 7600.0,
        "Cayenne Coupé": 8700.0,
        "911 Turbo": 15000.0,
        "Panamera 4 E-Hybrid": 12000.0
    },
    "audi": {
        "A3 Sedan": 850.0,
        "Q3 Performance": 1100.0,
        "A5 Coupé": 1600.0,
        "RS5 Sportback": 4500.0,
        "e-tron quattro": 2300.0
    },
    "nissan": {
        "Kicks Sense": 350.0,
        "Sentra Advance": 420.0,
        "Versa Exclusive": 380.0,
        "Frontier PRO-4X": 900.0,
        "X-Trail Hybrid": 750.0
    },
    "volkswagen": {
        "Golf R": 1800.0,
        "Tiguan Allspace": 900.0,
        "Virtus Highline": 520.0,
        "Nivus Comfortline": 450.0,
        "T-Cross Highline": 600.0
    },
    "bmw":{
        "320i Sport": 1700.0,
        "X1 sDrive": 1400.0,
        "M135i": 2400.0,
        "X3 M40i": 3600.0,
        "M3 Competition": 8000.0
    }
}
#Já ess dicionário é a lista de desejos de carros que a conscessionária deseja ter na loja.
#para o usuário vender somente a lista pré-determinada d carros
carros_desejado = {
    "Porsche": {
        "911 Turbo S": 1750000.0,
        "Cayenne E-Hybrid": 950000.0,
        "Panamera GTS": 1100000.0,
        "Taycan 4S": 1300000.0
    },
    "nissan": {
        "370Z": 250000.0,
        "Navara": 220000.0,
        "Juke Nismo": 140000.0,
        "Note e-POWER": 160000.0
    },
    "audi": {
        "Q7": 420000.0,
        "A5 Sportback": 270000.0,
        "RS6 Avant": 950000.0,
        "e-tron SUV": 680000.0
    },
    "volkswagen": {
        "Arteon": 190000.0,
        "ID.4": 210000.0,
        "Taos": 175000.0,
        "Golf R-Line": 180000.0
    }
}
#aqui foi criado um dicionário chamado inventário, para quando o cliente vender o carro, ele ser movido temporariamente
#para o invetário e depois o vendedor adicioná-lo a loja
inventario ={ }
#Aqui é criado um ID para o carro, para o vendedor poder adicionar o carro a loja principal com uma maior facilidade
ultimo_id_inventario = 0

#esse dois dicionários são responsáveis por armazenar os dados do usuário, ou seja, os dados de vendedor e de cliente que o usuário digitar
vendedor = { } #dados do vendedor logado
cliente = { } #dados do cliente logado

print("===== BEM VINDO A CONCESSIONÁRIA DOS UCHIHAS =====")
#comando para decidir se você vai querer entrar na loja como vendedo ou cliente (apenas uma das opções)
pessoa = int(input("você é um vendedor ou um cliente da loja? (1 para cliente | 2 para vendedor): "))

match pessoa:
    case 1: #caso você escolha 1, faz o cadrastro de cliente
        print("===== CADRASTRO CLIENTE =====")
        cliente ={
            "nome": input("nome: "),
            "email": input("endereço eletrônico (Email): "),
            "saldo": float(input("saldo atual (R$): "))
        }
        print("\nCliente Cadrastrado com sucesso!")

    case 2: #caso escolha 2, faz o cadrastro de vendedor
        print("===== CADRASTRO VENDEDOR =====")
        vendedor ={
            "nome": input("nome: "),
            "email": input("endereço eletrônico (Email): "),
            "id": int(input("ID do vendedor: "))
        }
        print("\nVendedor cadrastrado com sucesso!")

    case _: #caso a opção seja inválida
        print("opção não encontrada, tente novamente")


#aqui é definido o menudo cliente, exibido quando o usuário escolhe o menu cliente
def menu_cliente():
        print("\n===== MENU DO CLIENTE =====")
        print("1- comprar carro")
        print("2 - alugar carro")
        print("3- ver preços dos carros")
        print("4- vender carro para a loja")
        print("5- voltar ao menu principal")
        


#Aqui é defenido o menu do vendedor, exibido quando o usuário escolhe o menu vendedor
def menu_vendedor():
        print("\n===== MENU VENDEDOR =====")
        print(" 1- registrar carro novo no estoque")
        print(" 2- consultar tabela FIPE")
        print(" 3- ver invetário da loja")
        print(" 4- voltar ao menu incial")
        print(" 5- sair")

#aqui é definido a função de escolher o modelo, tanto como número quanto por nome do carro
def escolher_modelo(modelos_lista, mensagem="Escolha um modelo: "):
    modelo_real = None
    while modelo_real is None:
        # aqui é selecionado a entrada do usuário e remove os espaços antes/depois
        modelo_escolhido = input(mensagem).strip().lower()
        
        # Se o usuário digitou um número, verifica se o número é valido na lista
        if modelo_escolhido.isdigit():
            indice = int(modelo_escolhido) - 1 #aqui ajustamos o indice (A lista começa do 0)
            if 0 <= indice < len(modelos_lista):
                modelo_real = modelos_lista[indice] #aqui é selecionado o modelo coreto
            else:
                print("Número inválido, tente novamente.")
        
        # Se digitou o nome, verifica se corresponde a algum modelo que está na lista
        else:
            for m in modelos_lista:
                if m.lower() == modelo_escolhido:
                    modelo_real = m
                    break
                #se não for encontrado nenhum modelo correspodete
            if modelo_real is None:
                print("Modelo não encontrado, digite novamente.")
    return modelo_real #retorna ao modelo escolhido de forma correta

#Essa aqui é a função para mostrar marcas e modelos de um dicionário de carros
def mostrar_marcas_e_modelos(dicionario_carros, saldo_cliente=None):
  
    print("\nTemos essas marcas disponíveis:")
    for marca in dicionario_carros:
        print(f"- {marca}")

    escolha_marca = input("\nQual marca você deseja: ").lower().strip()

    if escolha_marca in dicionario_carros:
        print(f"\nModelos disponíveis da {escolha_marca.capitalize()}:")
        modelos_lista = list(dicionario_carros[escolha_marca].keys())
        for i, modelo in enumerate(modelos_lista, start=1):
            preco = dicionario_carros[escolha_marca][modelo]
            print(f"{i} - {modelo} | R$ {preco:.2f}")

        if saldo_cliente is not None:
            print(f"\nSeu saldo atual é: R$ {saldo_cliente:.2f}\n")

        # usa a função escolher_modelo para validar escolha
        modelo_real = escolher_modelo(modelos_lista, "\nQual modelo você deseja? (nome ou número) ")
        return escolha_marca, modelo_real

    else:
        print("\nMarca não encontrada.")
        return None, None


#Aqui temos a função para escolher a marca
# Essa função permite ao usuário escolher uma marca válida dentro do dicionário de carros
# Recebe o dicionário (carros, aluguel, etc.) e uma mensagem opcional para o input
# Retorna a marca escolhida, já validada
    
def escolher_marca(dicionario_carros, mensagem="Escolha a marca: "):
    while True:
        escolha_marca = input(mensagem).strip().lower() # lê a arca, remove espaços e coloca em minusculos
        if escolha_marca in dicionario_carros: #vereffica se a marca existe no dicionário
            return escolha_marca # retorna com a marca escolhida
        else:
            print("Marca não encontrada. Digite novamente.")

#essas são as listas de marcas
             
#essas são as marcas disponíveis para a compra 
marcas = ["Porsche", "Audi", "Nissan", "Volkswagen"]

#essas são as marcas disponíveis para aluguel
marcas_aluguel =["Porsche", "Audi", "Nissan", "Volkswagen", "BMW"]

#marcas que a concessionária deseja comprar dos clientes
marcas_desejadas =["Porsche", "Audi", "Nissan", "Volkswagen"]

#===== LOOP PRINCIPAL =====

while True:
    pessoa = int(input("escolha o menu: 1 para cliente | 2- para vendedor | 3 - sair do sistema: "))

    #Aqui o cliente é redirecionado ao menu de cliente, onde ele poderá escolher entre as opções
    if pessoa == 1:
        while True: #loop para ficar mostrando as opções para o usuário, do menu clientes
                menu_cliente()
                cliente_1 = int(input("\nescolhe a sua açao por favor: "))#pede ao usuário uma ação, de escolher 1 das opções do menu

                match cliente_1:
                    case 1: #menu de compra
                        print("\n===== MENU DE COMPRA =====")
                        print("\n Nós temos essas marcas disponíveis: ")
                        
                        #mostra as marcas e modelos dispníveis para a compra
                        escolha_marca, modelo_real = mostrar_marcas_e_modelos(carros, cliente['saldo'])

                        # cálculo do preço final
                        preco_base = carros[escolha_marca][modelo_real]
                        preco_final = preco_base * 1.25
                        print(f"\nPreço base: R$ {preco_base:.2f}")
                        print(f"Na nossa concessionária temos um acréscimo de 25% do preço do carro em cima da tabela FIPE.")
                        print(f"Então o valor final do carro {modelo_real} fica: R$ {preco_final:.2f}")

                            # confirmação de compra
                        confirmar = input("\nO senhor(a) ainda deseja comprar o carro? (S/N): ").strip().lower()
                        if confirmar == "s":
                                if cliente["saldo"] >= preco_final:
                                    cliente["saldo"] -= preco_final

                                    #se confirmar, vai remover o carro do estoque
                                    del carros[escolha_marca][modelo_real]
                                    print("\nCompra realizada com sucesso!")
                                    print(f"Saldo restante: R$ {cliente['saldo']:.2f}")
                                    print("\nObrigado por comprar em nossa loja, até mais!")
                                else:
                                    print("\nSaldo insuficiente para essa compra.")
                        else:
                            print("\nCompra cancelada")
          
                    case 2:#menu de aluguel dos veículos
                        print("\n===== MENU DE ALUGUEL =====")
                        print("Carros disponíveis para aluguel:\n")

                        #Aqui vai mostrar as marcas e modelos de carro disponíveis para o aluguel
                        marca_alugar, modelo_real = mostrar_marcas_e_modelos(aluguel, cliente['saldo'])

                        #pega o valor da diária do aluguel do carro
                        preco_dia = aluguel[marca_alugar][modelo_real]

                            # escolher tipo de aluguel
                        print("\n1 - Aluguel diário")
                        print("2 - Aluguel mensal (10% de desconto)")
                        tipo_aluguel = int(input("Escolha o tipo de aluguel: "))

                        if tipo_aluguel == 1:# Aqui o aluguel da diária
                                dias = int(input("Por quantos dias deseja alugar? "))
                                preco_total = preco_dia * dias
                                print(f"\nPreço total por {dias} dias: R$ {preco_total:.2f}")

                        elif tipo_aluguel == 2: #aqui é o aluguel do mês (mensal)
                                preco_original = preco_dia * 30
                                desconto = preco_original * 0.10
                                preco_total = preco_original - desconto

                                print(f"\nAluguel mensal selecionado.")
                                print(f"Preço original: R$ {preco_original:.2f}")
                                print(f"Desconto (10%): R$ {desconto:.2f}")
                                print(f"Preço final: R$ {preco_total:.2f}")

                            # Confirmação se o cliente quer realmente alugar o carro, e confirmação do pagamento
                        confirmar = input("\nDeseja confirmar o aluguel? (S/N) ").strip().lower()
                        if confirmar == "s":
                                if cliente["saldo"] >= preco_total:
                                    cliente["saldo"] -= preco_total
                                    print("\nAluguel realizado com sucesso!")
                                    print(f"Saldo restante: R$ {cliente['saldo']:.2f}")
                                else:
                                    print("\nSaldo insuficiente.")
                        else:
                                print("\nAluguel cancelado.")

                    case 3: #Aqui é o menu de consultar preços
                        print("===== TABELA DE PREÇOS - COMPRA =====")
                        #mostra o preço dos carros disponíveis para a compra
                        for marca, modelos in carros.items():
                            print(f"marca: {marca}")
                            modelos_lista = list(modelos.keys())
                            for i, modelo in enumerate(modelos_lista, start=1):
                                print(f"{i} - {modelo} | R$ {modelos[modelo]:.2f}")

                        print("\n===== TABELA DE PREÇOS - ALUGUEL (por dia) =====\n")
                        #Mostra o preço dos carros disponíveis para o aluguel
                        for marca, modelos in aluguel.items():
                            print(f"\nMarca: {marca}")
                            modelos_lista = list(modelos.keys())
                            for i, modelo in enumerate(modelos_lista, start=1):
                                print(f"{i} - {modelo} | R$ {modelos[modelo]:.2f} por dia")

                    case 4:#aqui o cliente escolhe vender o carro para a loja
                        print("===== VENDA DE CARRO PARA A LOJA =====")
                        print("\nConfira as marcas de carros que desejamos comprar:")

                        # usar a função para escolher marca e modelo
                        while True:
                            escolha_marca, modelo_real = mostrar_marcas_e_modelos(carros_desejado)
                            if escolha_marca is not None:
                                break  # marca válida, sai do loop

                        # cálculo do valor
                        preco_base = carros_desejado[escolha_marca][modelo_real]
                        preco_final = preco_base * 0.88  # desconto de 12%

                        print(f"\nOferta da loja pelo {modelo_real}: R$ {preco_final:.2f} (desconto de 12%)")

                        aceitar = input("Deseja vender o carro por esse valor? (S/N): ").strip().lower()

                        if aceitar == "s": 
                            cliente["saldo"] += preco_final
                            #adicona o carro ao invetário da loja
                            ultimo_id_inventario += 1
                            inventario[ultimo_id_inventario] = {
                                "marca": escolha_marca,
                                "modelo": modelo_real,
                                "preco_compra": preco_final
                            }
                            print(f"\nVenda realizada com sucesso! Seu novo saldo é: R$ {cliente['saldo']:.2f}")
                            print("O veículo foi para o inventário temporário para ser vendido mais tarde!")
                            print("Obrigado por vender seu carro para a nossa concessionária!")
                        else:
                            print("\nVenda cancelada!")

                    case 5:#Volta ao menu de escolha, cliente e vendedor
                        print("\nObrigado por confiar em nossos serviços, até a próxima!")
                        break
                    case _:
                        print("\n comando inválido, tente novamente")

    
    #aqui a pessoa é redirecionada ao menu de vendedor, onde será exigido um código para ser acessado
    elif pessoa == 2:  # Vendedor
        # Se não há vendedor cadastrado, pede cadastro
        if not vendedor:
            print("\nNenhum vendedor cadastrado! Vamos cadastrar agora:")
            vendedor["nome"] = input("Nome do vendedor: ")
            vendedor["email"] = input("Email do vendedor: ")
            vendedor["id"] = int(input("ID do vendedor: "))
            print("\nVendedor cadastrado com sucesso!")

        # Login: pede apenas o ID para confirmação
        while True:
            tentativa = int(input("\nDigite o seu ID de vendedor: "))
            if tentativa == vendedor["id"]:
                print("\nAcesso permitido")
                break  # Sai do loop e vai para o menu do vendedor
            else:
                print("\nID incorreto! Tente novamente.")

        # Menu do vendedor
        while True:
            menu_vendedor()
            vendedor_1 = int(input("\nEscolha a sua ação: "))

            match vendedor_1:
                    case 1: #aqui o vendedor registra o carro na conssecionária
                        print("===== REGISTRAR CARRO =====")
                        
                        if not inventario:
                            print("\nO inventário está vazio")
                        else:
                            print("\nCarros no inventário:")
                            for item_id, info in inventario.items():
                                print(f"{item_id} - {info['marca']} {info['modelo']} | R$ {info['preco_compra']:.2f}")
                            
                            escolha = int(input("\nDigite o ID do carro que quer registrar: "))
                            
                            if escolha in inventario:
                                dados = inventario[escolha]
                                marca = dados["marca"]
                                modelo = dados["modelo"]
                                preco = dados["preco_compra"]
                                
                                #adiciona o carro ao estoque oficalde carros, removendo ele do invetário
                                if marca not in carros:
                                    carros[marca] = {}
                                
                                carros[marca][modelo] = preco
                                del inventario[escolha]
                                
                                print(f"\nCarro {marca} {modelo} registrado com sucesso oficialmente na loja de carros!")
                            else:
                                print("\nID inválido!")

                    case 2:#consulta o preço de todos os carros da loja
                        print("===== CONSULTA TABELA FIPE =====")
                        for marca, modelos in carros.items():
                            print(f"\nMarca: {marca}")
                            for modelo, preco in modelos.items():
                                print(f"- {modelo}: R$ {preco:.2f}")
                                
                    case 3: #mostra o invetário da loja, depois que o cliente vende um carro
                        print("===== INVENTÁRIO LOJA ====")
                        if not inventario: #caso o invetário esteka vazio mostra essa menssagem
                            print("O inventário está vazio!")
                        else:
                            for i, (item_id, dados) in enumerate(inventario.items(), start=1):
                                print(f"{i} - {dados['marca']} | {dados['modelo']} | R$ {dados['preco_compra']:.2f}")
                                
                    case 4:
                        print("Voltando ao menu inicial")
                        break  # sai do menu do vendedor e volta ao menu principal
                        
                    case 5:
                        print("\nSaindo do programa...")
                        exit() #sai do programa encerrando-o
                        
                    case _:
                        print("Opção inválida, tente novamente!")


    #menssagem caso a pessoa queira sair do sistema
    elif pessoa == 3:
        print("\n saindo do sistema... Obrigado e até a próxima!!")
        break
    
    #Caso a pessoa digite um comando que não tenha esse comando, faz com que a pessoa seja redirecionada e possa tentar novamente
    else:
        print("comando não encontrado, tente novamente")