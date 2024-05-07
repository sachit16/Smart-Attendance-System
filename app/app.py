# app.py

from flask import Flask, render_template, request, redirect, url_for
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
# Import text-to-speech functionality
from win32com.client import Dispatch

# Initialize the Flask application
app = Flask(__name__)

# Function to speak text
def speak(str1):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

# Function to add faces
def add_faces(name,rollno):
    # Open a video capture object using the default camera (0)
    video = cv2.VideoCapture(0)

    # Load the Haar Cascade Classifier for face detection
    facedetect = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')

    # Initialize an empty list to store face data
    faces_data = []

    # Counter to keep track of the number of frames processed
    i = 0

    # Loop to capture video frames and detect faces
    while True:
        # Capture a frame from the video
        ret, frame = video.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        
        # Iterate over detected faces
        for (x, y, w, h) in faces:
            # Crop the face region from the frame
            crop_img = frame[y:y+h, x:x+w, :]
            
            # Resize the cropped face image to 50x50 pixels
            resized_img = cv2.resize(crop_img, (50, 50))

            # Append the resized face image to the faces_data list every 5 frames
            if len(faces_data) <= 5 and i % 5 == 0:
                faces_data.append(resized_img)

            i = i + 1
            cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

        # Display the current frame with annotations
        cv2.imshow("Frame", frame)

        # Wait for a key press or until 5 faces are captured
        k = cv2.waitKey(1)
        if k == ord('q') or len(faces_data) == 5:
            break
        time.sleep(0.2)

    # Release the video capture object and close all windows
    video.release()
    cv2.destroyAllWindows()

    # Convert the list of face images to a NumPy array and reshape it
    faces_data = np.asarray(faces_data)
    faces_data = faces_data.reshape(5, -1)

    # Check if 'names.pkl' is present in the 'Data/' directory
    if 'names.pkl' not in os.listdir('Data/'):
        # If not present, create a list with the entered name repeated 5 times
        names = [name] * 5
        # Save the list to 'names.pkl'
        with open('Data/names.pkl', 'wb') as f:
            pickle.dump(names, f)
    else:
        # If 'names.pkl' is present, load the existing list
        with open('Data/names.pkl', 'rb') as f:
            names = pickle.load(f)
        # Append the entered name 5 times to the existing list
        names = names + [name] * 5
        # Save the updated list to 'names.pkl'
        with open('Data/names.pkl', 'wb') as f:
            pickle.dump(names, f)

    # Check if 'roll_no.pkl' is present in the 'Data/' directory
    if 'roll_no.pkl' not in os.listdir('Data/'):
        # If not present, create a list with the entered name repeated 5 times
        rollnos = [rollno] * 5
        # Save the list to 'names.pkl'
        with open('Data/roll_no.pkl', 'wb') as f:
            pickle.dump(rollnos, f)
    else:
        # If 'names.pkl' is present, load the existing list
        with open('Data/roll_no.pkl', 'rb') as f:
            rollnos = pickle.load(f)
        # Append the entered name 5 times to the existing list
        rollnos = rollnos + [rollno] * 5
        # Save the updated list to 'names.pkl'
        with open('Data/roll_no.pkl', 'wb') as f:
            pickle.dump(rollnos, f)

    # Check if 'faces_data.pkl' is present in the 'Data/' directory
    if 'faces_data.pkl' not in os.listdir('Data/'):
        # If not present, save the NumPy array 'faces_data' to 'faces_data.pkl'
        with open('Data/faces_data.pkl', 'wb') as f:
            pickle.dump(faces_data, f)
    else:
        # If 'faces_data.pkl' is present, load the existing array
        with open('Data/faces_data.pkl', 'rb') as f:
            faces = pickle.load(f)
        # Append the new array 'faces_data' to the existing array
        faces = np.append(faces, faces_data, axis=0)
        # Save the updated array to 'faces_data.pkl'
        with open('Data/faces_data.pkl', 'wb') as f:
            pickle.dump(faces, f)

# Function to record attendance
# Function to record attendance
def record_attendance():
    # Open a video capture object using the default camera (0)
    video = cv2.VideoCapture(0)

    # Load the Haar Cascade Classifier for face detection
    facedetect = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')

    # Load pre-trained face recognition data from pickle files
    with open('Data/names.pkl', 'rb') as w:
        LABELS = pickle.load(w)
    with open('Data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)
    with open('Data/roll_no.pkl', 'rb') as f:
        ROLLNO = pickle.load(f)

    # Print the shape of the Faces matrix
    print('Shape of Faces matrix --> ', FACES.shape)
    print('Shape of Labels --> ', len(LABELS))  # Add this line to print the shape of labels
    print("sizeof the Roll No",len(ROLLNO))
    print("type the Roll No",type(LABELS))
    # Take the minimum number of samples from both FACES and LABELS
    min_samples = min(FACES.shape[0], len(LABELS))
    min_samples1=min(FACES.shape[0], len(ROLLNO))
    FACES = FACES[:min_samples]
    LABELS = LABELS[:min_samples]
    ROLLNO = ROLLNO[:min_samples1]  # Take only required number of samples from ROLLNO

    # Initialize a K-Nearest Neighbors classifier with 5 neighbors
    knn = KNeighborsClassifier(n_neighbors=5)
    knn1 = KNeighborsClassifier(n_neighbors=5)

    # Train the KNN classifier with the loaded face data and labels
    knn.fit(FACES, LABELS)
    

    knn1.fit(FACES, ROLLNO)  # Change FACES to LABELS

    # Define column names for attendance CSV file
    COL_NAMES = ['NAME', 'ROLLNO', 'TIME']

    # Start an infinite loop for real-time face recognition
    while True:
        # Capture a frame from the video
        ret, frame = video.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = facedetect.detectMultiScale(gray, 1.3, 5)

        # Iterate over detected faces
        for (x, y, w, h) in faces:
            # Crop the face region from the frame
            crop_img = frame[y:y+h, x:x+w, :]

            # Resize the cropped face image to 50x50 pixels and flatten it
            resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)

            # Predict the identity of the face using the trained KNN classifier
            output = knn.predict(resized_img)
            
            # Predict the roll number using the second KNN classifier
            rollno_output = knn1.predict(resized_img)

            # Get current timestamp
            ts = time.time()
            date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
            timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

            # Check if an attendance file for the current date already exists
            exist = os.path.isfile("Attendance_" + date + ".csv")

            # Draw rectangles and text on the frame for visualization
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.rectangle(frame, (x, y-50), (x+w, y), (200, 0, 0), -1)
            cv2.putText(frame, str(output[0]), (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
            cv2.putText(frame, str(rollno_output[0]), (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)

            # Create an attendance record with predicted identity and timestamp
            attendance = [str(output[0]), str(rollno_output[0]), str(timestamp)]

        # Display the current frame with annotations
        cv2.imshow("Frame", frame)

        # Wait for a key press
        k = cv2.waitKey(1)

        # If 'o' is pressed, announce attendance and save it to a CSV file
        if k == ord('o'):
            speak(f"{output[0]} Your Attendance Taken Successfully..")
            time.sleep(2)
            if exist:
                # If file exists, append attendance to it
                with open("Attendance_" + date + ".csv", "+a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(attendance)
            else:
                # If file doesn't exist, create it and write column names and attendance
                with open("Attendance_" + date + ".csv", "+a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    writer.writerow(attendance)

        # If 'q' is pressed, exit the loop
        if k == ord('q'):
            break
       

    # Release the video capture object and close all windows
    video.release()
    cv2.destroyAllWindows()

def read_csv(filename):
    records = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)
    return records
# Route to show attendance
@app.route('/show_attendance')
def show_attendance():
    # Get the current timestamp and format it for date
    ts = time.time()
    date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
    # Corrected file name concatenation
    filename = f"Attendance_{date}.csv"  # Using the formatted date in the file name
    # # Assuming the file is generated with this name
    # df = pd.read_csv(filename)
    records = read_csv(filename)
    return render_template('show_attendance.html', records=records)


# Route to add faces
@app.route('/add_faces', methods=['GET', 'POST'])
def add_faces_route():
    if request.method == 'POST':
        name = request.form['name']
        rollno=request.form['rollno']
        add_faces(name,rollno)
        return render_template('successful.html')
    return render_template('add_faces.html')

# Route to record attendance
@app.route('/record_attendance', methods=['GET', 'POST'])
def record_attendance_route():
    # return render_template('record_attendance.html')
    record_attendance()
    return render_template('index.html')

    

# Route to show attendance
@app.route('/')
def index():
    return render_template('index.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
