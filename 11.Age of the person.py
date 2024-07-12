# Age of the person
person_age = 28

# Age of the younger brother
younger_brother_age = 24

# Age difference between the person and his younger brother
age_difference = person_age - younger_brother_age

# Calculate the person's age when the older brother is 56
older_brother_age_56 = 56
person_age_56 = person_age + (older_brother_age_56 - younger_brother_age)

print("Person's age when the older brother is 56:", person_age_56)

# If the age difference is more than 3, find the age of the younger brother when the older brother was 5
if age_difference > 3:
    older_brother_age_5 = 5
    younger_brother_age_when_older_brother_was_5 = younger_brother_age - age_difference
    print("Younger brother's age when the older brother was 5:", younger_brother_age_when_older_brother_was_5)
