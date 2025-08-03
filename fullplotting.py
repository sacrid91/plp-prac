# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# -------------------------------
# 1. Generate Sample Data
# -------------------------------

np.random.seed(42)  # For reproducibility

# Student data
n_students = 100
data = {
    'Math': np.random.normal(75, 10, n_students),
    'Science': np.random.normal(70, 12, n_students),
    'English': np.random.normal(80, 8, n_students),
    'History': np.random.normal(65, 15, n_students),
    'Age': np.random.randint(16, 20, n_students),
    'Study_Hours': np.random.gamma(3, 2, n_students),  # Skewed right
    'Pass': np.random.choice(['Yes', 'No'], size=n_students, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Clip scores to realistic range
for col in ['Math', 'Science', 'English', 'History']:
    df[col] = df[col].clip(0, 100).round(1)

print("📊 Dataset Preview:")
print(df.head())
print("\n📈 Dataset Info:")
print(df.describe())

# -------------------------------
# 2. Histogram: Distribution of Math Scores
# -------------------------------

plt.figure(figsize=(10, 6))
plt.hist(df['Math'], bins=15, color='skyblue', edgecolor='navy', alpha=0.8)
plt.title('Distribution of Math Scores', fontsize=16, fontweight='bold')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.axvline(df['Math'].mean(), color='red', linestyle='--', label=f'Mean: {df["Math"].mean():.1f}')
plt.legend()
plt.grid(False)
plt.show()

# -------------------------------
# 3. Heatmap: Correlation Matrix
# -------------------------------

# Select only numeric columns
numeric_df = df.select_dtypes(include=[np.number])

plt.figure(figsize=(8, 6))
correlation_matrix = numeric_df.corr()

sns.heatmap(correlation_matrix,
            annot=True,
            cmap='coolwarm',
            center=0,
            square=True,
            linewidths=0.5,
            cbar_kws={"shrink": 0.8})
plt.title('Correlation Heatmap of Student Scores & Features', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()

# -------------------------------
# 4. Scatter Plot: Study Hours vs Math Score
# -------------------------------

plt.figure(figsize=(10, 6))
colors = np.where(df['Pass'] == 'Yes', 'green', 'red')
scatter = plt.scatter(df['Study_Hours'], df['Math'],
                      c=colors, alpha=0.7, s=60,
                      label=['Pass' if c == 'green' else 'Fail' for c in colors])

# Add trend line
z = np.polyfit(df['Study_Hours'], df['Math'], 1)
p = np.poly1d(z)
plt.plot(df['Study_Hours'], p(df['Study_Hours']), "b--", alpha=0.8, linewidth=2, label='Trend Line')

plt.title('Study Hours vs Math Score (Color: Pass/Fail)', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours per Week')
plt.ylabel('Math Score')
plt.legend(handles=[plt.scatter([], [], color='green', label='Pass'),
                    plt.scatter([], [], color='red', label='Fail'),
                    plt.plot([], [], 'b--', label='Trend')[0]])
plt.grid(True, alpha=0.3)
plt.show()

# -------------------------------
# 5. Box Plot: Subject-wise Score Comparison
# -------------------------------

plt.figure(figsize=(10, 6))
subjects = ['Math', 'Science', 'English', 'History']
box_data = [df[subj] for subj in subjects]

bp = plt.boxplot(box_data, labels=subjects, patch_artist=True,
                 medianprops=dict(color='white', linewidth=2),
                 boxprops=dict(facecolor='lightcoral', edgecolor='darkred'))

# Customize box colors
for patch in bp['boxes']:
    patch.set_facecolor('lightcoral')

plt.title('Box Plot: Score Distribution by Subject', fontsize=16, fontweight='bold')
plt.ylabel('Score')
plt.xlabel('Subjects')
plt.grid(True, alpha=0.3)
plt.show()

# -------------------------------
# 6. Bar Chart: Average Score by Subject (Using Pandas)
# -------------------------------

avg_scores = df[subjects].mean()

plt.figure(figsize=(10, 6))
avg_scores.plot(kind='bar', color='teal', edgecolor='darkslategray', alpha=0.8)
plt.title('Average Score by Subject', fontsize=16, fontweight='bold')
plt.ylabel('Average Score')
plt.xlabel('Subjects')
plt.xticks(rotation=45)
for i, v in enumerate(avg_scores):
    plt.text(i, v + 1, f"{v:.1f}", ha='center', va='bottom', fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# -------------------------------
# 7. Pie Chart: Pass/Fail Ratio
# -------------------------------

pass_fail = df['Pass'].value_counts()

plt.figure(figsize=(8, 8))
colors = ['#4CAF50', '#F44336']
explode = (0.05, 0.1)  # Emphasize "No"
plt.pie(pass_fail, labels=pass_fail.index, autopct='%1.1f%%',
        startangle=90, colors=colors, explode=explode, shadow=True)
plt.title('Student Pass/Fail Ratio', fontsize=16, fontweight='bold')
plt.show()

# -------------------------------
# 8. Line Chart: Subject Difficulty (Mean & Std)
# -------------------------------

summary = df[subjects].agg(['mean', 'std'])

plt.figure(figsize=(10, 6))
x = np.arange(len(subjects))
plt.plot(subjects, summary.loc['mean'], marker='o', linewidth=3, label='Average Score', color='blue')
plt.fill_between(subjects,
                 summary.loc['mean'] - summary.loc['std'],
                 summary.loc['mean'] + summary.loc['std'],
                 color='blue', alpha=0.2, label='±1 Std Dev')

plt.title('Average Score with Variability by Subject', fontsize=16, fontweight='bold')
plt.ylabel('Score')
plt.xlabel('Subjects')
plt.legend()
plt.grid(True, alpha=0.5)
plt.show()

# -------------------------------
# 9. Bonus: Pairplot (Seaborn - Multi-plot)
# -------------------------------

# Uncomment if you want to see pairwise relationships
# sns.pairplot(df[['Math', 'Science', 'English', 'Study_Hours', 'Pass']], hue='Pass', palette='Set1')
# plt.suptitle('Pairwise Relationships (Colored by Pass/Fail)', y=1.02, fontsize=16)
# plt.show()

# -------------------------------
# Optional: Save Data
# -------------------------------
# df.to_csv('student_data.csv', index=False)
# print("✅ Data saved as 'student_data.csv'")

print("\n🎉 All plots generated successfully!")