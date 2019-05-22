def getPostcodeDamageOriginal(postcode):
  sparql_query = """
  prefix p:       <http://ensembleprojects.org/ns/floodrisk/property#>
  prefix pd:      <http://ensembleprojects.org/ns/floodrisk/property_data#>

  select ?q2 ?q5 ?q10 ?q20 ?q50 ?q75 ?q100 ?q200 ?q1000
  from <http://ensembleprojects.org/floodrisk/property>
  where {{
        ?property pd:postcode "{}" ;
             pd:q2_existingDamageMean ?q2 ;
             pd:q5_existingDamagelMean ?q5 ;
             pd:q10_existingDamageMean ?q10 ;
             pd:q20_existingDamageMean ?q20 ;
             pd:q50_existingDamageMean ?q50 ;
             pd:q75_existingDamageMean ?q75 ;
             pd:q100_existingDamageMean ?q100 ;
             pd:q200_existingDamageMean ?q200 ;
             pd:q1000_existingDamagelMean ?q1000 .
  }}
  """.format(postcode)
  return sparql_query

def getPostcodeDamageUpdatedMean(postcode):
  sparql_query = """
    prefix pd:                  <http://ensembleprojects.org/ns/floodrisk/property_data#>
    prefix propertyDamage_data: <http://ensembleprojects.org/ns/floodrisk/propertyDamage_data#>

    select ?ead_mean ?ead_mean_50 ?ead_mean_100 ?ead_mean_200 ?ead_mean_500
    from <http://ensembleprojects.org/floodrisk/property>
    from <http://ensembleprojects.org/graph/floodrisk/damage#0>
    where {{
      ?property pd:postcode "{}" .
      ?property pd:jbapropRef ?ref .
      ?newProperty propertyDamage_data:propRef ?ref .
      ?newProperty propertyDamage_data:ead_mean ?ead_mean .
      ?newProperty propertyDamage_data:ead_mean_50 ?ead_mean_50 .
      ?newProperty propertyDamage_data:ead_mean_100 ?ead_mean_100 .
      ?newProperty propertyDamage_data:ead_mean_200 ?ead_mean_200 .
      ?newProperty propertyDamage_data:ead_mean_500 ?ead_mean_500 .
    }}
  """.format(postcode)
  return sparql_query

def getPosttownDamageOriginal(posttown):
  sparql_query = """
  prefix p:       <http://ensembleprojects.org/ns/floodrisk/property#>
  prefix pd:      <http://ensembleprojects.org/ns/floodrisk/property_data#>

  select ?q2 ?q5 ?q10 ?q20 ?q50 ?q75 ?q100 ?q200 ?q1000
  from <http://ensembleprojects.org/floodrisk/property>
  where {{
        ?property   pd:posttown "{}" ;
             pd:q2_existingDamageMean ?q2 ;
             pd:q5_existingDamagelMean ?q5 ;
             pd:q10_existingDamageMean ?q10 ;
             pd:q20_existingDamageMean ?q20 ;
             pd:q50_existingDamageMean ?q50 ;
             pd:q75_existingDamageMean ?q75 ;
             pd:q100_existingDamageMean ?q100 ;
             pd:q200_existingDamageMean ?q200 ;
             pd:q1000_existingDamagelMean ?q1000 .
  }}
  """.format(posttown)
  return sparql_query

def getPosttownDamageUpdatedMean(damageEstimate, posttown):
  sparql_query = """
    prefix pd:                  <http://ensembleprojects.org/ns/floodrisk/property_data#>
    prefix propertyDamage_data: <http://ensembleprojects.org/ns/floodrisk/property_data#>

    select ?ead_mean ?ead_mean_50 ?ead_mean_100 ?ead_mean_200 ?ead_mean_500
    from <http://ensembleprojects.org/floodrisk/property>
    from <http://ensembleprojects.org/graph/floodrisk/damage#{}>
    where {{
      ?property pd:posttown "{}" .
      ?property pd:jbapropRef ?ref .
      ?newProperty propertyDamage_data:propRef ?ref .
      ?newProperty propertyDamage_data:ead_mean ?ead_mean .
      ?newProperty propertyDamage_data:ead_mean_50 ?ead_mean_50 .
      ?newProperty propertyDamage_data:ead_mean_100 ?ead_mean_100 .
      ?newProperty propertyDamage_data:ead_mean_200 ?ead_mean_200 .
      ?newProperty propertyDamage_data:ead_mean_500 ?ead_mean_500 .
    }}
  """.format(damageEstimate, posttown)
  return sparql_query

def getGaugingStationDamageUpdatedMean(damageEstimate, posttown, gaugestation):
  sparql_query = """
    prefix pd:                  <http://ensembleprojects.org/ns/floodrisk/property_data#>
    prefix propertyDamage_data: <http://ensembleprojects.org/ns/floodrisk/property_data#>

    select ?ead_mean ?ead_mean_50 ?ead_mean_100 ?ead_mean_200 ?ead_mean_500
    from <http://ensembleprojects.org/floodrisk/property>
    from <http://ensembleprojects.org/graph/floodrisk/damage#{}>
    where {{
      ?property pd:posttown "{}" .
      ?property pd:station_name "{}" .
      ?property pd:jbapropRef ?ref .
      ?newProperty propertyDamage_data:propRef ?ref .
      ?newProperty propertyDamage_data:ead_mean ?ead_mean .
      ?newProperty propertyDamage_data:ead_mean_50 ?ead_mean_50 .
      ?newProperty propertyDamage_data:ead_mean_100 ?ead_mean_100 .
      ?newProperty propertyDamage_data:ead_mean_200 ?ead_mean_200 .
      ?newProperty propertyDamage_data:ead_mean_500 ?ead_mean_500 .
    }}
  """.format(damageEstimate, posttown, gaugestation)
  return sparql_query


