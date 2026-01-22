--количество строк в которых есть значение NULL
select 
    count(*) filter (where "PassengerId" is null) as passengerid_null,
    count(*) filter (where "Survived" is null) as survived_null,
    count(*) filter (where "Pclass" is null) as pclass_null,
    count(*) filter (where "Name" is null) as name_null,
    count(*) filter (where "Sex" is null) as sex_null,
    count(*) filter (where "Age" is null) as age_null,
    count(*) filter (where "SibSp" is null) as sibsp_null,
    count(*) filter (where "Parch" is null) as parch_null,
    count(*) filter (where "Ticket" is null) as ticket_null,
    count(*) filter (where "Fare" is null) as fare_null,
    count(*) filter (where "Cabin" is null) as cabin_null,
    count(*) filter (where "Embarked" is null) as embarked_null
from titanic.titanic;

