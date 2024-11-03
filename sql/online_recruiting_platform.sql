SELECT 
    experience as exp,
    SUM(CASE 
        WHEN (sql IS NULL OR sql = 100) AND 
             (algo IS NULL OR algo = 100) AND 
             (bug_fixing IS NULL OR bug_fixing = 100)
        THEN 1
        ELSE 0
    END) as max,
    COUNT(*) as count
FROM assesment
GROUP BY exp
ORDER BY exp DESC;


/* 
Let me break down the SQL problem statement:

Context:
- This is an online recruiting platform
- Companies can request candidates to complete skill tests
- Tests have 3 categories: SQL, Algo, and Bugfixing
- After test, company gets a report with:
  1. Candidate's years of experience (integer between 0-100)
  2. Scores in each category (0-100 or NULL)
  3. NULL score means no task was given in that category
  4. NULL is treated as a perfect score

Table Structure:
```sql
CREATE TABLE assesment(
    id integer not null,
    experience integer not null,
    sql integer,
    algo integer,
    bug_fixing integer,
    UNIQUE(id)
);
```

Task:
- Write a query that for each experience level shows:
  1. exp (years of experience)
  2. max (number of candidates who got perfect scores)
  3. count (total number of candidates with that experience)
- Perfect score means either 100 or NULL in all categories

Sample Data & Expected Output:
```sql
-- Input Data:
(1, 3, 100, NULL, 50)   -- not perfect (has 50)
(2, 5, NULL, 100, 100)  -- perfect (NULL treated as perfect)
(3, 1, 100, 100, 100)   -- perfect (all 100s)
(4, 5, 100, 50, NULL)   -- not perfect (has 50)
(5, 5, 100, 100, 100)   -- perfect (all 100s)

-- Expected Output:
exp | max | count
5   | 2   | 3    -- 2 perfect out of 3 candidates with 5 years exp
3   | 0   | 1    -- 0 perfect out of 1 candidate with 3 years exp
1   | 1   | 1    -- 1 perfect out of 1 candidate with 1 year exp
```

*/
