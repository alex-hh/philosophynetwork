import requests

q = """PREFIX wd: <http://www.wikidata.org/entity/>
       PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
       SELECT ?dob WHERE {
       ?phil wdt:P646 {} .
       ?phil wdt:P569 ?dob . }""".format(freebase_id)

# https://query.wikidata.org/#PREFIX%20wd%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fentity%2F%3E%0APREFIX%20wdt%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fprop%2Fdirect%2F%3E%0A%0ASELECT%20%20%3Fphil%20%3Fdb%20%20WHERE%20%7B%0A%20%3Fphil%20wdt%3AP646%20%22%2Fm%2F099bk%22%20.%0A%20%3Fphil%20wdt%3AP569%20%3Fdb%20.%0A%20%7D

endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"

payload = {'format': 'json', 'query': q}

r = requests.get(endpoint, params=payload)

dob = r.json()['results']['bindings'][0]['dob']['value']


# q_all """PREFIX wd: 
# SELECT ?signature WHERE { 
#   ?signature [some gene-symbol property] ?symbol .
#   FILTER (?symbol IN ("Ache", "Bcan", "Gjbl"))
# }
# GROUP BY ?signature

with open('philsutf8.csv', 'r+', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'freebase_id', 'dob']
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for row in reader:
        writer.writerow({'name': row['name'].encode('utf8'), 'freebase_id': row['freebase_id'], 'dob': row['dob']})

def dob_from_fbid(fbid):
    q = ("PREFIX wd: <http://www.wikidata.org/entity/> "
         "PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
         "SELECT ?dob WHERE { "
         "?phil wdt:P646 '%s' . "
         "?phil wdt:P569 ?dob . }") % (fbid)
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    payload = {'format': 'json', 'query': q}
    dob = ''
    try:
        r = requests.get(endpoint, params=payload, verify=False)
    except:
        return dob
    if r.status_code == 200:
        try:
            dob = r.json()['results']['bindings'][0]['dob']['value']
        except:
            pass
    return dob


def freebase_dob(fbid):
    payload = {'query': fbid, 'key': api_key, 'output': '(/people/person/date_of_birth)'}
    endpoint = "https://www.googleapis.com/freebase/v1/search"
    r = requests.get(endpoint, params=payload, verify=False)
    dob = ''
    if r.status_code == 200:
        try:
            dob = r.json()['result'][0]['output']['/people/person/date_of_birth']['/people/person/date_of_birth'][0]
        except:
            pass
    return dob

api_key = "AIzaSyCYuUBb7jEeEyf8GV6xIziV8i4X7NDduj8"

with open('phils3.csv', 'w') as outfile:
    with open('phils.csv', 'r') as csvfile:
        fieldnames = ['name', 'freebase_id', 'dob']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row['dob']:
                dob = freebase_dob(row['freebase_id'])
            else:
                dob = row['dob']
            writer.writerow({'name': row['name'].encode('utf8'),
                             'freebase_id': row['freebase_id'],
                             'dob': dob})


'/\d{3, 4}-{1}\d{2}-{1}\d{2}/$'
full_date_pattern = r"(-?\d{3,4}-{1}\d{2}-{1}\d{2})"

# make a new birth year column
with open('phils_birth_years.csv', 'w') as outfile:
    fieldnames = ['name', 'freebase_id', 'yob']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    with open('phils3.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        full_date_pattern = r"(-?\d{3,4})(-{1}\d{2}-{1}\d{2})"
        year_pattern = r"(-?\d{3,4})"
        for row in reader:
            full_match = re.match(full_date_pattern, row['dob'])
            y_match = re.match(year_pattern, row['dob'])
            if full_match:
                year = full_match.group(1)
            elif y_match:
                year = y_match.group(0)
            writer.writerow({'name': row['name'],
                             'freebase_id': row['freebase_id'],
                             'yob': year})

with open('phils.csv', 'w') as csvfile:
    fieldnames = ['name', 'freebase_id', 'dob']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for p in InfluenceNode.objects.filter(is_philosopher=True):
        dob = dob_from_fbid(p.freebase_id)
        writer.writerow({'name': p.name.encode('utf-8'), 'freebase_id': p.freebase_id, 'dob': dob})
