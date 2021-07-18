### Scope ###

## Age ##
# Find the average age, for all and gender

## Charges ##
# Average charge, for all and gender

## Smoking ##
# Find ratio of smokers in genders
# Find ratio of smokers with low, normal and high BMI
# Find ratio of smokers for people with and without kids
# Average price increanse for smokers vs non-smokers

## Regions ##
# Find ratio between regions
# Find price difference between regions
# Possible reason for higher, lower price in certain region

## Children ##
# Ratio of having kids vs not
# Average price increase of 1 child
# Average amount of kids in segment 'having kids'

## BMI ##
# Average BMI
# Average price increase for high BMI
# Ratio of BMI low, normal, high


import pandas as pd


insurance_data = pd.read_csv('insurance.csv')




## Age ##
#Average age, for all and gender
avg_age = insurance_data['age'].mean()
#prints 39.2

sum_f_age = 0
num_of_females = 0
if insurance_data['sex'] == 'female':
    sum_f_age += int(insurance_data['age'])
    num_of_females += 1

avg_age_female = sum_f_age / num_of_females
print(avg_age_female)


## Charges ##
# Average charge, for all and gender
avg_charge = insurance_data['charges'].mean()



## Smoking ##
# Find ratio of smokers in genders


# Find ratio of smokers with low, normal and high BMI
# Find ratio of smokers for people with and without kids
# Average price increanse for smokers vs non-smokers

## Regions ##
# Find ratio between regions
# Find price difference between regions
# Possible reason for higher, lower price in certain region

## Children ##
# Ratio of having kids vs not
# Average price increase of 1 child
# Average amount of kids in segment 'having kids'

## BMI ##
# Average BMI
# Average price increase for high BMI
# Ratio of BMI low, normal, high





