def is_palindrome(phrase):
    normalized_phrase = ''.join(char.lower() for char in phrase if char.isalnum())
    return normalized_phrase == normalized_phrase[::-1]

def main():
    user_input = input("Digite uma frase para verificar se é um palíndromo: ")
    if is_palindrome(user_input):
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")

if __name__ == "__main__":
    main()