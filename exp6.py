n=2020

leap_year= "leap year" if (n % 4==0 and n % 100 !=0 ) or n % 400 ==0 else "Not leap year"

print(leap_year)