import random

def jogar():
    print("*" * 20)
    print("Jogo da Forca")
    print("*" * 20)

    # Lista de palavras e escolha aleatória
    palavras = ["Banana Prata"]
    palavra_secreta = random.choice(palavras).lower()
    
    # Cria a visualização inicial: ['_', '_', '_']
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0
    max_tentativas = 6

    print(f"Palavra: {' '.join(letras_acertadas)}")

    while not enforcou and not acertou:
        chute = input("\nQual letra? ").strip().lower()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {max_tentativas - erros} tentativas.")

        enforcou = erros == max_tentativas
        acertou = "_" not in letras_acertadas
        
        print(" ".join(letras_acertadas))

    if acertou:
        print("\nParabéns, você ganhou! 🏆")
    else:
        print(f"\nGame Over! A palavra era: {palavra_secreta} 💀")

if __name__ == "__main__":
    jogar()