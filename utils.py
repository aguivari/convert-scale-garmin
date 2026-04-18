# Not very scientific logic for 'Physique Rating'.
# The thresholds can be adjusted for male/female 
# but these are not in the CSV file and need to come
# from the command line invocation
def get_physique_rating(fat, muscle_pct, gender):
    if gender.lower() == 'female':
        low_fat, high_fat = 21, 32
        low_muscle, high_muscle = 30, 40
    else:
        low_fat, high_fat = 12, 22
        low_muscle, high_muscle = 40, 50

    if fat > high_fat:
        return 1 if muscle_pct < low_muscle else 2 if muscle_pct < high_muscle else 3
    elif fat > low_fat:
        return 4 if muscle_pct < low_muscle else 5 if muscle_pct < high_muscle else 6
    else:
        return 7 if muscle_pct < low_muscle else 8 if muscle_pct < high_muscle else 9

