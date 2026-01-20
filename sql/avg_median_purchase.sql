--Средний и медианный чек 
select "PassengerId" ,
AVG(amount) as avg_amount,
PERCENTILE_CONT(0.5) within group (order by amount) as median_amount
from titanic.purchases
group by "PassengerId";
