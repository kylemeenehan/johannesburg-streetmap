import sqlite3
import pandas

conn = sqlite3.connect('db/johannesburg.db')
c = conn.cursor()

# print the number of rows in the nodes table
num_rows = pandas.read_sql('SELECT COUNT(*) as num_rows from nodes', conn)
print "\nNumber of rows in the nodes table:"
print num_rows

# print the number of entries for streets in the nodes_tags table
num_streets = pandas.read_sql('SELECT COUNT(*) FROM nodes_tags WHERE key = "street"', conn)
print "\nNumber of entries for streets in the nodes_tags table:"
print num_streets


# print the top ten streets by their number of entries
unique_streets= pandas.read_sql('SELECT value, COUNT(*) as count FROM nodes_tags WHERE key = "street" GROUP BY value ORDER BY count DESC LIMIT 10', conn)
print "\nTop ten streets by the number of entries with that street name, along with their counts:"
print unique_streets

# print the top ten tag types by the number of tags
num_tag_types= pandas.read_sql('SELECT key, COUNT(*) as count FROM nodes_tags GROUP BY key ORDER BY count DESC LIMIT 10', conn)
print "\nThe top ten tag types by number of those tags:"
print num_tag_types

# print the number of unique users
num_users = pandas.read_sql('SELECT COUNT(DISTINCT(combined.uid)) as num_users from (SELECT uid from nodes UNION ALL SELECT uid from ways GROUP BY uid) combined', conn)
print "\nThe number of unique users is: "
print num_users

# print the top ten users by contributions
top_users = pandas.read_sql('SELECT user, COUNT(*) as contributions FROM (SELECT id, user, uid from nodes UNION ALL SELECT id, user, uid from ways) GROUP BY uid ORDER BY contributions DESC LIMIT 10', conn)
print "\nThe top users by contributions are:"
print top_users

conn.close()