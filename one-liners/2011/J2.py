h,m = int(input()),int(input());l=[f"The balloon first touches ground at hour:\n{t}" if (-6*(t**4))+(h*(t**3))+(2*(t**2))+t <= 0 else '' for t in range(1, m+1)]+["The balloon does not touch ground in the given time."];print(l[l.count(''):][0])