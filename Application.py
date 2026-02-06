import pandas as pd
import time

class Application:
    def __init__(self):
        self.fileoutputs = {
            "Class List": "ClassList.txt",
            "Class List Trimmed": "ClassListFinal.txt",
            "Class List Eighth Grade": "ClassList8thGrade.txt",
            "Class List School X": "ClassListSchoolX.txt",
            "Class List School Y": "ClassListSchoolY.txt",
            "Class List School Z": "ClassListSchoolZ.txt",
            "Student List Final": "StudentListFinal.txt"
            }
        self.LtN = {
            "A+": 97,
            "A": 93,
            "A-": 90,
            "B+": 87,
            "B": 83,
            "B-": 80,
            "C+": 77,
            "C": 73,
            "C-": 70,
            "D+": 67,
            "D": 63,
            "D-": 60,
            "F": 0
        }
        self.classMemberCuttoff = 10
        for filename in self.fileoutputs.values():
            with open(filename, 'w') as f:
                f.write("")  # Clear the file contents

    def RUN(self):
        # Cleared for Anonymity
        filepath = input("Enter the Excel file name: ")
        schoolXName = input("Enter the name of School X as found in data: ")
        schoolYName = input("Enter the name of School Y as found in data: ")
        schoolZName = input("Enter the name of School Z as found in data: ")
        schoolCName = input("Enter the name of School C as found in data: ")

        # Parse File
        start_time = time.perf_counter()
        print("File Parsing Started")
        df = pd.read_excel(filepath)
        print("File Parsed Successfully")
        
        # Exclude Special Education Center
        print("Excluding Special Education Center Started")
        df = df[df["School Name"] != schoolCName]
        print("Exclusion Special Education Center Finished")

        # Exclude Virtual Classes
        print("Excluding Classes Started")
        f = open("ExclusionList.txt", "r")
        excludeList = f.readlines()
        f.close()
        for i in excludeList:
            df = df[df["Course Name"] != i.strip()]
        print("Exclusion Classes Finished")

        # List All Classes
        print("Class List Generation Started")
        classList = []
        classFinalList = []
        for i in df["Course Name"].unique():
            # For each class, run through once
            studentCount = 0
            for j in df[df["Course Name"] == i]["Student #"]:
                studentCount += 1
            classList.append((i, studentCount))

            # Trim Classes Below Cutoff
            if studentCount >= self.classMemberCuttoff:
                classFinalList.append((i, studentCount))
        print("Class List Generated Finished")

        # Seperate Specific Class Lists
        print("Class Separation Started")
        classEighthGradeList = []
        classSchoolXList = []
        classSchoolYList = []
        classSchoolZList = []
        for i in classFinalList:
            # Seperate 8th Grade Classes
            for k in df[df["Course Name"] == i[0]]["Grade"]:
                if k == 8:
                    classEighthGradeList.append(i)
                    break
            
            # Seperate School X Classes
            for l in df[df["Course Name"] == i[0]]["School Name"]:
                if l == schoolXName:
                    classSchoolXList.append(i)
                    break
            
            # Seperate School Y Classes
            for m in df[df["Course Name"] == i[0]]["School Name"]:
                if m == schoolYName:
                    classSchoolYList.append(i)
                    break
            
            # Seperate School Z Classes
            for n in df[df["Course Name"] == i[0]]["School Name"]:
                if n == schoolZName:
                    classSchoolZList.append(i)
                    break
        print("Class Separation Finished")

        #Get 8th Grade Class Adverages
        # print("8th Grade Class Average Calculation Started")
        # for i in classEighthGradeList:
        #     totalScore = 0
        #     for j in df[df["Course Name"] == i[0]]["Final Score"]:
        #         totalScore += self.LtN[j]
        #     averageScore = totalScore / i[1]
        #     print(f"Class: {i[0]} - Average Score: {averageScore:.2f}")
        # print("8th Grade Class Average Calculation Finished")


        # Print Outputs
        print("Output Started")
        for i in classList:
            self.PrintToFile("Class List", f"{i[0]} - {i[1]} students\n")
        for i in classFinalList:
            self.PrintToFile("Class List Trimmed", f"{i[0]} - {i[1]} students\n")
        for i in classEighthGradeList:
            self.PrintToFile("Class List Eighth Grade", f"{i[0]} - {i[1]} students\n")
        for i in classSchoolXList:
            self.PrintToFile("Class List School X", f"{i[0]} - {i[1]} students\n")
        for i in classSchoolYList:
            self.PrintToFile("Class List School Y", f"{i[0]} - {i[1]} students\n")
        for i in classSchoolZList:
            self.PrintToFile("Class List School Z", f"{i[0]} - {i[1]} students\n")
        for i in df["Student #"].unique():
            self.PrintToFile("Student List Final", f"{i}\n")
        print("Output Finished")
        # Conclusion
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Program Completed Successfully in {elapsed_time:.2f} Seconds.")

    def PrintToFile(self, fileAbriviation, content):
        filename = self.fileoutputs[fileAbriviation]
        with open(filename, 'a') as file:
            file.write(content)

        
    
