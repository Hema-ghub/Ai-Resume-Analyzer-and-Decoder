import ollama
import os

res = ollama.chat(
    model="llava:7b",
    messages=[
       {'role':'User',
        'content': 'See the image and summarize it',
        'image':['./image1.jpg']
        }
    ]
)

print(res['message']['content'])
