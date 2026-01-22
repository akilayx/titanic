--Рассчет для каждого пассажира с категориями по тратам
with total_spend_per_passenger as (
select
     t."PassengerId",
     sum(p.amount) as total_spend
  from titanic.titanic t
    left join titanic.purchases p
      on t."PassengerId" = p."PassengerId" 
    group by t."PassengerId")
select
"PassengerId",
 total_spend,
    case
        when total_spend is null then 'no_spend'
        when total_spend < 30 then 'low_spend'
        when total_spend < 50 then 'medium_spend'
        else 'high_spend'
    end as spend_segment
from total_spend_per_passenger
order by total_spend desc nulls last;


