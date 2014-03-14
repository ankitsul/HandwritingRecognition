import pickle

import SETTINGS

# Method to retrieve the list corresponding to values the variables take
def get_possible_values_list(variable_number, category):
    if category == "cursive":
        if variable_number == 1:
            return SETTINGS.cursive_var_1
        elif variable_number == 2: 
            return SETTINGS.cursive_var_2
        elif variable_number == 3: 
            return SETTINGS.cursive_var_3
        elif variable_number == 4: 
            return SETTINGS.cursive_var_4
        elif variable_number == 5: 
            return SETTINGS.cursive_var_5
        elif variable_number == 6: 
            return SETTINGS.cursive_var_6
        elif variable_number == 7: 
            return SETTINGS.cursive_var_7
        elif variable_number == 8: 
            return SETTINGS.cursive_var_8
        elif variable_number == 9: 
            return SETTINGS.cursive_var_9
        elif variable_number == 10: 
            return SETTINGS.cursive_var_10
        elif variable_number == 11: 
            return SETTINGS.cursive_var_11
        elif variable_number == 12: 
            return SETTINGS.cursive_var_12
        elif variable_number == 13: 
            return SETTINGS.cursive_var_13
    elif category == "printed":
        if variable_number == 1:
            return SETTINGS.printed_var_1
        elif variable_number == 2: 
            return SETTINGS.printed_var_2
        elif variable_number == 3: 
            return SETTINGS.printed_var_3
        elif variable_number == 4: 
            return SETTINGS.printed_var_4
        elif variable_number == 5: 
            return SETTINGS.printed_var_5
        elif variable_number == 6: 
            return SETTINGS.printed_var_6
        elif variable_number == 7: 
            return SETTINGS.printed_var_7
        elif variable_number == 8: 
            return SETTINGS.printed_var_8
        elif variable_number == 9: 
            return SETTINGS.printed_var_9
        elif variable_number == 10: 
            return SETTINGS.printed_var_10
        elif variable_number == 11: 
            return SETTINGS.printed_var_11
        elif variable_number == 12: 
            return SETTINGS.printed_var_12
        elif variable_number == 13: 
            return SETTINGS.printed_var_13    

        
# Method to load features from object files        
def load_features(category):
    if category == "cursive":
        # load the cursive features for all the grades and appending the respective grade to the end
        cursive_features_3rd = pickle.load(open(SETTINGS.cursive_object_file_3, "rb"))
        cursive_features_3rd = [x + [3] for x in cursive_features_3rd]
        
        cursive_features_4th = pickle.load(open(SETTINGS.cursive_object_file_4, "rb"))
        cursive_features_4th = [x + [4] for x in cursive_features_4th]

        return cursive_features_3rd + cursive_features_4th
    
    elif category == "printed":
        printed_features_1st = pickle.load(open(SETTINGS.printed_object_file_1, "rb"))
        printed_features_1st = [x + [1] for x in printed_features_1st]
        
        printed_features_2nd = pickle.load(open(SETTINGS.printed_object_file_2, "rb"))
        printed_features_2nd = [x + [2] for x in printed_features_2nd]

        printed_features_3rd = pickle.load(open(SETTINGS.printed_object_file_3, "rb"))
        printed_features_3rd = [x + [3] for x in printed_features_3rd]

        printed_features_4th = pickle.load(open(SETTINGS.printed_object_file_4, "rb"))
        printed_features_4th = [x + [4] for x in printed_features_4th]

        return printed_features_1st + printed_features_2nd + printed_features_3rd + printed_features_4th

        
        
# Method to get frequency of each combination of values        
def get_frequency(features, variable_pair, var_1_value, var_2_value):
    count = 0
    for feature in features:
        # Checking if the index of feature for variable_pair[0]==var_1_value ... etc
        if ((feature[variable_pair[0] - 1] == var_1_value) and (feature[variable_pair[1] - 1] == var_2_value)):
            count = count + 1
            
    return count        


def get_observed_frequency(dict_value):
    observed_values = []
    # iterating over each entry in the value map
    for key, value in dict_value.iteritems():
        observed_values.append(value)

    return observed_values


def get_expected_frequency(dict_value):
    expected_values = []
    for key, value in dict_value.iteritems():
        #Calculating expected value for each entry
        expected_values.append(get_cell_value(key, value, dict_value))

    return expected_values


def get_cell_value(key, value, dict_value):
    total_sum = 0
    row_sum = 0
    column_sum = 0
    
    variable_1 = key[0]
    variable_2 = key[1]
    
    for key_element, value_element in dict_value.iteritems():
        total_sum = total_sum + value_element
        if (key_element[0]==variable_1):
            row_sum = row_sum + value_element
        if (key_element[1]==variable_2):
            column_sum = column_sum + value_element    
    
    return (row_sum * column_sum)/total_sum
    