import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def generate_text_with_ollama(prompt, model_name="gemma3:1b"):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model_name,
        "prompt": prompt,
        "stream": False # Define como False para obter a resposta completa de uma vez
    }

    try:
        response = requests.post(OLLAMA_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Levanta um erro para status de resposta ruins (4xx ou 5xx)

        result = response.json()
        return result.get("response", "")

    except requests.exceptions.ConnectionError:
        return "Erro: Não foi possível conectar ao servidor Ollama. Certifique-se de que o Ollama está em execução."
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição Ollama: {e}"

conversation = "Você é um assistente útil que responde de maneira clara e objetiva. Cite uma frase de Sócrates."
response_text = generate_text_with_ollama(conversation, model_name="gemma3:1b")

print(response_text.strip())