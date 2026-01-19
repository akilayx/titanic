--поле в котором пропусков больше всего
select column_name, null_count
from (
    select 'PassengerId' as column_name, count(*) filter (where "PassengerId" is null) as null_count from titanic.titanic
    union all
    select 'Survived',count(*) filter (where "Survived" is null) from titanic.titanic
    union all
    select 'Pclass',count(*) filter (where "Pclass" is null) from titanic.titanic
    union all
    select 'Name',count(*) filter (where "Name" is null) from titanic.titanic
    union all
    select 'Sex',count(*) filter (where "Sex" is null) from titanic.titanic
    union all
    select 'Age',count(*) filter (where "Age" is null) from titanic.titanic
    union all
    select 'SibSp',count(*) filter (where "SibSp" is null) from titanic.titanic
    union all
    select 'Parch',count(*) filter (where "Parch" is null) from titanic.titanic
    union all
    select 'Ticket',count(*) filter (where "Ticket" is null) from titanic.titanic
    union all
    select 'Fare',count(*) filter (where "Fare" is null) from titanic.titanic
    union all
    select 'Cabin',count(*) filter (where "Cabin" is null) from titanic.titanic
    union all
    select 'Embarked',count(*) filter (where "Embarked" is null) from titanic.titanic) t
order by null_count desc
limit 1;
