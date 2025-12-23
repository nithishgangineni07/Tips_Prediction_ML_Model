
🧠 Machine Learning Project

This project demonstrates a complete end-to-end Machine Learning application, including environment setup, backend model training, and frontend deployment using Streamlit.


⚙️ Environment Setup
Step 1: Create Project Folder

Create a main project folder on your PC/Laptop.

mkdir ML_Project
cd ML_Project

Step 2: Create Virtual Environment
python -m venv venv

Step 3: Activate Virtual Environment

Windows

./venv/Scripts/activate

Mac/Linux

source venv/bin/activate

🧩 Backend Setup
Step 4: Backend Folder Structure

Inside the backend folder, create the following:

->data/

 ->load_data.py

->model/

 ->train_model/

->train_save.py

->app.py

requirements.txt

Step 5: Install Backend Dependencies

Navigate to the backend folder and install required libraries:

pip install -r requirements.txt

Step 6: Train and Save the Model

Run the training script to create the .pkl model file:

python train_save.py


This will generate the trained model and save it inside the model folder.

Step 7: Run Backend Application
python app.py

🎨 Frontend Setup (Streamlit)
Step 8: Frontend Folder Structure

Inside the frontend folder, create:

app.py

requirements.txt

Step 9: Install Frontend Dependencies

Navigate to the frontend folder:

->pip install -r requirements.txt

Step 10: Run Streamlit Application

Use the following command to launch the frontend:

->streamlit run app.py

🚀 Technologies Used

->Python

->Machine Learning

->Streamlit

->Virtual Environment (venv)

->Pickle

📌 Notes

Ensure the virtual environment is activated before installing dependencies.

Always install backend and frontend requirements separately.

Run the backend model training before starting the frontend.

🙌 Acknowledgment

This project is part of a structured Machine Learning training program and demonstrates practical implementation of ML concepts from training to deployment.


