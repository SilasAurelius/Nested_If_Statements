"""
Quick Decisions: The Event Planner 🎉
Objective:

To practice the use of shorthand if statements in determining event-related decisions.
"""

#Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2
equipment = "audio system" if attendees > 100 else "projector"
print(equipment)

#Task 3: Catering Choices
"""
Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
"""
food = input("Do you want a vegetarian menu? (Yes/No) ")
menu = "Veggie Delight Caterers" if food == "Yes" else "Gourment Meals Caterers"
print(menu)