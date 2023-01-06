<pre>class Student:

	# constructor
	def __init__(self,name,major):
		self._name = name
		self._major = major
		self._course_grades = []	# list of pairs (course,grade)

	# getter
	def get_name(self):
		pass

	# getter
	def	get_major(self):
		pass

	# getter
	def get_course_grades(self):
		pass

	# setter
	def set_major(self,major):
		pass

	# setter
	def set_course_grades(self,grades):
		pass

	# return True if student takes course numbered cno; False otherwise
	def takes_course(self,cno):
		pass

	# return GPA for student (rounded to 2 decimal places)
	def gpa(self):
		pass

	# add pair cg = (course,grade) to course_grades
	def add_course_grade(self,cg):
		pass

	# update grade for course with number cno; new grade is gr
	def update_course_grade(self,cno,gr):
		pass

	# return string representation of student
	# see sample run for exact format to display student object
	def __str__(self):
		pass</pre>
