#I think that i will need only nx and json
import networkx as nx
import json
from urlparse import urlparse

#A prototype for a url parser (from URL get domain)
#this will considered the source
def domainretrieve(link):
    parsed_uri = urlparse(link)
    domain = '{uri.scheme}://{uri.netloc}/'.format(parsed_uri)
    return domain

filename='semantic-entities.json'

fh = open('semantic-entities.json')

fc = open('graph.dot')

data = json.load(fh)

##Initialize NX graph
G = nx.MultiGraph()



##From here parse the JSON to get for each source the topics
#Ie consider to loop on each entity |-> check for errors? TODO

#Cycle for each entity

for (idx,entity) in enumerate(data):

    try:
        if(data[idx]["error"]):
            continue
    except KeyError:
        pass

    source = domainretrieve(data[idx]["url"])

    if source not in G.nodes():
        G.add_node(source)

    #Select the timestamp
    ts = data[idx]["timestamp"][1]["$date"]

    #For each topic add aNEW edge with the property timestamp
    for (jdx, topic_properties) in enumerate(data[idx]["annotations")]:

            topic = topic_properties["label"]

            #Create and edge

            G.add_edge(source,topic,timestamp=ts)

                ##Fr thos not present create a list of timestamps, set as property of the edge
            
            #Append to the edge's list the timestamp
    

#PASS to retrieve domain to get the URL -> this considered the SOURCE
#Cycle through the annotations, retrieve the title -> add the to the graph

#In the above cycle and edge property will be the timestamp here comes the only
#hard part : if teh edge is still present; then the new timestamp must be appended to a list
#OK i will check it with has_edge
#From the 


#Write in DOT formt the graph
write_dot(G,fc)

close(fh)
clos(fc)

#Open the DOT file (possibly above the fh)

#Write the graph on the DOT file

#Close both files
