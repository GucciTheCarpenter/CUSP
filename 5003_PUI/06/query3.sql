select avg(f.febFF - j.janFF) as broadway_ff_avg_diff 
from (select name as st_name, sum(ff) as janFF from fares_jan18 inner join stations on fares_jan18.station = stations.name where line = 'Broadway' group by station) j 
join 
(select name as st_name, sum(ff) as febFF from fares_feb1 join stations on fares_feb1.station = stations.name where line = 'Broadway' group by station) f 
on j.st_name = f.st_name;
