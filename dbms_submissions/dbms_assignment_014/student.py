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
    
    @classmethod
    def avg(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
                raise InvalidField
                
        if len(kwargs)>=1:
            temp = Student.filter(**kwargs)
            query = "select avg({}) from student where {} ".format(field, temp)
        else:
            query = "select avg({}) from student ".format(field)        
    
        final_output = read_data(query)
        return final_output[0][0]
       
    @classmethod
    def min(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
                raise InvalidField
        
        if len(kwargs)>=1:
            temp = Student.filter(**kwargs)
            query = "select min({}) from student where {} ".format(field, temp)
        else:
            query = "select min({}) from student ".format(field)        
    
        
        final_output = read_data(query)
        return final_output[0][0]
    
    @classmethod
    def max(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
                raise InvalidField
        
        if len(kwargs)>=1:
            temp = Student.filter(**kwargs)
            query = "select max({}) from student where {} ".format(field, temp)
        else:
            query = "select max({}) from student ".format(field)        
    
        
        final_output = read_data(query)
        return final_output[0][0]    

    @classmethod
    def sum(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
                raise InvalidField
        
        if len(kwargs)>=1:
            temp = Student.filter(**kwargs)
            query = "select sum({}) from student where {} ".format(field, temp)
        else:
            query = "select sum({}) from student ".format(field)        
    
        
        final_output = read_data(query)
        return final_output[0][0]
    
    @classmethod
    def count(cls, field = None, **kwargs):
        if field == None:
            query = "select count(*) from Student"
        elif field not in ('name','age','score','student_id'):
                raise InvalidField
        elif len(kwargs)>=1:
            temp = Student.filter(**kwargs)
            query = "select count({}) from student where {} ".format(field, temp)
        else:
            query = "select count({}) from student ".format(field)        
    
        
        final_output = read_data(query)
        return final_output[0][0]
        
    
    @classmethod
    def filter(cls, **data):
        cls.details=[]
        cls.operator={'lt':'<', 'lte':'<=', 'gt':'>', 'gte':'>=', 'neq':'!=', 'in':'in','contain':''}

        if len(data) >= 1:
            temp = []
            for ke,val in data.items():
                cls.key = ke
                cls.value = val
				
                fields = cls.key
                fields = fields.split('__')
				
                if fields[0] not in ('name','age','score','student_id'):
                    raise InvalidField 
                elif len(fields) == 1:
                    query = " {} ='{}'".format(cls.key, cls.value)
                elif fields[1] == 'contains':
                    query = " {} like '%{}%'".format(fields[0],cls.value)
                elif fields[1] == 'in':
                    query = " {} {} {}".format(fields[0],cls.operator[fields[1]],tuple(cls.value))
                else:
                    query = "{} {} '{}'".format(fields[0],cls.operator[fields[1]],cls.value)
                temp.append(query)
                    
            additional_condition = " and ".join(temp)       
            query= " " + additional_condition
            
        return query