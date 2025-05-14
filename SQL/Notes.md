## CTE
✅ CTE in SQL (Common Table Expression)
A CTE (Common Table Expression) is a temporary, named result set you can reference within a SELECT, INSERT, UPDATE, or 
DELETE query. It improves readability, modularity, and can be recursive.

```sql
WITH cte_name AS (
    SELECT ...
)
SELECT * FROM cte_name;
```
Get employees with salary above average:

```sql
WITH avg_salary AS (
    SELECT AVG(salary) AS avg_sal FROM employees
)
SELECT name, salary
FROM employees, avg_salary
WHERE employees.salary > avg_salary.avg_sal;
```
✔️ Why Use CTEs?
Make complex queries readable

Help avoid subquery repetition

Enable recursive queries

Scope-limited and cleaner than temp tables

## Views

| Feature                | **View**                             | **Materialized View**                     |
|------------------------|---------------------------------------|--------------------------------------------|
| **Definition**         | Virtual table based on a query        | Physical table storing query results       |
| **Storage**            | Does **not** store data               | **Stores** data on disk                    |
| **Performance**        | Slower (recomputed each time)         | Faster (precomputed and stored)            |
| **Freshness**          | Always up-to-date                     | May become **stale** unless refreshed      |
| **Refresh**            | Not required                          | Needs manual or automatic **refresh**      |
| **Usage**              | Good for frequently changing data     | Best for reporting, analytics              |
| **Write operations**   | Cannot perform DML directly           | Usually read-only; some DBs support updates|
| **Indexed**            | Cannot have indexes                   | Can be **indexed** like regular tables     |

Normal View
```sql
CREATE VIEW high_salary_employees AS
SELECT * FROM employees WHERE salary > 50000;
```
Materialized View
```sql
CREATE MATERIALIZED VIEW high_salary_employees_mv AS
SELECT * FROM employees WHERE salary > 50000;

```
🧠 Summary
Use View when data must always be real-time.

Use Materialized View when performance is critical and data can be slightly stale.


