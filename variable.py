# python variable no data type declaration
# integer type variables
number_one = 123456789
number_two = 987654321
result = number_one + number_two
print(result)
# string types variables
first_name = "Black"
last_name = 'Spider'
full_name = first_name + last_name
print(full_name)
# floating types variables
float_one = 3.1416
float_two = 2.1416
count = float_one + float_two
print(count)
# multiple variable input
name,age,hight,wight,country = "Blackspider\n",26,5.5,52,"bangladesh"
print("Hello, Mr. " + name + 'Age : ' + str(age) + '\n'+ 'Hight : ' + str(hight) +' inch \n'+ 'Wight : ' + str(wight) +' kg \n'+ 'Country : ' + country)
# diff var same value
x=y=z=1
a=b=c=2
i=j=k=4
eq1 = x + a + k
eq2 = y - b - j
eq3 = z * c * k
print(eq1 ,eq2 ,eq3)