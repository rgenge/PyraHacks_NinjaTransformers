#This program takes a screenshot of a website does ocr on the image and then uses chatgpt to summarize
import easyocr
import cv2
import numpy as np
import tkinter as tk
import pyautogui
import time
import openai
import os

# Initialize the EasyOCR object
ocr = easyocr.Reader(['en'],gpu=False)

#check for openai credentials
if os.path.exists("SECRET.txt")==False:
    openai_credentials_file=open("SECRET.txt","w")
    openai_credentials_file.write("PUT OPENAI_API_KEY HERE")
    openai_credentials_file.close()
    print("Enter your openai api key in the openai_credentials.txt file and then run this program again.")
    exit()
else:
    pass

#set openai api key and model
openai_credentials_file=open("SECRET.txt","r")
key=openai_credentials_file.readline().split(" ")[0]
openai.api_key = key
openai_model="gpt-4"#"gpt-3.5-turbo"
text_display=""

def main():
    global ocr
    global text_display

    #create tkinter gui
    root = tk.Tk()
    root.title("OCR")
    root.geometry("400x230")
    root.geometry("+0+0")

    #make button for screenshot summary to run_functions with args
    button = tk.Button(root, text="Screenshot Summary", command=run_functions)
    button.pack()

    #Text Box to display
    textbox_text=tk.StringVar()
    textbox_text.set("Summary: ")
    textbox = tk.Text(root, height=10, width=50)
    textbox.pack()
    def update_textbox():
        textbox_text.set(text_display)
        textbox.delete('1.0', tk.END)
        textbox.insert(tk.END, textbox_text.get())
        root.after(1000, update_textbox) 
    update_textbox()

    #display the tkinter gui
    root.mainloop()



def run_ocr(image):
    global ocr
    result = ocr.readtext(image)
    text = ""
    for i in result:
        text += i[1] + " "
    return(text)

def run_summary(text):
    print(text)
    global openai_model
    prompt_text="I am going to give you text and I want you to give the best summary that you can. Some of this will be gibberish but that is okay do your best. Here is the text to summarize into a very brief 1-2 sentances at most: "+str(text) +"\n And now your extremely short summary: "
    completion=openai.ChatCompletion.create(
        model=openai_model,
        messages=[{"role": "user", "content": str(prompt_text)}],
    )
    return(completion.choices[0].message.content)

def take_screenshot():
    image = pyautogui.screenshot()
    image = np.array(image)
    image[0:250,0:410]=0
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite('screenshot.jpg', image)
    return('screenshot.jpg')

def run_functions():
    global text_display
    image=take_screenshot()
    ocr_text=run_ocr(image)
    text_display=run_summary(ocr_text)
    print(text_display)

if __name__ == "__main__":
    main()
    print("Done!")