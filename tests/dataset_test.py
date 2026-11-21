import pyarrow.parquet as pq

table = pq.read_table("data/part-00000-66e0628d-2c7f-425a-8f5b-738bcd6bf198-c000.snappy.parquet")
print("Columns:", table.column_names)
print("Total rows:" , table.num_rows)
print("First 5 rows:", table.slice(0, 5).to_pydict())
print("-----------------------\n" , table.to_pydict())