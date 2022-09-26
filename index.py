import cx_Oracle
import csv
from logging import exception

# referencing oracle client directory to call packages
cx_Oracle.init_oracle_client(
    lib_dir=r"C:\Users\Rajiv\Desktop\rnn\instantclient_21_6")

# connecting to oracle omega server
try:

    con = cx_Oracle.connect("rrn6606", "RajivNidumolu6606",
                            'acaddbprod.uta.edu:1523/pcse1p.data.uta.edu')

    if con:
        print("cx_Oracle version:", cx_Oracle.version)
        print("Database version:", con.version)
        print("Client version:", cx_Oracle.clientversion())
    else:
        print("Connection to database failed....")
    # Creating cursor variable to access the database
    cursor = con.cursor()

    # Executing test query
    cursor.execute("select sys.database_name from dual")
    row = cursor.fetchone()
    print(row)

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# inserting Country.csv data to Country Table
with open("Country.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i in csv_reader:
        Country_Name = i[0]

        Population = i[1]
        No_of_Worldcup_won = i[2]
        Manager = i[3]
        sql = '''INSERT INTO COUNTRY (Country_Name,Population,No_of_Worldcup_won,Manager) VALUES (:a,:b,:c,:d)'''
        cursor.execute(sql, (Country_Name, Population,
                       No_of_Worldcup_won, Manager))
        con.commit()
# inserting Player.csv data to Player Table
with open("Players.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i in csv_reader:
        Player_id = i[0]
        Name = i[1]
        Fname = i[2]
        Lname = i[3]
        Dob = i[4]
        Country = i[5]
        Height = i[6]
        Club = i[7]
        Position = i[8]
        Caps_for_Country = i[9]
        Is_captain = i[10]
        sql = '''INSERT INTO PLAYERS (Player_id,Name,Fname,Lname,Dob,Country,Height,Club,Position,Caps_for_Country,Is_captain) VALUES(:A,:B,:C,:D,:E,:F,:G,:H,:I,:J,:K)'''
        cursor.execute(sql, (
            Player_id, Name, Fname, Lname, Dob, Country, Height, Club, Position, Caps_for_Country, Is_captain))
        con.commit()
# inserting Match_results.csv data into Match_results table
with open("Match_results.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i in csv_reader:
        Match_id = i[0]
        Date_of_match = i[1]
        Start_time_of_match = i[2]
        Team1 = i[3]
        Team2 = i[4]
        Team1_score = i[5]
        Team2_score = i[6]
        Stadium_Name = i[7]
        Host_City = i[8]

        sql = '''INSERT INTO MATCH_RESULTS (Match_id,Date_of_match,Start_time_of_match,Team1,Team2,Team1_score,Team2_score,Stadium_Name,Host_City) VALUES(:A,:B,:C,:D,:E,:F,:G,:H,:I)'''
        cursor.execute(sql, (
            Match_id, Date_of_match, Start_time_of_match, Team1, Team2, Team1_score, Team2_score, Stadium_Name,
            Host_City))
        con.commit()
# inserting Player_Cards.csv data to player cards Table
with open("Player_Cards.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i in csv_reader:
        Player_id = i[0]
        Yellow_Cards = i[1]
        Red_Cards = i[2]

        sql = '''INSERT INTO Player_Cards (Player_id,Yellow_Cards,Red_Cards) VALUES(:A,:B,:C)'''
        cursor.execute(sql, (Player_id, Yellow_Cards, Red_Cards))
        con.commit()
# inserting Player_assists_goals.csv into palyer_assists_goals table
with open("Player_Assists_Goals.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i in csv_reader:
        Player_id = i[0]
        No_of_Matches = i[1]
        Goals = i[2]
        Assists = i[3]
        Minutes_Played = i[4]

        sql = '''INSERT INTO Player_Assists_Goals (Player_id,No_of_Matches,Goals,Assists,Minutes_Played) VALUES(:A,:B,:C,:D,:E)'''
        cursor.execute(sql, (Player_id, No_of_Matches,
                       Goals, Assists, Minutes_Played))
        con.commit()
