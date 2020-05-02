# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))

census = np.concatenate((data, new_record))

age = census[:, 0]

max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = age.std()

race_0 = census[census[:, 2] == 0][:, 2]
race_1 = census[census[:, 2] == 1][:, 2]
race_2 = census[census[:, 2] == 2][:, 2]
race_3 = census[census[:, 2] == 3][:, 2]
race_4 = census[census[:, 2] == 4][:, 2]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = 0
min = len_0

min, minority_race = (min, minority_race) if (min < len_1) else (len_1, 1)
min, minority_race = (min, minority_race) if (min < len_2) else (len_2, 2)
min, minority_race = (min, minority_race) if (min < len_3) else (len_3, 3)
min, minority_race = (min, minority_race) if (min < len_4) else (len_4, 4)
#print(minority_race)

# step 4
senior_citizens = census[census[:, 0] > 60]
working_hours_sum = sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum/ senior_citizens_len
print(round(avg_working_hours, 2))

high = census[census[:, 1] > 10]
low = census[census[:, 1] <= 10]

avg_pay_high = high[:, 7].mean()
avg_pay_low = low[:, 7].mean()
print(avg_pay_high)
print(avg_pay_low)






