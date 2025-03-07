import sys
from constants import country_codes

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    # If the length is odd, return the middle element
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    # If the length is even, return the average of the two middle elements
    else:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        return (middle1 + middle2) / 2

data = []
stations = dict()
year = 0
country = 0
#ASN00086071,1855,167
first = True
for i in sys.stdin:
    if first:
        first = False
        year = int(i[12:16])
    country = country_codes.get(i[:2]) 
    stations.setdefault(country, []).append(int(i[17:].strip()))
#print(country,year,find_median(data),sep=",")

for i in stations.keys():
    #print(len(stations[i]), i)
    print(i,year,find_median(stations[i])/10,sep=",")

