# Smart Attendance System using Face Recognition

This is a simple attendance system using face recognition built using Python, Flask, OpenCV, and scikit-learn. The system allows you to:

- Add faces along with their names and roll numbers.
- Record attendance by recognizing faces in real-time.
- View attendance records.

## Features

- **Add Faces**: Add faces along with their names and roll numbers.
- **Record Attendance**: Recognize faces in real-time and record attendance with just one key press.
- **View Attendance Records**: View attendance records for the current date.

[![Watch the video](https://github.com/sachit16/Smart-Attendance-System/blob/main/Smart%20Attendence%20System.mkv)](https://github.com/sachit16/Smart-Attendance-System/blob/main/Smart%20Attendence%20System.mkv)

[<img src="https://github.com/sachit16/Smart-Attendance-System/blob/main/Smart%20Attendence%20System.mkv" width="600" height="300"
/>](https://github.com/sachit16/Smart-Attendance-System/blob/main/Smart%20Attendence%20System.mkv)


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sachit16/Smart-Attendance-System
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

## Usage

### 1. Add Faces

- Navigate to the "Add Faces" page by clicking on the "Add Faces" link in the navigation menu.
- Enter the name and roll number, and follow the instructions to add faces.

### 2. Record Attendance

- Navigate to the "Record Attendance" page by clicking on the "Record Attendance" link in the navigation menu.
- Follow the instructions to record attendance.

### 3. View Attendance Records

- Navigate to the "View Attendance" page by clicking on the "View Attendance" link in the navigation menu.
- View attendance records for the current date.
Sure, here are the technical details for the Attendance System using Face Recognition:

## Technical Details

- **Python**: Python is the primary programming language used in this project.
  
- **Flask**: Flask is a micro web framework written in Python used to develop the web application.

- **OpenCV (cv2)**: OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. In this project, OpenCV is used for face detection, recognition, and capturing video frames.

- **scikit-learn**: scikit-learn is a machine learning library for Python. It provides simple and efficient tools for data mining and data analysis. In this project, scikit-learn is used to train the K-Nearest Neighbors classifier for face recognition.

- **Pickle**: Pickle module is used for serializing and deserializing Python objects. In this project, it is used to save and load face data, labels, and roll numbers.

- **NumPy**: NumPy is a Python library used for numerical computing. In this project, NumPy is used for array manipulation and processing.

- **CSV**: CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. In this project, CSV files are used to store attendance records.

- **win32com.client**: This module provides access to the Windows Component Object Model (COM) and is used to provide text-to-speech functionality.

- **Haar Cascade Classifier**: Haar Cascade Classifier is a machine learning-based approach used for object detection, especially faces. In this project, the Haar Cascade Classifier is used for face detection.

- **HTML/CSS/Bootstrap**: HTML, CSS, and Bootstrap are used for the front-end development of the web application.

- **Jinja2**: Jinja2 is a template engine for Python. In this project, it is used as a template engine for Flask to generate HTML content.

- **DateTime**: The `datetime` module supplies classes for manipulating dates and times. In this project, it is used to get the current timestamp and format it for date and time.

### System Requirements

- **Operating System**: Windows/Linux/macOS
- **Python Version**: Python 3.x
- **Web Browser**: Google Chrome, Mozilla Firefox, Safari, etc.

## Screenshots

![Add Faces](screenshots/add_faces.png)
![Record Attendance](screenshots/record_attendance.png)
![View Attendance](screenshots/view_attendance.png)

## Contributing

Contributions are welcome! Please feel free to open a new issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
