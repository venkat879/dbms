Q1 ="""SELECT A.id, A.fname, A.lname, A.gender FROM Actor A INNER JOIN Cast C ON A.id = C.pid 
    INNER JOIN Movie M ON C.mid = M.id WHERE M.name LIKE 'Annie%';"""
    
Q2 ="""SELECT M.id, M.name, M.rank, M.year FROM Movie M INNER JOIN MovieDirector MD ON M.id = MD.mid
    INNER JOIN Director D ON MD.did = D.id WHERE D.fname = 'Biff' AND D.lname = 'Malibu' AND 
    (M.year=1999 OR M.year=1994 OR M.year=2003) ORDER BY M.rank DESC, M.year ASC;"""
    
Q3 ="""SELECT year, COUNT(id) AS no_of_movies FROM Movie GROUP BY year 
    HAVING AVG(rank) > (SELECT AVG(rank) FROM Movie);""" 
    
Q4 ="""SELECT * FROM Movie WHERE year=2001 AND (rank < (SELECT AVG(rank) FROM Movie WHERE year=2001)) 
    ORDER BY rank DESC LIMIT 10;"""
    
Q5 ="""SELECT """

Q6 ="""SELECT DISTINCT pid FROM Cast INNER JOIN Movie ON mid=id GROUP BY pid, mid HAVING COUNT(DISTINCT role) > 1 LIMIT 100;"""

Q7 ="""SELECT fname, COUNT(id) count FROM Director GROUP BY fname HAVING count > 1;"""

Q8 ="""SELECT * FROM Director d 
    WHERE EXISTS(SELECT md.did FROM Cast c INNER JOIN MovieDirector md ON md.mid=c.mid 
    WHERE md.did=d.id GROUP BY md.did, md.mid HAVING COUNT(DISTINCT c.pid) >= 100)
    AND NOT EXISTS(SELECT md.did FROM Cast c INNER JOIN MovieDirector md on md.mid=c.mid 
    WHERE md.did=d.id GROUP BY md.did, md.mid HAVING COUNT(distinct c.pid) < 100);"""