--Различие в сумме покупок между классами
select  t."Pclass",
SUM(p.amount) as total_spent
from  titanic.titanic t
left join titanic.purchases p on t."PassengerId" = p."PassengerId"
group by t."Pclass";