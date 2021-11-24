import sqlite3
import argparse




def queryAndPrint(SQLlocation, DBlocation):
    SQLfile = open(SQLlocation)
    sql_as_string = SQLfile.read()

    con = sqlite3.connect(DBlocation)

    cur = con.cursor()

    print("{:<15} {:<15} {:<20} {:<20} {:<20}".format("id", "timeOpen", "timeWaitingCustomer", "timeTilResolved", "timeToFirstResponse"))
    for row in cur.execute(sql_as_string):
        print("{:<15} {:<15} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4]))

    con.close()

if __name__ == "__main__":
    #set up command arguments
    parser = argparse.ArgumentParser(prog="runSQL.py SQLfile Database")
    parser.add_argument('SQLfile', type=str,
                    help='directory of sql query to run')
    parser.add_argument('database', type=str,
                    help='directory to database to run the query on')
    args = parser.parse_args()
    
    SQLfilee = args.SQLfile
    database = args.database

    queryAndPrint(SQLfilee, database)
