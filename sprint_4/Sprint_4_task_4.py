class Testpaper:
    def __init__(self, dis, tAns, minPoint):
        self.subject = dis
        self.markscheme = tAns
        self.pass_mark = minPoint


class Student:
    def __init__(self):
        self.knt = 0
        self.tests_taken = "No tests taken"

    def take_test(self, paper, studentAns):
        goodAns = []
        if self.knt == 0:
            self.tests_taken = {}
        self.knt += 1
        for stAns in studentAns:
            if stAns in paper.markscheme:
                goodAns.append(stAns)
        res = round(len(goodAns)/len(paper.markscheme)*100)
        if int(paper.pass_mark[:-1]) <= res:
            self.tests_taken[paper.subject] = f"Passed! ({res}%)"
        else:
            self.tests_taken[paper.subject] = f"Failed! ({res}%)"





paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()

print(student1.tests_taken)  # ➞ "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken)  # ➞ {"Maths" : "Passed! (80%)"}

student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken)  # ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}
