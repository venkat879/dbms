class DoesNotExist(Exception):
	pass

class MultipleObjectsReturned(Exception):
	pass

class InvalidField(Exception):
	pass

def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor()
	crsr.execute("PRAGMA foreign_keys=on;")
	crsr.execute(sql_query)
	connection.commit()
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query)
	ans= crsr.fetchall()
	connection.close()
	return ans
	
class Student:
	def __init__(self, name, age, score):
		self.name = name
		self.student_id = None
		self.age = age
		self.score = score
		
	def save(self):
		if self.student_id == None:
			query="insert into student(name,age,score) values ('{}',{},{})".format(self.name,self.age,self.score)
			write_data(query)
			q1='select student_id from student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
			a=read_data(q1)   
			self.student_id=a[0][0]
		else:
			sql_query="update student set student_id={},name='{}',age={},score={} where student_id={}".format(self.student_id,self.name,self.age,self.score,self.student_id)
			write_data(sql_query) 
		
		q = "select * from student where student_id={}".format(self.student_id)	
		obj = read_data(q)
		
		if len(obj)==0:
			query ="insert into student(student_id,name,age,score) values({},'{}',{},{})".format(self.student_id,self.name,self.age,self.score)
			write_data(query)
		
	def delete(self):
		sql_query="delete from student where student_id={}".format(self.student_id)
		write_data(sql_query)
		
	@classmethod
	def get(cls, **keys):
		for k,v in keys.items():
			cls.a=k
			cls.b=v
			if str(k) not in ('name','age','score','student_id'):
				raise InvalidField
           
			query="select * from student where {} = '{}'".format(cls.a,cls.b)
        
		obj=read_data(query)
		if len(obj)>1:
			raise MultipleObjectsReturned
		elif len(obj)==0:
			raise DoesNotExist
		elif len(obj)==1:
			c=Student(obj[0][1],obj[0][2],obj[0][3])
			c.student_id=obj[0][0]
			return c
    
	
	