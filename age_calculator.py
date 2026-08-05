quest=input("enter your birth year")
year=int(quest)
q2=input("enter birt month")
month=int(q2)
q6=input("enter birth date:")
date=int(q6)
q3=input("enter cureent year")
current_year=int(q3)
q4=input("enter current month")
current_month=int(q4)
q5=input("enter current date")
current_date=int(q5)
if(current_month>month):
    age=current_year-year
elif(current_month==month):
    if(current_date>=date):
        age=current_year-year 
    else:
     print("{}days left to become2 {}".format(date-current_date,current_year-year))
     age=current_year-year-1 
elif(current_month<month):
   age=current_year-year-1 

print(' your Age=',age)

