import os
import networkx as nx
import json

print("working directory is "+os.getcwd())
os.chdir("www.submarinecablemap.com-master\public\\api\\v2\country")
print(os.getcwd())
print(os.listdir(os.getcwd()))
countries =os.listdir(os.getcwd())
country_cables={}
for filename in os.listdir(os.getcwd()):
    read_file=open(filename,encoding="utf8")
    country_name=filename.split(".")[0]
    data=json.load(read_file)
    cables_id=[]
    for cables in data["cables"]:
        cables_id.append(cables["cable_id"])
    country_cables[country_name]=cables_id
print(country_cables)

G=nx.Graph()
for name in country_cables:
    G.add_node(name)
print(list(G.nodes))
con_rem=dict(country_cables)
for x in country_cables:
    con_rem.pop(x)
    for y in country_cables[x]:
        for t in con_rem:
            for k in con_rem[t]:
                if y==k:
                    G.add_edge(x,t)
print(G.number_of_nodes())
print(G.number_of_edges())
print(list(G.edges))
os.chdir("/cableParser")
nx.write_gexf(G, "cableSub.gexf")