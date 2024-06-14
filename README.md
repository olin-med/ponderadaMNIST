


# Aplicação Web MNIST

Este projeto é uma aplicação web simples que usa um modelo convolucional treinado para reconhecer dígitos numéricos escritos à mão. A aplicação consiste em um backend construído com FastAPI que fornece duas rotas: uma para predizer o dígito a partir de uma imagem enviada e outra para exibir uma página HTML com um formulário para upload de imagens.

## Estrutura do Projeto

- `main.py`: Contém as rotas da API.
- `templates/`: Pasta para armazenar o arquivo HTML.
- `static/`: Pasta para armazenar arquivos estáticos, como imagens, CSS, etc.
- `model/`: Pasta onde você armazena o seu modelo treinado.

## Pré-requisitos

Certifique-se de ter o Python 3.7+ instalado em sua máquina. Você pode verificar a versão do Python instalada usando:

```bash
python --version
```

## Instalação

1. Clone este repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/digit-recognizer.git
cd digit-recognizer
```

2. Instale as dependências necessárias:

```bash
pip install fastapi uvicorn jinja2 tensorflow numpy opencv-python
```

3. Coloque seu modelo treinado na pasta `model/` e renomeie para `modelo.h5` (ou ajuste o nome no código).

## Execução

Para executar o servidor, use o seguinte comando:

```bash
uvicorn main:app --reload
```

Isso iniciará o servidor FastAPI na porta 8000. Você pode acessar a aplicação no seu navegador em `http://localhost:8000`.

## Uso

- Acesse `http://localhost:8000` para visualizar a página HTML com o formulário para upload de imagens.
- Envie uma imagem de um dígito manuscrito através do formulário para ver o dígito reconhecido.

Este projeto foi desenvolvido por Ólin Medeiros Costa
