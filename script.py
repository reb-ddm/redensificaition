import wandb

wandb.login()
# 1. Start a W&B run
wandb.init(project='redensificaition', entity='redensificators')

# 2. Save model inputs and hyperparameters
config = wandb.config
config.learning_rate = 0.01

# Model training here

# 3. Log metrics over time to visualize performance
wandb.log({"loss": 0.1})
