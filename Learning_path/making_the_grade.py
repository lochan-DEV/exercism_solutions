"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    result = []                     
    for score in student_scores:     
        rounded = round(score)
        result.append(rounded)      
    return result                    
        
        
def count_failed_students(student_scores):
    n=0
    for x in student_scores:
        if x<=40:
            n=n+1
    return n

def above_threshold(student_scores, threshold):
    list=[]
    for x in student_scores:
        if x>=threshold:
            list.append(x)
    return list


def letter_grades(highest):
    diff=(highest-40)//4
    list=[]
    for i in range(4):
        x=41+i*diff
        list.append(x)
    return list


def student_ranking(student_scores, student_names):
    list=[]
    for n in range(len(student_names)):
        y = f"{n+1}. {student_names[n]}: {student_scores[n]}"
        list.append(y)
    return list


def perfect_score(student_info):
    for i in range(len(student_info)):
        x, y = student_info[i]
        if y == 100:
            return [x, y]
    return []


        