![Logo](https://github.com/Safnaj/School-Management-System/blob/master/src/sms/other/img/MainDashboard.jpg)

# Facial Recognition & Identification System
This Repository contain Code for Facial Recognition and Identification using Open CV and Python with tkinter GUI interface.




### DISCRIPTION 
 

- __Facial Recognition & Identification based attendance system__”.
Attendance of students in a large classroom is hard to be handled by the traditional system, as it is time-consuming and has a high probability of error during the process of inputting data into the computer, Our project proposed automated attendance marking system using face recognition technique. The system deployed __Haar cascade classifier__ to find the positive and negative image of the face and __LBPH__ (Local binary pattern histogram) algorithm for face recognition by using python programming and OpenCV library. Here we use the __tkinter__ GUI interface for user interface purpose.


###STATEMENT OF PROBLEM:
- Attendance of students in a large classroom is hard to be handled by the traditional system, as it is time-consuming and has a high probability of error during the process of inputting data into the computer. Our project proposed automated attendance marking system using face recognition technique. RESULT: The system deployed Haar cascade classifier to find the positive and negative of the face and LBPH (Local binary pattern histogram) algorithm for face recognition by using python programming and OpenCV library. Here we use the tkinter GUI interface for user interface purpose. Firstly, our app asks to fill the details of the student and take image of the particular student. It takes 60 images as sample and store them in folder Training Image. After completion it notify that images saved. After taking image sample we have to click Train Image button. Now it takes few seconds to train machine for the images that are taken by clicking Take Image button and creates a Trainner.yml file and store in TrainingImageLabel folder. Now all initial setups are done. By clicking Track Image button camera of running machine is opened again. If face is recognized by system then Id and Name of person is shown on Image. Press Q (or q) for quit this window. The attendance of the student was updated to the Excel sheet after student's face has been recognized

__Harrcascade__ - basically a machine learning approach , where cascade function used to train the both the positive and negative images after that using that image to detect other object.

__LBPH__(Local Binary Pattern Histogram) it is used to recognize the face of person.Its a simple yet very efficent texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and consider the result as a binary number.


## Technologies Used
* Python
* OpenCV
* Tkinter GUI
* MySQL
* VS CODE (IDE)

## Used Algorithms 
* Haar Cascade   
* LBPH(Local Binary Pattern Histogram)

 

## Contributing

* **Abhishek Rawe** - *Developer* - [Website](https://abhishek-rawe.netlify.app/)

## Authors

* **Abhishek Rawe** - *Developer* Who's the author of those contents - [Abhishek Rawe](https://abhishek-rawe.netlify.app/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/abhishekrawe//LICENSE) file for details

