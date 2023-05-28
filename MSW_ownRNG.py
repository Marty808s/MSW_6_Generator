import platform  # build in
import cpuinfo

import psutil
import datetime
import time

digits_to_keep = 5

def date():
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.timestamp()
    print(timestamp)
    return timestamp


def seed(iter):
    # SEED
    cpu_list = []

    # cpu % v intervalu 0,1
    for i in range(iter):
        cpu = psutil.cpu_percent(interval=0.1)
        cpu_list.append(cpu)
        print("ve for cpu%usage", cpu_list)

    cpu_clock = time.perf_counter()

    print("AKTUALNI CPU up time clock:",cpu_clock)

    cpu_perc = round(((sum(cpu_list) * cpu_clock)*date()))

    shorted_number = cpu_perc//10**(len(str(cpu_perc)) - digits_to_keep)

    print("Výsledná suma rounded:", shorted_number)
    return shorted_number


# ANALÝZA
pocet_prvku = 1000
analytic_seed = []

for i in range(pocet_prvku):
    x = seed(15)
    analytic_seed.append(x)

print(analytic_seed)
print(len(analytic_seed))

analytic_seed_remover = analytic_seed.copy()

def check(analytic_seed, analytic_seed_remover):
    duplicit = []
    for _ in range(len(analytic_seed)):
        print("Číslo pozice:", _)

        y = analytic_seed[_]
        print("y je:", y)

        analytic_seed_remover.remove(y)
        print("Zbylé znaky ke kontrole:", analytic_seed_remover)

        if y not in analytic_seed_remover:
            print("Ales gute!")
        else:
            print("Schoda na znaku!:",y)
            duplicit.append(y)
            next

    print("DUPLICITY:", duplicit)
    print("POČET DUPL. ZNAKŮ:", len(duplicit))
    return duplicit


#RUN CHECK
check(analytic_seed,analytic_seed_remover)


