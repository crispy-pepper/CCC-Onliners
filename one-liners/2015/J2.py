t = input();print(((t.count(":-)")>t.count(":-("))*"happy")+((t.count(":-(") > t.count(":-)"))*"sad")+((t.count(":-)") == t.count(":-(") == 0)*"none")+((t.count(":-)") == t.count(":-(") and t.count(":-)") !=0)*"unsure"))