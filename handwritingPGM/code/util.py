from os import listdir
from os.path import isfile, join
import re

def read_file(folderpath):
    features_cursive_3rd = []
    # folder_path_cursive_3rd = SETTINGS.file_path_cursive_3rd
    files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
    # Reading each fileVar one by one
    for fileVar in files:                                  
        f = open(join(folderpath, fileVar), 'r')
    
        # Reading each line
        for line in f:          
            features_cursive_3rd.append(line)
        f.close()    
        
    return features_cursive_3rd    


def parse_data(data):
    # Extracting numerals
    cleanData = re.sub("CTV1", "" , data)
    
    matched = re.search("( *\\-?[0-9]+,){14}", cleanData)
    if matched != None:    
        extractedData = str(matched.group())
    else:
        extractedData = ""    
    
    
    # Cleaning commas as well
    extractedData = extractedData.strip()
    
    f = extractedData.split(", ")

    # removing comma from the last feature
    elements = []
    for element in f:
        elements.append(re.sub(",", "", element))
    
    f = []
    f = elements
    
    # removing empty elements from the list 
    f = filter(None, f)
    
    # avoiding the empty list
    if len(f) > 1:
        # Converting to integer
        f_return = [ int(x) for x in f ]
        return f_return
    
    
def get_similarity_score(feature, mean_feature):
    max_element = max(feature)
    score = 0.0
    for i in range(14):
        score += abs(feature[i] - mean_feature[i])
    score = score / max_element
    score = score / 14
    return score    
    

#Creating a feature map using the features
def get_feature_map(features):    
    feature_map = {}
    for feature in features:
        if feature_map.has_key(tuple(feature)):
            value = feature_map[tuple(feature)]
            value += 1
            feature_map[tuple(feature)] = value
        else:
            feature_map[tuple(feature)] = 1;

    return feature_map
