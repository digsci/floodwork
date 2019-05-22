from SPARQLWrapper import SPARQLWrapper, JSON
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
from sklearn import datasets, linear_model
import numpy as np
import utility

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

def getQueryString(n):
    sparql_query = """
    prefix p:       <http://ensembleprojects.org/ns/floodrisk/property#>
    prefix pd:      <http://ensembleprojects.org/ns/floodrisk/property_data#>

    select *
    from <http://ensembleprojects.org/floodrisk/property>
    where {{
        p:{} pd:q5_gauge ?q5_gauge ;
            pd:q10_gauge ?q10_gauge ;
            pd:q20_gauge ?q20_gauge ;
            pd:q50_gauge ?q50_gauge ;
            pd:q75_gauge ?q75_gauge ;
            pd:q100_gauge ?q100_gauge ;
            pd:q200_gauge ?q200_gauge ;
            pd:q1000_gauge ?q1000_gauge ;
            pd:q5_existingLevelMean ?q5_existingLevelMean ;
            pd:q10_existingLevelMean ?q10_existingLevelMean ;
            pd:q20_existingLevelMean ?q20_existingLevelMean ;
            pd:q20_existingLevelMean ?q20_existingLevelMean ;
            pd:q50_existingLevelMean ?q50_existingLevelMean ;
            pd:q75_existingLevelMean ?q75_existingLevelMean ;
            pd:q100_existingLevelMean ?q100_existingLevelMean ;
            pd:q200_existingLevelMean ?q200_existingLevelMean ;
            pd:q1000_existingLevelMean ?q1000_existingLevelMean ;
            pd:property_thresh ?property_thresh .
    }}
    """.format(n)
    return sparql_query

def getMetaDataString(n):
    sparql_metadata = """
    prefix p:       <http://ensembleprojects.org/ns/floodrisk/property#>
    prefix pd:      <http://ensembleprojects.org/ns/floodrisk/property_data#>
    prefix gd:      <http://ensembleprojects.org/ns/floodrisk/gauge_data#>
    prefix damage:  <http://ensembleprojects.org/ns/floodrisk/damage#>

    select ?model_name ?company ?date ?modelsource ?propertytype ?gauge ?ead_mean
    from <http://ensembleprojects.org/floodrisk/property>
    from <http://ensembleprojects.org/floodrisk/gauge>
    from <http://ensembleprojects.org/gauge>
    from <http://ensembleprojects.org/floodrisk/damage#0>
    where {{
    p:{} pd:model ?model ;
        pd:modelSource ?modelsource ;
        pd:jbapropertyType ?propertytype ;
        pd:jbapropRef ?propertyref ;
        pd:station_name ?gauge ;
        pd:gauge_siteRef ?gauge_siteref .
    ?s gd:site_reference ?gauge_siteref ;
        gd:station_model_id ?id .
    ?id gd:station_model_name ?model_name ;
        gd:station_model_company ?company ;
        gd:station_model_date ?date .
    ?ds damage:jbapropRef ?propertyref ;
        damage:ead_mean ?ead_mean 
        }}
    """.format(n)
    return sparql_metadata

def damageEstimate(property):
    sparql_endpoint = "http://localhost:8890/sparql"
    sparql_query = getQueryString(property)
    sparql = SPARQLWrapper(sparql_endpoint)
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    val_array = []
    depth_array = []
    for result in results["results"]["bindings"]:
        for k, v in result.items():
            if k == 'property_thresh':
                property_threshold = float(result[k]['value'])
            else:
                val_array.append(float(result[k]['value']))
    gauge_array = val_array[:int(len(val_array)/2)]
    flood_array = val_array[int(len(val_array)/2):]
    for d in flood_array:
        f = d-property_threshold
        if f > 0:
            depth_array.append(d-property_threshold)
        else:
            depth_array.append(0.0)
    plt.plot(gauge_array, depth_array,'--bo', label="Piecewise Linear")
    plt.xlabel("Gauge Level")
    plt.ylabel("Property Flood Height")
    depth_array_2d = np.reshape(depth_array, (-1, 1))
    gauge_array_2d = np.reshape(gauge_array, (-1, 1))
    regr = linear_model.LinearRegression()
    regr.fit(gauge_array_2d, depth_array_2d)
    predictions = regr.predict(gauge_array_2d)
    plt.plot(gauge_array_2d,predictions.flatten(),'--r', label="Linear Regression")
    plt.legend(loc='upper left')
    plt.show()
    sparql_query = getMetaDataString(property)
    sparql.setQuery(sparql_query)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("Model Study:\t", result['model_name']['value'])
        print("Organisation:\t", result['company']['value'])
        print("Date:\t\t", result['date']['value'])
        print("Model Source:\t", result['modelsource']['value'])
        print("Property Type:\t", result['propertytype']['value'])
        print("Gauge Station:\t", result['gauge']['value'])
    sparql_query = """
      PREFIX rt:<http://environment.data.gov.uk/flood-monitoring/def/core/>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX geo:<http://www.w3.org/2003/01/geo/wgs84_pos#>
      SELECT ?latestValue
      FROM <http://environment.data.gov.uk/flood-monitoring/id/stations.rdf>
      FROM <http://environment.data.gov.uk/flood-monitoring/id/measures.rdf>
      FROM <http://environment.data.gov.uk/flood-monitoring/data/readings.rdf>
      WHERE {
        ?s rdfs:label 'Bulwell' .
        ?s rt:measures ?measures .
        ?measures rt:latestReading ?latestReading .
        ?latestReading rt:value ?latestValue .
      }
      """
    sparql.setQuery(sparql_query)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("\nCurrent River Level from Environment Agency Real-Time Flood API: ", result['latestValue']['value'])
   
from SPARQLWrapper import SPARQLWrapper, JSON
import utility
import matplotlib
import matplotlib.pyplot as plt
def c_at_r_ead(posttown):
    sparql_endpoint = "http://localhost:8890/sparql"
    sparql = SPARQLWrapper(sparql_endpoint)
    sparql.setReturnFormat(JSON)
    sparql_query = utility.getPosttownDamageOriginal(posttown)
    sparql.setQuery(sparql_query)
    results = sparql.query().convert()
    returnPeriods = [2,5,10,20,50,75,100,200,1000]
    damageEstimations = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for result in results['results']['bindings']:
        n = 0
        for returnPeriod in result:
            damageEstimations[n] += float(result[returnPeriod]['value']) / 1000000.0
            n += 1   
    fig = plt.figure(figsize=(22, 6))
    ax1 = fig.add_subplot(1,2,1)
    line, = ax1.plot(returnPeriods, damageEstimations, color='#1B3022', marker='o', lw=2, label="Damage Estimation")
    fill = plt.fill_between(returnPeriods,damageEstimations,0.1,color='#395756', label='Expected Annual Damage')
    matplotlib.pyplot.setp(fill, alpha=0.3)
    ax1.set_xlabel("Return Period")
    ax1.set_ylabel("Damage Estimation (£M)")
    ax1.set_xscale('log')
    ax1.set_xticks([2,5,10,20,50,75,100,200,1000])
    ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax1.get_xaxis().set_tick_params(which='minor', size=0)
    ax1.get_xaxis().set_tick_params(which='minor', width=0) 
    ax1.set_title(posttown + ": Damage Estimation from C@R")
    plt.legend(loc='upper left', title='Legend')
    plt.show()

def damageEstimateMetaData(onsetOfFlooding):
    sparql_endpoint = "http://localhost:8890/sparql"
    sparql = SPARQLWrapper(sparql_endpoint)
    sparql.setReturnFormat(JSON)
    sparql_query = """
      PREFIX damage: <http://ensembleprojects.org/ns/floodrisk/damage#>
      PREFIX damage_data: <http://ensembleprojects.org/ns/floodrisk/damage_data#>
      SELECT ?attribute ?value 
      FROM <http://ensembleprojects.org/graph/floodrisk/damageEstimates>
      WHERE {{
        damage:{} ?attribute ?value
      }}
    """.format(onsetOfFlooding)
    sparql.setQuery(sparql_query)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print (result["attribute"]["value"].split('#')[1],':', result["value"]["value"])

