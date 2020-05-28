Q1 ="""SELECT id, fname FROM Director
    WHERE EXISTS(SELECT did FROM MovieDirector 
    INNER JOIN Movie ON mid=id WHERE Movie.year > 2000 AND did==Director.id)
    AND NOT EXISTS(SELECT did FROM MovieDirector 
    INNER JOIN Movie ON id=mid 
    WHERE Movie.year<2000 AND did=Director.id)ORDER BY Director.id ASC;"""
    
Q2 ="""SELECT fname, (SELECT name FROM Movie INNER JOIN MovieDirector on `Movie`.id==`MovieDirector`.mid 
    WHERE did==`Director`.id ORDER BY rank DESC, name ASC LIMIT 1) AS name FROM Director LIMIT 100;"""
    
Q3 ="""SELECT * FROM Actor WHERE 
    NOT EXISTS(SELECT pid FROM Cast INNER JOIN Movie ON mid=id WHERE year between 1990 AND 2000 AND (pid=`Actor`.id)) 
    ORDER BY Actor.id DESC LIMIT 100;"""