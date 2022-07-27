from operator import contains
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.http import require_http_methods
import requests
import os
import time
from random import randint

apiUrl = "https://api.rsc.org/compounds/v1/filter/element"
apiKey = os.environ.get("API_KEY")

# @require_http_methods(["POST"])
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    params = {
        "includeElements":["H", "B", "C", "N", "O", "F", "Al", "Si", "P", "S", "Cl"],
        "excludeElements":["He", "Li", "Be", "Ne", "Na", "Mg", "Ar", "K", "Ca", "Sc", "Ti", "V"],
        "orderBy": "molecularWeight"
    }
    response = requests.post(apiUrl, headers = {'apikey': apiKey}, json = params) 
    # print(response.status_code)
    elementRequest = response.json()
    # print(f'element request: {elementRequest}')
    print(JsonResponse(elementRequest))
    elementRequestDisplay= get_query_status(elementRequest)
    return JsonResponse(elementRequestDisplay)


def get_query_status(query_id):
    query_id = query_id["queryId"]
    res = requests.get(f'https://api.rsc.org/compounds/v1/filter/{query_id}/status', headers={'apikey': apiKey})
    data = res.json()
    # print(f'data response: {data}')
    queryResultDisplay = get_query_result(query_id)
    return queryResultDisplay

def get_query_result(query_id):
    print(query_id)
    #randomize the molecules
    params={
        "start": randint(0,990),
        "count": 10
    }
    print(params)
    start= time.time()
    res = requests.get(f'https://api.rsc.org/compounds/v1/filter/{query_id}/results', params = params, headers={'apikey': apiKey})
    end=start-time.time()
    print(end)
    data = res.json()
    # print(f'data response: {data}')
    getMolecularDisplay = get_molecular_data(data["results"])
    return getMolecularDisplay

def get_molecular_data(data):
    # print(data)
    
    params={
        "recordIds":data,
        "fields": ["commonName", "stdinchiKey", "molecularWeight"]
    }

    res = requests.post(f'https://api.rsc.org/compounds/v1/records/batch', json = params, headers={'apikey': apiKey})
    data = res.json()
    # print(f'data response: {data}')
    filterMolecularData = filter_molecular_data(data)
    return filterMolecularData

#filter out common name constraint and return a list with valid molecules
def filter_molecular_data(data):
    filtered_molecules_common_name = []
    # print(len(data["records"]))
    #as we go thru every molecule and we check every name and see if that is in our common names and if it is, skip it(molecule) and not add it to our list.
    #Given, do, return
    for molecule in data["records"]:
        # print(molecule["commonName"])
        
        if isMoleculeInCommonName(molecule) == False:
            filtered_molecules_common_name.append(molecule)

    # print(f'filtered name: {filtered_molecules_common_name}')
    
    filtered_by_charge(data)

    return data

#helper function
def isMoleculeInCommonName(molecule):
    common_names = ["ion", "ide", "ite", "ate", "ic", "ous", "ium", "hypo", "per", "(", ")", "I"]
    for name in common_names:
        molecule_name = molecule["commonName"]
        molecule_name = molecule_name.replace(" ", "")

        if name in molecule_name:
        # if name in molecule["commonName"]:
            return True
        elif molecule_name.isalnum():
            return False 
    return True

def filtered_by_charge(data):
    filtered_molecules = []    
        # print(data["records"])
    print("lengthBefore", len(data["records"]))
    for molecule in data["records"]:
        stdinchi_key = molecule["stdinchiKey"]
        # smiles = molecule["smiles"]
        res = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{stdinchi_key}/property/MolecularFormula,Charge,Complexity/JSON')
        res_data = res.json()
        if "Fault" in res_data:
            continue
        elif res_data["PropertyTable"]["Properties"][0]["Charge"] == 0: 
            filtered_molecules.append(res_data["PropertyTable"]["Properties"][0]["MolecularFormula"])
        # try:
        #     if res_data["PropertyTable"]["Properties"][0]["Charge"] == 0:
        #         filtered_molecules.append(res_data["PropertyTable"]["Properties"][0]["MolecularFormula"])
        # except KeyError:
        #     print(res_data)
        #     raise
    print(filtered_molecules)
    print("lengthAfter", len(filtered_molecules))
    remove_molecules_starting_with_num(filtered_molecules)
    return data

def remove_molecules_starting_with_num(filtered_molecules):
    filtered_list = []
    # iterate through every formula
    # if first char is not num:
        # add to list
    for molecule in filtered_molecules:
        if molecule[0].isdigit():
            filtered_list.append(molecule)

    print("filtered list:", filtered_list)
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




