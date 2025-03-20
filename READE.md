# Análise de Complexidade Ciclomática

Este script utiliza a biblioteca `lizard` para calcular a complexidade ciclomática do código-fonte Java.

## 📌 Pré-requisitos

Antes de executar o script, certifique-se de que possui:

- Python 3 instalado
- O pacote `lizard` instalado

### 🔹 Instalando o `lizard`

Caso ainda não tenha o `lizard`, siga um dos métodos abaixo:

#### 🔹 MacOS
##### Opção 1: Usando Homebrew
```bash
brew install lizard
```
##### Opção 2: Usando pip (Recomendado)
```bash
python3 -m venv ~/venv  # Criar ambiente virtual (opcional)
source ~/venv/bin/activate  # Ativar ambiente virtual
pip install lizard  # Instalar lizard
```

#### 🔹 Windows
##### Opção 1: Usando pip
1. Abra o Prompt de Comando (cmd) ou PowerShell.
2. Execute:
   ```bash
   python -m venv venv  # Criar ambiente virtual (opcional)
   venv\Scripts\activate  # Ativar ambiente virtual
   pip install lizard  # Instalar lizard
   ```
##### Opção 2: Instalando diretamente
1. Abra o Prompt de Comando (cmd) ou PowerShell.
2. Execute:
   ```bash
   pip install lizard
   ```

#### 🔹 Linux
##### Opção 1: Usando gerenciador de pacotes
- Para distribuições Debian/Ubuntu:
  ```bash
  sudo apt install lizard
  ```
- Para distribuições baseadas em Arch Linux:
  ```bash
  sudo pacman -S lizard
  ```
##### Opção 2: Usando pip
```bash
python3 -m venv ~/venv  # Criar ambiente virtual (opcional)
source ~/venv/bin/activate  # Ativar ambiente virtual
pip install lizard  # Instalar lizard
```

## 🚀 Como executar o script

1. Salve o código Python fornecido em um arquivo, por exemplo, `detalhe_funcao_complexidade_ciclomatica.py`.
2. No terminal, execute:
   ```bash
   python3 detalhe_funcao_complexidade_ciclomatica.py
   ```

## 📂 Personalização

Se desejar analisar outro arquivo, edite a variável `file_path` no script para o caminho do arquivo desejado.

## 🏆 Saída esperada

O script exibirá no terminal a complexidade ciclomática de cada função, ordenada da mais complexa para a menos complexa.

---

📢 **Observação:** Caso tenha problemas ao executar, verifique se o Python e o `lizard` estão corretamente instalados. Se precisar de ajuda, me avise! 🚀

