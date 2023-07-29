import openai
import cv2
from PIL import Image
import os
import requests

#set openai api key and model
openai_credentials_file=open("SECRET.txt","r")
key=openai_credentials_file.readline().split(" ")[0]
openai_credentials_file.close()
openai_model="gpt-3.5-turbo"
openai.api_key = key

while True:
    user_input=input("What chemistry operations do you want to perform: ")
    prompt_text="I am going to give you chemistry instructions and I want you to tell me what happens when I mix them as if I actually were. Describe what is happenning as it is happening. I want you to also give me a visual description in a few words of what the reaction is so that I can imagine it. Seperate the visual description from the text description with a : and make sure to keep the visual description extremely short if possible ex <eliphant toothpaste>. Here is what the user does- "+user_input+"\n"
    completion=openai.ChatCompletion.create(
            model=openai_model,
            messages=[{"role": "user", "content": str(prompt_text)}],
    )
    filtered_text=completion.choices[0].message.content
    print(filtered_text)
    print(filtered_text.split(":")[0])
    image_prompt=filtered_text.split(":")[1]
    response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="512x512"#"1024x1024"#"512x512"
    )
    image_url = response['data'][0]['url']
    url = image_url
    response = requests.get(url)
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    img = cv2.imread('image.jpg')
    cv2.imshow('image',img)
    cv2.waitKey(0)
