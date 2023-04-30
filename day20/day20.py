#pip

import numpy
import pandas
import requests
#import webbrowser the tutorial says that package comes with python

lst = [1,2,3,4,5]
np_arr = numpy.array(lst)
print(np_arr)

np_arr *= 2
print(np_arr)


url = "https://youtube.com"
#webbroswer.open_new_tab(url)

#pip uninstall package to uninstall
#pip list to list packages
#pip show (package) to get information about a package

#pip freeze generates a list of packages and their installed versions for use in a requirements.txt document during deployment


#I have used the requests package before during some ctfs

#I got a 404 error with this url
url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"

response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
#print(response.text)

#this website seems to be down too
url = "https://restcountries.eu/rest/v2/all"
#response = requests.get(url)
#print(response)
#print(response.status_code)

#countries = response.json
#print(countries[:1])

#a package can contain one of more relevant modules

from mypackage import arithmetic as ar

print(ar.add_numbers(1,2,3,4,5))
print(ar.multiple(5,3))

print(ar.division(1,10))
print(ar.remainder(100,57))
print(ar.power(12,65))
