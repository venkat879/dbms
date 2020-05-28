Q1 ="SELECT fname, lname FROM Actor INNER JOIN Cast on `Actor`.id==`Cast`.pid WHERE `Cast`.mid==12148;"
Q2 ="SELECT COUNT(mid) FROM Actor INNER JOIN Cast on id==pid WHERE fname = 'Harrison (I)' AND lname = 'Ford';"
Q3 ="SELECT distinct pid FROM Cast INNER JOIN Movie on `Movie`.id=`Cast`.mid WHERE name LIKE 'Young Latin Girls%';"
Q4 ="SELECT COUNT(distinct pid) FROM Cast INNER JOIN Movie on `Movie`.id=`Cast`.mid WHERE year between 1990 AND 2000;"