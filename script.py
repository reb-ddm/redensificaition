import os
import wandb
import streamlit as st
import requests
from PIL import Image, ImageDraw
import json
from dotenv import load_dotenv

# environment variables in the file ".env"
load_dotenv()


prediction_key = os.environ.get("prediction_key")
prediction_base_url = os.environ.get("prediction_base_url")

##weights & biases
# wandb.login()
# # 1. Start a W&B run
# wandb.init(project='redensificaition', entity='redensificators')

# # 2. Save model inputs and hyperparameters
# config = wandb.config
# config.learning_rate = 0.01

# # Model training here

# # 3. Log metrics over time to visualize performance
# wandb.log({"loss": 0.1})
st.write("Hello world")

# file uploader
uploaded_file = st.file_uploader("Upload Files", type=['png', 'jpeg'])
if uploaded_file is not None:
    # request prediction by our AI model on Azure
    # prediction key and URL are in the .env file
    content_type = "application/octet-stream"

    headers = {'content-type': content_type, 'Prediction-Key': prediction_key}
    r = requests.post(prediction_base_url, data=uploaded_file, headers=headers)
    response = r.json()

    # open image and draw the predicted labels
    im = Image.open(uploaded_file)
    d = ImageDraw.Draw(im)
    imagex = im.size[0]
    imagey = im.size[1]
    for prediction in response['predictions']:

        if(prediction['probability'] > 0.2):

            left = prediction['boundingBox']['left']
            top = prediction['boundingBox']['top']
            width = prediction['boundingBox']['width']
            height = prediction['boundingBox']['height']

            topleft = (left*imagex, top*imagey)
            bottomright = ((left+width)*imagex, (top+height)*imagey)

            line_color = (255, 0, 0)

            #d.line([top, left, right, top], fill=line_color, width=2)
            d.rectangle([topleft, bottomright], outline=line_color, width=2)
            # #d.text(position, string, options)
    # show image
    st.image(im)
    # print actual response from model (for debugging)
    st.write(r.content)
