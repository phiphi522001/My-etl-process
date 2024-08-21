# My-etl-process
This project aims to practice etl skills using python on vscode platform.

## The data i have used

### Enrollees data
As enrollies are submitting their request to join the course via Google Forms, we have the Google Sheet that stores data about enrolled students, containing the following columns:

enrollee_id: unique ID of an enrollee.\
full_name: full name of an enrollee.\
city: the name of an enrollie's city.\
gender: gender of an enrollee.

The data source is attached in this repository.

### Enrollees education
After enrollment everyone should fill the form about their education level. This form is being digitalized manually. 

This table contains the following columns:

enrollee_id: A unique identifier for each enrollee. This integer value uniquely distinguishes each participant in the dataset.\
enrolled_university: Indicates the enrollee's university enrollment status. Possible values include no_enrollment, Part time course, and Full time course.\
education_level: Represents the highest level of education attained by the enrollee. Examples include Graduate, Masters, etc.\
major_discipline: Specifies the primary field of study for the enrollee. Examples include STEM, Business Degree, etc.

The data source is attached in this repository.

### Enrollees's working experience
Another survey that is being collected manually by educational department is about working experience.

This table contains the following columns:

enrollee_id: A unique identifier for each enrollee. This integer value uniquely distinguishes each participant in the dataset.\
relevent_experience: Indicates whether the enrollee has relevant work experience related to the field they are currently studying or working in. Possible values include Has relevent experience and No relevent experience.\
experience: Represents the number of years of work experience the enrollee has. This can be a specific number or a range (e.g., >20, <1).\
company_size: Specifies the size of the company where the enrollee has worked, based on the number of employees. Examples include 50−99, 100−500, etc.\
company_type: Indicates the type of company where the enrollee has worked. Examples include Pvt Ltd, Funded Startup, etc.\
last_new_job: Represents the number of years since the enrollee's last job change. Examples include never, >4, 1, etc.

The data source is attached in this repository.

### Training hours
From LMS system's database you can retrieve a number of training hours for each student that they have completed.

Database credentials:

Database type: `MySQL`\
Host: `112.213.86.31`\
Port: `3360`\
Login: `etl_practice`\
Password: `550814`\
Database name: `company_course`\
Table name: `training_hours`

### City development index
Another source that can be usefull is the table of City development index.\
The City Development Index (CDI) is a measure designed to capture the level of development in cities. It may be significant for the resulting prediction of student's employment motivation.\
It is stored here: https://sca-programming-school.github.io/city_development_index/index.html

### Employment
From LMS database you can also retrieve the fact of employment. If student is marked as employed, it means that this student started to work in our company after finishing the course.
Database credentials:

Database type: `MySQL`\
Host: `112.213.86.31`\
Port: `3360`\
Login: `etl_practice`\
Password: `550814`\
Database name: `company_course`\
Table name: `employment`

## Instructions for viewing detailed descriptions of implementation steps in the attached py file
You can read the comments inside the py file to understand my steps clearly.
Or you can view my colab file [here](https://colab.research.google.com/drive/1zF4HnsOtTmt4LWgeEnYgarcSZFFWEn1-?usp=sharing)

## Scheduling the script on Windows

**1. Open Task Scheduler:**

* Search for "Task Scheduler" in the Start menu and open it.

**2. Create a New Task:**

* In the right-hand pane, click on "Create Basic Task".
* Give your task a name and description, then click "Next".

**3. Trigger the Task:**

* Select "Daily" and click "Next".
* Set the start date and time, and specify that the task should recur every day.

**4. Action:**

* Select "Start a Program" and click "Next".
* Click "Browse" and select the Python executable (usually python.exe or pythonw.exe in your Python installation directory).
* In the "Add arguments (optional)" field, enter the path to your ETL script, e.g., `C:\path\to\your_script.py.`

**5. Finish the Task:**

* Review your settings and click "Finish".
