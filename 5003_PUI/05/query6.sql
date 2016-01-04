select name as stop_f
from stations 
where stations.lines like '%F%' order by name;
