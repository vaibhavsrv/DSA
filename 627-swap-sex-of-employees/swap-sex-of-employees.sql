# Write your MySQL query statement below
update salary set sex =
case sex 
        WHEN 'm' then 'f'
        else'm'
end;