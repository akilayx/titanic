--Количество выживших пассажиров которые не сделали ни одной покупки
select COUNT(*) as survived_no_purchase
from  titanic.titanic t
left join titanic.purchases p on t."PassengerId" = p."PassengerId"
where t."Survived" = 1
  and p."PassengerId" is null;