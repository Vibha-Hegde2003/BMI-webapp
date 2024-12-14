
# def predict_bmi_centi(weight_c, height_c):
#     height_in_meters = height_c / 100  # convert cm to meters
#     return weight_c / (height_in_meters ** 2)

# def predict_bmi_meter(weight_, height_):  #Height is in meters
#             return weight_ / (height_ ** 2)

# # Define a function to categorize BMI
# def bmi_category(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         return "Normal weight"
#     elif 25 <= bmi < 29.9:
#         return "Overweight"
#     else:
#         return "Obesity"
    
# def health_tips(category):
#     if category == "Underweight":
#         print("Health Implications: Risk of nutrient deficiencies, weakened immune system, fatigue, and potential underlying health issues.") 
#         print("Tips to improve Health: \n Diet: Focus on nutrient-dense, calorie-rich foods like nuts, avocados, whole grains, and lean proteins. \n Exercise: Include resistance training to build muscle mass.\n Lifestyle: Eat smaller, frequent meals and avoid skipping meals. Ensure adequate sleep and consult a doctor for potential underlying conditions.")   

#     if category == "Normal weight":
#         print("Health Implications: Generally considered healthy; lower risk of weight-related diseases.")
#         print("Tips to Maintain Health: \n Diet: Maintain a balanced diet with fruits, vegetables, lean proteins, and healthy fats. \n Exercise: Regular physical activity such as 150 minutes of moderate exercise per week.\n Lifestyle: Stay hydrated, manage stress, and monitor weight periodically.")

#     if category == "Overweight":
#         print("Health Implications: Increased risk of cardiovascular diseases, diabetes, and joint issues.")
#         print("Tips to Improve Health:\n Diet: Adopt portion control, reduce sugary and processed foods, and increase fiber intake.\n Exercise: Engage in regular cardio (like walking, running, or cycling) and strength training.\n Lifestyle: Develop a consistent meal plan, avoid late-night snacking, and monitor progress.")

#     if category == "Obesity":
#         print("Health Implications: Higher risk of heart disease, diabetes, sleep apnea, and certain cancers.")
#         print(" Tips to Improve health: \n Diet: Work with a dietitian to create a calorie-controlled meal plan focused on whole foods.\n Exercise: Start with low-impact activities like swimming or walking, gradually increasing intensity. \n Lifestyle: Set realistic weight-loss goals, seek support from health professionals, and address emotional eating.")

# def main():
#     print("To enter the input select : 1. Height in centimeters or 2. Height in meters ")
#     choice = int(input("Enter your choice 1 or 2: "))

#     if(choice ==1):
#         height = float(input("Enter height in centimeters (e.g., 175): "))
#         weight = float(input("Enter weight in kilograms (e.g., 70): "))
#         predicted_bmi = predict_bmi_centi(weight, height)
#         print(f"Predicted BMI: {predicted_bmi:.1f}")
#         cat = bmi_category(predicted_bmi)
#         print("BMI Category is : ", cat)
#         health_tips(cat)

#     if(choice == 2):
#         height = float(input("Enter height in meters (e.g., 1.75): "))
#         weight = float(input("Enter weight in kilograms (e.g., 70): "))
#         predicted_bmi = predict_bmi_meter(weight, height)
#         print(f"Predicted BMI: {predicted_bmi:.1f}")
#         cat = bmi_category(predicted_bmi)
#         print("BMI Category is : ", cat)
#         health_tips(cat)

# if __name__ == "__main__":
#     main()