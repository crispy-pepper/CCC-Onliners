m,d = int(input()),int(input());print(((m > 2 or (m == 2 and d > 18))*"After")+((m < 2 or (m == 2 and d < 18))*"Before")+((m == 2 and d == 18)*"Special"))