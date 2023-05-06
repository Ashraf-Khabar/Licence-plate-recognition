Project Title: Vehicle License Plate Detection and Recognition Radar
====================================================================

This project aims to enhance road safety and vehicle identification by developing a radar system that utilizes advanced detection technologies to capture real-time images of vehicle license plates and send them to a central database for processing.

Project Overview
----------------

This project consists of two main folders: `model` and `api`. The `model` folder contains a deep learning model created using Python and TensorFlow for license plate detection and recognition. The `api` folder contains the main Flask API, which has several APIs. Each API renders an HTML template with an image input and then tries to fetch the license plate value from an Oracle database to send an email to the vehicle owner and the city of the license plate.

<center><img title="index" alt="Index Page" src="./source/indexPage.PNG" ></center>

Folder Structure
----------------

```
├── 📁 model
│   ├── 📝 License_plate_detection_model.ipynb
│   ├── 📝 License_plate_recognition_model.ipynb
│   ├── 📄 license_plate_detection.h5
│   └── 📄 license_plate_recognition.h5
└── 📁 api
    ├── 📝 main.py
    ├── 📁 templates
    │   ├── 📝 index.html
    │   └── 📝 users.html
    └── 📝 script.sh
    └── 📝 script.sql
 ```

The `model` folder contains two Jupyter notebooks that were used to create the license plate detection and recognition models. The trained models are also included in the `model` folder.

The `api` folder contains the main Flask API, which is located in the `main.py` file. The `templates` folder contains the HTML templates for the web application, and the `config.py` file contains the configuration settings for the API.

Getting Started
---------------

To get started with this project, you'll need to follow the steps below:

1.  Clone the repository to your local machine.
2.  Install the required packages by running `pip install --upgrade --force-reinstall -r requirement.txt` in your terminal.
3.  Start the API by running `python api/main.py` in your terminal.
4.  Access the web application by visiting `http://localhost:5000/` in your browser.

Technologies Used
-----------------

-   Python 🐍
-   TensorFlow 🧠
-   Flask 🌶️
-   Oracle 🔮

Conclusion
----------

This project is a great example of how technology can be used to improve road safety and vehicle identification. By developing a radar system that can detect and recognize license plates in real-time, we can create a safer and more secure environment for drivers and pedestrians alike.
