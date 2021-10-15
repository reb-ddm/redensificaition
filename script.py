import wandb
import streamlit as st

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


uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg']) 
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)