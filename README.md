# Projeto Flask - IMC

Este projeto é uma atividade desenvolvida para o curso de **Informática para Internet** do Instituto Federal do Ceará (IFCE).

## Descrição

Aplicação web simples utilizando Python e Flask para calcular o IMC (Índice de Massa Corporal) do usuário. O sistema possui páginas dinâmicas e utiliza formulários para entrada de dados.

## Funcionalidades
- Página inicial com formulário para entrada de peso e altura
- Cálculo do IMC e exibição do resultado
- Página do autor com informações acadêmicas e profissionais

## Estrutura do Projeto
```
flask-u1-t1/
├─ app/
│  ├─ controllers/
│  │  └─ __init__.py
│  │  └─ AutorController.py
│  │  └─ ResultadoController.py
│  │  └─ StaticController.py
│  ├─ models/
│  │  └─ __init__.py
│  │  └─ Resultado.py
│  └─ views/
│     ├─ autor/
│     │  └─ autor.html
│     ├─ index/
│     │  └─ index.html
│     └─ resultado/
│        └─ resultado.html
│  └─ __init__.py
├─ static/
│  └─ css/
│     └─ style.css
├─ app.py
└─ README.md

```

## Como executar
1. Crie e ative um ambiente virtual: (Se for preciso)
	```powershell
	python -m venv venv
	.\venv\Scripts\Activate
	```
2. Instale as dependências:
	```powershell
	pip install flask
	```
3. Execute a aplicação:
	```powershell
	python app.py
	```
4. Acesse no navegador:
	- [http://127.0.0.1:5000/index](http://127.0.0.1:5000/index)

## Autor
- Nome: [Vanágila Xavier Rodrigues]
- Curso: Informática para Internet
- Instituição: Instituto Federal do Ceará

---
Atividade prática de desenvolvimento web com Flask.
# flask-u1-t1