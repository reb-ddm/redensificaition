import os
import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
import json
from dotenv import load_dotenv

# environment variables in the file ".env"
load_dotenv()


prediction_key = os.environ.get("prediction_key")
prediction_base_url = os.environ.get("prediction_base_url")

st.write("# redensificAItors")
st.write("### Using Azure CustomVision.ai to classify redensification potential zones in aerial images")

# file uploader
uploaded_file = st.file_uploader("Upload Files", type=['png', 'jpeg'])
if uploaded_file is not None:
    # request prediction by our AI model on Azure
    # prediction key and URL are in the .env file
    content_type = "application/octet-stream"

    headers = {'content-type': content_type, 'Prediction-Key': prediction_key}
    r = requests.post(prediction_base_url, data=uploaded_file, headers=headers)
    response = r.json()

    if 'predictions' in response.keys():
        # open image and draw the predicted labels
        im = Image.open(uploaded_file)
        d = ImageDraw.Draw(im)
        imagex = im.size[0]
        imagey = im.size[1]
        for prediction in response['predictions']:

            if(prediction['probability'] > 0.4):

                left = prediction['boundingBox']['left']
                top = prediction['boundingBox']['top']
                width = prediction['boundingBox']['width']
                height = prediction['boundingBox']['height']

                topleft = (left*imagex, top*imagey)
                bottomright = ((left+width)*imagex, (top+height)*imagey)

                colors = {
                    "Untouchable": (255, 0, 0),  # red
                    "Low Redensification Potential":  (255, 165, 0),  # orange
                    # yellow
                    "Medium Redensification Potential": (255, 255, 0),
                    "High Redensification Potential": (2, 156, 7)  # green
                }

                line_color = (hash(prediction['tagName']) & 255, hash(prediction['tagName']) >> 55, hash(
                    prediction['tagName']) & 17592186044415 >> 35)

                rectangle_color = (0, 0, 0)
                if prediction['tagName'] in colors.keys():
                    rectangle_color = colors[prediction['tagName']]
                d.rectangle([topleft, bottomright],
                            outline=rectangle_color, width=6)
                font = ImageFont.truetype("AltoneTrial-Regular.ttf", 50)

        # show image
        st.image(im)
        st.image("colour_legend.png")
    # print actual response from model (for debugging)
    st.write(response)
