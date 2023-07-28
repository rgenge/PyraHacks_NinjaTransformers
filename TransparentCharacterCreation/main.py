import openai
import cv2
from PIL import Image


#set openai api key and model
openai_credentials_file=open("SECRET.txt","r")
key=openai_credentials_file.readline().split(" ")[0]
openai_credentials_file.close()
openai.api_key = key


while (True):
    character=input("Enter the prompt for your character or type q to quit: ")
    if character=="q":
        exit()
    #openai image generator
    prompt_text=character+", White Background, Character with white background"
    print(prompt_text)
    response = openai.Image.create(
        prompt=prompt_text,
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

    img=Image.open("image.jpg").convert("RGBA")
    datas=img.getdata()
    newData=[]
    for item in datas:
        if (item[0] in list(range(200, 256)) and item[1] in list(range(200, 256)) and item[2] in list(range(200, 256))):
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save("image.png","PNG")

    

    cv2.imshow("image",cv2.imread("image.jpg"))
    cv2.waitKey(0)