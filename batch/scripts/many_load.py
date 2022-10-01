import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for database in [Site, Category, State, Region, Iso]:
        database.objects.all().delete()

    # Format
    # name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso
    # |_0_|____1______|______2______|_3__|___4_____|____5___|______6______|___7____|__8__|__9___|_10_|

    for row in reader:
        print(row[0])

        name = row[0]; desc = row[1]
        justify = row[2] if row[2] != 'NaN' else None

        try: year = int(row[3])
        except: year = None

        try: longi = float(row[4])
        except: longi = None

        try: lati = float(row[5])
        except: lati = None

        try: area = float(row[6])
        except: area = None


        _Category, is_created = Category.objects.get_or_create(name=row[7])
        _State, is_created = State.objects.get_or_create(name=row[8])
        _Region,is_created  = Region.objects.get_or_create(name=row[9])
        _Iso, is_created  = Iso.objects.get_or_create(name=row[10])

        site = Site(name = name,
                    year = year,
                    longitude = longi,
                    latitude = lati,
                    description = desc,
                    justification = justify,
                    area_hectares = area,
                    category = _Category,
                    state = _State,
                    region = _Region,
                    iso = _Iso,
                  )
        site.save()
