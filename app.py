# application that can take the image as an input . we write a prompt and the LLM should\
#connect the prompt with image and then generate the output

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # enable the local environment variables..
from PIL import Image # this will store image

# configure genai
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# designing the webpage
st.header('image-caption-generator',divider='green')
user_input = st.text_input("input prompt: ")
file_upload = st.file_uploader('upload the image..',type = ['JPG','JPEG','PNG'])

# display the image
if file_upload is not None:
    img = Image.open(file_upload)
    st.image(img,caption="image uploaded",use_column_width=True)


# create a button
submit = st.button('do the magic')


# create a function for response

def gemini_response(user_input,img):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    if user_input != "":
        response = model.generate_content([user_input,img])
    else:
        response = model.generate_content(img)
    return response.text
if submit:
    response =  gemini_response(user_input= user_input , img=img)
    st.subheader('the response is :',divider=True)
    st.write(response)
        
