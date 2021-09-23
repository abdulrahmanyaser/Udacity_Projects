/* question set 1  part 1 */
with family_movies as(
      select f.title film_title,
          c.name category_name,
          count(r.rental_id) rental_count
      from category c
          join film_category fc
          on c.category_id = fc.category_id
          join film f
          on fc.film_id = f.film_id
          join inventory i
          on i.film_id = f.film_id
          join rental r
          on i.inventory_id = r.inventory_id
      where c.name IN ('Animation','Children','Classics','Comedy', 'Family','Music')
      group by  1, 2)
      
select
        film_title,
        category_name,
        rental_count
from family_movies
order by  2, 1 ;
/*--------------------------------------------------*/
/* question set 1 Part 2 */
select
    f.title as title,
    c.name as name,
    f.rental_duration rental_duration,
    ntile(4) over ( order by f.rental_duration)
    as standard_quartile
from category c
    join film_category fc
    on c.category_id = fc.category_id
    join film f
    on f.film_id = fc.film_id
where
    c.name IN ('Animation', 'Children','Classics', 'Comedy', 'Family', 'Music');
/*-----------------------------------------------------*/
# question set 1 part 3
SELECT name,
standard_quartile,
COUNT(*)
from (
    select
        f.title as title ,
        c.name as name,
        f.rental_duration rental_duration,
        ntile(4) over ( order by f.rental_duration)
   		AS standard_quartile
    from category c
        join film_category fc
        on c.category_id = fc.category_id
        join film f
        on f.film_id = fc.film_id
    where
        c.name IN ('Animation', 'Children','Classics','Comedy', 'Family', 'Music')) t1
GROUP BY 1, 2
ORDER BY 1, 2
/*-------------------------------------------------------*/
/* question set 2 Part 1 */
SELECT
      DATE_PART('year', r.rental_date)
      AS rental_year,
      DATE_PART('month', r.rental_date)
      AS rental_month,
      s.store_id store_id,
      COUNT(r.rental_id) count_rentals
FROM store s
      JOIN staff sf
      ON s.store_id = sf.store_id
      JOIN rental r
      ON r.staff_id = sf.staff_id
GROUP BY 1, 2, 3
ORDER BY count_rentals DESC ;
