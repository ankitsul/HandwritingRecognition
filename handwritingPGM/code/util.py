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
        f_int = [ int(x) for x in f ]
        
        # Removing first two columns as they are not features
        f_return = f_int[2:]
        
        
        return f_return
    
    
def remove_inconsistencies(features):
    for feature in features:
        for index in range(len(feature)):
            # Replacing -1 and 99 with None 
            if feature[index] == -1 or feature[index] == 99:
                feature[index] = None
    
    # Getting approximate value for each 'None'
    for feature in features:
        for index in range(len(feature)):
            if feature[index] == None:
                feature[index] = get_approximate_value(features, index)
                
    return features            
                
def get_approximate_value(features, index):
    # dictionary to store the count of each tuple - tuple is formed of size 11, except the missing value - (approx_list,[count_of_occurance of this probable_value,probable_value])
    approx_dict = {}
    for f in features:
        # list formed every time to form a key for the dictionary approx_dict
        approx_list = []
        probable_value = 0
        for i in range(len(f)):
            if i != index:
                approx_list.append(f[i])
            else:
                #adding 100 (can be anything) to create placeholder for the missing value
                approx_list.append(i+100)
                probable_value = f[i]
             
        # save into approximate dictionary
        # If dictionary already contains this tuple, then increment the count of probable value
        if probable_value != None:
            approx_list_with_probable_value = [tuple(approx_list), probable_value] 
            if(approx_dict.has_key(tuple(approx_list_with_probable_value))):
                count = approx_dict[tuple(approx_list_with_probable_value)]
                count = count + 1
                approx_dict[tuple(approx_list_with_probable_value)] = count
            else:
                count = 1                    
                approx_dict[tuple(approx_list_with_probable_value)] = count              
#     print "Approx Dict", approx_dict    
    
    # Iterating over dictionary to return the probable_value which occur most number of times
    max_value = 0
    approx_value = 0;
    for key, value in approx_dict.iteritems():
        if value > max_value:
            approx_value = key[1]
            
    return approx_value        
    
    
def get_similarity_score(feature, mean_feature):
    max_element = max(feature)
    score = 0.0
    for i in range(12):
        score += abs(feature[i] - mean_feature[i])
    score = float(score) / max_element
    score = float(score) / 12
    return score    
    

# Creating a feature map using the features
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
