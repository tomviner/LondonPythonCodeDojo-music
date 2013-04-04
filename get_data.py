import csv

def main():
    r = csv.reader(open('./planet-data.csv'))

    planets = r.next()
    planets = [{'name': p.strip('\xc2\xa0')} for p in planets][1:]
    print planets
    data = list(r)
    notes = []
    for row in data:
        print row
        name = row[0]
        rest = row[1:]
        notes.extend(rest)
        for pl, n in zip(planets, rest):
            pl[name] = n
    return notes

if __name__ == '__main__':
    main()