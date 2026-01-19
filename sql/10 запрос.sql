--Судьба самых пьяных пассажиров
select
t."PassengerId",
t."Survived",
sum(p.amount) as alcohol_spend
from titanic.purchases p
join titanic.titanic t
on p."PassengerId" = t."PassengerId"
where p.category = 'alcohol'
group by t."PassengerId", t."Survived"
order by alcohol_spend desc
limit 20;


