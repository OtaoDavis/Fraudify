### 5.2.3 System Requirements

#### 5.2.3.1 Operating System
The system is developed on the Windows 10 operating system. The fraud detection application is designed to run on devices with Windows 11 or Ubuntu 20.04 LTS.

#### 5.2.3.2 Web Server
The system includes an administrator module that requires the Apache HTTP Server, an open-source HTTP Server that provides HTTP services compliant with current HTTP standards (Foundation, The Apache Software, 2021).

#### 5.2.3.3 Database
The system uses a MySQL database to store and manage data efficiently. MySQL is a widely used relational database management system known for its reliability, ease of use, and robust performance.

### 5.3 Description of Testing
System testing involves validating the functionality of different modules to ensure they meet the specified functional and non-functional requirements. Testing for the developed system was conducted by providing correct input and verifying the expected system behavior. Incorrect input was also tested to ensure proper error handling and system stability. This process was applied to all implemented modules in the system to confirm they met the requirements specified.

### 5.4 Testing Paradigms
This section discusses the testing paradigms used for system testing: white box testing and black box testing.

#### 5.4.1 White Box Testing
White box testing evaluates the internal structure of an application. This method requires in-depth knowledge of the system and involves reviewing each line of code. Due to its exhaustive nature, white box testing was applied to sensitive modules, such as the authentication module, to ensure there were no code errors that could compromise user accounts.

#### 5.4.2 Black Box Testing
Black box testing examines the functionality of an application without prior knowledge of its internal structure. This testing was performed on all modules implemented in the system. Test data with predicted outcomes was used to compare the expected output with the system's actual output, helping to understand system behavior and identify possible errors. Non-functional requirements were tested by providing incorrect input to see if the system would still perform optimally as specified in the non-functional requirements.

### 5.5 Testing Results
Testing results for the previously outlined modules are provided below.

---

### Chapter 6: Conclusion, Recommendations, and Future Works

#### 6.1 Conclusion
The primary goal of this project was to address the challenges of detecting and preventing credit card fraud in Kenya by developing a machine learning-based fraud detection system. This system aims to accurately identify fraudulent transactions and prevent financial losses. The system was tested to ensure its effectiveness in identifying and preventing credit card fraud, and the results indicate that it meets the specified objectives.

#### 6.2 Recommendations
To further enhance the fraud detection system, it is recommended to:
1. Continuously update the machine learning model with new data to improve its accuracy and adaptability to evolving fraud patterns.
2. Integrate additional features, such as real-time transaction monitoring and automated alerts for suspicious activities, to improve response times and security.
3. Collaborate with financial institutions to share insights and develop more robust fraud prevention strategies.

#### 6.3 Future Works
Future work could focus on incorporating transaction frequency and location considerations into the fraud detection system. By analyzing patterns related to transaction frequency and location, the system could improve its accuracy in identifying fraudulent activities. Additionally, further research could explore the integration of advanced machine learning techniques, such as deep learning and reinforcement learning, to enhance the system's performance and adaptability to new fraud patterns.
