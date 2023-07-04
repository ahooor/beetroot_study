# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

weekdays_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays_dict = {}
weekdays_dict_rev = {}

for day in weekdays_list:
    weekdays_dict[day] = weekdays_list.index(day) + 1
print(weekdays_dict)

for day in weekdays_list:
    weekdays_dict_rev[weekdays_list.index(day) + 1] = day
print(weekdays_dict_rev)