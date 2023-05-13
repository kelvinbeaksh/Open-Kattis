for _ in range(int(input())):
    d,m = map(str, input().split(" "))
    if (m == "Mar" and int(d)>=21) or (m =="Apr" and int(d)<=20):
        print("Aries")
    if (m == "Apr" and int(d)>=21) or (m =="May" and int(d)<=20):
        print("Taurus")
    if (m == "May" and int(d)>=21) or (m =="Jun" and int(d)<=21):
        print("Gemini")
    if (m == "Jun" and int(d)>=22) or (m =="Jul" and int(d)<=22):
        print("Cancer")
    if (m == "Jul" and int(d)>=23) or (m =="Aug" and int(d)<=22):
        print("Leo")
    if (m == "Aug" and int(d)>=23) or (m =="Sep" and int(d)<=21):
        print("Virgo")
    if (m == "Sep" and int(d)>=22) or (m =="Oct" and int(d)<=22):
        print("Libra")
    if (m == "Oct" and int(d)>=23) or (m =="Nov" and int(d)<=22):
        print("Scorpio")
    if (m == "Nov" and int(d)>=23) or (m =="Dec" and int(d)<=21):
        print("Sagittarius")
    if (m == "Dec" and int(d)>=22) or (m =="Jan" and int(d)<=20):
        print("Capricorn")
    if (m == "Jan" and int(d)>=21) or (m =="Feb" and int(d)<=19):
        print("Aquarius")
    if (m == "Feb" and int(d)>=20) or (m =="Mar" and int(d)<=20):
        print("Pisces")