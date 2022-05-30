def computepay(h, r):
    if h > 40:
        reg = h * r
        over = (h-40)*(r*0.5)
        salary = reg + over
    else:
        salary = h * r
    return salary


hrs = input("Enter Hours:")
rate = input("Enter rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Incorrect value")

p = computepay(h, r)
print("Pay", p)
