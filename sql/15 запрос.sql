--покупки с нулевой или отрицательной суммой
select *
from titanic.purchases
where amount <= 0;
