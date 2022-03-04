-- insert into accountm values('savings',3960,1965)
-- insert into students values(5,17)
-- select account_type,tdbal-ydbal,tdbal,ydbal from accountm;

-- select account_type,sum(tdbal)-sum(ydbal),sum(tdbal),sum(ydbal) from accountm
-- group by account_type;

SELECT 
	account_type,
-- 	net_sales,
	LAG(tdbal,1) OVER (
		PARTITION BY account_type
	) previous_month_sales
FROM 
	accountm;
# cross join of students having marks greater than others  students
# rollno marks
# 1	67
# 2	27
# 3	77
# 4	7
# 5	17
with res as(
select 
a.rollno as rollnos,a.marks as markst,b.marks
-- count(a.marks)
from students a
cross join students b
--   group by a.rollno
-- having 
where 
a.marks <> b.marks and 
a.marks>b.marks)
--   group by rollno;
-- SELECT rollnos,markst from res
select rollnos,count(markst) from res group by rollnos
order by count(markst);