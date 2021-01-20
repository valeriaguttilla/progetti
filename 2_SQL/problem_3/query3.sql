--#3. The quarter value (QV) of a customer id (C) at the date id (T) is the sum of revenues minus the costs of the products 
--that the customer C buys in the quarter of T. It is required to produce a CSV le with three columns: customer id, time it, QV.


select
	sf.customer_id,
	sf.time_id,
	t.quarter,
	t.the_year,
	sum(sum(sf.store_sales - sf.store_cost)) OVER  (PARTITION BY sf.customer_id, t.quarter,t.the_year) AS QV
from sales_fact sf JOIN time_by_day t ON sf.time_id=t.time_id
group by sf.customer_id, sf.time_id,t.quarter, t.the_year
order by customer_id, t.quarter ;
