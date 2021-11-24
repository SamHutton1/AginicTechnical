#!/bin/bash

#generates tickets
py E:/Aginic/commandLine.py 500 ticketOutput.JSON

#read tickets write DB
py E:/Aginic/readJSON.py ticketOutput.JSON ticket.db

#run given SQL query on given db
py E:/Aginic/runSQL.py sqlScript.sql ticket.db




