from operator import contains
from urllib import response
from django.http import HttpResponse, JsonResponse
import requests
import os
import time
from random import randint

apiUrl = "https://api.rsc.org/compounds/v1/filter/element"
apiKey = os.environ.get("API_KEY")

def index(request):
    params = {
        "includeElements":["H", "B", "C", "N", "O", "F", "Al", "Si", "P", "S", "Cl"],
        "excludeElements":["He", "Li", "Be", "Ne", "Na", "Mg", "Ar", "K", "Ca", "Sc", "Ti", "V"],
        "orderBy": "molecularWeight"
    }
    response = requests.post(apiUrl, headers = {'apikey': apiKey}, json = params) 
    elementRequest = response.json()
    elementRequestDisplay= get_query_status(elementRequest)
    return JsonResponse(elementRequestDisplay)


def get_query_status(query_id):
    query_id = query_id["queryId"]
    res = requests.get(f'https://api.rsc.org/compounds/v1/filter/{query_id}/status', headers={'apikey': apiKey})
    data = res.json()
    queryResultDisplay = get_query_result(query_id)
    return queryResultDisplay

def get_query_result(query_id):
    #randomize the molecules
    params={
        "start": randint(0,990),
        "count": 10
    }
    start= time.time()
    res = requests.get(f'https://api.rsc.org/compounds/v1/filter/{query_id}/results', params = params, headers={'apikey': apiKey})
    end=start-time.time()
    print(end)
    data = res.json()
    getMolecularDisplay = get_molecular_data(data["results"])
    return getMolecularDisplay

def get_molecular_data(data):
    params={
        "recordIds":data,
        "fields": ["commonName", "stdinchiKey", "molecularWeight"]
    }

    res = requests.post(f'https://api.rsc.org/compounds/v1/records/batch', json = params, headers={'apikey': apiKey})
    data = res.json()
    filterMolecularData = filter_molecular_data(data)
    return filterMolecularData

#filter out common name constraint and return a list with valid molecules
def filter_molecular_data(data):
    filtered_molecules_common_name = []
    # print(len(data["records"]))
    #as we go thru every molecule and we check every name and see if that is in our common names and if it is, skip it(molecule) and not add it to our list.
    #Given, do, return
    for molecule in data["records"]:        
        if isMoleculeInCommonName(molecule) == False:
            filtered_molecules_common_name.append(molecule)
    filtered_by_charge(data)
    return data

#helper function
def isMoleculeInCommonName(molecule):
    common_names = ["ion", "ide", "ite", "ate", "ic", "ous", "ium", "hypo", "per", "(", ")", "I"]
    for name in common_names:
        molecule_name = molecule["commonName"]
        molecule_name = molecule_name.replace(" ", "")

        if name in molecule_name:
            return True
        elif molecule_name.isalnum():
            return False 
    return True

def filtered_by_charge(data):
    filtered_molecules = []    
    for molecule in data["records"]:
        stdinchi_key = molecule["stdinchiKey"]
        res = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{stdinchi_key}/property/MolecularFormula,Charge,Complexity/JSON')
        res_data = res.json()
        if "Fault" in res_data:
            continue
        elif res_data["PropertyTable"]["Properties"][0]["Charge"] == 0: 
            filtered_molecules.append(res_data["PropertyTable"]["Properties"][0]["MolecularFormula"])
    remove_molecules_starting_with_num(filtered_molecules)
    return data

def remove_molecules_starting_with_num(filtered_molecules):
    filtered_list = []
    for molecule in filtered_molecules:
        if molecule[0].isdigit():
            filtered_list.append(molecule)
    filter_atoms(filtered_list)

# filter for only 6 atoms
final_list = []
def filter_atoms(filtered_list):
    for formula in filtered_list:
        if not formula.isalpha():
            print("entered helper function")
            filter_for_max_atoms(formula)
        else:
            count = len(formula)
            print(count)
            if count <= 6:
                final_list.append(formula)
    print(final_list)

# helper function to filter atoms
def filter_for_max_atoms(filtered_list):
    for formula in filtered_list:
        count = 0
        for char in range(len(formula) - 1):
            if (formula[char] + 1).isdigit():
                count += int(formula[char] + 1)
            else:
                count += 1
    if count <= 6:
        final_list.append(formula)   
    print(count)




