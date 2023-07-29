import openai
import cv2
from PIL import Image
import os

while True:
    #set openai api key and model
    openai_credentials_file=open("SECRET.txt","r")
    key=openai_credentials_file.readline().split(" ")[0]
    openai_credentials_file.close()
    openai_model="gpt-3.5-turbo"
    openai.api_key = key


    prompt_text="I am making a flashcard game where you will give a randomized middle school biology terminology other than cell then a description for a text to image generator to make it for a flash card. I want you to format this precisely as <TERMINLOGY>:<IMAGEGENERATORPROMPT> without the <>s. Only include those two things in your response, make sure not to suggest any labels as the image generators can't handle that, it should only be symbolic.\n"
    completion=openai.ChatCompletion.create(
            model=openai_model,
            messages=[{"role": "user", "content": str(prompt_text)}],
    )
    filtered_text=completion.choices[0].message.content
    term=filtered_text.split(":")[0]
    im_prompt=filtered_text.split(":")[1]
    #print(term,", ",im_prompt)

    #
    response = openai.Image.create(
        prompt="biology, "+term,
        n=1,
        size="512x512"#"1024x1024"#"512x512"
    )
    image_url = response['data'][0]['url']
    #print(image_url)
    import requests
    url = image_url
    response = requests.get(url)
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    #show response
    img = cv2.imread('image.jpg')
    cv2.imshow('image',img)
    cv2.waitKey(0)

    #get input
    input_text=input("What is this called and what is it's description? or enter q to quit: ")
    if input_text=="q":
        exit()
    else:
        #use chat gpt to score respone
        prompt_text="I am going to give you a description of a Biology terminology and I want you to score it on a scale of 1 to 10 and only return the score /10, ex: <description>\n<score>/10 without the <>s. Only include the score in your response. The term being described is supposed to be "+term+". Here is the description from the user for you to score: "+input_text+"\n"
        completion=openai.ChatCompletion.create(
                model=openai_model,
                messages=[{"role": "user", "content": str(prompt_text)}],
        )
        filtered_text=completion.choices[0].message.content
        print(filtered_text, " Term was ", term)
   
cv2.destroyAllWindows()


