# Attendence-System-using-Facial-Recognition
FaceAttend is a cutting-edge attendance system that utilizes facial recognition technology to mark attendance for students in a university setting. This innovative system ensures accuracy, efficiency, and convenience for both students and administrators.

**Key Features:**

**1**- Facial Recognition: Utilizes face_recognition library to identify students and mark their attendance.
**2**- Real-time Attendance: Marks attendance in real-time, eliminating the need for manual attendance taking.
**3**- Automated Reporting: Generates attendance reports in CSV format, making it easy to track student attendance.
**4**- Department-wise Attendance: Supports multiple departments, allowing for separate attendance tracking and reporting.
**5**- Voice Output: Provides audio feedback for students when their attendance is marked.

**Technology Stack:**

**1**- Backend: Python
**2**- Libraries: face_recognition, OpenCV, pyttsx3
**3**- Database: CSV files

**Installation:**

**1**- Install Python and required libraries: pip install face_recognition opencv-python pyttsx3

**2**- Clone the repository: git clone <repository-url>

**3**- Create a new directory for the project and navigate into it: mkdir FaceAttend && cd FaceAttend

**4**- Run the script: python main.py

**Usage:**

Run the script: python main.py

The system will start capturing video from the default camera.

When a student's face is recognized, their attendance will be marked, and their name will be displayed on the screen.

To mark attendance for all students, press 's' on the keyboard.

To exit the system, press 'l' on the keyboard.

**Note:**

This project requires a dataset of student images for facial recognition. Please ensure that you have a sufficient dataset for accurate recognition.
The system is designed for a university setting, but can be adapted for other use cases with minimal modifications.

**Contributions:**

Contributions to FaceAttend are welcome! Please fork the repository and submit a pull request with any improvements or new features.

**Author:**
Laraib Khalid

I hope this helps
