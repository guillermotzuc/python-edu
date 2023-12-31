import pandas as pd
from csv import DictReader
from pandas.api.types import CategoricalDtype

employee_info = []
with open("/home/gtzuc/Documents/code/python-edu/labs/pandas/employees.csv", newline="") as f:
    reader = DictReader(f)
    for row in reader:
        row["age"] = int(row["age"])
        row["salary"] = float(row["salary"])
        employee_info.append(row)

columns = employee_info[0].keys()
employee_frame = pd.DataFrame.from_records(employee_info, columns=columns)

print(f"Number of Unique Job Titles: {employee_frame.job_title.value_counts().count()}")

job_title_unique_gender_count = employee_frame.groupby('job_title')['gender'].nunique()
job_titles_with_two_genders = job_title_unique_gender_count.where(job_title_unique_gender_count == 2).dropna().index
job_title_gender_frame = employee_frame[employee_frame.job_title.isin(job_titles_with_two_genders)]

gender_difference_table = pd.pivot_table(job_title_gender_frame, columns='gender', values=['salary'], index=['job_title'])
gender_difference_table[('salary', 'difference')] = gender_difference_table[('salary', 'Female')] - gender_difference_table[('salary', 'Male')]
print(gender_difference_table)

employee_frame['age_range'] = pd.cut(employee_frame.age, [18, 41, 80], labels=['18 - 40', '41 - 80'])
employee_frame.age_range.cat.add_categories(['difference'])

job_title_unique_age_range_count = employee_frame.groupby('job_title')['age_range'].nunique()
job_titles_with_two_age_ranges = job_title_unique_age_range_count.where(job_title_unique_age_range_count == 2).dropna().index
job_title_age_range_frame = employee_frame[employee_frame.job_title.isin(job_titles_with_two_age_ranges)]

age_difference_table = pd.pivot_table(job_title_age_range_frame, columns='age_range', values=['salary'], index=['job_title'])
age_difference_table[('salary', 'difference')] = age_difference_table[('salary', '18 - 40')] - age_difference_table[('salary', '41 - 80')]
print(age_difference_table)