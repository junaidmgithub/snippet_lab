SELECT 
count(*) FILTER (WHERE id IN (1,2,3) ) AS id123count
FROM
tbl_users;


SELECT 
COUNT(id=1) AS id1count
FROM
tbl_users;
