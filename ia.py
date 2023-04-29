import openai

def get_gpt3_response(prompt):
    openai.api_key = "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"
    
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
