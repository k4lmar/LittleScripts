import datetime
year=int(input("YEAR? ->"))
d=datetime.date(year,1,1)
s=""
honapok=["Január", "Február","Március",
         "Április","Május","Június",
         "Július","Augusztus","Szeptember",
         "Október","November","December"]
midx=-1;
while d.year<year+1:
    if d.day==1:
        midx+=1
        s+="\n"+honapok[midx]+"\nH\tK\tSze\tCs\tP\tSzo\tV\n"
        for i in range(d.weekday()):
            s+="\t"
    s+=str(d.day)
    if d.weekday()<6:
        s+="\t"
    else: s+="\n"
    d+=datetime.timedelta(days=1)
print(s)
if(int(input("Write to file? (1->yes)"))==1):
    filename=str(year)+"calendar.txt"
    open(filename,"w").write(s)
