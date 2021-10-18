SELECT 
count(*) FILTER (WHERE id IN (1,2,3) ) AS id123count
FROM
tbl_users;

