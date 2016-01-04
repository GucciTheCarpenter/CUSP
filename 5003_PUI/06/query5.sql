select rtrim(f.station) as station_with_largest_decrease
from (select station, sum(ff) as FF from fares_feb1 group by station) f join (select station, sum(ff) as FF from fares_jan18 group by station) j on f.station = j. station where (f.FF - j.FF) = 
(
select min(t.diff) from (select f.station as station, f.FF - j.FF as diff from (select station, sum(ff) as FF from fares_feb1 group by station) f join (select station, sum(ff) as FF from fares_jan18 group by station) j on f.station = j. station) t);
