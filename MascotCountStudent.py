# @author Emaad Gafoor

def main():
    schools = getSchoolMascots("KansasHighSchoolsSubsetUnclean.txt")
    #schools = getSchoolMascots("TestMascotCount.txt")
    mascotCount = getMascotCount(schools)
    showMascotCount(mascotCount)
    
# getSchoolMascots reads each school and their mascot from the given file.
# @param filename The file containing the schools and mascots.
# @precondition Each line in the file is of the form school:mascot
# @return schoolDictionary A dictionary of school-mascot pairs   
def getSchoolMascots(filename):
    input = open(filename,"r")
    schoolDictionary = {}
    for school in input:
        school = school.split(":")
        school[0] = school[0].strip().title()
        school[1] = school[1].strip().title()
        schoolDictionary[school[0]] = school[1]
    input.close()
    return schoolDictionary

# getMascotCount tallies the number of times each mascot occurs
# @param schools A dictionary of school-mascot pairs
# @return mascotCount A dictionary of mascot-count pairs
def getMascotCount(schools):
    mascotCount = {}
    for mascot in schools.values():
        if mascot in mascotCount.keys():
            mascotCount[mascot] = (mascotCount[mascot] + 1)
        else:
            mascotCount[mascot] = 1
    return mascotCount

# showMacotCount displays the mascots in sorted order. Each mascot 
# count is shown by the mascot.
# @param mascotCount A dictionary containing each mascot and the number
#        of times it occurred.
def showMascotCount(mascotCount):
    for mascot in sorted(mascotCount.items()):
        print(f"{mascot[0]}: {mascot[1]}")
main()