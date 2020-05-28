Q1 ="SELECT AVG(age) FROM Player;"

Q2 ="SELECT match_no, play_date FROM Match WHERE audience > 50000 ORDER BY match_no ASC;"

Q3 ="""SELECT team_id, COUNT(win_lose) AS w FROM MatchTeamDetails WHERE win_lose='W' GROUP BY team_id 
     ORDER BY w DESC, team_id ASC;"""
    
Q4 ="""SELECT match_no, play_date FROM Match WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match) 
    ORDER BY match_no DESC;"""

Q5 ="""SELECT `MatchCaptain`.match_no, `Team`.name,`Player`.name FROM MatchCaptain 
    INNER JOIN Team on `MatchCaptain`.team_id=`Team`.team_id 
    INNER JOIN Player on `MatchCaptain`.captain=`Player`.player_id 
    ORDER BY `MatchCaptain`.match_no ASC, `Team`.name ASC;"""
    
Q6 ="""SELECT `Match`.match_no, `Player`.name, `Player`.jersey_no FROM Match 
    INNER JOIN Player on `Player`.player_id=`Match`.player_of_match ORDER BY match_no ASC;"""    

Q7 ="""SELECT `Team`.name, (SELECT AVG(age) FROM Player 
    WHERE `Team`.team_id=`Player`.team_id)
    AS average_age  FROM Team where average_age>26;"""
    
Q8 ="""SELECT `Player`.name, `Player`.jersey_no, `Player`.age, COUNT(`GoalDetails`.player_id) 
    AS gol FROM Player INNER JOIN GoalDetails on `Player`.player_id=`GoalDetails`.player_id 
    WHERE `Player`.age <= 27 GROUP BY `Player`.player_id ORDER BY gol DESC, `Player`.name ASC;"""
    
Q9 ="""SELECT team_id, ((COUNT(goal_id)*100.0)/(SELECT COUNT(goal_id) FROM GoalDetails)) 
    FROM GoalDetails GROUP BY team_id;"""

Q10 ="""SELECT AVG(gol_count) FROM(SELECT Count(team_id) AS gol_count 
     FROM GoalDetails GROUP BY team_id);"""

Q11 ="""SELECT `Player`.player_id, `Player`.name, `Player`.date_of_birth 
    FROM Player WHERE NOT EXISTS(SELECT `GoalDetails`.player_id
    FROM GoalDetails WHERE `Player`.player_id=`GoalDetails`.player_id);"""

Q12 ="""SELECT t.name, m.match_no, m.audience ,
    m.audience - (SELECT AVG(audience) FROM Match AS ma
    INNER JOIN MatchTeamDetails AS mtd ON mtd.match_no = ma.match_no AND mtd.team_id = t.team_id)
    FROM Team AS t
    INNER JOIN MatchTeamDetails AS mtd ON t.team_id = mtd.team_id
    INNER JOIN Match AS m ON m.match_no = mtd.match_no
    ORDER BY m.match_no;"""