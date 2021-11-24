import sqlite3
import json
from datetime import datetime
import argparse


def openJSONsaveDB(JSONfile, DBfile):
  with open(JSONfile) as f:
    data = json.load(f)

  #database stuff
  #
  #
  #
  #
  con = sqlite3.connect(DBfile)
  cur = con.cursor()
  # Create table
  cur.execute('''DROP TABLE IF EXISTS tickets''')
  cur.execute('''CREATE TABLE IF NOT EXISTS tickets
                ( id, openDate, waitingForCustomerDate, waitingForThirdPartyDate, pendingDate, resolvedDate, closeDate)''')

  # Insert a row of data
  #cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
  for i in range(data['metadata']['activities_count']):
    id = data['activies_data'][i][0]['ticket_id']
    openDate = datetime.strptime(data['activies_data'][i][0]['performed_at'][:-5], '%d-%m-%Y %H:%M:%S ')
    waitingCustomerDate = datetime.strptime(data['activies_data'][i][1]['performed_at'][:-5], '%d-%m-%Y %H:%M:%S ')
    waitingThirdParty = datetime.strptime(data['activies_data'][i][2]['performed_at'][:-5], '%d-%m-%Y %H:%M:%S ')
    pendingDate = datetime.strptime(data['activies_data'][i][3]['performed_at'][:-5], '%d-%m-%Y %H:%M:%S ')
    resolvedDate = datetime.strptime(data['activies_data'][i][4]['performed_at'][:-5], '%d-%m-%Y %H:%M:%S ')
    closedDate = datetime.strptime(data['activies_data'][i][5]['performed_at'][:-5], '%d-%m-%Y %H:%M:%S ')
    cur.execute("insert into tickets values (?, ?, ?, ?, ?, ?, ?)", (id, openDate, waitingCustomerDate, waitingThirdParty,
    pendingDate, resolvedDate, closedDate))


  # Save (commit) the changes
  con.commit()


  # for row in cur.execute('SELECT * FROM tickets'):
  #         print(row)

  # We can also close the connection if we are done with it.
  # Just be sure any changes have been committed or they will be lost.
  con.close()

if __name__ == "__main__":

        #set up command arguments
    parser = argparse.ArgumentParser(prog="readJSON.py JSONfile DBfile")
    parser.add_argument('JSONfile', type=str,
                    help='location of JSON file')
    parser.add_argument('DBfile', type=str,
                    help='location of DB to save to')
    args = parser.parse_args()
    
    jsonfile = args.JSONfile
    dbfile = args.DBfile

    openJSONsaveDB(jsonfile, dbfile)


