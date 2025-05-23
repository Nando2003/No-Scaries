import re
import json
import requests
from typing import TypedDict
from django.conf import settings


class HuggingFaceServiceResponse(TypedDict):
    classification: str
    suggestion_response: str


class HuggingFaceService:    
    
    API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
    
    DEFAULT_TEXT = (
        "Você é um assistente de atendimento de uma empresa do setor financeiro.\n"
        "Analise o e-mail abaixo e retorne duas informações:\n\n"
        "1. Classificação do e-mail: indique se o e-mail é \"Produtivo\" ou \"Improdutivo\".\n"
        "- Considere como \"Produtivo\" todo e-mail que solicita uma informação, esclarecimento, suporte, resolução de problema, envio de documento, atualização de status, ou qualquer mensagem que exija resposta, ação ou providência da equipe. Mesmo que os dados estejam incompletos, ainda assim é produtivo.\n"
        "- Considere como \"Improdutivo\" apenas mensagens de agradecimento, felicitação, confirmação sem perguntas, ou mensagens que não demandam ação ou resposta da equipe.\n\n"
        "2. Sugestão de resposta: escreva uma resposta profissional adequada para esse e-mail.\n\n"
        "Importante: Ao redigir a sugestão de resposta, não utilize o nome do cliente, remetente ou destinatário. Quando necessário, use apenas o termo [CLIENTE], [REMETENTE] ou [DESTINATARIO] no lugar do nome.\n\n"
        "Responda usando o seguinte formato JSON:\n"
        "{{\n"
        '  "classificacao": "<Produtivo ou Improdutivo>",\n'
        '  "resposta": "<Sugestão de resposta aqui>"\n'
        "}}\n"
        "E-mail:\n"
        "{EMAIL}"
    )
    
    def __init__(self, clean_body: str):
        self.clean_body = clean_body
    
    def get_response(self) -> dict:
        headers = {
            "Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"
        }
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": self.DEFAULT_TEXT.format(EMAIL=self.clean_body)
                }
            ],
            "model": "deepseek/deepseek-v3-0324",
        }
        
        response = requests.post(self.API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]
    
    def parse_response(self, response: dict) -> HuggingFaceServiceResponse:
        content = response['content']
        json_str = re.sub(r"^```json|```$", "", content, flags=re.MULTILINE).strip()

        data = json.loads(json_str)

        classification = data['classificacao']
        suggestion_response = data['resposta']
        
        return HuggingFaceServiceResponse(
            classification=classification,
            suggestion_response=suggestion_response
        )
    