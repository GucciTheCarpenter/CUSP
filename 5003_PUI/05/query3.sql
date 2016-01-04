select lat, lng, sum(ff) as ff from stations inner join fares_jan18 on stations.name = fares_jan18.station where line = 'Broadway' group by lat order by sum(ff) desc;
