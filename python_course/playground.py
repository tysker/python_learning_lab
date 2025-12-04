def life_in_weeks(curr_age):
    life_expectancy = 90
    years_left = life_expectancy - curr_age
    weeks_per_year = 12 * 4
    weeks_left = weeks_per_year * years_left
    return f"You have {weeks_left} weeks left."


print(life_in_weeks(20))

# Constant
MY_URL = "https://myurl.dk"
# Global value
a_value = 0 

def fetch():
    print(MY_URL)
    print(a_value + 10)

print(a_value)
fetch()
