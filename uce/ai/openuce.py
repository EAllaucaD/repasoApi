import openai
from pydantic import BaseModel

openai.organization = 'org-2wJUCGKBvFD1KsyjlmtDw8yo'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'programacion'


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programación universitaria, proporciona una explicación
            al tema que se te proporcione
      
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
