# redensificAItion

## Dependencies

You need Python3 and pip.

Install dependencies with:

```
pip install streamlit
pip install python-dotenv
```

To install streamlit with windows we suggest to use the anaconda terminal.

[more information](https://docs.streamlit.io/library/get-started/installation)

## How to run the application

First you need to set the environment variables `prediction_key` and `prediction_base_url` in the `.env` file. You can find them on Azure when you publish a Custom Vision model.

Then run `streamlit run script.py`.

## Features

You can choose a file, which gets sent to a published Azure Custom Vision model for labeling. Then the predicted labels are shown in the app. In order to choose the model that will be used by the program, the `.env` file has to be updated with the right URL and prediction key.

It only shows the labels with a probability greater than 20%.
