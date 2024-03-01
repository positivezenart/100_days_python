#GET == Extract data
#POST == Post a data
#PUT == Update a data
#DELETE == Delete a data
import requests
import datetime as dt
TOKEN= "NPRHBXKY5LOQA1DQ"
USER_NAME = "mjack855"

today = dt.date.today().strftime("%Y%m%d")
pixela_end_point = 'https://pixe.la/v1/users'
user_params = {
        "token":"NPRHBXKY5LOQA1DQ",
        "username":"mjack855",
        "agreeTermsOfService":"yes",
        "notMinor": "yes",
        "thanksCode":"ThisIsThanksCode"
        
}
Graph_end_point = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
graph_config ={
    "id": "graph1",
    "name":"Bike Riding Graph",
    "unit" : "Km",
    "type": "float",
    "color" :"shibafu"
}
headers ={
    "X-USER-TOKEN":TOKEN
}

pers_graph_end_point ="https://pixe.la/v1/users/mjack855/graphs/graph1"
bike_graph ={
    "date":today,
    "quantity":"20"
}
#response=requests.post(url=pixela_end_point,json=user_params)
#response.raise_for_status()
#print(response.text)

#response_graph = requests.post(url=Graph_end_point,json=graph_config,headers=headers)

#pixel_sent = requests.post(url=pers_graph_end_point,json=bike_graph,headers=headers)
update_kM_pixel ="https://pixe.la/v1/users/mjack855/graphs/graph1/20240301"
update_graph = requests.put(url=update_kM_pixel,json={"quantity":"25"},headers=headers)
print(update_graph.text)

delete_a_graph = requests.delete(url="https://pixe.la/v1/users/mjack855/graphs/graph1/20231223",headers=headers)
print(delete_a_graph.text)


