#Subject_names
subject_names=["Mathematics","Physics","Chemistry","Biology","English"]

#input and validation
subjects = {}
for name in subject_names:
  marks = float(input(f"Enter marks in {name}:"))
  if not (0 <= marks <= 100):
    print(f"invalid input for {name}.Enter marks between 0 and 100.")
    exit()
  subjects[name] = marks

#Grade calc function
def get_grade(avg_marks):
  if   avg_marks>=90: return "A+"
  elif avg_marks>=80: return "A"
  elif avg_marks>=70: return "B"
  elif avg_marks>=60: return "C"
  elif avg_marks>=50: return "D"
  else: return "FAIL"

#Averages
all_avg = sum(subjects.values()) / len(subject_names)
top_3_avg = sum(sorted(subjects.values(),reverse=True)[:3])/3
grade = get_grade(all_avg)

#output statements
print("\n----------- RESULT -----------")
if grade!= "FAIL":
  print(f"           CONGRATULATIONS!!!         ")
else:
  print(f"BETTER LUCK NEXT TIME")
print(f"Average marks in all subjects is: {all_avg:.3f}")
print(f"Grade                           :{grade}")
print(f"Best of 3 Average is            :{top_3_avg:.3f}")
print(f"\nTop 3 Subjects:")
for subject, marks in sorted(subjects.items(), key= lambda x: x[1],reverse=True)[:3]:
      print(f"{subject}: {marks}")
