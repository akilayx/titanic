--топ 10 пассажиров с их информацией
select
    t."Name",
    t."Pclass",
    t."Survived",
    sum(p.amount) as total_spend
from titanic.titanic t
left join titanic.purchases p
    on t."PassengerId" = p."PassengerId"
group by t."Name", t."Pclass", t."Survived"
order by total_spend desc
limit 10;

