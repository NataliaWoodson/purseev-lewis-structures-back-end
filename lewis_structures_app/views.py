from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.http import require_http_methods
import requests
import os

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


# def getQueryStatus(queryId):
#     query_Id = queryId["queryId"]
#     res = requests.get(f'https://api.rsc.org/compounds/v1/filter/{query_Id}/status', headers={'apikey': apiKey})
#     data = res.json
#     print(f'dataresponse: {data}')
#     return JsonResponse(data)

def get_query_status(query_id):
    query_id = query_id["queryId"]
    res = requests.get(f'https://api.rsc.org/compounds/v1/filter/{query_id}/status', headers={'apikey': apiKey})
    data = res.json()
    # print(f'data response: {data}')
    queryResultDisplay = get_query_result(query_id)
    return queryResultDisplay

def get_query_result(query_id):
    print(query_id)
    params={
        "start": 0,
        "count": 10
    }
    res = requests.get(f'https://api.rsc.org/compounds/v1/filter/{query_id}/results', params = params, headers={'apikey': apiKey})
    data = res.json()
    # print(f'data response: {data}')
    getMolecularDisplay = get_molecular_data(data["results"])
    return getMolecularDisplay

def get_molecular_data(data):
    # print(data)
    params={
        "recordIds":data,
        "fields": ["Formula","smiles", "commonName", "stdinchiKey", "molecularWeight"]
    }
    res = requests.post(f'https://api.rsc.org/compounds/v1/records/batch', json = params, headers={'apikey': apiKey})
    data = res.json()
    # print(f'data response: {data}')
    return data



