import sqlite3
import pandas

NODES_PATH = "csv/nodes.csv"
NODE_TAGS_PATH = "csv/nodes_tags.csv"
WAYS_PATH = "csv/ways.csv"
WAY_NODES_PATH = "csv/ways_nodes.csv"
WAY_TAGS_PATH = "csv/ways_tags.csv"

DB_PATH = 'db/johannesburg.db'

conn = sqlite3.connect(DB_PATH)
conn.text_factory = str

def populate_nodes():
    df = pandas.read_csv(NODES_PATH)
    df.to_sql('nodes', conn, if_exists='replace', index=False)

def populate_nodes_tags():
    df = pandas.read_csv(NODE_TAGS_PATH)
    df.to_sql('nodes_tags', conn, if_exists='replace', index=False)

def populate_ways():
    df = pandas.read_csv(WAYS_PATH)
    df.to_sql('ways', conn, if_exists='replace', index=False)

def populate_way_nodes():
    df = pandas.read_csv(WAY_NODES_PATH)
    df.to_sql('way_nodes', conn, if_exists='replace', index=False)

def populate_way_tags():
    df = pandas.read_csv(WAY_TAGS_PATH)
    df.to_sql('way_tags', conn, if_exists='replace', index=False)

if __name__ == '__main__':
    populate_nodes()
    populate_nodes_tags()
    populate_ways()
    populate_way_nodes()
    populate_way_tags()

    