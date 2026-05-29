# Write your MySQL query statement below
select a.product_name,b.year,b.price from Sales b left join Product a on b.product_id
= a.product_id;