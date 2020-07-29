from tkinter import *
import tkinter.ttk as ttk
import csv
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
window.title('QUESTIONNAIRE')

#DISPLAY CSV 
width = 1300
height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() 
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2) 
window.geometry("%dx%d+%d+%d" %(width, height, x, y)) 

TableMargin = Frame(window, width=1000)
TableMargin.pack(side=RIGHT)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Company", "Program", "Demographic", "Year in College", "Role", "Majors", 'Programming Languages/Software'), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)


#COLORS FOR LEFT SIDE
headerColor = "#f1faee"
headerTextColor = "black"
bodyColor = "#a8dadc"
bodyTextColor = "black"
skillsColor = "#457b9d"
skillsTextColor = "white"

#STYLING FOR LEFT SIDE
headerCanvas = Canvas(TableMargin, width=490, height=50, bg=headerColor, highlightbackground=headerColor)
headerCanvas.pack(side=LEFT)
headerCanvas.place(x=0)
headerCanvas.tag_lower(headerCanvas)

bodyCanvas = Canvas(TableMargin, width=490, height=600, bg=bodyColor, highlightbackground=bodyColor)
bodyCanvas.pack(side=LEFT)
bodyCanvas.place(x=0,y=50)
bodyCanvas.tag_lower(headerCanvas)

skillsCanvas = Canvas(TableMargin, width=490, height=500, bg=skillsColor, highlightbackground=skillsColor)
skillsCanvas.pack(side=LEFT)
skillsCanvas.place(x=0, y=280)
skillsCanvas.tag_lower(bodyCanvas)

borderCanvas = Canvas(TableMargin, width=2, height=1000, bg="#1d3557", highlightbackground="#1d3557")
borderCanvas.pack(side=LEFT)
borderCanvas.place(x=490, y=0)
borderCanvas.tag_raise(headerCanvas)

#SCROLLING FOR CVS FILE
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Company', text="Company", anchor=W)
tree.heading('Program', text="Program", anchor=W)
tree.heading('Demographic', text="Demographic", anchor=W)
tree.heading('Year in College', text="Year in College", anchor=W)
tree.heading('Role', text="Role", anchor=W)
tree.heading('Majors', text="Majors", anchor=W)
tree.heading('Programming Languages/Software', text="Programming Languages/Software", anchor=W)
tree.column('#0', stretch=YES, minwidth=510, width=500)
tree.column('#1', stretch=YES, minwidth=175, width=175)
tree.column('#2', stretch=YES, minwidth=285, width=285)
tree.column('#3', stretch=YES, minwidth=255, width=255)
tree.column('#4', stretch=YES, minwidth=120, width=120)
tree.column('#5', stretch=YES, minwidth=200, width=200)
tree.column('#6', stretch=YES, minwidth=700, width=700)
tree.column('#7', stretch=YES, minwidth=400, width=400)

tree.pack()

#OPENING CVS FILE
with open('./Diversity Tech Programs Spreadsheet - Sheet1.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        company = row['Company']
        program = row['Program']
        demographic = row['Demographic']
        yearIn = row['Year in College']
        role = row['Role']
        majors = row['Majors']
        skills = row['Programming Languages/Software']
        tree.insert("", 0, values=(company, program, demographic, yearIn, role, majors, skills))


#FIRST NAME
firstLabel = Label(window, text="First name: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
firstLabel.place(x=25, y=17)
firstName = StringVar(window)
firstName = Entry(window, width=10, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
firstName.place(x=105, y=16)

#MIDDLE INITIAL
middleLabel = Label(window, text="MI: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
middleLabel.place(x=200, y=17)
middleInitial = Entry(window, width=2, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
middleInitial.place(x=230, y=16)

#LAST NAME
lastLabel = Label(window, text="Last name: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
lastLabel.place(x=260, y=17)
lastName = Entry(window, width=10, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
lastName.place(x=340, y=16)

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
undergraduate.place(x=130, y=150)
graduate = Radiobutton(window, text="Graduate", variable=classification, value="GRAD")
graduate.config(bg=bodyColor, fg=bodyTextColor)
graduate.place(x=255, y=150)
otherEducation = Radiobutton(window, text="Other", variable=classification, value="OTHER")
otherEducation.config(bg=bodyColor, fg=bodyTextColor)
otherEducation.place(x=345, y=150)

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


# window.geometry("1300x600+10+10")
# window.resizable(True, True)
window.mainloop()