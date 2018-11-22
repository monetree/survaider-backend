from django.shortcuts import render
from django.http import JsonResponse
import pymongo

myclient = pymongo.MongoClient("mongodb://mongo:27017/")
mydb = myclient["survaider"]


def graph_data(request):
    col = mydb["adult"]

    lst=[]
    male_lst=[]
    female_lst=[]
    dict = {}

    #male relationship list
    male_Unmarried_lst = []
    male_Husband_lst = []
    male_own_child_lst = []
    male_not_in_family_lst = []
    male_wife_lst = []

    #female relationship list
    female_Unmarried_lst = []
    female_Husband_lst = []
    female_own_child_lst = []
    female_not_in_family_lst = []
    female_wife_lst = []

    for x in col.find({"sex":"Male"}):
        male_lst.append(x)
    for i in male_lst:
        i.pop('_id', None)



    #find male relationships
    for x in col.find({"sex":"Male","relationship":"Unmarried"}):
        male_Unmarried_lst.append(x)
    dict["male_Unmarried"] = len(male_Unmarried_lst)

    for x in col.find({"sex":"Male","relationship":"Husband"}):
        male_Husband_lst.append(x)
    dict["male_Husband"] = len(male_Husband_lst)

    for x in col.find({"sex":"Male","relationship":"Own-child"}):
        male_own_child_lst.append(x)
    dict["male_own_child"] = len(male_own_child_lst)

    for x in col.find({"sex":"Male","relationship":"Not-in-family"}):
        male_not_in_family_lst.append(x)
    dict["male_not_in_family"] = len(male_not_in_family_lst)

    for x in col.find({"sex":"Male","relationship":"Wife"}):
        male_wife_lst.append(x)
    dict["male_wife"] = len(male_wife_lst)
    ################# end ##############################



    for x in col.find({"sex":"Female"}):
        female_lst.append(x)

    for i in female_lst:
        i.pop('_id', None)



    #find female relationships
    for x in col.find({"sex":"Female","relationship":"Unmarried"}):
        female_Unmarried_lst.append(x)
    dict["female_Unmarried"] = len(female_Unmarried_lst)

    for x in col.find({"sex":"Female","relationship":"Husband"}):
        female_Husband_lst.append(x)
    dict["female_Husband"] = len(female_Husband_lst)

    for x in col.find({"sex":"Female","relationship":"Own-child"}):
        female_own_child_lst.append(x)
    dict["female_own_child"] = len(female_own_child_lst)

    for x in col.find({"sex":"Female","relationship":"Not-in-family"}):
        female_not_in_family_lst.append(x)
    dict["female_not_in_family"] = len(female_not_in_family_lst)

    for x in col.find({"sex":"Female","relationship":"Wife"}):
        female_wife_lst.append(x)
    dict["female_wife"] = len(female_wife_lst)
    ################# end ##############################

    #total male and female count
    dict["males"] = len(male_lst)
    dict["females"] = len(female_lst)
    lst.append(dict)
    chart_format = [{'label': k, 'value': v} for k, v in lst[0].items()]
    chart = {"dataSource":{"chart":{},"data":{}}}
    chart["type"] = "Pie3D"
    chart["width"] = 1000
    chart["height"] = 700
    chart["dataFormat"] = "json"
    chart["dataSource"]["chart"] =  {
              "caption": "Male and female details",
              "subCaption": "To display total Male AND Females with relationships",
              "showValues": "1",
              "showPercentInTooltip": "0",
              "enableMultiSlicing": "1",
              "theme": "fusion"
            }
    chart["dataSource"]["data"] = chart_format

    return JsonResponse(chart,safe=False)

def table_data(request):
    col = mydb["adult"]
    lst=[]
    for x in col.find():
        lst.append(x)
    for i in lst:
        i.pop('_id', None)
    return JsonResponse(lst,safe=False)
