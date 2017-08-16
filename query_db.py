import sqlite3
import pandas

conn = sqlite3.connect('db/johannesburg.db')
c = conn.cursor()

num_rows = pandas.read_sql('SELECT COUNT(*) as num_rows from nodes', conn)
print num_rows

num_streets = pandas.read_sql('SELECT COUNT(*) as num_streets from nodes, nodes_tags WHERE nodes.id = nodes_tags.id AND nodes_tags.key = "street"', conn)
print num_streets

unique_streets= pandas.read_sql('SELECT value, COUNT(*) as count FROM nodes_tags WHERE key = "street" GROUP BY value ORDER BY count DESC LIMIT 10', conn)
print unique_streets

num_tag_types= pandas.read_sql('SELECT key, COUNT(*) as count FROM nodes_tags GROUP BY key ORDER BY count DESC LIMIT 10', conn)
print num_tag_types

top_users = pandas.read_sql('SELECT user, COUNT(*) as contributions FROM nodes GROUP BY uid ORDER BY contributions DESC LIMIT 5', conn)
print top_users

test = pandas.read_sql('SELECT * from nodes_tags', conn)
print test.head()

conn.close()