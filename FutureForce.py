def testcasesexuality(string):
  if (string == "Male" or string == "male" or string == "Female" or string == "female" or string == "NaN" or string == "Genderfluid"):
    return True
  else:
    return False;

def classificationtest(string):
  if (string == "HS Student" or string == "College Student" or string == "Graduate" or string == "HS student" or string == "college student" or string == "graduate"):
    return True
  else:
    return False

def yeartest(string):
  if (string == "Freshman" or string == "Sophomore" or string == "Junior" or string == "Senior" or string == "freshman" or string == "sophomore" or string == "junior" or string == "senior"):
    return True
  else:
    return False

def ethnictest(string):
  if(string == "Black" or string == "White" or string == "Latinx" or string == "Asian" or string == "Middle Eastern"):
    return True
  else:
    return False

    
print("Hello! Please input your details below! ")
print('\n')
name = input("What is your name? ")
print('\n')

gendertest = False
while(gendertest == False):
  sexuality = input("What is your sexuality? Possible values are Male, Female, Genderfluid, and NaN for 'prefer not to disclose': ")
  gendertest = testcasesexuality(sexuality)
  if (gendertest == False):
    print("Invalid value entered. Please try again \n")
print('\n')

classtest = False
while (classtest == False):
  classification = input("What is your classification? Possible classifications include HS Student, College Student, and graduate: ")
  classtest = classificationtest(classification)
  if (classtest == False):
    print("Invalid value entered. Please try again! \n")

if (classification == "College Student"):
  yearTest = False
  while (yearTest == "False"):
    
    year = input("What is your academic year?")
    yearTest = yeartest(year)
    if(yearTest == False):
      print("Invalid year entered. Acceptable values are Freshman, Sophomore, Junior and Senior. ")

else:
  year = "N/A"

print('\n')
racetest = False
while (racetest == False):
  race = input("What is your ethnicity? Accepted values are Black, White, Latinx, Asian and Middle Eastern. \n")
  racetest = ethnictest(race)
  if (racetest == False):
    print ("Invalid value entered. Please try again. \n")
print('\n')
major = input("What is your major? " )
major = major.capitalize()
for i in range(0,len(major)):
  if (major[i] == " "):
    maj = str(major[i+1])
    maj = maj.upper()
    majlist = list(major)
    majlist[i+1] = maj
    major= "".join(majlist)
print (major)
print('\n')
skill_list = []
skillend = False
while (skillend != True):
  skill = input("Please input a programming language: ")
  skill_list.append(skill)
  skillcheckloop = False
  while(skillcheckloop is not True):
    skillcheck = input("Would you like to add another? Please type Y for yes and N for No: ")
    if (skillcheck == 'Y' or skillcheck == 'y'):
      skillend = False
      skillcheckloop = True
    elif(skillcheck == 'N' or skillcheck == 'n'):def testcasesexuality(string):
  if (string == "Male" or string == "male" or string == "Female" or string == "female" or string == "NaN" or string == "Genderfluid"):
    return True
  else:
    return False;

def classificationtest(string):
  if (string == "HS Student" or string == "College Student" or string == "Graduate" or string == "HS student" or string == "college student" or string == "graduate"):
    return True
  else:
    return False

def yeartest(string):
  if (string == "Freshman" or string == "Sophomore" or string == "Junior" or string == "Senior" or string == "freshman" or string == "sophomore" or string == "junior" or string == "senior"):
    return True
  else:
    return False

def ethnictest(string):
  if(string == "Black" or string == "White" or string == "Latinx" or string == "Asian" or string == "Middle Eastern"):
    return True
  else:
    return False
print("Hello! Please input your details below! ")
print('\n')
name = input("What is your name? ")
print('\n')

gendertest = False
while(gendertest == False):
  sexuality = input("What is your sexuality? Possible values are Male, Female, Genderfluid, and NaN for 'prefer not to disclose': ")
  gendertest = testcasesexuality(sexuality)
  if (gendertest == False):
    print("Invalid value entered. Please try again \n")
print('\n')

classtest = False
while (classtest == False):
  classification = input("What is your classification? Possible classifications include HS Student, College Student, and graduate: ")
  classtest = classificationtest(classification)
  if (classtest == False):
    print("Invalid value entered. Please try again! \n")

if (classification == "College Student"):
  yearTest = False
  while (yearTest == "False"):
    
    year = input("What is your academic year?")
    yearTest = yeartest(year)
    if(yearTest == False):
      print("Invalid year entered. Acceptable values are Freshman, Sophomore, Junior and Senior. ")

else:
  year = "N/A"

print('\n')
racetest = False
while (racetest == False):
  race = input("What is your ethnicity? Accepted values are Black, White, Latinx, Asian and Middle Eastern. \n")
  racetest = ethnictest(race)
  if (racetest == False):
    print ("Invalid value entered. Please try again. \n")
print('\n')
major = input("What is your major? " )
major = major.capitalize()
for i in range(0,len(major)):
  if (major[i] == " "):
    maj = str(major[i+1])
    maj = maj.upper()
    majlist = list(major)
    majlist[i+1] = maj
    major= "".join(majlist)
print (major)
print('\n')
skill_list = []
skillend = False
while (skillend == False):
  skill = input("Please input your notable skills: ")
  skill_list.append(skill)
  skillcheckloop = False
  while(skillcheckloop == False):
    skillcheck = input("Would you like to add another? Please type Y for yes and N for No: ")
    if (skillcheck == 'Y' or skillcheck == 'y'):
      skillend = False
      skillcheckloop = True
    elif(skillcheck == 'N' or skillcheck == 'n'):
      skillend = True
      skillcheckloop == True
    else:
      print("Invalid value entered: ")
  if (skillcheckloop == True):
    skillend = True

    #Something similar could be used for programming languages
      skillend = True
      skillcheckloop == True
    else:
      print("Invalid value entered: ")
  if (skillcheckloop == True):
    skillend = True