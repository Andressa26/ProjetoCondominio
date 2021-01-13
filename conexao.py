#teste
import sqlite3
from sqlite3 import Error

class Conexao:
  def __init__(self):
    self.db_file = "database.db"
    """ create a database connection to a SQLite database """
    self.conn = None
    self.sqlite = sqlite3
    try:
        self.conn = self.sqlite.connect(self.db_file)
    except Error as e:
        print(e)

  def create_table(self, conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = self.conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
  
  def task(self, sql, data):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    try:
      cur = self.conn.cursor()
      cur.execute(sql, data)
      self.conn.commit()
      return True
    except Error as e:
      return e

  def select_all(self, table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    try:
      cur = self.conn.cursor()
      query = "SELECT * FROM "+table
      cur.execute(query)
      rows = cur.fetchall()
      return rows
    except Error as e:
      return e
  
  def select(self, table, id, namepk):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = self.conn.cursor()
    cur.execute("SELECT * FROM "+table+" WHERE "+ namepk +"=?", (id,))
    rows = cur.fetchall()
    return rows

  def checkExistence(self, table, id, namepk):
    if len(self.select( table, id, namepk)) > 0:
      return True
    return False