#objetivo: Gerar um código que simula uma concessionária, com compra, aluguel e venda de veiculos

#primeiramente criei um dicionário de carros, com  marca dele, depois os modelos e preços
#esse é o dicionário de compra
TABELA_FIPE = {
    "porsche": {
        "911 carrera s": 1162000.00,
        "911 turbo s": 1950000.00,
        "911 gt3": 1920000.00,
        "taycan turbo s": 12500000.00,
        "mascan t": 625000.00,
        "macan eletric": 560000.00,
        "cayenne e-hybrid": 815000.00,
        "cayenne turbo gt": 1631000.00,
        "718 cayman gt4": 1523000.00,
        "panamera 4s e-hybrid": 1212000.00
    },
    "bmw": {
        "320i m sport": 346900.00,
        "m3 competition": 894950.00,
        "x1 sdrive20i": 330950.00,
        "x5 xdrive50e": 859950.00,
        "x7 m60i": 1026000.00,
        "m2 coupe": 683950.00,
        "i7 xdrive60": 1373000.00,
        "ix m60": 1101000.00,
        "z4 m40i": 624950.00,
        "serie 8 gran coupe": 999000.00
    },
    "audi": {
        "a3 sedan": 289990.00,
        "rs3 sedan": 659990.00,
        "rs6 avant performace": 1251000.00,
        "q3 sportback": 353990.00,
        "q5 tfsle": 480990.00,
        "q8 e-tron": 729990.00,
        "e-tron gtr": 769990.00,
        "rs q8": 1295000.00,
        "q6 e-tron": 529990.00,
        "a5 sportback": 360990.00
    },
    "mercedes-benz": {
        "classe a 200 amg": 376900.00,
        "c 300 amg line": 450000.00,
        "e 300 eexclusive": 589900.00,
        "g 63 amg": 1989900.00,
        "amg gt 63 e-performace": 1967000.00,
        "glc 300 matic": 539000.00,
        "gle 45d": 844900.00,
        "eqs sedan": 1453000.00,
        "sl 63 amg roadster": 1750000.00
    },
    "ferrari": {
        "roma spider": 3850000.00,
        "296 gtb": 3999000.00,
        "sf90 stradale": 6900000.00,
        "purosangue": 7200000.00,
        "812 comptizione": 6500000.00,
        "f8 tributo": 4200000.00,
        "portofino m": 7900000.00,
        "12cilindri": 5500000.00,
        "daytona sp3": 15000000.00,
        "296 gts": 4300000.00
    },
    "volkswagen": {
        "polo gts": 155000.00,
        "golf gti": 320000.00,
        "virtus exclusive": 154000.00,
        "jetta gli": 254000.00,
        "t-cross highline": 180000.00,
        "taos highline": 215000.00,
        "tiguan allspace": 285000.00,
        "id.4": 330000.00,
        "id.buzz (kombi)": 450000.00,
        "touareg r-hybrid": 650000.00
    },
    "toyota": {
        "corolla xre": 158000.00,
        "corolla cross xre": 178000.00,
        "hillux srx": 324000.00,
        "sw4 diamnond": 433000.00,
        "yaris hatch xls": 122000.00,
        "yaris sendan xls": 127000.00,
        "rav4 hybrid": 349000.00,
        "gr corolla": 416000.00,
        "carmy hibrid": 360000.00,
        "prius hybrid": 280000.00
    }
}

TABELA_ALUGUEL = {
    "porsche": {
        "718 boxter style edition (conversivel)": 1800.00,
        "cayne couple platinum": 1400.00,
        "panamera platinum edition": 1600.00,
        "macan started (entrada)": 900.00
    },
    "bmw": {
        "z4 sdrive30i (conversivel)": 1300.00,
        "x3 m400i (suv esportivo)": 1100.00,
        "serie 4 cabrio": 1450.00,
        "i4 edrive35 (eletrico)": 1000.00
    },
    "audi": {
        "q7 55 tfsi (7 lugares)": 1200.00,
        "a5 cabriolet": 1350.00,
        "tt rs coupe": 1700.00,
        "q8 55 tfsi": 1500.00
    },
    "mercedes-benz": {
        "classe v (vans de luxo)": 1100.00,
        "glb 200 (7 lugares)": 850.00,
        "cle coupe (lançamento)": 1400.00,
        "eqe suv (eletrico luxo)": 1600.00
    },
    "ferrari": {
        "california t": 4500.00,
        "488 gtb": 6000.00,
        "gtc4lusso (4 lugares)": 5500.00
    },
    "volkswagen": {
        "amarock v6 extreme": 750.00,
        "id. buzz (kombi eletrica)": 950.00,
        "nivus highline": 400.00,
        "tiguan r-line": 600.00
    },
    "toyota": {
        "hillux gr-sport": 800.00,
        "corolla croos hibryd": 500.00,
        "sw4 gr-sport (7 lugares)": 950.00,
        "rav4 plug-in hybrid": 700.00
    }
}

TABELA_DESEJO = {
    "porsche": {
        "911 s/t (edição 60 anos)": 2500000.00,
        "918 spider": 12000000.00,
        "mission x (conceito)": 15000000.00 
    },
    "bmw": {
        "3.0 csl (ultra limitada)": 4500000.00,
        "m5 touring (lançamento)": 1100000.00,
        "m4 csl": 1300000.00 
    },
    "audi": {
        "r8 v10 gt rwd (o ultimo r8)": 2100000.00,
        "rs6 gt (edição especial de colecionador)": 1400000.00,
        "rs e-tron gt ice race edition": 900000.00
    },
    "mercedes-benz": {
        "mercedes-amg one (motor de formula 1)": 25000000.00,
        "project mybach": 5000000.00,
        "g-class ev (eqg)": 1200000.00 
    },
    "ferrari": {
        "f40 (clássica)": 18000000.00,
        "leferrari": 22000000.00,
        "ferrari monza sp2": 12500000.00
    },
    "volkswagen": {
        "golf r 333": 450000.00,
        "xl1": 1000000.00,
        "id. gti concept": 350000.00
    },
    "toyota": {
        "lfa (lexus/toyota)": 8000000.00,
        "supra mk4 (reliquia)": 800000.00,
        "gr super sport": 10000000.00
    }
}

# Mantenha os dicionários como estão
inventario = {}
ultimo_id_inventario = 0
vendedor = {} 
cliente = {} 

print("===== BEM VINDO A CONCESSIONÁRIA DOS UCHIHAS =====")

# Colocamos um loop para garantir o cadastro
while True:
    try:
        pessoa = int(input("Você é um vendedor ou um cliente da loja? (1 para cliente | 2 para vendedor): "))

        if pessoa == 1:
            print("\n===== CADASTRO CLIENTE =====")
            cliente = {
                "nome": input("Nome: "),
                "email": input("Email: "),
                "saldo": float(input("Saldo atual (R$): "))
            }
            print("\nCliente Cadastrado com sucesso!")
            break # Cadastro feito, sai do loop

        elif pessoa == 2:
            print("\n===== CADASTRO VENDEDOR =====")
            vendedor = {
                "nome": input("Nome: "),
                "email": input("Email: "),
                "id": int(input("ID do vendedor: "))
            }
            print("\nVendedor cadastrado com sucesso!")
            break # Cadastro feito, sai do loop

        else:
            print("Opção não encontrada, tente novamente (1 ou 2).")
            
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

# As funções de menu estão PERFEITAS, não precisa mexer:
def menu_cliente():
    print("\n===== MENU DO CLIENTE =====")
    print("1- comprar carro")
    print("2- alugar carro")
    print("3- ver preços dos carros")
    print("4- vender carro para a loja")
    print("5- voltar ao menu principal")

def menu_vendedor():
    print("\n===== MENU VENDEDOR =====")
    print("1- registrar carro novo no estoque")
    print("2- consultar tabela FIPE")
    print("3- ver inventário da loja")
    print("4- voltar ao menu inicial")
    print("5- sair")

    
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
                        escolha_marca, modelo_real = mostrar_marcas_e_modelos(TABELA_FIPE, cliente['saldo'])

                        # cálculo do preço final
                        preco_base = TABELA_FIPE[escolha_marca][modelo_real]
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
                                    del TABELA_FIPE[escolha_marca][modelo_real]
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
                        marca_alugar, modelo_real = mostrar_marcas_e_modelos(TABELA_ALUGUEL, cliente['saldo'])

                        #pega o valor da diária do aluguel do carro
                        preco_dia = TABELA_ALUGUEL[marca_alugar][modelo_real]

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
                        for marca, modelos in TABELA_FIPE.items():
                            print(f"marca: {marca}")
                            modelos_lista = list(modelos.keys())
                            for i, modelo in enumerate(modelos_lista, start=1):
                                print(f"{i} - {modelo} | R$ {modelos[modelo]:.2f}")

                        print("\n===== TABELA DE PREÇOS - ALUGUEL (por dia) =====\n")
                        #Mostra o preço dos carros disponíveis para o aluguel
                        for marca, modelos in TABELA_ALUGUEL.items():
                            print(f"\nMarca: {marca}")
                            modelos_lista = list(modelos.keys())
                            for i, modelo in enumerate(modelos_lista, start=1):
                                print(f"{i} - {modelo} | R$ {modelos[modelo]:.2f} por dia")

                    case 4:#aqui o cliente escolhe vender o carro para a loja
                        print("===== VENDA DE CARRO PARA A LOJA =====")
                        print("\nConfira as marcas de carros que desejamos comprar:")

                        # usar a função para escolher marca e modelo
                        while True:
                            escolha_marca, modelo_real = mostrar_marcas_e_modelos(TABELA_DESEJO)
                            if escolha_marca is not None:
                                break  # marca válida, sai do loop

                        # cálculo do valor
                        preco_base = TABELA_DESEJO[escolha_marca][modelo_real]
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
                                if marca not in TABELA_FIPE:
                                    TABELA_FIPE[marca] = {}
                                
                                TABELA_FIPE[marca][modelo] = preco
                                del inventario[escolha]
                                
                                print(f"\nCarro {marca} {modelo} registrado com sucesso oficialmente na loja de carros!")
                            else:
                                print("\nID inválido!")

                    case 2:#consulta o preço de todos os carros da loja
                        print("===== CONSULTA TABELA FIPE =====")
                        for marca, modelos in TABELA_FIPE.items():
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