import os
import pyaes

## Função para descriptografar o arquivo
def decrypt_file(encrypted_file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(encrypted_file_name, "rb") as file:
            file_data = file.read()

        # Inicializar o AES com a chave fornecida
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(encrypted_file_name)

        # Criar o arquivo descriptografado
        decrypted_file_name = encrypted_file_name.replace(".ransomwaretroll", "")
        with open(decrypted_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo descriptografado salvo como: {decrypted_file_name}")

    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

if __name__ == "__main__":
    encrypted_file_name = "teste.txt.ransomwaretroll"
    
    # Chave de descriptografia (deve ser a mesma usada para criptografar)
    key = b"testeransomwares"

    decrypt_file(encrypted_file_name, key)
