import pandas as pd
students = [   
   {'Name': 'Alice', 'Age': 20, 'Scores': (90, 80, 70)},
   {'Name': 'Bob', 'Age': 21, 'Scores': (85, 75, 65)},
   {'Name': 'Charlie', 'Age': 22, 'Scores': (70, 60, 50)},
   {'Name': 'Dave', 'Age': 23, 'Scores': (60, 50, 40)},
   {'Name': 'Eve', 'Age': 24, 'Scores': (50, 40, 30)},
]

print("1. Get Average Score\n2. Get Youngest Student\n3. Get Highest Score\n4. Add Student\n5. Remove Student\n6. Get Common Students\n7. Find Students with Consistent Improvement\n8. Exit")
def add_student(df, name, age, score):
     df = df.append({'Name': name, 'Age': age, 'Score': score}, ignore_index=True) 
     return df

def remove_student(df, name): 
    df = df[df['Name'] != name] 
    return df

def get_common_students(df1, df2):
     return df1.merge(df2, on='Name')

def find_students_with_consistent_scores(df):
     return df[df['Score'].std() == 0]

def main():
     df = pd.DataFrame()

