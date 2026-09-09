
import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="student_analytics"
)

query = "SELECT * FROM student_performance"

df = pd.read_sql(query, mydb)
print(df)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

# ==============================
# STUDENT PERFORMANCE ANALYSIS
# ==============================

# 1. Total Students
print("Total Students:", len(df))


# 2. Average Marks
print("Average Marks:", df["marks"].mean())


# 3. Average Attendance
print("Average Attendance:", df["attendance"].mean())


# 4. Highest Marks
print("Highest Marks:", df["marks"].max())


# 5. Lowest Marks
print("Lowest Marks:", df["marks"].min())


# 6. Top 5 Students
print("\nTop 5 Students:")
print(
    df[["name", "marks"]]
    .sort_values("marks", ascending=False)
    .head(5)
)


# 7. Course-wise Analysis
print("\nCourse-wise Analysis:")
course_analysis = df.groupby("course").agg(
    total_students=("student_id", "count"),
    average_marks=("marks", "mean"),
    highest_marks=("marks", "max")
)

print(course_analysis)


# 8. City-wise Analysis
print("\nCity-wise Analysis:")
city_analysis = df.groupby("city").agg(
    total_students=("student_id", "count"),
    average_marks=("marks", "mean"),
    highest_marks=("marks", "max")
)

print(city_analysis)


# 9. High Performers
print("\nHigh Performers:")
high_performers = df[df["marks"] >= 80]
print(high_performers[["name", "course", "marks", "attendance"]])


# 10. Excellent Students
print("\nExcellent Students:")
excellent_students = df[
    (df["marks"] >= 90) &
    (df["attendance"] >= 90)
]

print(excellent_students[["name", "course", "marks", "attendance"]])



import matplotlib.pyplot as plt

course_avg = df.groupby("course")["marks"].mean()

course_avg.plot(kind="bar")

plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.savefig("charts/course_average.png")
plt.show()


city_avg = df.groupby("city")["marks"].mean()

city_avg.plot(kind="bar")

plt.title("Average Marks by City")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)

plt.show()

plt.hist(df["marks"], bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()




plt.scatter(df["attendance"], df["marks"])

plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")

plt.show()


