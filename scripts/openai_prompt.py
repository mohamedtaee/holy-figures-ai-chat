import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def ai_prompt(holybook, holyfigure, question):
    prompt = f"""
        Role play as you are {holyfigure} from the {holybook}. Just answer the question and tie it in with a quote from 
        {holybook}. Don't summarize what you are doing. My question is {question}
        """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0,
        top_p=1,
    )

    return response