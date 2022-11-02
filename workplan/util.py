from .models import *

workplan = open('wp_import.txt','r').read()
wp_periods = workplan.split('-'*100)

def create_period():
    "Iterate over wp_periods and create Period instances"
    items = wp_periods[0].strip().split('\n')
    print(items)
    i = input('Continue?')
    if not i == "y":
        return
    months = items[-1].split('-')
    if len(months) == 1:
        months = 2 * months
    months = tuple(map(int,months))
    users = items[-2].split(',')
    if users == ["ALL"]:
        users = User.objects.all()
    else:
        users = [User.objects.get(username=u.strip()) for u in users]
    period = Period.objects.create()
    period.users.set(users)
    period.set_start_end(*months)
    for i in items[:-2]:
        s = i.split()
        t = i[0]
        label = s[0]
        text = ' '.join(s[1:])
        Item.objects.create(type=t,label=label,text=text.strip(),period=period)
    wp_periods.pop(0)
