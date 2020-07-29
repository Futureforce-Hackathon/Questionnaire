from tkinter import *
import tkinter.ttk as ttk
import csv
from tkinter.ttk import Combobox


#########################################################
#TO CLARIFY, THE INFORMATION GIVEN BY THE USER: 
# NAME (string) - firstName, middleInitial, lastName
# GENDER (string) - genderChoice
# EDUCATION (string) - classification
#   YEAR (string) - yearChoice
# ETHNICITY (string) - ethnicChoice
# MAJOR (string) - majorChoice
# SKILLS (list) - skillsList[]
# Look at printInfo() to see how I got the variables
#########################################################




############################################################################################
# getYearNew()
# Function that updates the year when the user changes inputs
############################################################################################
def getYearNew():
    yearLabel = Label(window, text="Undergraduate year?", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
    yearLabel.place(x=25, y=185)
    global yearChoiceB
    yearChoiceB = StringVar()
    yearChoiceB.set("Freshman")
    yearDropdown = OptionMenu(window, yearChoiceB, "Freshman", "Sophomore", "Junior", "Senior")
    yearDropdown.config(bg=bodyColor)
    yearDropdown.place(x=175, y=185)




############################################################################################
# printInfoNew()
# Function that updates users info when they click Refresh
############################################################################################
def printInfoNew(): #FOR TESTING PURPOSES, THIS WILL DISPLAY THE INFO SO FAR
    print("\nNAME: %s %s %s " %(firstNameB.get(), middleInitialB.get(), lastNameB.get()))
    print("GENDER: %s" %(genderChoiceB.get()))
    print("EDUCATION: %s" %(classificationB.get()))

    yearB = "ANY"
    if classificationB.get() == "UNDERGRAD":
         print("YEAR: %s" %(yearChoiceB.get()))
         yearB = yearChoiceB.get()
    print("ETHNICITY: %s" %(ethnicChoiceB.get()))
    print("MAJOR: %s" %(majorChoiceB.get()))
    skillsIndeces = list(map(int, languageDropdown.curselection()))
    skillsList = []
    for i in range(len(skillsIndeces)):
        skillIndex = skillsIndeces[i]
        skillsList.append(languageList[skillIndex])

    print("SKILLS: ", skillsList)   

    filterPrograms(firstNameB.get(), middleInitialB.get(), lastNameB.get(), genderChoiceB.get(), classificationB.get(), yearB, ethnicChoiceB.get(), majorChoiceB.get(), skillsList)




############################################################################################
# filterPrograms()
# Function that will first filter the CSV file using the user inputs and then display them. 
############################################################################################
def filterPrograms(firstNameNew, middleInitialNew, lastNameNew, genderNew, educationNew, yearNew, ethnicityNew, majorNew, skillsNew):
    global TableMargin
    TableMargin = Frame(window, width=1000)
    TableMargin.pack(side=RIGHT)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    global tree
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
    borderCanvas.tag_lower(headerCanvas)
    
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
    tree.column('#0', stretch=YES, minwidth=500, width=500)
    tree.column('#1', stretch=YES, minwidth=175, width=175)
    tree.column('#2', stretch=YES, minwidth=285, width=285)
    tree.column('#3', stretch=YES, minwidth=255, width=255)
    tree.column('#4', stretch=YES, minwidth=120, width=120)
    tree.column('#5', stretch=YES, minwidth=200, width=200)
    tree.column('#6', stretch=YES, minwidth=700, width=700)
    tree.column('#7', stretch=YES, minwidth=400, width=400)

    tree.pack()
    
    #OPENING CVS FILE
    refreshCounts = 0
    filteredPrograms = "filteredPrograms.csv" # separate file that will be shown when filtered
    with open('./Diversity Tech Programs Spreadsheet - Sheet1.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        refreshCounts = refreshCounts + 1
        rowID = 1
        for row in reader:
            rowID = rowID  + 1
            company = row['Company']
            program = row['Program']
            demographic = row['Demographic']
            yearIn = row['Year in College']
            role = row['Role']
            majors = row['Majors']
            skills = row['Programming Languages/Software']
            
            if str(ethnicityNew) in str(demographic):
                print("\nETHNICITY + DEMOGRAPHIC == ", ethnicityNew, demographic)
                tree.insert("", 0, values=(company, program, demographic, yearIn, role, majors, skills))

            ##########################################
            #    FILTERING ALGORITHM WILL GO HERE    #
            ##########################################


    print("4444444444444444444444444444444444444444444444444444444444444\n")

    #FIRST NAME
    firstLabel = Label(window, text="First name: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
    global firstNameB
    firstNameB = StringVar()
    firstNameBLabel = Label(window, text=firstNameNew, font='Helvetica 13 bold', bg=headerColor, fg=headerTextColor)
    firstLabel.place(x=15, y=17)
    firstNameBLabel.place(x=105,y=16)
    # global firstNameB
    # firstNameB = StringVar()
    # firstNameB = Entry(window, width=10, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
    # firstNameB.place(x=105, y=16)

    #MIDDLE INITIAL
    middleLabel = Label(window, text="MI: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
    middleLabel.place(x=190, y=17)
    global middleInitialB
    middleInitialB = StringVar()
    middleInitialBLabel = Label(window, text=middleInitialNew, font='Helvetica 13 bold', bg=headerColor, fg=headerTextColor)
    # middleInitialB = Entry(window, width=2, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
    middleInitialBLabel.place(x=230, y=16)

    #LAST NAME
    lastLabel = Label(window, text="Last name: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
    lastLabel.place(x=250, y=17)
    global lastNameB
    lastNameB = StringVar()
    lastNameBLabel = Label(window, text=lastNameNew, font='Helvetica 13 bold', bg=headerColor, fg=headerTextColor)
    # lastNameB = Entry(window, width=10, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
    lastNameBLabel.place(x=340, y=16)

    #GENDER
    chooseGenderLabel = Label(window, text="Please choose your current preferred gender: ", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
    chooseGenderLabel.place(x=25, y=60)
    global genderChoiceB
    genderChoiceB = StringVar(window)
    genderChoiceB.set(genderNew)
    genderDropdown = OptionMenu(window, genderChoiceB, "Female", "Male", "Genderfluid", "Other")
    genderDropdown.config(bg=bodyColor)
    genderDropdown.place(x=25, y=85)

    #CLASSIFICATION / EDUCATION LEVEL
    classificationLabel = Label(window, text="Current education level?", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
    classificationLabel.place(x=25, y=130)
    global classificationB
    classificationB = StringVar()
    highschool = Radiobutton(window, text="High School", variable=classificationB, value="HS")
    highschool.config(bg=bodyColor, fg=bodyTextColor)
    highschool.place(x=25, y=150)
    undergraduate = Radiobutton(window, text="Undergraduate", variable=classificationB, value="UNDERGRAD", command=getYearNew)
    undergraduate.config(bg=bodyColor, fg=bodyTextColor)
    undergraduate.place(x=130, y=150)
    graduate = Radiobutton(window, text="Graduate", variable=classificationB, value="GRAD")
    graduate.config(bg=bodyColor, fg=bodyTextColor)
    graduate.place(x=255, y=150)
    otherEducation = Radiobutton(window, text="Other", variable=classificationB, value="OTHER")
    otherEducation.config(bg=bodyColor, fg=bodyTextColor)
    otherEducation.place(x=345, y=150)
    classificationB.set(educationNew)

    #ETHNICITY 
    ethnicityLabel = Label(window, text="What is your ethnicity?", font="Helvetica 13 italic", bg=bodyColor, fg=bodyTextColor)
    ethnicityLabel.place(x=25, y=210)
    global ethnicChoiceB
    ethnicChoiceB = StringVar()
    ethnicChoiceB.set(ethnicityNew)
    ethnicityDropdown = OptionMenu(window, ethnicChoiceB, "American Indian/Alaska Native", "Asian", "African American", "Black", "Indian", "Latino", "Native Hawaiian/Other Pacific Islander", "White")
    ethnicityDropdown.config(bg=bodyColor, fg=bodyTextColor)
    ethnicityDropdown.place(x=175, y=210)

    #MAJOR 
    majorLabel = Label(window, text="What is your major?", font="Helvetica 13 italic", bg=bodyColor, fg=bodyTextColor)
    majorLabel.place(x=25, y=235)
    global majorChoiceB
    majorChoiceB = StringVar()
    majorChoiceB.set(majorNew)
    majorDropdown = OptionMenu(window, majorChoiceB, 
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
                                "Software Engineering",
                                "Theology, Religious Vocations",
                                "Transportation/ Materials Moving",
                                "Visual and Performing Arts",
                                "None/Other")
    majorDropdown.config(bg=bodyColor)
    majorDropdown.place(x=175, y=235)

    #PROGRAMMING LANGUAGES
    languagesLabel = Label(window, text="Select any programming skills you know (scroll): ", font="Helvetica 13 italic", bg=skillsColor, fg=skillsTextColor)
    languagesLabel.place(x=20, y=290)
    global languageDropdown
    languageDropdown = Listbox(window, selectmode = "multiple", bd=1, selectbackground="#bee6e5", bg="#e1e8e8")
    languageDropdown.place(x=25, y=315)
    global languageList
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


    giveInfo = Button(window, highlightbackground = skillsColor, font="Helvetica 13", text="Refresh", command = printInfoNew)
    giveInfo.place(x=25, y=500)


############################################################################################
# getYear()
# Function that displays the "Undergraduate year?" label and entry box for undergraduates.
############################################################################################
def getYear():
    yearLabel = Label(window, text="Undergraduate year?", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
    yearLabel.place(x=25, y=185)
    global yearChoice 
    yearChoice = StringVar()
    yearChoice.set("Freshman")
    yearDropdown = OptionMenu(window, yearChoice, "Freshman", "Sophomore", "Junior", "Senior")
    yearDropdown.config(bg=bodyColor)
    yearDropdown.place(x=175, y=185)




############################################################################################
# printInfo()
# Temp function that prints the info the user has input. 
# This function then calls the filterPrograms() function.
############################################################################################
def printInfo(): #FOR TESTING PURPOSES, THIS WILL DISPLAY THE INFO SO FAR
    print("\nNAME: %s %s %s " %(firstName.get(), middleInitial.get(), lastName.get()), "TYPES: ", type(firstName.get()), type(middleInitial.get()), type(lastName.get()))
    print("GENDER: %s" %(genderChoice.get()), type(genderChoice.get()))
    print("EDUCATION: %s" %(classification.get()), type(classification.get()))

    year = "ANY"
    if classification.get() == "UNDERGRAD":
         print("YEAR: %s" %(yearChoice.get()), type(yearChoice.get()))
         year = yearChoice.get()
    print("ETHNICITY: %s" %(ethnicChoice.get()), type(ethnicChoice.get()))
    print("MAJOR: %s" %(majorChoice.get()), type(majorChoice.get()))
    skillsIndeces = list(map(int, languageDropdown.curselection()))
    skillsList = []
    for i in range(len(skillsIndeces)):
        skillIndex = skillsIndeces[i]
        skillsList.append(languageList[skillIndex])

    print("SKILLS: ", skillsList, type(skillsList))   

    filterPrograms(firstName.get(), middleInitial.get(), lastName.get(), genderChoice.get(), classification.get(), year, ethnicChoice.get(), majorChoice.get(), skillsList)

    #TO CLARIFY, THE INFORMATION GIVEN BY THE USER: 
    # NAME (string) - firstName, middleInitial, lastName
    # GENDER (string) - genderChoice
    # EDUCATION (string) - classification
    #   YEAR (string) - yearChoice
    # ETHNICITY (string) - ethnicChoice
    # MAJOR (string) - majorChoice
    # SKILLS (list) - skillsList[]




############################################################################################
# Main portion of the program
############################################################################################
def main():
    global window
    window = Tk()
    window.title('QUESTIONNAIRE')

    #DISPLAY CSV 
    width = 1300
    height = 550
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight() 
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2) 
    window.geometry("%dx%d+%d+%d" %(width, height, x, y)) 

    # TableMargin = Frame(window, width=10)
    # TableMargin.pack(side=LEFT)
    # scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    # scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    # tree = ttk.Treeview(TableMargin, columns=("Company", "Program", "Demographic", "Year in College", "Role", "Majors", 'Programming Languages/Software'), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)


    #COLORS FOR LEFT SIDE
    global headerColor
    headerColor = "#f1faee"
    global headerTextColor
    headerTextColor = "black"
    global bodyColor
    bodyColor = "#a8dadc"
    global bodyTextColor
    bodyTextColor = "black"
    global skillsColor
    skillsColor = "#457b9d"
    global skillsTextColor
    skillsTextColor = "white"

    #STYLING FOR LEFT SIDE
    headerCanvas = Canvas(window, width=490, height=50, bg=headerColor, highlightbackground=headerColor)
    headerCanvas.pack(side=LEFT)
    headerCanvas.place(x=0)
    headerCanvas.tag_lower(headerCanvas)

    bodyCanvas = Canvas(window, width=490, height=600, bg=bodyColor, highlightbackground=bodyColor)
    bodyCanvas.pack(side=LEFT)
    bodyCanvas.place(x=0,y=50)
    bodyCanvas.tag_lower(headerCanvas)

    skillsCanvas = Canvas(window, width=490, height=500, bg=skillsColor, highlightbackground=skillsColor)
    skillsCanvas.pack(side=LEFT)
    skillsCanvas.place(x=0, y=280)
    skillsCanvas.tag_lower(bodyCanvas)

    borderCanvas = Canvas(window, width=2, height=1000, bg="#1d3557", highlightbackground="#1d3557")
    borderCanvas.pack(side=LEFT)
    borderCanvas.place(x=490, y=0)
    borderCanvas.tag_raise(headerCanvas)

    # SCROLLING FOR RIGHT SIDE
    # scrollbary.config(command=tree.yview)
    # scrollbary.pack(side=RIGHT, fill=Y)
    # scrollbarx.config(command=tree.xview)
    # scrollbarx.pack(side=BOTTOM, fill=X)
    # tree.heading('Company', text="Company", anchor=W)
    # tree.heading('Program', text="Program", anchor=W)
    # tree.heading('Demographic', text="Demographic", anchor=W)
    # tree.heading('Year in College', text="Year in College", anchor=W)
    # tree.heading('Role', text="Role", anchor=W)
    # tree.heading('Majors', text="Majors", anchor=W)
    # tree.heading('Programming Languages/Software', text="Programming Languages/Software", anchor=W)
    # tree.column('#0', stretch=YES, minwidth=510, width=500)
    # tree.column('#1', stretch=YES, minwidth=175, width=175)
    # tree.column('#2', stretch=YES, minwidth=285, width=285)
    # tree.column('#3', stretch=YES, minwidth=255, width=255)
    # tree.column('#4', stretch=YES, minwidth=120, width=120)
    # tree.column('#5', stretch=YES, minwidth=200, width=200)
    # tree.column('#6', stretch=YES, minwidth=700, width=700)
    # tree.column('#7', stretch=YES, minwidth=400, width=400)

    # tree.pack()

    #OPENING CVS FILE
    # with open('./Diversity Tech Programs Spreadsheet - Sheet1.csv') as f:
    #     reader = csv.DictReader(f, delimiter=',')
    #     for row in reader:
    #         company = row['Company']
    #         program = row['Program']
    #         demographic = row['Demographic']
    #         yearIn = row['Year in College']
    #         role = row['Role']
    #         majors = row['Majors']
    #         skills = row['Programming Languages/Software']
    #         tree.insert("", 0, values=(company, program, demographic, yearIn, role, majors, skills))


    #FIRST NAME
    firstLabel = Label(window, text="First name: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
    firstLabel.place(x=25, y=17)
    global firstName
    firstName = StringVar(window)
    firstName = Entry(window, width=10, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
    firstName.place(x=105, y=16)

    #MIDDLE INITIAL
    middleLabel = Label(window, text="MI: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
    middleLabel.place(x=200, y=17)
    global middleInitial
    middleInitial = StringVar() #SHOULD I KEEP THIS?
    middleInitial = Entry(window, width=2, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
    middleInitial.place(x=230, y=16)

    #LAST NAME
    lastLabel = Label(window, text="Last name: ", font='Helvetica 13 italic', bg=headerColor, fg=headerTextColor)
    lastLabel.place(x=260, y=17)
    global lastName
    lastName = StringVar() #SHOULD I KEEP THIS?
    lastName = Entry(window, width=10, borderwidth=0.5, highlightthickness=0.5, highlightcolor="#b8b8b8", bg="#E5F6DF")
    lastName.place(x=340, y=16)

    #GENDER
    chooseGenderLabel = Label(window, text="Please choose your current preferred gender: ", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
    chooseGenderLabel.place(x=25, y=60)
    global genderChoice
    genderChoice = StringVar(window)
    genderChoice.set("Other")
    genderDropdown = OptionMenu(window, genderChoice, "Female", "Male", "Genderfluid", "Other")
    genderDropdown.config(bg=bodyColor)
    genderDropdown.place(x=25, y=85)

    #CLASSIFICATION / EDUCATION LEVEL
    classificationLabel = Label(window, text="Current education level?", font='Helvetica 13 italic', bg=bodyColor, fg=bodyTextColor)
    classificationLabel.place(x=25, y=130)
    global classification 
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
    global ethnicChoice
    ethnicChoice = StringVar()
    ethnicChoice.set("American Indian/Alaska Native")
    ethnicityDropdown = OptionMenu(window, ethnicChoice, "American Indian/Alaska Native", "Asian", "African American", "Black", "Indian", "Latino", "Native Hawaiian/Other Pacific Islander", "White")
    ethnicityDropdown.config(bg=bodyColor, fg=bodyTextColor)
    ethnicityDropdown.place(x=175, y=210)

    #MAJOR 
    majorLabel = Label(window, text="What is your major?", font="Helvetica 13 italic", bg=bodyColor, fg=bodyTextColor)
    majorLabel.place(x=25, y=235)
    global majorChoice
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
                                "Software Engineering",
                                "Theology, Religious Vocations",
                                "Transportation/ Materials Moving",
                                "Visual and Performing Arts",
                                "None/Other")
    majorDropdown.config(bg=bodyColor)
    majorDropdown.place(x=175, y=235)

    #PROGRAMMING LANGUAGES
    languagesLabel = Label(window, text="Select any programming skills you know (scroll): ", font="Helvetica 13 italic", bg=skillsColor, fg=skillsTextColor)
    languagesLabel.place(x=20, y=290)
    global languageDropdown
    languageDropdown = Listbox(window, selectmode = "multiple", bd=1, selectbackground="#bee6e5", bg="#e1e8e8")
    languageDropdown.place(x=25, y=315)
    global languageList
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


    window.mainloop()

if __name__ == "__main__":
    main()