-- Problem 4.
--A product id is female-specific if the number of distinct women customers who bought the product is at least 1.5 times the number 
--of distinct male customers who bought it. It is required to produce a CSV with all female-specific product id's.

with Gender_Products_Count as(
select s.product_id, p.product_name,
	count (distinct case when c.gender = 'f' then c.customer_id else null end) as FemaleCount,
	count (distinct case when c.gender = 'm' then c.customer_id else null end) as MaleCount
from sales_fact s join customer c on c.customer_id = s.customer_id
join product p on p.product_id = s.product_id
group by s.product_id, p.product_name )

select g.product_id, g.product_name
from Gender_Products_Count g
where g.FemaleCount >= g.MaleCount*1.5
order by g.product_id