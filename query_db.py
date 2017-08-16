import sqlite3
import pandas

conn = sqlite3.connect('db/johannesburg.db')
c = conn.cursor()

num_rows = pandas.read_sql('SELECT COUNT(*) as num_rows from nodes', conn)
print num_rows

num_streets = pandas.read_sql('SELECT COUNT(*) as num_streets from nodes, nodes_tags WHERE nodes.id = nodes_tags.id AND nodes_tags.key = "street"', conn)
print num_streets

unique_streets= pandas.read_sql('SELECT value, COUNT(*) FROM nodes_tags WHERE key = "street" GROUP BY value', conn)
print unique_streets

top_users = pandas.read_sql('SELECT user, COUNT(*) as contributions FROM nodes GROUP BY uid ORDER BY contributions DESC LIMIT 5', conn)
print top_users

test = pandas.read_sql('SELECT * from nodes_tags LIMIT 5', conn)
print test

conn.close()