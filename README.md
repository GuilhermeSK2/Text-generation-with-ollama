# Geração de Texto com Ollama API

Este projeto Python fornece um script simples para interagir com a API local do Ollama, permitindo a geração de texto usando modelos de linguagem grandes (LLMs) que você tenha configurado em seu ambiente Ollama. O exemplo demonstra como enviar um prompt ao modelo e receber uma resposta.

## Visão Geral

O Ollama é uma ferramenta que permite executar e gerenciar modelos de linguagem grandes localmente. Este script atua como um cliente básico para a API RESTful do Ollama, facilitando o envio de prompts para um modelo específico (por exemplo, `gemma3:1b`) e a obtenção de suas respostas de forma programática. Isso é ideal para testes rápidos, integrações personalizadas ou construção de aplicações que utilizam LLMs em um ambiente local ou controlado.

## Estrutura do Projeto

* `ollama.py`: O script Python principal que contém a função para interagir com a API do Ollama e um exemplo de uso.

## Tecnologias Utilizadas

* **Python 3**
* **`requests` library**: Para fazer requisições HTTP para a API do Ollama.
* **Ollama**: Servidor local para execução de LLMs.
* **Modelo de Linguagem Grande (LLM)**: Ex. `gemma3:1b` (ou qualquer outro modelo disponível no seu Ollama).

## Pré-requisitos

Antes de executar este script, você precisa ter o Ollama instalado e um modelo de linguagem grande baixado.

1.  **Instale o Ollama:** Siga as instruções de instalação em [https://ollama.com/](https://ollama.com/).
2.  **Baixe um modelo:** Abra seu terminal e use o comando `ollama run` para baixar um modelo. Por exemplo:
    ```bash
    ollama run gemma3:1b
    ```
    Isso iniciará o modelo e o manterá em cache para uso posterior. Você pode sair do prompt do modelo (Ctrl+D) e o servidor Ollama continuará em execução em segundo plano.
    

## Configuração

O script `ollama.py` contém as seguintes variáveis configuráveis:

* `OLLAMA_API_URL`: O endpoint da API do seu servidor Ollama. O padrão é `"http://localhost:11434/api/generate"`. Altere-o se seu servidor Ollama estiver em um endereço ou porta diferente.
* `model_name`: O nome do modelo que você deseja usar para a geração de texto. O padrão é `"gemma3:1b"`. Certifique-se de que este modelo esteja baixado e disponível em seu Ollama.

## Tratamento de Erros

O script inclui tratamento de erros básicos para:

* **`requests.exceptions.ConnectionError`**: Se o script não conseguir se conectar ao servidor Ollama (verifique se o Ollama está em execução).
* **`requests.exceptions.RequestException`**: Para outros problemas de requisição HTTP (como erros 4xx ou 5xx).
