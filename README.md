# Projeto de Gerência de Carros

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5)](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Contribuições](https://img.shields.io/badge/Contribuições-Bem--vindo-brightgreen)](#-como-contribuir)

Um sistema simples e eficaz para **cadastro, visualização e gerenciamento de carros**, desenvolvido com **Python** e **HTML**.  
Ideal para aprendizado de desenvolvimento web full-stack.  

---

## Funcionalidades

- ➕ Cadastro de carros (marca, modelo, ano etc.)  
- 📋 Listagem de carros cadastrados  
- 🖊️ Edição de informações  
- ❌ Exclusão de registros  
- 👤 Sistema de autenticação de usuários (accounts)  
- 🖼️ Upload e exibição de imagens dos carros  

---

## Como rodar o projeto localmente

1. Clone este repositório
```bash
git clone https://github.com/doug-oliver/carros.git
cd carros


2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instale as dependências
pip install -r requirements.txt

4. Execute as migrações
python manage.py migrate

5. Inicie o servidor
python manage.py runserver

Agora acesse em: http://127.0.0.1:8000/


## Como Contribuir

Contribuições são super bem-vindas!
Para contribuir:

Faça um fork do projeto 🍴

Crie uma branch para sua feature/bugfix

git checkout -b minha-feature


Commit suas alterações

git commit -m "Adiciona nova funcionalidade X"


Faça push para a branch

git push origin minha-feature


Abra um Pull Request
