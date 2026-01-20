--общее количество выживших и погибших
select  titanic."Survived", count(*) as count
from titanic.titanic
group by titanic."Survived";

