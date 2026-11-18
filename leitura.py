def conversar():
    fala = input("Você: ").strip().lower()
    encontrou = False

    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if " - " in linha:
                    pergunta, resposta = linha.strip().split(" - ", 1)
                    if fala == pergunta.strip().lower():
                        print(f"Bot: {resposta.strip()}")
                        encontrou = True
                        break

    except FileNotFoundError:
        print("Bot: Meu cérebro está vazio! Me ensine algo primeiro.")
        return

    if not encontrou:
        print("Bot: Desculpe, não sei a resposta. Use a opção 2 para me ensinar.")


def ensinar():
    pergunta = input("Qual pergunta você quer me ensinar? ").strip()
    resposta = input("Qual deve ser a minha resposta? ").strip()

    if pergunta and resposta:
        with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{pergunta} - {resposta}\n")
        print("Bot: Obrigado! Já salvei isso na minha memória.")
    else:
        print("Bot: A pergunta e a resposta não podem ficar vazias.")


def listar_conhecimento():
    base_dados = []
    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Bot: Meu cérebro está vazio! Me ensine algo primeiro.")
        return

    for linha in linhas:
        if " - " in linha:
            dados = linha.strip().split(" - ", 1)
            if len(dados) == 2:
                base_dados.append((dados[0].strip(), dados[1].strip()))

    # Ordena alfabeticamente ignorando maiúsculas e minúsculas
    base_dados.sort(key=lambda item: item[0].lower())

    if base_dados:
        print("O que eu já sei:")
        for pergunta, resposta in base_dados:
            print(f"{pergunta} - {resposta}")
    else:
        print("Bot: Ainda não aprendi nada.")


# Menu principal para manter o chat funcionando
while True:
    print("\n--- MENU DO CHATBOT ---")
    print("1 - Fazer uma pergunta")
    print("2 - Ensinar uma nova resposta")
    print("3 - Ver tudo o que eu já sei")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        conversar()
    elif opcao == "2":
        ensinar()
    elif opcao == "3":
        listar_conhecimento()
    elif opcao == "4":
        print("Bot: Até mais!")
        break
    else:
        print("Bot: Opção inválida. Digite 1, 2, 3 ou 4.")
