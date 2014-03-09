# Compare data related to students who have moved to the next grade
from math import log

import SETTINGS
from util import read_csv_file, parse_data, remove_inconsistencies, get_feature_map

def get_parsed_data(features):
    parsed_features = []
    # parsing line by line
    for feature in features:
        parsed_data = parse_data(str(feature))
        
        # If list is not empty
        if parsed_data != None:
            parsed_features.append(parsed_data)
            
    final_features = remove_inconsistencies(parsed_features)      
      
    return final_features


def get_relative_entropy(p_features, q_features):
    s = 0
    max_sample = max(len(p_features), len(q_features))
    
    p_feature_map = get_feature_map(p_features)
    q_feature_map = get_feature_map(q_features)
    
    for feature_p, feature_q in zip(p_features, q_features):
        p_x = float(p_feature_map[tuple(feature_p)]) / max_sample
        q_x = float(q_feature_map[tuple(feature_q)]) / max_sample
        
        s += (log(float(p_x/q_x)))
    
    s = s/ max_sample
    return s


if __name__ == "__main__":
    # Extract all the features from the csv file
    total_feat_printing_1st_to_2nd_1st, total_feat_printing_1st_to_2nd_2nd, total_feat_printing_2nd_to_3rd_2nd, total_feat_cursive_2nd_to_3rd_3rd, total_feat_printing_2nd_to_3rd_3rd, total_feat_cursive_3rd_to_4th_3rd, total_feat_printing_3rd_to_4th_3rd, total_feat_cursive_3rd_to_4th_4th, total_feat_printing_3rd_to_4th_4th, total_feat_cursive_4th_to_5th_4th, total_feat_printing_4th_to_5th_4th, total_feat_cursive_4th_to_5th_5th, total_feat_printing_4th_to_5th_5th = read_csv_file(SETTINGS.file_path_temporal_data)
    
    #Grade 1st to 2nd
    total_feat_printing_1st_to_2nd_1st = get_parsed_data(total_feat_printing_1st_to_2nd_1st)
    total_feat_printing_1st_to_2nd_2nd = get_parsed_data(total_feat_printing_1st_to_2nd_2nd)

    
    #Grade 2nd to 3rd
    total_feat_printing_2nd_to_3rd_2nd = get_parsed_data(total_feat_printing_2nd_to_3rd_2nd)
    
    total_feat_cursive_2nd_to_3rd_3rd = get_parsed_data(total_feat_cursive_2nd_to_3rd_3rd)
    total_feat_printing_2nd_to_3rd_3rd = get_parsed_data(total_feat_printing_2nd_to_3rd_3rd)

    
    #Grade 3rd to 4th
    total_feat_cursive_3rd_to_4th_3rd = get_parsed_data(total_feat_cursive_3rd_to_4th_3rd)
    total_feat_printing_3rd_to_4th_3rd = get_parsed_data(total_feat_printing_3rd_to_4th_3rd)
    
    total_feat_cursive_3rd_to_4th_4th = get_parsed_data(total_feat_cursive_3rd_to_4th_4th)
    total_feat_printing_3rd_to_4th_4th = get_parsed_data(total_feat_printing_3rd_to_4th_4th)
    
    
    #Grade 4th to 5th
    total_feat_cursive_4th_to_5th_4th = get_parsed_data(total_feat_cursive_4th_to_5th_4th)
    total_feat_printing_4th_to_5th_4th = get_parsed_data(total_feat_printing_4th_to_5th_4th)
    
    total_feat_cursive_4th_to_5th_5th = get_parsed_data(total_feat_cursive_4th_to_5th_5th)
    total_feat_printing_4th_to_5th_5th = get_parsed_data(total_feat_printing_4th_to_5th_5th)
    
#     print len(total_feat_printing_4th_to_5th_4th), len(total_feat_printing_4th_to_5th_5th)
    
    #KL divergence between distributions related to students from grade 1 to grade 2 - printing
    relative_entropy_printing_approximate_1st_to_2nd = get_relative_entropy(total_feat_printing_1st_to_2nd_1st, total_feat_printing_1st_to_2nd_2nd)
    print "Grade 1 to Grade 2 - printing", relative_entropy_printing_approximate_1st_to_2nd
    
    #KL divergence between distributions related to students from grade 2 to grade 3 - printing
    relative_entropy_printing_approximate_2nd_to_3rd = get_relative_entropy(total_feat_printing_2nd_to_3rd_2nd, total_feat_printing_2nd_to_3rd_3rd)
    print "Grade 2 to Grade 3 - printing", relative_entropy_printing_approximate_2nd_to_3rd

    #KL divergence between distributions related to students from grade 3 to grade 4 - cursive and printing
    relative_entropy_cursive_approximate_3rd_to_4th = get_relative_entropy(total_feat_cursive_3rd_to_4th_3rd, total_feat_cursive_3rd_to_4th_4th)
    relative_entropy_printing_approximate_3rd_to_4th = get_relative_entropy(total_feat_printing_3rd_to_4th_3rd, total_feat_printing_3rd_to_4th_4th)
    print "Grade 3 to Grade 4 - cursive", relative_entropy_cursive_approximate_3rd_to_4th
    print "Grade 3 to Grade 4 - printing", relative_entropy_printing_approximate_3rd_to_4th
    
    #KL divergence between distributions related to students from grade 4 to grade 5 - cursive and printing
    relative_entropy_cursive_approximate_4th_to_5th = get_relative_entropy(total_feat_cursive_4th_to_5th_4th, total_feat_cursive_4th_to_5th_5th)
    relative_entropy_printing_approximate_4th_to_5th = get_relative_entropy(total_feat_printing_4th_to_5th_4th, total_feat_printing_4th_to_5th_5th)
    print "Grade 4 to Grade 5 - cursive", relative_entropy_cursive_approximate_4th_to_5th
    print "Grade 4 to Grade 5 - printing", relative_entropy_printing_approximate_4th_to_5th


    