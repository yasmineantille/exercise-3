import requests
import urllib
from requests.exceptions import HTTPError
import csv
graph_address = "https://graphdb.interactions.ics.unisg.ch/repositories/was-assignment-3/statements?update="

user ="was-students"
passcode = "assignment-3-is-fun"

def readfile(filename):
    f = open(filename,"r")
    string_query = f.read()
    return string_query
 
def print_query_results(sparql_query_results):
    reader = csv.reader(sparql_query_results.splitlines(), delimiter=';')
    for row in reader:
        for r in row:
            fields = r.split(',')
            for f in fields:
                print("Fields: ", f)
                
def execute_SPARQL_Update(string_query): 
    encoded_query = urllib.parse.quote_plus(string_query)
    query = graph_address + encoded_query
    response = requests.post(query, auth=(user, passcode), verify=True)
    try:
        print('Success executing query! \n')   
        sparql_query_results = response.text
        return sparql_query_results   
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def main():
    fileName = input("Name of the SPARQL update file: ")
    string_query = readfile(fileName)
    sparql_query_results = execute_SPARQL_Update(string_query)
    print_query_results(sparql_query_results)

if __name__ == "__main__":
    main()