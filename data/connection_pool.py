from psycopg_pool import ConnectionPool

pool = ConnectionPool(
    "host=localhost port=5432 dbname = task_manager user=postgres password=Password4242",
    min_size= 2
)
