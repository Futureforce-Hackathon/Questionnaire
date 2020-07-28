from tkinter import *
from tkinter.ttk import Combobox



def getYear():
    yearLabel = Label(window, text="Undergraduate year?", font='Helvetica 13 italic')
    yearLabel.place(x=25, y=185)
    global yearChoice 
    yearChoice = StringVar()
    yearChoice.set("Freshman")
    yearDropdown = OptionMenu(window, yearChoice, "Freshman", "Sophomore", "Junior", "Senior")
    yearDropdown.place(x=175, y=185)

window=Tk()

#FIRST NAME
firstLabel = Label(window, text="First name: ", font='Helvetica 13 italic')
firstLabel.place(x=25, y=17)
firstName = Entry(window, width=15)
firstName.place(x=105, y=10)

#MIDDLE INITIAL
middleLabel = Label(window, text="MI: ", font='Helvetica 13 italic')
middleLabel.place(x=240, y=17)
middleInitial = Entry(window, width=2, )
middleInitial.place(x=265, y=10)

#LAST NAME
lastLabel = Label(window, text="Last name: ", font='Helvetica 13 italic')
lastLabel.place(x=305, y=17)
lastName = Entry(window)
lastName.place(x=380, y=10)

#GENDER
chooseGenderLabel = Label(window, text="Please choose your current preferred gender: ", font='Helvetica 13 italic')
chooseGenderLabel.place(x=25, y=60)
genderChoice = StringVar(window)
genderChoice.set("Other")
genderDropdown = OptionMenu(window, genderChoice, "Female", "Male", "Genderfluid", "Other")
genderDropdown.place(x=25, y=85)

#CLASSIFICATION / EDUCATION LEVEL
classificationLabel = Label(window, text="Current education level?", font='Helvetica 13 italic')
classificationLabel.place(x=25, y=130)
classification = StringVar()
highschool = Radiobutton(window, text="High School", variable=classification, value="HS")
highschool.place(x=25, y=150)
undergraduate = Radiobutton(window, text="Undergraduate", variable=classification, value="UNDERGRAD", command=getYear)
undergraduate.place(x=150, y=150)
graduate = Radiobutton(window, text="Graduate", variable=classification, value="GRAD")
graduate.place(x=290, y=150)
otherEducation = Radiobutton(window, text="Other", variable=classification, value="OTHER")
otherEducation.place(x=420, y=150)

#ETHNICITY 
ethnicityLabel = Label(window, text="What is your ethnicity?", font="Helvetica 13 italic")
ethnicityLabel.place(x=25, y=210)
ethnicChoice = StringVar()
ethnicChoice.set("American Indian/Alaska Native")
ethnicityDropdown = OptionMenu(window, ethnicChoice, "American Indian/Alaska Native", "Asian", "Black/African American", "Hispanic/LatinX", "Native Hawaiian/Other Pacific Islander", "White")
ethnicityDropdown.place(x=175, y=210)

#MAJOR 
majorLabel = Label(window, text="What is your major?", font="Helvetica 13 italic")
majorLabel.place(x=25, y=235)
majorChoice = StringVar()
majorChoice.set("Computer Science")
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
                            "Visual and Performing Arts")
majorDropdown.place(x=175, y=235)

#PROGRAMMING LANGUAGES
languagesLabel = Label(window, text="Select any programming skills you know (scroll): ", font="Helvetica 13 italic")
languagesLabel.place(x=25, y=270)
languageDropdown = Listbox(window, selectmode = "multiple", bd=1, selectbackground="lightblue")
languageDropdown.place(x=25, y=290)
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



window.title('QUESTIONNAIRE')
window.geometry("625x600+10+10")
window.mainloop()