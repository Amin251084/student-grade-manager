def avg(subjects_score):
    total = sum(subjects_score.values())
    average = total / len(subjects_score)
    return average

def max_grades(subjects_score):
    return max(subjects_score.values())

def min_grades(subjects_score):
    return min(subjects_score.values())