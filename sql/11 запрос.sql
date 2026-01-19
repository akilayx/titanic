--Общее окличестов назначеннных в шлюпку и не назначенных
select
case
when l."PassengerId" is null then 'not_assigned'
else 'assigned'
end as lifeboat_status,
count(*) as passengers
from titanic.titanic t
left join titanic.lifeboat_assignments l
    on t."PassengerId" = l."PassengerId"
group by lifeboat_status;
