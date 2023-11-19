
Num_scores = int(input("How many scores do you want to enter? "))
scores = []
for i in range(Num_scores):
    valid_score = False
    
    while not valid_score:
        try:
           
            score = float(input(f"Enter score {i + 1}: "))
            
            
            if 0 <= score <= 100:
               
                valid_score = True
            else:
                
                print("Invalid score! The score entered should be between 0 and 100.")
        except ValueError:
            
            print("Invalid input! Please enter a numeric value.")

   
    scores.append(score)

lowest_score = min(scores)


print(f"Lowest score: {lowest_score}")

print("Modified list of scores (sorted in ascending order):")
mod_scores = sorted(scores)
print(mod_scores)


average_score = sum(mod_scores) / Num_scores
print(f"Scores average: {average_score:.2f}")


if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")






