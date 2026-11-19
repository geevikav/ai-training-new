import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")
df.columns = df.columns.str.strip().str.lower()
avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8,5))
bars = plt.bar(avg_salary.index,avg_salary.values)
plt.title("Average salary per department")
plt.xlabel("Department")
plt.ylabel("Average salary")

plt.bar_label(bars, fmt="%2f")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.figure(figsize=(8,5))
plt.hist(df["salary"],bins=5,edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")
plt.figure(figsize=(8,5))
for department in df["department"].unique():
    dept_data = df[df["department"] == department]
    plt.scatter(
        dept_data["id"],
        dept_data["salary"],
        label=department
    )
plt.title("Employee id vs Salary") 
plt.xlabel("Employee id")
plt.ylabel("salary")
plt.legend(title="Department")
plt.tight_layout()
plt.savefig("scatter_plot.png")
months = ["Jan","Feb","Mar","Apr","May","Jun"]
sales =  [12,15,14,18,22,25]  
plt.figure(figsize=(8,5))
plt.plot(months,sales,marker="o")
plt.title("Monthly sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()
print("All 4 charts created and savedd successfully!!")