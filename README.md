# Challenge Summary

This project involves a comprehensive analysis of school performance based on various factors. The data set includes information about schools and students, such as school type, size, budget, and student grades.

The analysis begins with a high-level snapshot of the district’s key metrics, including:

Total number of unique schools
Total students
Total budget
Average math score
Average reading score
Percentage of students passing math
Percentage of students passing reading
Overall passing percentage for both math and reading
Next, a detailed summary of each school is created, including:

School name
School type
Total students
Total school budget
Per student budget
Average math score
Average reading score
Percentage of students passing math
Percentage of students passing reading
Overall passing percentage for both math and reading

The schools are then ranked based on their overall passing percentage. The top five and bottom five schools are identified and saved in separate DataFrames, “top_schools” and “bottom_schools” respectively.

The analysis also includes a breakdown of average math and reading scores for students of each grade level (9th, 10th, 11th, 12th) at each school.

School performance is further analyzed based on average spending ranges per student. Schools are categorized into spending bins, and the average math score, average reading score, and passing percentages are calculated for each spending range.

The analysis also considers school size, categorizing schools as small, medium, or large based on the total number of students. A DataFrame called “size_summary” breaks down school performance based on these size categories.

Finally, the analysis looks at school performance based on school type. A new DataFrame, “type_summary”, shows key metrics for each type of school.

This comprehensive analysis provides valuable insights into the factors that may influence school and student performance. However, it’s important to remember that correlation does not imply causation, and further investigation would be needed to determine the underlying causes of these trends.
