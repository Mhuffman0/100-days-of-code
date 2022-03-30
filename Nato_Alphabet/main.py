import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(100)
    else:
        print(row.score)
