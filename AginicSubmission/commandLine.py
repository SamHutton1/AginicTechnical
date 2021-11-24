
import json
import random
import datetime
import copy
import argparse



#generate random date from 2015 - 2021
def randomDate():
    time_between_dates = end - start
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start + datetime.timedelta(days=random_number_of_days)
    date_and_time = datetime.datetime(random_date.year, random_date.month, random_date.day, 0, 0, 0)

    
    hour_change = datetime.timedelta(hours=random.randint(0, 23))
    min_change = datetime.timedelta(minutes=random.randint(0, 59))
    sec_change = datetime.timedelta(seconds=random.randint(0, 59))
    new_time = date_and_time + hour_change + min_change + sec_change
    return new_time

#adds up to 7 days from initial start date to activity dates
def addRandomTime(start_date): 
    day_change = datetime.timedelta(days=random.randint(0, 6))
    hour_change = datetime.timedelta(hours=random.randint(0, 23))
    min_change = datetime.timedelta(minutes=random.randint(0, 59))
    sec_change = datetime.timedelta(seconds=random.randint(0, 59))

    random_date = start_date + day_change + hour_change + min_change + sec_change
    return random_date

#returns the start date and end date (tickets are done over a 2 week time period)
def returnDates():
    date = list()

    start_date = randomDate()
    end_date = start_date
    add_days = datetime.timedelta(days=14)
    end_date = end_date + add_days

    date.append(start_date)
    date.append(end_date)

    return date

#todo def random address

def incrementOtherID():
    global otherIDCount
    global endIDCount
    otherIDCount = otherIDCount + 1
    endIDCount = endIDCount - 1

def incrementActivities():
    global numActivities
    numActivities = numActivities + 1 
    
#random time change (up to 33 hours)
def addLessTime(currentTime):
    hour_change = datetime.timedelta(hours=random.randint(0, 32))
    min_change = datetime.timedelta(minutes=random.randint(0, 59))
    sec_change = datetime.timedelta(seconds=random.randint(0, 59))

    random_date = currentTime + hour_change + min_change + sec_change
    return random_date

#creates the json for an activity 
def createActivities():
    currentDate = addRandomTime(finalDates[0])
    id = ticketIDs[numActivities]
    performer = otherID[otherIDCount]
    src = random.randint(1, 10)
    priority = random.randint(1, 10)
    groupChoice = random.choice(group)
    agent = otherID[otherIDCount]
    requester = otherID[-1]
    


    this = random.choice(category)
    
    if this == "Computer":
        this1 = random.choice(computer)
    if this == "Phone":
        this1 = random.choice(phone)
    if this == "TV":
        this1 = random.choice(tv)
    if this == "Appliance":
        this1 = random.choice(appliance)

    
    
    activity = {"performed_at": currentDate.strftime('%d-%m-%Y %H:%M:%S +0000'),
            "ticket_id": id,
            "performer_type": "user",
            "performer_id": performer,
            "activity":
                {"shipping_address": "N/A", #maybe generate random address
                "shipment_date": currentDate.strftime('%d %B, %Y'),
                "category": this,
                "contacted_customer": False,
                "issue_type": random.choice(issue),
                "source": src,
                "status": "Open",
                "priority": priority,
                "group": groupChoice,
                "agent_id": agent,
                "requester": requester,
                "product": this1}}


    activity1 = copy.deepcopy(activity)
    activity2 = copy.deepcopy(activity)
    activity3 = copy.deepcopy(activity)
    activity4 = copy.deepcopy(activity)
    activity5 = copy.deepcopy(activity)

    #change the status for each activity 
    activity1['activity']['status'] = "Waiting for Customer"
    activity2['activity']['status'] = "Waiting for Third Party"
    activity3['activity']['status'] = "Pending"
    activity4['activity']['status'] = "Resolved"
    activity5['activity']['status'] = "Closed"

    #add time to each of the previous statusses
    timeToAdd = addLessTime(currentDate)
    timeToAdd1 = addLessTime(timeToAdd)
    timeToAdd2 = addLessTime(timeToAdd1)
    timeToAdd3 = addLessTime(timeToAdd2)
    timeToAdd4 = addLessTime(timeToAdd3)

    #adjust for the new time period
    activity1['performed_at'] = timeToAdd.strftime('%d-%m-%Y %H:%M:%S +0000')
    activity2['performed_at'] = timeToAdd1.strftime('%d-%m-%Y %H:%M:%S +0000')
    activity3['performed_at'] = timeToAdd2.strftime('%d-%m-%Y %H:%M:%S +0000')
    activity4['performed_at'] = timeToAdd3.strftime('%d-%m-%Y %H:%M:%S +0000')
    activity5['performed_at'] = timeToAdd4.strftime('%d-%m-%Y %H:%M:%S +0000')

    incrementActivities()
    incrementOtherID()

    return activity, activity1, activity2, activity3, activity4, activity5



if __name__ == "__main__":

        #set up command arguments
    parser = argparse.ArgumentParser(prog="commandLine.py 1000 data.json")
    parser.add_argument('numberTickets', type=int,
                    help='number of tickets you want generated')
    parser.add_argument('outputFile', type=str,
                    help='location of where JSON file should save')
    args = parser.parse_args()
    
    numTickets = args.numberTickets
    file = args.outputFile

    #initialise variables
    start = datetime.date(2015, 1, 1)
    end = datetime.date(2021, 1, 1)

    category = ["Phone", "TV", "Appliance", "Computer"]
    phone = ["Plan", "New Device", "Old Device"]
    tv = ["Big", "Small", "Flatscreen"]
    appliance = ["Toaster", "Microwave", "Kettle"]
    computer = ["Keyboard", "Mouse", "Desktop"]

    group = ["Refund", "Purchase", "Invoice", "Quote"]
    issue = ["Incident", "None", "Accident"]
    contacted = [True, False]

    otherIDCount = 0
    endIDCount = -1
    numActivities = 0

    ticketIDs = list(range(1, 10000))
    random.shuffle(ticketIDs)

    otherID = list(range(1, 90000))
    random.shuffle(otherID)

    finalDates = returnDates()

    #initialise JSON
    x = {
        "metadata":[],
        "activies_data": []
    }

    #create as many tickets as entered in arguments and add to activities data
    v = 0
    while v < numTickets:
        x["activies_data"].append(createActivities())
        v += 1

    #add start and end dates + activity count to metadata in JSON
    x.update({"metadata": {"start_at": finalDates[0].strftime('%d-%m-%Y %H:%M:%S +0000'),
         "end_at": finalDates[-1].strftime('%d-%m-%Y %H:%M:%S +0000'),
         "activities_count": numActivities}})

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(x, f, ensure_ascii=False, indent=4)
    