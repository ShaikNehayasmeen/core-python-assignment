def calculate_positive_feedback_percentage(ratings):
    
    if not ratings:
        return "No ratings available."
    positive_feedback_count = sum(1 for rating in ratings if rating >= 4)
    positive_percentage = (positive_feedback_count / len(ratings)) * 100
    return round(positive_percentage, 2)  
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)
print("```")
if isinstance(positive_feedback_percentage, str):
    print(positive_feedback_percentage)
else:
    print(f"Positive Feedback: {positive_feedback_percentage}%")
print("```")
