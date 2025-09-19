# 🎯 Build Docker image for diseases classification from symptoms
This repository contains the code to build a Docker Image, which will then be deployed to IBM Cloud. Model can predict cattle disease from symptoms.

# Prerequisites
Make sure you have installed Docker on your local machine.

# ⚙️ Steps
- Clone the repository
  ```sh
  git clone https://github.com/FajarRamadhanBBX/deploy-model-disease-classification
  ```
- Build te Image
  ```sh
  docker build -t disease-classification-from-symptoms:latest .
  ```  
- Verify the Image
   ```sh
   docker images
   ```
   You should see disease-classification-from-symptoms with the tag latest in the list.
