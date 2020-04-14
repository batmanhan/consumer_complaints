import csv
import datetime
from sys import argv

files = sys.argv[1:]
input_file = files[0]
output_file = files[1]

# Load
with open(files[0], 'rb') as _file:
    data = list(csv.reader(_file))

# List of Product
pd = []
for n in range(len(data)):
    if n <> 0:
        pd.append(data[n][1].lower())
pd_list = set(pd)

# List of Year
yr = []
for n in range(len(data)):
    if n <> 0:
        yr.append(datetime.datetime.strptime(data[n][0], '%Y-%m-%d').year)
yr_list = set(yr)


# Generate Output
output = []
grp = 1
for _pdt in pd_list:
    for _yr in yr_list:
        df = []
        for n in range(len(data)):
            if n <> 0:
                d_yr = datetime.datetime.strptime(data[n][0], '%Y-%m-%d').year
                d_pdt = data[n][1].lower()
                if d_yr == _yr and d_pdt == _pdt:
                    df.append(data[n][7].lower())

        d = {x: df.count(x) for x in set(df)}

        if d:
            claims = sum(d.values())
            companies = len(d)
            perc = int(round(float(sorted(d.items(), reverse=True, key=lambda x: x[1])[0][1]) / float(claims) * 100))

            output.append([_pdt, _yr, claims, companies, perc])
            print(str(grp) + '/' + str(len(yr_list) * len(pd_list)) + ' from ' + _pdt + ' in Year of ' + str(_yr))
        grp = grp + 1

# Sort by Product and Year Fields
output = sorted(output, key=lambda x: (x[0], x[1]))

# Add "
for i in range(len(output)):
    if output[i][0].count(',') > 0:
        output[i][0] = '"' + output[i][0] + '"'

# Create CSV
with open(files[1],'wb') as file:
    for sublist in output:
        for item in sublist:
            file.write(str(item) + ',')
        file.write('\n')

print('done!')
