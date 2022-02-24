!bin/bash

# activating environment and install dependencies
source .venv/bin/activate
pip install -r requirements.txt

# creating the file with infrastructure configurated
cdk synth

# call the user credentials profile
export AWS_PROFILE=diegopmayer

# deploying infrastructure
cdk bootstrap --force
cdk deploy