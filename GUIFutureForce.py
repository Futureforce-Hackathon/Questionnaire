from tkinter import *
from tkinter.ttk import Combobox

###########################################################################################
    #TO CLARIFY, THE INFORMATION GIVEN BY THE USER: 
    # NAME (string) - firstName, middleInitial, lastName
    # GENDER (string) - genderChoice
    # EDUCATION (string) - classification
    #   YEAR (string) - yearChoice
    # ETHNICITY (string) - ethnicChoice
    # MAJOR (string) - majorChoice
    # SKILLS (list) - skillsList[]

    # Look at printInfo() to see how I got the variables
###########################################################################################

def getYear():
    yearLabel = Label(window, text="Undergraduate year?", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
    yearLabel.place(x=25, y=185)
    global yearChoice 
    yearChoice = StringVar()
    yearChoice.set("Freshman")
    yearDropdown = OptionMenu(window, yearChoice, "Freshman", "Sophomore", "Junior", "Senior")
    yearDropdown.config(bg=bodyColor)
    yearDropdown.place(x=175, y=185)

def printInfo(): #FOR TESTING PURPOSES, THIS WILL DISPLAY THE INFO SO FAR
    print("\nNAME: %s %s %s " %(firstName.get(), middleInitial.get(), lastName.get()))
    print("GENDER: %s" %(genderChoice.get()))
    print("EDUCATION: %s" %(classification.get()))
    if classification.get() == "UNDERGRAD":
         print("YEAR: %s" %(yearChoice.get()))
    print("ETHNICITY: %s" %(ethnicChoice.get()))
    print("MAJOR: %s" %(majorChoice.get()))
    skillsIndeces = list(map(int, languageDropdown.curselection()))
    skillsList = []
    for i in range(len(skillsIndeces)):
        skillIndex = skillsIndeces[i]
        skillsList.append(languageList[skillIndex])

    print("SKILLS: ", skillsList)   

    #TO CLARIFY, THE INFORMATION GIVEN BY THE USER: 
    # NAME (string) - firstName, middleInitial, lastName
    # GENDER (string) - genderChoice
    # EDUCATION (string) - classification
    #   YEAR (string) - yearChoice
    # ETHNICITY (string) - ethnicChoice
    # MAJOR (string) - majorChoice
    # SKILLS (list) - skillsList[]
    
window = Tk()

#COLORS
headerColor = "#e63946"
headerTextColor = "#ffffff"
bodyColor = "#ddeef8"
bodyTextColor = "#112a38"
skillsColor = "#abc5f5"
skillsTextColor = "#0d1717"

#STYLING
headerCanvas = Canvas(window, width=800, height=50, bg=headerColor, highlightbackground=headerColor)
headerCanvas.grid()
headerCanvas.tag_lower(headerCanvas)

bodyCanvas = Canvas(window, width=800, height=210, bg=bodyColor, highlightbackground=bodyColor)
bodyCanvas.grid()
bodyCanvas.tag_lower(headerCanvas)

skillsCanvas = Canvas(window, width=800, height=500, bg=skillsColor, highlightbackground=skillsColor)
skillsCanvas.grid()
skillsCanvas.tag_lower(headerCanvas)

#FIRST NAME
firstLabel = Label(window, text="First name: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
firstLabel.place(x=25, y=17)
firstName = StringVar(window)
firstName = Entry(window, width=15, borderwidth=0, highlightthickness=0.5, highlightcolor="#b8b8b8")
firstName.place(x=105, y=16)

#MIDDLE INITIAL
middleLabel = Label(window, text="MI: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
middleLabel.place(x=235, y=17)
middleInitial = Entry(window, width=2, borderwidth=0, highlightthickness=0.5, highlightcolor="#b8b8b8")
middleInitial.place(x=265, y=16)

#LAST NAME
lastLabel = Label(window, text="Last name: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
lastLabel.place(x=300, y=17)
lastName = Entry(window, borderwidth=0, highlightthickness=0.5, highlightcolor="#b8b8b8")
lastName.place(x=380, y=16)

#GENDER
chooseGenderLabel = Label(window, text="Please choose your current preferred gender: ", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
chooseGenderLabel.place(x=25, y=60)
genderChoice = StringVar(window)
genderChoice.set("Other")
genderDropdown = OptionMenu(window, genderChoice, "Female", "Male", "Genderfluid", "Other")
genderDropdown.config(bg=bodyColor)
genderDropdown.place(x=25, y=85)

#CLASSIFICATION / EDUCATION LEVEL
classificationLabel = Label(window, text="Current education level?", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
classificationLabel.place(x=25, y=130)
classification = StringVar()
highschool = Radiobutton(window, text="High School", variable=classification, value="HS")
highschool.config(bg=bodyColor, fg=bodyTextColor)
highschool.place(x=25, y=150)
undergraduate = Radiobutton(window, text="Undergraduate", variable=classification, value="UNDERGRAD", command=getYear)
undergraduate.config(bg=bodyColor, fg=bodyTextColor)
undergraduate.place(x=150, y=150)
graduate = Radiobutton(window, text="Graduate", variable=classification, value="GRAD")
graduate.config(bg=bodyColor, fg=bodyTextColor)
graduate.place(x=290, y=150)
otherEducation = Radiobutton(window, text="Other", variable=classification, value="OTHER")
otherEducation.config(bg=bodyColor, fg=bodyTextColor)
otherEducation.place(x=420, y=150)

#ETHNICITY 
ethnicityLabel = Label(window, text="What is your ethnicity?", font="Helvetica 13 italic", bg=bodyColor, fg=bodyTextColor)
ethnicityLabel.place(x=25, y=210)
ethnicChoice = StringVar()
ethnicChoice.set("American Indian/Alaska Native")
ethnicityDropdown = OptionMenu(window, ethnicChoice, "American Indian/Alaska Native", "Asian", "Black/African American", "Hispanic/LatinX", "Native Hawaiian/Other Pacific Islander", "White")
ethnicityDropdown.config(bg=bodyColor, fg=bodyTextColor)
ethnicityDropdown.place(x=175, y=210)

#MAJOR 
majorLabel = Label(window, text="What is your major?", font="Helvetica 13 italic", bg=bodyColor, fg=bodyTextColor)
majorLabel.place(x=25, y=235)
majorChoice = StringVar()
majorChoice.set("Agriculture")
majorDropdown = OptionMenu(window, majorChoice, 
                            "Agriculture",
                            "Architecture",
                            "Area, Ethnic, Cultural, Gender Studies",
                            "Aviation",
                            "Biological/Biomedical", 
                            "Business, Management, Marketing",
                            "Communication, Journalism",
                            "Communications Technologies/Technicians",
                            "Computer Science, Information Science",
                            "Education",
                            "Engineering Technologies",
                            "Engineering",
                            "English Language, Literature",
                            "Family and Consumer Sciences, Human Sciences",
                            "Foreign Languages, Literatures, Linguistics",
                            "Health Professions, Nurse",
                            "Homeland Security, Law Enforcement",
                            "Human Services",
                            "Legal Professions and Studies",
                            "Liberal Arts and Sciences Studies, Humanities",
                            "Library Science",
                            "Mathematics and Statistics",
                            "Mechanical, Repair Technologies/Technicans",
                            "Military Technologies/Applied Sciences",
                            "Multi/Interdisciplinary Studies",
                            "Natural Resources and Conservation",
                            "Parks, Recreations, Leisure, and Fitness Studies",
                            "Personal and Culinary Studies",
                            "Philosophy and Religious Studies",
                            "Physical Sciences",
                            "Precision Production",
                            "Psychology",
                            "Science Technologies/Technicians",
                            "Social Sciences",
                            "Theology, Religious Vocations",
                            "Transportation/ Materials Moving",
                            "Visual and Performing Arts",
                            "None/Other")
majorDropdown.config(bg=bodyColor)
majorDropdown.place(x=175, y=235)

#PROGRAMMING LANGUAGES
languagesLabel = Label(window, text="Select any programming skills you know (scroll): ", font="Helvetica 13 italic", bg=skillsColor, fg=skillsTextColor)
languagesLabel.place(x=20, y=290)
languageDropdown = Listbox(window, selectmode = "multiple", bd=1, selectbackground="#bee6e5", bg="#e1e8e8")
languageDropdown.place(x=25, y=315)
languageList = ["C", 
                "C++", 
                "Java", 
                "Python", 
                "R", 
                "Go", 
                "Ruby", 
                "JavaScript", 
                "Swift", 
                "PHP", 
                "SQL", 
                "Kotlin", 
                "Perl", 
                "Objective-C", 
                "TypeScript", 
                "Rust", 
                "Lua", 
                "Assembly", 
                "COBOL", 
                "Lisp", 
                "MySQL", 
                "MATLAB", 
                "Julia", 
                "Visual Basic", 
                "Ruby on Rails", 
                "HTML/CSS"]
for each_item in range(len(languageList)):
    languageDropdown.insert(END, languageList[each_item])


giveInfo = Button(window, highlightbackground = skillsColor, font="Helvetica 13", text="Search", command = printInfo)
giveInfo.place(x=25, y=500)


window.title('QUESTIONNAIRE')
window.geometry("600x600+10+10")
window.resizable(0,0)
window.mainloop()