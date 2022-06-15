from apyori import apriori
import numpy as np

from api.models import Purchases

from .helpers import frozenset2list, is_subvector

def generate_reliations():
    record = {}
    reliations = Purchases.objects.all().values()
    for relation in reliations:
        record[relation["userid"]] = []
    for relation in reliations:
        record[relation["userid"]].append(relation["productid"])
    return list(record.values())

def generate_associations():
    reliations = generate_reliations()
    association_rules = apriori(reliations, min_support=0.01, min_confidence=0.01, min_lift=1, min_length=2)
    association_results = list(association_rules)

    associations_collection = []
    for association in association_results:
        for i in range(len(frozenset2list(association[2]))):
            #print(str(frozenset2list(association[2][i][0])) + " -> " + str((frozenset2list(association[2][i][1]))) + ", sup: " + str(association[1]) + ", conf: " + str(((association[2][i][2]))) + ", lift: " + str(((association[2][i][3]))))
            associations_collection.append({
                "base": frozenset2list(association[2][i][0]),
                "added": frozenset2list(association[2][i][1]),
                "support": association[1],
                "confidence": association[2][i][2],
                "lift": association[2][i][3]
            })
    return associations_collection

def make_recommend(userid):
    PAs = Purchases.objects.filter(userid = userid).values()
    appIds = []
    for pa in PAs:
        appIds.append(pa["productid"])
    associations = generate_associations()
    recommendation = []
    for association in associations:
        asso = list(association.values())
        base = list(map(int, asso[0]))
        added = list(map(int, asso[1]))
        #print(appIds, base, added, is_subvector(appIds, base))
        if(is_subvector(appIds, base)):
            if(len(added)==1):
                #print(added[0], appIds)
                if(added[0] not in appIds):
                    if(int(asso[1][0]) not in recommendation):
                        recommendation.append(int(asso[1][0]))
                    # recommendation.append({
                    #     "suggestionAppId": int(asso[1][0]),
                    #     "sup": asso[2],
                    #     "conf": asso[3],
                    #     "lift": asso[4]
                    # })
    return recommendation

