import os
import openai
import json
import textwrap
import re
from time import time,sleep



def open_file(filepath) :
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
        

openai.api_key = open_file('openaiapikey.txt')




def gpt3_completion(prompt, engine='test-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequently_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'] [0] ['text'].strip()
    return text
        
if __name__ == '__main__':
    prompt = 'write a list of famous cties in India'
    response = gpt3_completion(prompt)
    print(response)
    