teachers = ["Barry", "Bell", "Epstein", "Hayes", "Hicks", "Miller", "Neubauer"]
classes = ["Tech Edge", "Marketing", "Programming 1", "APCS", "Accounting", "Consumer Ed", "Business Law"]

inum = teachers.index("Barry")
teachers[inum] = "Pitt"

classes[2:4] = ["Intro to Business", "Programming 2"]

inum = teachers.index("Bell")
del teachers[inum]
del classes[inum]

for num in range(len(teachers)):
    print("{:<20}{:<20}".format(teachers[num], classes[num]))

search = input("\nEnter a teacher's last name: ")
if search.title() in teachers:
    print(search, "teaches a business class at NCHS")
else: 
    print(search, "DOESN'T teach a business class at NCHS")
    

inum = teachers.index("Epstein")
print(teachers[inum], "teaches", classes[inum])

print(teachers[4:])