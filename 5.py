def inverter_string(s):
    # Inicializa uma variável para armazenar a string invertida
    string_invertida = ""

    # Itera pelos caracteres da string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]

    return string_invertida


# Entrada do usuário
entrada = input("Digite uma string para inverter: ")

# Chama a função e exibe o resultado
resultado = inverter_string(entrada)
print("String invertida:", resultado)