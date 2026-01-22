--Средняя сумма затраченная по категориям класс и пол
select
    t."Sex",
    t."Pclass",
round(avg(p.amount), 2) as avg_spend
from titanic.titanic t
left join titanic.purchases p
    on t."PassengerId" = p."PassengerId"
group by t."Sex", t."Pclass"
order by t."Sex", t."Pclass";
