--количество пассажиров которые не сделали ни одной покупки
select COUNT(*) AS no_purchases
from titanic.titanic t
LEFT JOIN titanic.purchases p ON t."PassengerId" = p."PassengerId"
WHERE p."purchase_id" IS NULL;
