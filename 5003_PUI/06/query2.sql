select RTRIM(f.st_name) as name
from 
(select station as st_name, sum(ff) as janFF from fares_jan18 group by station) j 
join 
(select station as st_name, sum(ff) as febFF from fares_feb1 group by station) f 
on j.st_name = f.st_name
where f.febFF - j.janFF < -1000;
