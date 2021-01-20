-- Problem 1.
-- A sale was done during a travel if the store of the sale was not in the city of residence of the
-- customer. It is required to produce a CSV with a row for every customer and her/his percentage
-- of sales done during travel over the total sales of the customer.
select
	sf.customer_id,
	count(case when s.store_city <> c.city then 1 else null end) as tot_travel_sales,
	count(sf.fact_id) as tot_sales,
	cast(
		(
			1.0 * count(case when s.store_city <> c.city then 1 else null end) / count(sf.fact_id)
		) * 100 as numeric(5,2)
	) as percent_of_travel_tot_sales
from sales_fact sf, customer c, store s
where sf.customer_id = c.customer_id and sf.store_id = s.store_id
group by sf.customer_id
order by sf.customer_id;