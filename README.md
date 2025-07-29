# Project Name

This project is a minimal frontend application developed with Flask, which serves as an initial basis for building dynamic web interfaces.

It is designed to be the starting point for a Flask application, offering a simple but extensible structure that facilitates the development of custom features and integration with APIs or backend services.


# ⚙️ Installation

1. Clone the repository:

```text

git clone https://github.com/yourusername/project-name.git
cd project-name
```

## Shell scripts

```text
chmod +x env.sh
chmod +x 1.sh

./env.sh
./1.sh
```

# Deploy

* http://127.0.0.1:1024

* http://192.168.1.6:1024/

* https://github.com/LesXon/flask-template


# Virtual Environment

## Creation
```text
python3 -m venv venv
```

## Activation
```text

# On Mac/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

## Deactivation
```text
deactivate
```

# Install dependencies:

```text
pip install -r requirements.txt

pip freeze > requirements.txt
```

# 🧪 Testing. Pendiente. Pending 

To run tests:

```text
pytest
```

# .env Configuration

## Database configuration

```text
SUPABASE_DB_URL="your_actual_supabase_url"
```

## Environment variables

```text
Pending
```

# Consult Environment variables

## All variables:

```text
# On Mac/Linux:
printenv

# On Windows
Pending
```

## A specific variable

```text
# On Mac/Linux:
echo $VARIABLE_NAME

# On Windows
Pending
```

# Project execution

```bash
python app.py
```

# Address already in use

```text
lsof -i :5002
kill -9 <PID>

kill -9 $(lsof -ti :5002)
```

# Backup

## libpq

```
brew reinstall libpq
brew list libpq
pg_dump --version
```

### Backup.Data

#### Supabase
```
pg_dump -h db.gferixzbvlodjgkjyqgr.supabase.co -U postgres -d postgres -p 5432 --data-only -Fc > backup.dump
```

#### Local
```
pg_dump -h 127.0.0.1 -U postgres -d postgres -p 54322 --data-only -Fc > backup.dump
```

### Backup.Data and Tables

#### Supabase
```
pg_dump -h db.gferixzbvlodjgkjyqgr.supabase.co -U postgres -d postgres -p 5432 -Fc > backupall.dump
```

#### Local
```
pg_dump -h 127.0.0.1 -U postgres -d postgres -p 54322 -Fc > backupall.dump
```

### Dump to SQL
```
pg_restore --verbose --no-owner --no-privileges --format=custom --file=backup.sql backup.dump

pg_restore --verbose --no-owner --no-privileges --format=custom --file=backupall.sql backupall.dump
```

### Restore.Supabase

```
pg_restore -U postgres -d postgres -h db.gferixzbvlodjgkjyqgr.supabase.co < backup.dump

pg_restore -U postgres -d postgres -h db.gferixzbvlodjgkjyqgr.supabase.co < backupall.dump
```

### Restore.rivendell

```
pg_restore -U postgres.4ut0tr4ckr -d postgres -h rivendell.axionomic.ai < backup.dump

pg_restore -U postgres.4ut0tr4ckr -d postgres -h db.gferixzbvlodjgkjyqgr.supabase.co < backupall.dump
```

### Restore.Local

```
pg_restore -U postgres -d postgres -h 127.0.0.1 -p 54322 < backup.dump

pg_restore -U postgres -d postgres -h 127.0.0.1 -p 54322 < backupall.dump

```

# Upload data from CSV

## pgloader 

```text
pgloader data.load
```

## data.load file

```text
LOAD CSV
     FROM './data.csv'
     INTO postgresql://postgres:postgres@127.0.0.1:54322/postgres
     TARGET TABLE transactions
     (code, timestamp, yy, mm, dd, hh, ms, ss, type, qty, price)

 WITH skip header = 1

 SET client_encoding TO 'utf8'

;
```

# SQL

## Total database records

```sql
-- Create a temporary function that returns table counts
CREATE OR REPLACE FUNCTION get_table_counts()
RETURNS TABLE(tbl_name TEXT, total_records TEXT, size_bytes TEXT) AS $$
DECLARE 
    rec RECORD;
    sql_query TEXT := '';
    sql_total TEXT := '';
    sql_size_total TEXT := '';
BEGIN
    -- Build the query dynamically
    FOR rec IN 
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public' 
        AND table_type = 'BASE TABLE'
        AND table_name NOT LIKE 'pg_%'
        AND table_name NOT LIKE 'sql_%'
        ORDER BY table_name
    LOOP
        IF sql_query != '' THEN
            sql_query := sql_query || ' UNION ALL ';
            sql_total := sql_total || ' + ';
            sql_size_total := sql_size_total || ' + ';
        END IF;
        
        sql_query := sql_query || 
            'SELECT ''' || rec.table_name || ''' AS tbl_name, ' ||
            'TO_CHAR(COUNT(*), ''FM999,999,999,999'') AS total_records, ' ||
            'pg_size_pretty(pg_total_relation_size(''' || rec.table_name || ''')) AS size_bytes ' ||
            'FROM ' || rec.table_name;
            
        -- Build total sum
        sql_total := sql_total || '(SELECT COUNT(*) FROM ' || rec.table_name || ')';
        sql_size_total := sql_size_total || 'pg_total_relation_size(''' || rec.table_name || ''')';
    END LOOP;
    
    -- Add the grand total row
    IF sql_query != '' THEN
        sql_query := sql_query || ' UNION ALL ';
        sql_query := sql_query || 
            'SELECT ''GRAND TOTAL'' AS tbl_name, ' ||
            'TO_CHAR((' || sql_total || '), ''FM999,999,999,999'') AS total_records, ' ||
            'pg_size_pretty(' || sql_size_total || ') AS size_bytes';
    END IF;
    
    -- Wrap in subquery to use ORDER BY with CASE
    sql_query := 'SELECT tbl_name, total_records, size_bytes FROM (' || sql_query || ') AS counts ' ||
                 'ORDER BY CASE WHEN tbl_name = ''GRAND TOTAL'' THEN 1 ELSE 0 END, tbl_name';
    
    -- Return the results
    RETURN QUERY EXECUTE sql_query;
END $$ LANGUAGE plpgsql;

-- Execute the function and get the results
SELECT * FROM get_table_counts();

-- Drop the temporary function (optional)
DROP FUNCTION get_table_counts();
```

## Delete Row. Delete the data and restart the counter

```sql
TRUNCATE TABLE transactions RESTART IDENTITY;
TRUNCATE TABLE markets RESTART IDENTITY;
TRUNCATE TABLE platforms_markets RESTART IDENTITY;
```

## Last record

```sql
SELECT *
FROM public.transactions
ORDER BY "timestamp" DESC
LIMIT 1;
```

## How many records exist in a table?

```sql
SELECT TO_CHAR(COUNT(*), 'FM999,999,999,999') AS total_formateado
FROM transactions;
```

## Attribute details

```sql
SELECT
  c.ordinal_position AS position,
  c.column_name,
  c.data_type,
  c.numeric_precision,
  c.numeric_scale,
  c.is_nullable,
  c.column_default,
  CASE 
    WHEN tc.constraint_type = 'UNIQUE' THEN 'YES'
    ELSE 'NO'
  END AS is_unique,
  d.description AS comment
FROM 
  information_schema.columns c
LEFT JOIN pg_class cls 
  ON cls.relname = c.table_name
LEFT JOIN pg_description d 
  ON d.objoid = cls.oid AND d.objsubid = c.ordinal_position
LEFT JOIN information_schema.key_column_usage kcu 
  ON c.column_name = kcu.column_name
  AND c.table_name = kcu.table_name
  AND c.table_schema = kcu.table_schema
LEFT JOIN information_schema.table_constraints tc 
  ON kcu.constraint_name = tc.constraint_name
  AND tc.table_schema = c.table_schema
  AND tc.constraint_type = 'UNIQUE'
WHERE 
  c.table_schema = 'public'
  AND c.table_name = 'digital_assets'
ORDER BY 
  c.ordinal_position;
```

# Prompts

```text
Document the following code according to PEP 257 — Official guide for docstrings in Python:


```

# Semantic Commits

* Semantic commits are a convention for writing commit messages in Git in a structured, clear, and meaningful way.

* This helps to easily understand what kind of change was made, where in the project, and why.

## A commit must be atomic

* One thing per commit (example: fix a bug, add a feature, refactor).

* Do not mix unrelated changes.

## Common message structure:

```
<type>(<area>): <short message in present tense>
```

| Type       | Description                                                                  |
|------------|------------------------------------------------------------------------------|
| `feat`     | New functionality                                                            |
| `fix`      | Bug fix                                                                      |
| `docs`     | Changes to documentation                                                     |
| `style`    | Formatting changes (spaces, commas, indentation) that do not affect the code |
| `refactor` | Internal code changes without adding new features or fixing bugs             |
| `test`     | Adds or modifies tests                                                       |
| `chore`    | General tasks such as maintenance, configuration, or dependencies            |
| `perf`     | Changes aimed at improving performance                                       |
| `build`    | Changes that affect the build system or external dependencies                |
| `ci`       | Changes to configuration or continuous integration scripts                   |
| `revert`   | Reverting a previous commit                                                  |

| Scope        | Description                                              |
|--------------|----------------------------------------------------------|
| `api`        | Changes to endpoints, controllers, or API logic          |
| `auth`       | Authentication and authorization                         |
| `db`         | Changes to the database schema, migrations, SQL          |
| `ui`         | User interface, changes to views or styles               |
| `core`       | Core business logic or base architecture                 |
| `config`     | Environment configuration, `.env` files, settings, etc.  |
| `deps`       | Addition, removal, or update of dependencies             |
| `test`       | Test files and logic                                     |
| `build`      | Build or packaging scripts                               |
| `docs`       | Documentation (README, comments, etc.)                   |
| `ci`         | Continuous integration files (GitHub Actions, GitLab CI) |


## Prompting. feature title

```text
Improve the following description for a git project feature title with a technical focus and good practice. Replace spaces with a hyphen. Translate it into English:

LEXENG-4 Diseñar el api rest para almacenar los diagramas de flujo version alfa
```

## Prompting. commit description

```text
Improve the following description for a commit of a git project as a technique and good practice. Translate it to English:

feat(api): create MCP server to expose API as a tool for AI integration
```

# 📄 License

This project is licensed under the MIT License – see the LICENSE file for details.