from os import listdir
from os.path import isfile, join
import re
import xlrd

def read_file(folderpath):
    features = []
    # folder_path_cursive_3rd = SETTINGS.file_path_cursive_3rd
    files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
    # Reading each fileVar one by one
    for fileVar in files:                                  
        f = open(join(folderpath, fileVar), 'r')
    
        # Reading each line
        for line in f:          
            features.append(line)
        f.close()    
        
    return features    

def read_csv_file(filepath):
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_name("Sheet1")

    #From grade 1st to 2nd
    #To store features of student going from 1st to 2nd grade - 1st grade
    total_feat_printing_1st_to_2nd_1st = []
    
    #To store features of student going from 1st to 2nd grade - 2nd grade
    total_feat_printing_1st_to_2nd_2nd = []
    
    #From grade 2nd to 3rd
    total_feat_printing_2nd_to_3rd_2nd = []
    
    total_feat_cursive_2nd_to_3rd_3rd = []
    total_feat_printing_2nd_to_3rd_3rd = []
    
    #From grade 3rd to 4th
    total_feat_cursive_3rd_to_4th_3rd = []
    total_feat_printing_3rd_to_4th_3rd = []
    
    total_feat_cursive_3rd_to_4th_4th = []
    total_feat_printing_3rd_to_4th_4th = []
    
    #From grade 4th to 5th 
    total_feat_cursive_4th_to_5th_4th = []
    total_feat_printing_4th_to_5th_4th = []
    
    total_feat_cursive_4th_to_5th_5th = []
    total_feat_printing_4th_to_5th_5th = []
        
        
    for row_index in range(sheet.nrows):
        #First set, which is from first grade to second grade
        if row_index < 151:
            year_eleven_twelve = sheet.cell(row_index, 1)
            year_twelve_thirteen = sheet.cell(row_index, 4)
            
            #For 1st column i.e grade 1
            if 'text' in str(year_eleven_twelve):
                total_feat_printing_1st_to_2nd_1st.append(str(year_eleven_twelve))
                
            #For 4th column i.e grade 2
            if 'text' in str(year_twelve_thirteen):
                total_feat_printing_1st_to_2nd_2nd.append(str(year_twelve_thirteen))
        
        #Second set, which is from second grade to third grade
        elif row_index > 151 and row_index < 1189:
            year_eleven_twelve = sheet.cell(row_index, 1)
            year_twelve_thirteen = sheet.cell(row_index, 4)
            
            #For 1st column i.e grade 2
            if 'text' in str(year_eleven_twelve):
                total_feat_printing_2nd_to_3rd_2nd.append(str(year_eleven_twelve))
                
            #For 4th column i.e grade 3    
            if 'text' in str(year_twelve_thirteen) and 'cursi' in str(year_twelve_thirteen):
                total_feat_cursive_2nd_to_3rd_3rd.append(str(year_twelve_thirteen))
            elif 'text' in str(year_twelve_thirteen) and 'print' in str(year_twelve_thirteen):
                total_feat_printing_2nd_to_3rd_3rd.append(str(year_twelve_thirteen))
                    
        #Third set, which is from third grade to fourth grade            
        elif row_index > 1198 and row_index < 1720:
            year_eleven_twelve = sheet.cell(row_index, 1)
            year_twelve_thirteen = sheet.cell(row_index, 4)
            
            #For 1st column i.e grade 3
            if 'text' in str(year_eleven_twelve) and 'cursi' in str(year_eleven_twelve):
                total_feat_cursive_3rd_to_4th_3rd.append(str(year_eleven_twelve))
            elif 'text' in str(year_eleven_twelve) and 'print' in str(year_eleven_twelve):
                total_feat_printing_3rd_to_4th_3rd.append(str(year_eleven_twelve))
                    
            #For 4th column i.e grade 4    
            if 'text' in str(year_twelve_thirteen) and 'cursi' in str(year_twelve_thirteen):
                total_feat_cursive_3rd_to_4th_4th.append(str(year_twelve_thirteen))
            elif 'text' in str(year_twelve_thirteen) and 'print' in str(year_twelve_thirteen):
                total_feat_printing_3rd_to_4th_4th.append(str(year_twelve_thirteen))
                
        #Third set, which is from fourth grade to fifth grade
        elif row_index > 1734 and row_index < 2163:
            year_eleven_twelve = sheet.cell(row_index, 1)
            year_twelve_thirteen = sheet.cell(row_index, 4)
            
            #For 1st column i.e grade 3
            if 'text' in str(year_eleven_twelve) and 'cursi' in str(year_eleven_twelve):
                total_feat_cursive_4th_to_5th_4th.append(str(year_eleven_twelve))
            elif 'text' in str(year_eleven_twelve) and 'print' in str(year_eleven_twelve):
                total_feat_printing_4th_to_5th_4th.append(str(year_eleven_twelve))
                    
            #For 4th column i.e grade 4    
            if 'text' in str(year_twelve_thirteen) and 'cursi' in str(year_twelve_thirteen):
                total_feat_cursive_4th_to_5th_5th.append(str(year_twelve_thirteen))
            elif 'text' in str(year_twelve_thirteen) and 'print' in str(year_twelve_thirteen):
                total_feat_printing_4th_to_5th_5th.append(str(year_twelve_thirteen))        
            
    return total_feat_printing_1st_to_2nd_1st, total_feat_printing_1st_to_2nd_2nd, total_feat_printing_2nd_to_3rd_2nd, total_feat_cursive_2nd_to_3rd_3rd, total_feat_printing_2nd_to_3rd_3rd, total_feat_cursive_3rd_to_4th_3rd, total_feat_printing_3rd_to_4th_3rd, total_feat_cursive_3rd_to_4th_4th, total_feat_printing_3rd_to_4th_4th, total_feat_cursive_4th_to_5th_4th, total_feat_printing_4th_to_5th_4th, total_feat_cursive_4th_to_5th_5th, total_feat_printing_4th_to_5th_5th


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
    count = 0 
    number_of_inconsistent_rows=0
    for feature in features:
        
        #Counting the number of inconsistent rows for statistics 
        if(count>0):
            number_of_inconsistent_rows = number_of_inconsistent_rows+1
        count=0
        
        for index in range(len(feature)):
            # Replacing -1 and 99 with None
            if feature[index] == -1 or feature[index] == 99:
                feature[index] = None
                count=count+1
    
    #print "Number of inconsistent rows:" + str(number_of_inconsistent_rows)
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
