1. SELECT c.name AS name, count(f.film_id) as "total_films" from category c JOIN film_category fc ON  c.category_id = fc.category_id JOIN film f ON fc.film_id = f.film_id GROUP BY name;
2. select c.name AS name, AVG(f.rental_duration) AS "AVG_RENTAL_DURATION" from film f JOIN film_category fc ON f.film_id = fc.film_id JOIN category c ON fc.category_id = c.category_id GROUP BY c.name;
3. select title, (rental_rate * rental_duration) AS total_revenue from film ORDER BY title asc limit 10;
4. select c.customer_id, c.first_name, c.last_name, count(r.rental_id) as total_rentals from customer c JOIN rental r ON c.customer_id = r.customer_id GROUP BY c.customer_id, c.first_name, c.last_name limit 10;
5.select f.rating, avg(f.replacement_cost) as avg_replacement_cost from film f GROUP BY f.rating limit 10;
6.select l.name, avg(f.rental_rate) as avg_rental_rate from language l LEFT JOIN film f ON f.language_id = l.language_id GROUP BY l.name;
7.select s.staff_id, s.first_name, s.last_name, sum(p.amount) as total_payments from staff s JOIN payment p ON p.staff_id = s.staff_id GROUP BY s.staff_id, s.first_name, s.last_name limit 2;
8. select c.name, count(r.rental_id) as total_rentals from category c LEFT JOIN film_category fc ON fc.category_id = c.category_id LEFT JOIN film f ON fc.film_id = f.film_id JOIN inventory i ON f.film_id = i.film_id LEFT JOIN rental r ON i.inventory_id = r.inventory_id  GROUP BY c.name;
9. select c.customer_id, c.first_name, c.last_name, r.rental_id from customer c, rental r WHERE c.customer_id = r.customer_id limit 10;