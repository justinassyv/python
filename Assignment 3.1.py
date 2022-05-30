sh = input("Enter hours: ")
sr = input("Enter rate :")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error enter numeric value")
    quit()

print(fh, fr)

if fh > 40:
    # calculate overtime
    reg = fh * fr
    over = (fh - 40) * (fr * 0.5)
    salary = reg + over
else:
    salary = fh * fr
print("Pay:", salary)
