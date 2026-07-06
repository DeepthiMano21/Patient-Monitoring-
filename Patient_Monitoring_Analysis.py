import pandas as pd
import numpy as np

df = pd.read_csv("diabetes_012_health_indicators_BRFSS2015.csv")

print(df.info())
print(df.describe())

print(df.isnull().sum())
df = df.dropna()
df = df.drop_duplicates()

print("Total Records:", len(df))

# Patient ID
df["PatientID"] = range(1, len(df)+1)

# Admission Dates 2021-2025
df["Admission_Date"] = pd.to_datetime(
    np.random.choice(
        pd.date_range("2021-01-01", "2025-12-31"),
        len(df)
    )
)

df["Year"] = df["Admission_Date"].dt.year
df["Month"] = df["Admission_Date"].dt.month_name()

# Wards
df["Ward"] = np.random.choice(
    ["ICU", "General", "Cardiology", "Pulmonology"],
    len(df)
)

# Risk Category 
def risk_category(row):

    score = 0

    if row["BMI"] > 30:
        score += 1

    if row["HighBP"] == 1:
        score += 1

    if row["HighChol"] == 1:
        score += 1

    if row["HeartDiseaseorAttack"] == 1:
        score += 1

    if row["Diabetes_012"] == 2:
        score += 2

    if score <= 1:
        return "Low Risk"

    elif score <= 3:
        return "Moderate Risk"

    else:
        return "High Risk"

df["Risk_Category"] = df.apply(
    risk_category,
    axis=1
)

# Heart Rate 
df["Heart_Rate"] = np.where(
    df["Risk_Category"] == "High Risk",
    np.random.randint(95, 130, len(df)),
    np.where(
        df["Risk_Category"] == "Moderate Risk",
        np.random.randint(75, 105, len(df)),
        np.random.randint(60, 85, len(df))
    )
)

# SpO2 
df["SpO2"] = np.where(
    df["Risk_Category"] == "High Risk",
    np.random.randint(85, 93, len(df)),
    np.where(
        df["Risk_Category"] == "Moderate Risk",
        np.random.randint(92, 97, len(df)),
        np.random.randint(96, 100, len(df))
    )
)

# Respiratory Rate 
df["Respiratory_Rate"] = np.where(
    df["Risk_Category"] == "High Risk",
    np.random.randint(20, 30, len(df)),
    np.where(
        df["Risk_Category"] == "Moderate Risk",
        np.random.randint(16, 22, len(df)),
        np.random.randint(12, 18, len(df))
    )
)

# Length of Stay 
df["Length_of_Stay"] = np.where(
    df["Risk_Category"] == "High Risk",
    np.random.randint(10, 20, len(df)),
    np.where(
        df["Risk_Category"] == "Moderate Risk",
        np.random.randint(5, 12, len(df)),
        np.random.randint(1, 7, len(df))
    )
)


def age_group(age):

    if age <= 3:
        return "18-34"

    elif age <= 6:
        return "35-49"

    elif age <= 9:
        return "50-64"

    else:
        return "65+"

df["Age_Group"] = df["Age"].apply(age_group)


df["Nurse_Response_Time"] = np.where(
    df["Risk_Category"] == "High Risk",
    np.random.randint(1, 10, len(df)),
    np.where(
        df["Risk_Category"] == "Moderate Risk",
        np.random.randint(5, 15, len(df)),
        np.random.randint(10, 30, len(df))
    )
)

# Outcome 
df["Outcome"] = np.where(
    df["Diabetes_012"] == 0,
    "Non-Diabetic",
    "Diabetic"
)

# Alert Generation
df["Alert_Generated"] = np.where(
    (df["SpO2"] < 92) |
    (df["Heart_Rate"] > 110),
    "Yes",
    "No"
)

# Alert Type
conditions = [
    df["SpO2"] < 92,
    df["Heart_Rate"] > 110
]

choices = [
    "Low SpO2",
    "High Heart Rate"
]

df["Alert_Type"] = np.select(
    conditions,
    choices,
    default="No Alert"
)

print("\nAverage BMI:")
print(df["BMI"].mean())

print("\nAverage Age:")
print(df["Age"].mean())

print("\nAverage SpO2:")
print(df["SpO2"].mean())

print("\nRisk Category Distribution:")
print(df["Risk_Category"].value_counts())

print("\nOutcome Distribution:")
print(df["Outcome"].value_counts())


df = df[
    [
        "PatientID",
        "Admission_Date",
        "Year",
        "Month",
        "Age",
        "Age_Group",
        "Sex",
        "BMI",
        "HighBP",
        "HighChol",
        "Smoker",
        "PhysActivity",
        "HeartDiseaseorAttack",
        "Ward",
        "Heart_Rate",
        "SpO2",
        "Respiratory_Rate",
        "Length_of_Stay",
        "Alert_Generated",
        "Alert_Type",
        "Nurse_Response_Time",
        "Risk_Category",
        "Outcome"
    ]
]

df = df.sample(n=10000, random_state=42)
df.to_csv(
    "enhanced_patient_monitoring_data.csv",
    index=False
)

print("\nDataset Saved Successfully!")
print(df.head())

from google.colab import files

files.download("enhanced_patient_monitoring_data.csv")