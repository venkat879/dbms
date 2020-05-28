# Q1 ="""SELECT * FROM Player p
#     WHERE EXISTS(SELECT mc.captain FROM MatchCaptain mc WHERE p.player_id=mc.captain)
#     AND NOT EXISTS(SELECT gd.player_id FROM GoalDetails AS gd INNER JOIN MatchCaptain mc on gd.player_id=mc.captain
#     WHERE gd.player_id = p.player_id);"""


Q1 ="""SELECT p.player_id, p.team_id, p.jersey_no, p.name, p.date_of_birth, p.age
    FROM Player AS p INNER JOIN MatchCaptain AS mc ON p.team_id = mc.team_id
    LEFT JOIN GoalDetails AS gd ON gd.player_id=p.player_id WHERE p.player_id=mc.captain AND gd.goal_id is null;"""
    
Q2 ="SELECT team_id, COUNT(team_id) AS no_of_games FROM MatchTeamDetails GROUP BY team_id;"

Q3 ="""SELECT team_id, ((COUNT(goal_id)*1.0)/(SELECT COUNT(player_id) FROM Player GROUP BY team_id))
    FROM GoalDetails GROUP BY team_id;"""
    
Q4 ="""SELECT captain, COUNT(player_id) FROM MatchCaptain AS mc INNER JOIN Player AS p ON mc.captain=p.player_id
    GROUP BY p.player_id;"""
    
Q5 ="""SELECT COUNT(DISTINCT mc.captain) AS no_players 
    FROM MatchCaptain AS mc INNER JOIN Match AS m ON mc.match_no=m.match_no
    WHERE mc.captain=m.player_of_match;"""
    
Q6 ="""SELECT DISTINCT mc.captain FROM MatchCaptain AS mc 
    WHERE EXISTS(SELECT m.match_no  FROM Match AS m WHERE mc.match_no=m.match_no)
    AND NOT EXISTS(SELECT m.match_no FROM Match AS m WHERE mc.captain=m.player_of_match);"""
    
Q7 ="""SELECT strftime('%m', play_date) AS month, COUNT(match_no) AS no_of_matches 
    FROM Match GROUP BY month ORDER BY no_of_matches DESC;"""
    
Q8 ="""SELECT p.jersey_no, COUNT(mc.captain) AS no_captains 
   FROM Player AS p INNER JOIN MatchCaptain AS mc ON p.player_id=mc.captain GROUP BY p.jersey_no 
   ORDER BY no_captains DESC, p.jersey_no DESC;"""
   
Q9 ="""SELECT player_id, AVG(audience) AS avg_audience FROM Match AS m INNER JOIN MatchTeamDetails AS mtd ON m.match_no=mtd.match_no
    INNER JOIN Player AS p ON mtd.team_id=p.team_id GROUP BY player_id ORDER BY avg_audience DESC, player_id DESC;"""

Q10 ="SELECT team_id, AVG(age) FROM Player GROUP BY team_id;"

Q11 ="""SELECT AVG(age) AS avg_age_of_captains 
    FROM Player AS p INNER JOIN MatchCaptain AS mc ON p.player_id=mc.captain 
    WHERE p.player_id=mc.captain;"""
    
Q12 ="""SELECT strftime('%m',date_of_birth) AS month, COUNT(player_id) AS no_of_players 
    FROM Player GROUP BY month ORDER BY no_of_players DESC, month DESC;"""
    
Q13 ="""SELECT mc.captain, COUNT(win_lose) AS no_of_wins 
    FROM MatchTeamDetails AS mtd INNER JOIN MatchCaptain AS mc ON mtd.match_no = mc.match_no 
    INNER JOIN Player AS p on p.team_id = mtd.team_id
    WHERE mtd.win_lose='W' and p.player_id = mc.captain GROUP BY mc.captain ORDER BY no_of_wins DESC;"""   