# 🎓 Student Management & Performance Analytics System

## 📖 Project Overview

The Student Management & Performance Analytics System is a web-based application developed using Python and Streamlit. It helps users manage student records, maintain subject-wise marks, analyze academic performance, visualize data through graphs, identify toppers, and export records for reporting purposes.

This application eliminates the need for maintaining student information manually and provides an easy-to-use interface for managing and analyzing student performance.

---

# 🎯 Problem Statement

Managing student records manually can be difficult, especially when dealing with multiple students and subjects.

Common challenges include:

* Difficulty in maintaining records
* Time-consuming updates
* Difficulty in searching student information
* No automatic performance analysis
* No graphical representation of results
* Difficulty in identifying toppers

This project solves these challenges by providing a centralized student management and analytics platform.

---

# 🚀 Features

## 📚 Subject Management

* Add new subjects
* Delete existing subjects
* Automatically updates all student records when a new subject is added
* Automatically removes subject data when a subject is deleted

---

## 👨‍🎓 Student Management

* Add Student
* View Student Records
* Search Student by ID
* Update Student Information
* Delete Student Records
* Prevent Duplicate Student IDs

---

## 📊 Dashboard Analytics

The dashboard provides:

* Total Students
* Class Average
* Overall Topper
* Subject-wise Average Marks

---

## 📈 Data Visualization

### Individual Student Performance Graph

Displays subject-wise marks of a student using a bar chart.

Example:


Python  ███████████ 95
DSA     ██████████   88
DBMS    ████████████ 100


### Subject-wise Average Graph

Displays average marks of each subject across all students.

Example:

```text
Python ██████████ 84.5
DSA    ████████   78.2
DBMS   █████████  81.7
```

These visualizations help users quickly understand performance trends.

---

## 🏆 Performance Analysis

### Overall Topper

Displays:

* Student ID
* Student Name
* Average Marks

### Top 3 Students

Ranks students based on average marks.

### Subject Toppers

Displays the highest scorer in each subject.

---

## 📄 Data Export

Export all student records into CSV format.

Benefits:

* Backup records
* Share data easily
* Open in Microsoft Excel
* Further data analysis

---

# 🖥️ Application Modules

## 1️⃣ Dashboard

Displays:

* Total Students
* Class Average
* Overall Topper
* Subject Average Graph

---

## 2️⃣ Manage Subjects

Used for:

* Adding subjects
* Deleting subjects

---

## 3️⃣ Add Student

Allows users to:

* Enter Student ID
* Enter Student Name
* Enter Subject-wise Marks

---

## 4️⃣ View Students

Displays all student records in tabular format.

Example:

| ID  | Name | Python | DSA | DBMS | Average |
| --- | ---- | ------ | --- | ---- | ------- |
| 101 | Sai  | 95     | 88  | 100  | 94.33   |
| 102 | Ganesh | 90     | 95  | 85   | 90.00   |

---

## 5️⃣ Search Student

Search student details using Student ID.

Displays:

* Student Information
* Subject-wise Marks
* Average Marks
* Performance Graph

---

## 6️⃣ Update Student

Allows modification of:

* Student Name
* Student Marks

---

## 7️⃣ Delete Student

Removes a student record permanently.

---

## 8️⃣ Top 3 Students

Displays the top-performing students.

Example:

1. Sai    - 94.33
2. Ganesh - 91.50
3. Akhil  - 89.25

---

## 9️⃣ Subject Topper

Displays the highest scorer in every subject.

Example:

Python → Sai (98)
DSA → Ganesh (95)
DBMS → Akhil (97)

---

## 🔟 Export CSV

Exports all student records to: "students.csv"

---

# 📊 Sample Workflow

### Step 1: Add Subjects

Add subjects that will be used for all students.

Example:

Python
DSA
DBMS

---

### Step 2: Add Student

Enter student details.

Example:

Student ID : 101
Student Name : Sai

Python : 95
DSA : 88
DBMS : 100

---

### Step 3: View Students

Displays all students in a table.

---

### Step 4: Search Student

Search by Student ID.

Example:

Student ID : 101


Displays:

ID : 101
Name : Sai

Python : 95
DSA : 88
DBMS : 100

Average : 94.33

---

### Step 5: View Student Graph

Automatically generates a bar graph showing subject-wise marks.

This helps identify strengths and weaknesses quickly.

---

### Step 6: Update Student

Modify student details and marks.

Example:

Before:

Name : Sai
Python : 95
DSA : 88

After:

Name : Sai Ganesh
Python : 98
DSA : 90


---

### Step 7: Delete Student

Select a student and delete the record permanently.

---

### Step 8: View Dashboard

Dashboard automatically calculates:

* Total Students
* Class Average
* Overall Topper

and displays subject-wise average graph.

---

### Step 9: View Top 3 Students

Displays the highest-performing students.

---

### Step 10: View Subject Toppers

Displays toppers for each subject.

---

### Step 11: Export Data

Download all records as CSV.

---

# 🛠️ Technologies Used

| Technology | Purpose            |
| ---------- | ------------------ |
| Python     | Core Programming   |
| Streamlit  | Web Interface      |
| Pandas     | Data Processing    |
| Matplotlib | Data Visualization |
| JSON       | Data Storage       |
| CSV        | Data Export        |

---

# 📂 Project Structure

Student-Management-System/
│
├── main.py
├── data.json
├── subjects.json
├── requirements.txt
└── README.md

---

# ⚙️ Installation

### Clone Repository

git clone https://github.com/your-username/student-marks-analysis.git

### Move into Project Folder

cd student-marks-analysis

### Install Dependencies

pip install streamlit pandas matplotlib

### Run Application

streamlit run main.py

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python Programming
* JSON File Handling
* CRUD Operations
* Data Analysis
* Data Visualization
* Streamlit Development
* Git & GitHub
* Building End-to-End Projects

---

# 🔮 Future Enhancements

Potential future improvements:

* SQLite Database Integration
* User Authentication
* PDF Report Card Generation
* Attendance Management
* Student Photo Upload
* Cloud Deployment
* Email Notifications
* Teacher/Admin Dashboard

---

# 👨‍💻 Author

**Sai Ganesh**

B.Tech Computer Science & Engineering Student

