links={'BB1':[12,23,33]}
links['BB2']='BB3'
links['BB2']='BB1'
links['BB3']=[44]
if links.get('BB3'):
    links['BB3'].append(45)
else:
    links['BB3']=[44]

print(links)