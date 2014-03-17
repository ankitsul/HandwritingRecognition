import itertools
import numpy as np
from scipy import stats
import networkx as nx
import pickle

from util import get_possible_values_list, load_features, get_frequency, get_observed_frequency, get_expected_frequency, get_log_likelihood, load_variables_combinations
from networkx.algorithms.dag import is_directed_acyclic_graph

# Method to get the dict_values of all the possible combinations (pairs) of variables
# dict_values in turn contains the frequency of combination of each possible value taken by (pair of) variables 
def get_all_combinations_of_variables(category):
    # List for all the variables involved
#     random_variables = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    random_variables = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # Dictionary to store the variable values
    dict_variables = {}
    dict_values = {}
    
    features = load_features(category)
    
#     #Writing to disk
#     if category == "cursive":    
#         pickle.dump(features, open("../total_features_cursive.p", "wb"))
#     elif category == "printed":
#         pickle.dump(features, open("../total_features_printed.p", "wb"))    
#     
#     print len(features)
    # Generating all combinations of length 2 
    for random_var in range(0, len(random_variables) + 1):
        for variable_pair in itertools.combinations(random_variables, random_var):
            if len(variable_pair) == 2:
                dict_values = get_dict_values(features, variable_pair, category)
                dict_variables[variable_pair] = dict_values
                # print(variable_pair)
    
    return dict_variables

# Method to populate the value dict with all possible values (taken by variables in variable_pair) along with their frequencies
def get_dict_values(features, variable_pair, category):
    # variable_pair contains the variable numbers. Fetching the possible values each variable can take from SETTINGS
    # For first element in the tuple
    dict_values = {}
    
    values_for_var_1 = get_possible_values_list(variable_pair[0], category)
    values_for_var_2 = get_possible_values_list(variable_pair[1], category)
    
    for var_1_value in values_for_var_1:
        for var_2_value in values_for_var_2:
            # variable_pair contains the variable number and var_1_value/var_2_value denotes the specific values of variable_pair variables respectively
            dict_values[tuple(str(var_1_value) + str(var_2_value))] = get_frequency(features, variable_pair, var_1_value, var_2_value)

    return dict_values


def calculate_chi_square(dict_variables):
    chi_square_values = {}
    variables_observed_frequency = {}
    variables_expected_frequency = {}
    
    # Calculating set of expected and observed frequencies for all keys(all pair of variables)
    for key, value in dict_variables.iteritems():
        variables_observed_frequency[key] = get_observed_frequency(value)
        variables_expected_frequency[key] = get_expected_frequency(value)
        
    # Removing zeros expected values
    for key, value in variables_expected_frequency.iteritems():
        list_var_expected = []
        list_var_observed = []
        for element in value:
            if element != 0:
                # Getting the index of non-zero element
                index = value.index(element)
                # appending to the new expected value list
                list_var_expected.append(element)
                # Retrieving the value at same position in the observed value list and appending it to the final list
                temp_observed_list = variables_observed_frequency[key]
                list_var_observed.append(temp_observed_list[index])
                
        variables_expected_frequency[key] = list_var_expected
        variables_observed_frequency[key] = list_var_observed
        # Calculating Chi square value
        chi_square_values[key] = stats.chisquare(np.asarray(variables_observed_frequency[key]), np.asarray(variables_expected_frequency[key]))
    
    return chi_square_values
    
    
# method to construct Bayesian Network - type_network is either "cursive" or "printed"    
def construct_bayesian_network(chi_square_values, category):
    # sorting the chi square values in descending order
    chi_square_values = sorted(chi_square_values.items(), key=lambda e:e[1][0], reverse=True)
    print chi_square_values
    
    #Loading variable_combinations
    variables_combinations = load_variables_combinations(category)
    # creating a graph
    G = nx.DiGraph()
    
#     G.add_edges_from([variable_pair])
    while chi_square_values:
        G1 = nx.DiGraph()
        G2 = nx.DiGraph()
        
        # Extracting first element from sorted list (variable_pair and chi-Square_value)
        variable_pair = chi_square_values[0][0]
        var1, var2 = variable_pair
        
        G1.add_edges_from(G.edges())
        #checking for at most 2 parents and also if the node is already present or not
#         if G1.in_degree([var2]) < 2 or G1.has_node(var2) == False:
        G1.add_edge(var1, var2)
        
        G2.add_edges_from(G.edges())
#         if G2.in_degree([var1]) < 2 or G2.has_node(var1) == False:
        G2.add_edge(var2, var1)
        
        s_G, s_G1 = get_log_likelihood(G, G1, category, variables_combinations)
        if s_G1 < s_G and is_directed_acyclic_graph(G1): 
            G = G1
            print "G1"
            print G.edges()
            
        s_G, s_G2 = get_log_likelihood(G, G2, category, variables_combinations)
        if s_G2 < s_G and is_directed_acyclic_graph(G2):
            G = G2
            print "G2"
            print G.edges()
        
        # Deleting the extracted edge
        del chi_square_values[0]
            
#     print len(G.edges())
    return G
    
    
if __name__ == "__main__":
    # For cursive
    dict_variables_cursive = get_all_combinations_of_variables("cursive")
    
    # For printed
    dict_variables_printed = get_all_combinations_of_variables("printed")
    
#     print dict_variables_cursive
    pickle.dump(dict_variables_cursive, open("../variables_combination_cursive.p", "wb"))
    pickle.dump(dict_variables_printed, open("../variables_combination_printed.p", "wb"))
    
    # calculating chi square value
    chi_square_cursive = calculate_chi_square(dict_variables_cursive)
    chi_square_printed = calculate_chi_square(dict_variables_printed)


    G_cursive = construct_bayesian_network(chi_square_cursive, "cursive")
    print G_cursive.edges()
    print G_cursive.out_degree([1,2,3,4,5,6,7,8,9,10,11,12,13])
    print len(G_cursive.edges())

#     G_printed = construct_bayesian_network(chi_square_printed, "printed")
#     print G_printed.edges()
#     print G_printed.out_degree([1,2,3,4,5,6,7,8,9,10,11,12,13])
#     print len(G_printed.edges())
    