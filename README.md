# Desafio do Santander Bootcamp Cibersegurança #2 - Ransomware na Prática com Python

Este repositório contém um script Python para criptografar arquivos, simulando o comportamento de um ransomware.

## Como Funciona
O script utiliza a biblioteca `pyaes` para criptografar um arquivo com AES no modo CTR. O arquivo original é removido e substituído por uma versão criptografada com a extensão `.ransomwaretroll`.

## Requisitos
- Python 3.x
- Biblioteca `pyaes` (instale com `pip install pyaes`)

## Como Usar
1. Coloque o arquivo que deseja criptografar (ex: `teste.txt`) no mesmo diretório do script.
2. Execute o script:
   ```bash
   python encrypt.py
