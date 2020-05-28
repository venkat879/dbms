Q1 ="SELECT COUNT(id) FROM Movie WHERE year < 2000;"
Q2 ="SELECT AVG(rank) FROM Movie WHERE year = 1991;"
Q3 ="SELECT MIN(rank) FROM Movie WHERE year = 1991;"
Q4 ="SELECT fname, lname FROM Actor INNER JOIN Cast on `Actor`.id==`Cast`.pid WHERE `Cast`.mid = 27;"
Q5 ="SELECT COUNT(mid) FROM Actor INNER JOIN Cast on `Actor`.id==`Cast`.pid WHERE fname = 'Jon' AND lname = 'Dough';"
Q6 ="SELECT name AS names FROM Movie WHERE name LIKE 'Young Latin Girls%' AND year between 2003 and 2006;"
Q7 ="SELECT fname, lname FROM Director INNER JOIN MovieDirector on `Director`.id==`MovieDirector`.did INNER JOIN Movie on `Movie`.id=`MovieDirector`.mid WHERE name LIKE 'Star Trek%';"
Q8 ="SELECT name FROM Movie INNER JOIN MovieDirector on `Movie`.id==`MovieDirector`.mid INNER JOIN Director on `Director`.id==`MovieDirector`.did INNER JOIN Cast on `Cast`.mid==`MovieDirector`.mid INNER JOIN Actor on `Actor`.id==`Cast`.pid WHERE Actor.fname='Jackie (I)' AND Director.fname='Jackie (I)' AND Actor.lname='Chan' AND Director.lname='Chan' ORDER BY name ASC;"
Q9 ="SELECT fname, lname FROM Director INNER JOIN MovieDirector on `Director`.id==`MovieDirector`.did INNER JOIN Movie on `Movie`.id=`MovieDirector`.mid WHERE year=2001 GROUP BY did HAVING COUNT(mid)>=4 ORDER BY fname ASC, lname DESC;"
Q10 ="SELECT gender, COUNT(id) FROM Actor GROUP BY gender HAVING gender = 'M' OR gender = 'F' ORDER BY gender ASC;"

Q11 ="SELECT m1.name, m2.name, m1.rank, m1.year FROM Movie AS m1 INNER JOIN Movie AS m2 on m1.id > m2.id WHERE m1.rank=m2.rank AND m1.year=m2.year ORDER BY m1.name ASC LIMIT 100;"
Q12 ="SELECT `Actor`.fname, `Movie`.year, AVG(rank) AS rank FROM Actor INNER JOIN Cast ON `Actor`.id = `Cast`.pid INNER JOIN Movie ON `Movie`.id = `Cast`.mid GROUP BY `Actor`.id , `Movie`.year ORDER BY `Actor`.fname, `Movie`.year DESC  LIMIT 100;"
Q13 ="SELECT `Actor`.fname, `Director`.fname , AVG(rank) AS Score FROM Movie INNER JOIN Cast  ON `Movie`.id = `Cast`.mid INNER JOIN MovieDirector ON `MovieDirector`.mid = `Movie`.id INNER JOIN Actor ON `Actor`.id = `CAST`.pid INNER JOIN  Director ON `Director`.id = `MovieDirector`.did GROUP BY `Actor`.id, `Director`.id HAVING COUNT(`MovieDirector`.mid) >= 5 ORDER BY Score DESC,`Director`.fname ASC, `Actor`.fname DESC LIMIT 100;"


#Q10 ="SELECT gender, COUNT(id) FROM Actor GROUP BY gender ORDER BY gender ASC;"

