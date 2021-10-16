# redensificAItion

## How to run the application

First you need to set the environment variables `prediction_key` and `prediction_base_url` in the `.env` file. You can find them on Azure when you publish a Custom Vision model.

Then run `streamlit run script.py`.

## Usage

You can choose a file, which gets sent to Azure for labeling. Then the predicted labels are shown on the browser.

## How to install wandb (not necessary at the moment)

Install with `pip install wandb` and login by running
```
import wandb
wandb.login()
```
and then paste the API key, which you can find under `wandb.ai/settings`