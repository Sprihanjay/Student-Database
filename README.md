# Student Database
Python program to keep track of courses, students, and their grades in courses they have taken.

In this programming assignment, I developed a Python program to keep track of courses, students, and their grades in courses they have taken.

We will use four Python Classes:

1.  **Course.py**: encapsulates information such as cno, ctitle, and credits for the course object. The constructor method is shown below:
    <pre>
    def __init__(self,cn,ct,cr):
    	self._cno = cn
    	self._ctitle = ct
    	self._credits = cr
      </pre>
    
2.  **Courses.py**: encapsulates information about ALL courses in a dictionary format. The course number will serve as the "key" in the dictionary and the Course object containing details of the course will serve as the value for the key. The constructor method is shown below:
    <pre>
    def __init__(self):
    	self._data = {}
      </pre>
    
3.  **Student.py**: encapsulates information such as name, major, and courses taken by student and provides certain methods to operate on Student objects. The constructor method is shown below:
    <pre>
    def __init__(self,name,major):
    		self._name = name
    		self._major = major
    		self._course_grades = []   # list of pairs (course,grade)</pre>
    
4.  **Students.py**: encapsulates information about ALL students in a dictionary format. The student name will serve as the "key" in the dictionary and the Student object containing details of the student will serve as the value for the key. The Students class also provides useful methods that access and manipulate the data about students. The constructor method is shown below:
    <pre>
    def __init__(self):
    	self._data = {}</pre>
    

The program takes the name of a folder as command-line argument. This folder should contain three data files:
<pre>
data/courses.dat
data/students.dat
data/grades.dat</pre>

The courses.dat file contains course number, course title, and credits (one course per line) with the ":" symbol separating the values.

The students.dat file contains names of students and their majors (one student per line) with the ":" symbol separating the values.

The grades.dat file contains courses taken by students along with the letter grade received by the student in the course. We will assume 5 letter grades (A, B, C, D, and F). Again, one course per line with values separated by ":".

Your program should make sure that you do not have a situation where a student takes a course that is not in the courses.dat file. If such a situation occurs, you should flag an error and skip the record.

The following are skeleton files for you to use in the assignment:
<pre>
Course.md
Courses.md
Student.md
Students.md
Driver.md
</pre>

Sample run of the program is shown below:
<pre>
Mac-mini:p5-grades sb$ python3 Driver.py data

Welcome to Grades Database Program

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: p

Name: Blake
Major: CSC
CSC1301:Principles of Computer Science I:4 GRADE = B
CSC1302:Principles of Computer Science II:4 GRADE = B
CSC2720:Data Structures:3 GRADE = B
CSC3320:Systems Level Programming:3 GRADE = B
GPA: 3.0

Name: Jones
Major: CSC
CSC1301:Principles of Computer Science I:4 GRADE = A
CSC1302:Principles of Computer Science II:4 GRADE = A
CSC2720:Data Structures:3 GRADE = B
CSC2720:Data Structures:3 GRADE = C
CSC3320:Systems Level Programming:3 GRADE = D
GPA: 2.94

Name: Smith
Major: MATH
CSC1301:Principles of Computer Science I:4 GRADE = B
CSC1302:Principles of Computer Science II:4 GRADE = B
CSC2720:Data Structures:3 GRADE = B
GPA: 3.0

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: s Smith

Name: Smith
Major: MATH
CSC1301:Principles of Computer Science I:4 GRADE = B
CSC1302:Principles of Computer Science II:4 GRADE = B
CSC2720:Data Structures:3 GRADE = B
GPA: 3.0

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: s Sunderraman

Sunderraman NOT FOUND

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: m CSC

Jones	2.94
Blake	3.0

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: m MATH

Smith	3.0

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: m aaa

NO Students FOUND!

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: g 2.0

Smith	MATH	3.0
Blake	CSC	3.0
Jones	CSC	2.94

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: g 3.0

Smith	MATH	3.0
Blake	CSC	3.0

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: a Smith:CSC3320:A

 ['Smith', 'CSC3320', 'A']  ADDED

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: s Smith

Name: Smith
Major: MATH
CSC1301:Principles of Computer Science I:4 GRADE = B
CSC1302:Principles of Computer Science II:4 GRADE = B
CSC2720:Data Structures:3 GRADE = B
CSC3320:Systems Level Programming:3 GRADE = A
GPA: 3.21

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: c Smith:CSC3320:B
GRADE CHANGED


p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: s Smith

Name: Smith
Major: MATH
CSC1301:Principles of Computer Science I:4 GRADE = B
CSC1302:Principles of Computer Science II:4 GRADE = B
CSC2720:Data Structures:3 GRADE = B
CSC3320:Systems Level Programming:3 GRADE = B
GPA: 3.0

p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: q

Bye!

Mac-mini:p5-grades sb$</pre>
