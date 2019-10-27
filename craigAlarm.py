from craigslist import CraigslistForSale
cl_h = CraigslistForSale(site='vancouver', area='van', category='cta',
                         filters=dict(max_price=15000, min_price=1000, make='lexus', max_miles=200000, has_image=True))

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    print (result)

