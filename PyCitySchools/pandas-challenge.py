# Analysis
'''
The analysis begins by creating a high-level snapshot of the district’s key metrics, including the total number of unique schools, total students, total budget, average math score, average reading score, percentage of students passing math, percentage of students passing reading, and the overall passing percentage for both math and reading.

Next, a detailed school summary is created. This includes each school’s name, type, total students, total school budget, per student budget, average math score, average reading score, and the percentages of students passing math, reading, and both.

The schools are then ranked based on their overall passing percentage. The top 5 schools, saved in a DataFrame called “top_schools”, are those with the highest overall passing percentages. Conversely, the bottom 5 schools, saved in a DataFrame called “bottom_schools”, have the lowest overall passing percentages.

The analysis also includes a breakdown of average math and reading scores for students of each grade level (9th, 10th, 11th, 12th) at each school.

School performance is further analyzed based on average spending ranges per student. Schools are categorized into spending bins, and the average math score, average reading score, and passing percentages are calculated for each spending range.

The analysis also considers school size, categorizing schools as small, medium, or large based on the total number of students. A DataFrame called “size_summary” breaks down school performance based on these size categories.

Finally, the analysis looks at school performance based on school type. A new DataFrame, “type_summary”, shows key metrics for each type of school. This comprehensive analysis provides valuable insights into the factors that may influence school and student performance.

Based on the data, we can draw several conclusions:

School Type and Performance: Charter schools tend to have a higher overall passing percentage compared to District schools. For instance, the top five schools in terms of overall passing percentage are all Charter schools, with Cabrera High School leading at approximately 91.33%. On the other hand, the bottom five schools, which are all District schools, have an overall passing percentage just above 50%.

School Size and Performance: There seems to be a correlation between school size and student performance. Smaller schools (with fewer students) tend to have higher average math and reading scores. For example, Pena High School, which is smaller in size, has high average scores in both math (83.62 in 9th grade) and reading (83.67 in 9th grade).

Grade Level and Performance: The average math and reading scores do not vary significantly across different grade levels within the same school. This suggests that the school’s teaching quality is consistent across all grades.

Spending and Performance: Higher spending per student does not necessarily lead to better performance. In fact, schools that spend less per student often have higher overall passing percentages. This suggests that factors other than funding may play a more significant role in student performance.
'''

# Dependencies and Setup
import pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("/Users/davidskaff/Desktop/schools_complete.csv")
student_data_to_load = Path("/Users/davidskaff/Desktop/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()

print(school_data_complete)

df = school_data_complete

# Total number of unique schools
total_schools = df['school_name'].nunique()

# Total students
total_students = df['Student ID'].nunique()

# Total budget
total_budget = df['budget'].unique().sum()

# Average math score
avg_math_score = df['math_score'].mean()

# Average reading score
avg_reading_score = df['reading_score'].mean()

# Percentage of students passing math
passing_math = df[df['math_score'] >= 70]['Student ID'].nunique() / total_students * 100

# Percentage of students passing reading
passing_reading = df[df['reading_score'] >= 70]['Student ID'].nunique() / total_students * 100

# Overall passing percentage for both math and reading
overall_passing = df[(df['math_score'] >= 70) & (df['reading_score'] >= 70)]['Student ID'].nunique() / total_students * 100

# Create a DataFrame to hold the above results
summary_df = pd.DataFrame({
    'Total Schools': [total_schools],
    'Total Students': [total_students],
    'Total Budget': [total_budget],
    'Average Math Score': [avg_math_score],
    'Average Reading Score': [avg_reading_score],
    'Percentage Passing Math': [passing_math],
    'Percentage Passing Reading': [passing_reading],
    'Overall Passing Percentage': [overall_passing]
})

print(summary_df)

# Group by school_name
grouped_schools = df.groupby(['school_name'])

# School type (as it's the same for all students of the same school, we can just take the first)
school_types = grouped_schools['type'].first()

# Total students per school
total_students_per_school = grouped_schools.size()

# Total school budget (as it's the same for all students of the same school, we can just take the first)
total_budget_per_school = grouped_schools['budget'].first()

# Per student budget
per_student_budget = total_budget_per_school / total_students_per_school

# Average math score per school
avg_math_score_per_school = grouped_schools['math_score'].mean()

# Average reading score per school
avg_reading_score_per_school = grouped_schools['reading_score'].mean()

# % passing math per school
passing_math_per_school = df[df['math_score'] >= 70].groupby(['school_name']).size() / total_students_per_school * 100

# % passing reading per school
passing_reading_per_school = df[df['reading_score'] >= 70].groupby(['school_name']).size() / total_students_per_school * 100

# % overall passing per school
overall_passing_per_school = df[(df['math_score'] >= 70) & (df['reading_score'] >= 70)].groupby(['school_name']).size() / total_students_per_school * 100

# Create a DataFrame to hold the above results
school_summary_df = pd.DataFrame({
    'School Type': school_types,
    'Total Students': total_students_per_school,
    'Total School Budget': total_budget_per_school,
    'Per Student Budget': per_student_budget,
    'Average Math Score': avg_math_score_per_school,
    'Average Reading Score': avg_reading_score_per_school,
    'Percentage Passing Math': passing_math_per_school,
    'Percentage Passing Reading': passing_reading_per_school,
    'Overall Passing Percentage': overall_passing_per_school
})

print(school_summary_df)

# Sort and display the top five schools in overall passing rate
top_schools = school_summary_df.sort_values('Overall Passing Percentage', ascending=False)
top_schools = top_schools.head(5)

print(top_schools)

# Sort and display the bottom five schools in overall passing rate
bottom_schools = school_summary_df.sort_values('Overall Passing Percentage', ascending=True)
bottom_schools = bottom_schools.head(5)

print(bottom_schools)

# Create a pandas series for each grade. Group each series by school
ninth_graders = df[df['grade'] == '9th'].groupby('school_name')['math_score'].mean()
tenth_graders = df[df['grade'] == '10th'].groupby('school_name')['math_score'].mean()
eleventh_graders = df[df['grade'] == '11th'].groupby('school_name')['math_score'].mean()
twelfth_graders = df[df['grade'] == '12th'].groupby('school_name')['math_score'].mean()

# Combine the series into a dataframe
math_scores_by_grade = pd.DataFrame({
    '9th': ninth_graders,
    '10th': tenth_graders,
    '11th': eleventh_graders,
    '12th': twelfth_graders
})

print(math_scores_by_grade)

# Create a pandas series for each grade. Group each series by school
ninth_graders = df[df['grade'] == '9th'].groupby('school_name')['reading_score'].mean()
tenth_graders = df[df['grade'] == '10th'].groupby('school_name')['reading_score'].mean()
eleventh_graders = df[df['grade'] == '11th'].groupby('school_name')['reading_score'].mean()
twelfth_graders = df[df['grade'] == '12th'].groupby('school_name')['reading_score'].mean()

# Combine the series into a dataframe
reading_scores_by_grade = pd.DataFrame({
    '9th': ninth_graders,
    '10th': tenth_graders,
    '11th': eleventh_graders,
    '12th': twelfth_graders
})

print(reading_scores_by_grade)

# Create bins for spending ranges
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]

# Use pd.cut to categorize spending based on the bins
school_summary_df['Spending Ranges (Per Student)'] = pd.cut(per_student_budget, spending_bins, labels=labels)

# Group by spending
school_spending_df = school_summary_df.groupby(["Spending Ranges (Per Student)"])

# Calculate averages for the desired columns
spending_math_scores = school_spending_df["Average Math Score"].mean()
spending_reading_scores = school_spending_df["Average Reading Score"].mean()
spending_passing_math = school_spending_df["% Passing Math"].mean()
spending_passing_reading = school_spending_df["% Passing Reading"].mean()
overall_passing_spending = school_spending_df["% Overall Passing"].mean()

# Create the DataFrame
spending_summary = pd.DataFrame({
    "Average Math Score" : spending_math_scores,
    "Average Reading Score": spending_reading_scores,
    "% Passing Math": spending_passing_math,
    "% Passing Reading": spending_passing_reading,
    "% Overall Passing": overall_passing_spending})

print(spending_summary)

# Create bins for school sizes
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Use pd.cut to categorize schools based on the bins
school_summary_df['School Size'] = pd.cut(school_summary_df['Total Students'], size_bins, labels=labels)

# Group by school size
size_grouped = school_summary_df.groupby(["School Size"])

# Calculate averages for the desired columns
size_math_scores = size_grouped["Average Math Score"].mean()
size_reading_scores = size_grouped["Average Reading Score"].mean()
size_passing_math = size_grouped["% Passing Math"].mean()
size_passing_reading = size_grouped["% Passing Reading"].mean()
size_overall_passing = size_grouped["% Overall Passing"].mean()

# Assemble into DataFrame
size_summary = pd.DataFrame({
    "Average Math Score" : size_math_scores,
    "Average Reading Score": size_reading_scores,
    "% Passing Math": size_passing_math,
    "% Passing Reading": size_passing_reading,
    "% Overall Passing": size_overall_passing})

print(size_summary)

# Group by school type
type_grouped = school_summary_df.groupby(["School Type"])

# Calculate averages for the desired columns
type_math_scores = type_grouped["Average Math Score"].mean()
type_reading_scores = type_grouped["Average Reading Score"].mean()
type_passing_math = type_grouped["% Passing Math"].mean()
type_passing_reading = type_grouped["% Passing Reading"].mean()
type_overall_passing = type_grouped["% Overall Passing"].mean()

# Assemble into DataFrame
type_summary = pd.DataFrame({
    "Average Math Score" : type_math_scores,
    "Average Reading Score": type_reading_scores,
    "% Passing Math": type_passing_math,
    "% Passing Reading": type_passing_reading,
    "% Overall Passing": type_overall_passing})

print(type_summary)

