g=int(input("enter marks"))
# if--elif


if(g>80):
    print("Grade is A")
elif(g>70 and g<=80):
    print("Grade is B+")
elif g>=60 and g<=70:
    print("Grade is B")
elif g<60 and g>=40:
    print("Grade is D")
else:
    print("FAIL")