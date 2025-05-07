#MatchCaseEx4.py
wkn=input("Enter Week Name:")
if wkn.upper() in ["MON",'TUE','WED',"THU","FRI","SAT","SUN","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]:
    match(wkn[0:3].upper()):
        case "MON" | 'TUE'|'WED'|"THU"|"FRI":
            print("{} is Working Day".format(wkn))
        case "SAT":
            print("{} is WEEK END".format(wkn))
        case "SUN":
            print("{} is HOLI Day".format(wkn))
else:
    print("{} is not a week day".format(wkn))