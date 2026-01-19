--категория покупок и их количество с общей суммой
select category,
COUNT(*) AS num_purchases,
SUM(amount) AS total_amount
from titanic.purchases
group by category;
