Prediction of Air Pollution Using Machine Learning

Overview
--------
This project is a web-based application developed using Django and Machine Learning techniques to predict Air Quality Index (AQI) based on real-world air pollution data. The system analyzes various pollutant parameters and classifies air quality levels such as Good, Moderate, Poor, and Severe.

This project demonstrates the integration of data science, machine learning, and full-stack web development.

--------------------------------------------------

Technologies Used
-----------------
• Python  
• Django Framework  
• Machine Learning (Linear Regression)  
• Pandas, NumPy, Scikit-learn  
• HTML, CSS, JavaScript  
• CanvasJS for charts  
• SQLite Database  

--------------------------------------------------

Air Pollution Parameters
------------------------
The prediction model uses the following pollutants:

• PM2.5  
• PM10  
• NO  
• NO2  
• NOx  
• NH3  
• CO  
• SO2  
• O3  
• Benzene  
• Toluene  
• Xylene  

These values are used to calculate AQI and predict pollution severity.

--------------------------------------------------

Project Features
----------------
• User Registration and Login  
• Service Provider (Admin) Login  
• Dataset Upload and Training  
• Air Quality Prediction  
• Pollution Severity Classification  
• Graphical Visualization (Charts)  
• Prediction Ratio and Accuracy Analysis  
• Download Trained Dataset  

--------------------------------------------------

Project Folder Structure
------------------------
Prediction_of_Air_Pollution  
│  
├── prediction_of_air_pollution   (Django settings and configuration)  
├── Remote_User                   (User module)  
├── Service_Provider              (Admin / Service Provider module)  
├── Template                      (HTML templates)  
├── screenshots                   (Application screenshots)  
├── Air_Pollution_Datasets.csv    (Dataset)  
├── db.sqlite3                    (Database)  
├── manage.py                     (Django entry file)  

--------------------------------------------------

Screenshots
-----------
All application screenshots such as:
• Login Page  
• Registration Page  
• Dashboard  
• Training & Testing Results  
• Charts & Graphs  
• Prediction Output  

are available inside the **screenshots/** folder of this repository.

--------------------------------------------------

How to Run the Project
---------------------
Step 1: Install Python (3.10 or above)

Step 2: Install required libraries
pip install django pandas numpy scikit-learn

Step 3: Apply migrations
python manage.py migrate

Step 4: Load dataset into database
python manage.py shell
from Remote_User.load_dataset import run
run()
exit()

Step 5: Run the server
python manage.py runserver

Step 6: Open browser
http://127.0.0.1:8000/

--------------------------------------------------

Use Case
--------
This system can be used by students, researchers, and environmental analysts to study air pollution trends and predict air quality using machine learning.

