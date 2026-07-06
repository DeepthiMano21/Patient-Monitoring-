**Objectives**

* Analyze patient risk levels using clinical indicators.
* Monitor patient vital signs and alert generation.
* Track clinical and operational healthcare metrics.
* Identify trends across age groups, wards, and risk categories.
* Build interactive dashboards for healthcare analytics.
* Dataset Enhancement



**Project Workflow**

* Load and clean healthcare data.
* Remove duplicates and null values.
* Generate healthcare monitoring variables.
* Create risk categories using clinical indicators.
* Generate alerts based on vital sign thresholds.
* Perform exploratory analysis using Python.
* Build interactive dashboards in Power BI.
* Publish project through GitHub.



**The original dataset contained demographic and health-related attributes such as:**

* Age
* Gender
* BMI
* High Blood Pressure
* High Cholesterol
* Smoking Status
* Physical Activity
* Heart Disease History
* Diabetes Status



**Additional healthcare monitoring variables were generated using Python:**

* Patient ID
* Admission Date
* Year and Month
* Ward Allocation
* Heart Rate
* SpO₂
* Respiratory Rate
* Length of Stay
* Alert Generation
* Alert Type
* Nurse Response Time
* Risk Category
* Risk Stratification Model



**Patients were categorized into risk groups using a rule-based scoring system based on:**

* BMI > 30
* High Blood Pressure
* High Cholesterol
* Heart Disease History
* Diabetes Status



**Risk Categories:**

* Low Risk
* Moderate Risk
* High Risk
* Alert Generation Logic



**Clinical alerts were generated when:**

* SpO₂ < 92%
* Heart Rate > 110 bpm



**Alert Types:**

* Low SpO₂ Alert
* High Heart Rate Alert
* No Alert



**Tools \& Technologies**

**Programming \& Data Processing**

* Python
* Pandas
* NumPy
* Data Analysis
* Statistical Analysis
* Data Cleaning
* Feature Engineering
* Visualization
* Power BI
* Version Control
* Git
* GitHub



**Dashboard Pages**

***1. Patient Risk Overview***

Provides insights into:



Total Patients

High Risk Patients

Alert Patients

Average Nurse Response Time

Risk Category Distribution

Alert Type Distribution

Ward Distribution

Age Group vs Risk Category

Ward vs Risk Category



***2. Clinical Monitoring \& Trend Analysis***

Provides insights into:



Average SpO₂

Average Heart Rate

Average Respiratory Rate

Average Length of Stay

Patient Admission Trends

Clinical Monitoring Trends Across Risk Categories



**Key Insights**

* High-risk patients showed lower average SpO₂ levels and higher heart rates.
* Clinical alerts were primarily triggered by abnormal SpO₂ and heart rate values.
* Patient distribution varied across hospital wards.
* Older age groups exhibited a higher concentration of moderate and high-risk patients.
* Length of stay increased with patient risk level.





