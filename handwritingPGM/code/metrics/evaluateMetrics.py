from math import log
import pickle
import numpy as np
import operator

import SETTINGS
from util import read_file, parse_data, get_similarity_score, get_feature_map, remove_inconsistencies


def get_features(folderpath):
    features = []
    fileData = read_file(folderpath)
    # For each line
    for dataVar in fileData:
        parsed_data = parse_data(dataVar)
        # If list is not empty
        if parsed_data != None:
            features.append(parsed_data)
    
    # Imputing missing data        
    final_features = remove_inconsistencies(features)  
          
    return final_features


def calculate_mean(features):
    sumList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for feature in features:
        for i in range(len(feature)):
            sumList[i] = sumList[i] + feature[i]
        
    meanList = [float(x) / len(features) for x in sumList]
        
    return meanList    


def get_similar_samples(features, mean_feature):
    scores = []
    
    for feature in features:
        score = get_similarity_score(feature, mean_feature)
        scores.append(score)
    
    # Return top n scores - use heapq 
    
    return scores

def get_similar_samples_list(similar_samples_scores, feature_filepath):
    indices_sorted_array = (-np.array(similar_samples_scores)).argsort()[:10]
    features = pickle.load(open(feature_filepath, "rb"))    
    similar_features_to_mean = [] 
    print "Sorted"
    print indices_sorted_array
    for index in indices_sorted_array:
        similar_features_to_mean.append(features[index])
    
    return similar_features_to_mean


def get_entropy(features):
    s = 0
    no_samples = len(features)
    
    # creating feature map to calculate the probability of each feature set
    feature_map = get_feature_map(features)
    
    for feature in features:
        p_x = float(feature_map[tuple(feature)])
        s += log(p_x / no_samples)

    s = s / no_samples
    s = -s
    return s    
    

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


def most_unusual_sample(feature_filepath):
    features = pickle.load(open(feature_filepath, "rb"))
    feature_map = get_feature_map(features)
    sorted_feature_map = sorted(feature_map.iteritems(), key=operator.itemgetter(1))
    return sorted_feature_map[0][0]


if __name__ == "__main__":
    total_feat_cursive_3rd = get_features(SETTINGS.file_path_cursive_3rd)
    total_feat_cursive_4th = get_features(SETTINGS.file_path_cursive_4th)
         
    total_feat_printed_1st = get_features(SETTINGS.file_path_printed_1st)
    total_feat_printed_2nd = get_features(SETTINGS.file_path_printed_2nd)
    total_feat_printed_3rd = get_features(SETTINGS.file_path_printed_3rd)
    total_feat_printed_4th = get_features(SETTINGS.file_path_printed_4th)
    
    #writing features to files
    pickle.dump(total_feat_cursive_3rd, open("../cursive_3rd.p", "wb"))
    pickle.dump(total_feat_cursive_4th, open("../cursive_4th.p", "wb"))
    
    pickle.dump(total_feat_printed_1st, open("../printed_1st.p", "wb"))
    pickle.dump(total_feat_printed_2nd, open("../printed_2nd.p", "wb"))
    pickle.dump(total_feat_printed_3rd, open("../printed_3rd.p", "wb"))
    pickle.dump(total_feat_printed_4th, open("../printed_4th.p", "wb"))
     
     
    print "Features", len(total_feat_cursive_3rd), len(total_feat_cursive_4th), len(total_feat_printed_1st), len(total_feat_printed_2nd), len(total_feat_printed_3rd), len(total_feat_printed_4th)
       
    # Calculating mean    
    mean_cursive_3rd = calculate_mean(total_feat_cursive_3rd)
    mean_cursive_4th = calculate_mean(total_feat_cursive_4th)
       
    mean_printed_1st = calculate_mean(total_feat_printed_1st)
    mean_printed_2nd = calculate_mean(total_feat_printed_2nd)
    mean_printed_3rd = calculate_mean(total_feat_printed_3rd)
    mean_printed_4th = calculate_mean(total_feat_printed_4th)
     
    print "Mean", mean_cursive_3rd, mean_cursive_4th, mean_printed_1st, mean_printed_2nd, mean_printed_3rd, mean_printed_4th 
     
    # Finding samples which are closest to the mean
    similar_scores_mean_cursive_3rd = get_similar_samples(total_feat_cursive_3rd, mean_cursive_3rd)
    similar_scores_mean_cursive_4th = get_similar_samples(total_feat_cursive_4th, mean_cursive_4th)
      
    similar_scores_mean_printed_1st = get_similar_samples(total_feat_printed_1st, mean_printed_1st)
    similar_scores_mean_printed_2nd = get_similar_samples(total_feat_printed_2nd, mean_printed_2nd)
    similar_scores_mean_printed_3rd = get_similar_samples(total_feat_printed_3rd, mean_printed_3rd)
    similar_scores_mean_printed_4th = get_similar_samples(total_feat_printed_4th, mean_printed_4th)
      
    #TODO: Need to get top samples  
    print "Similarity scores", similar_scores_mean_cursive_3rd, len(similar_scores_mean_cursive_4th), len(similar_scores_mean_printed_1st), len(similar_scores_mean_printed_2nd), len(similar_scores_mean_printed_3rd), len(similar_scores_mean_printed_4th)

    similar_samples_cursive_3rd = get_similar_samples_list(similar_scores_mean_cursive_3rd, "../cursive_3rd.p")  
    similar_samples_cursive_4th = get_similar_samples_list(similar_scores_mean_cursive_4th, "../cursive_4th.p")
    
    similar_samples_printed_1st = get_similar_samples_list(similar_scores_mean_printed_1st, "../printed_1st.p")
    similar_samples_printed_2nd = get_similar_samples_list(similar_scores_mean_printed_2nd, "../printed_2nd.p")
    similar_samples_printed_3rd = get_similar_samples_list(similar_scores_mean_printed_3rd, "../printed_3rd.p")
    similar_samples_printed_4th = get_similar_samples_list(similar_scores_mean_printed_4th, "../printed_4th.p")

    print "Similar samples", similar_samples_cursive_3rd, similar_samples_cursive_4th, similar_samples_printed_1st, similar_samples_printed_2nd, similar_samples_printed_3rd, similar_samples_printed_4th
      
    
    entropy_cursive_3rd = get_entropy(total_feat_cursive_3rd)
    entropy_cursive_4th = get_entropy(total_feat_cursive_4th)
      
    entropy_printed_1st = get_entropy(total_feat_printed_1st)
    entropy_printed_2nd = get_entropy(total_feat_printed_2nd)
    entropy_printed_3rd = get_entropy(total_feat_printed_3rd)
    entropy_printed_4th = get_entropy(total_feat_printed_4th)
      
    print "Entropy", entropy_cursive_3rd, entropy_cursive_4th, entropy_printed_1st, entropy_printed_2nd, entropy_printed_3rd, entropy_printed_4th
      
     
    relative_entropy_cursive_approximate_3rd_with_4th = get_relative_entropy(total_feat_cursive_3rd, total_feat_cursive_4th)
    #relative_entropy_cursive_approximate_4th_with_3rd = get_relative_entropy(total_feat_cursive_4th, total_feat_cursive_3rd)  
    
    
    relative_entropy_printed_approximate_1st_with_2nd = get_relative_entropy(total_feat_printed_1st, total_feat_printed_2nd)
    #relative_entropy_printed_approximate_2nd_with_1st = get_relative_entropy(total_feat_printed_2nd, total_feat_printed_1st)
    relative_entropy_printed_approximate_1st_with_3rd = get_relative_entropy(total_feat_printed_1st, total_feat_printed_3rd)  
    relative_entropy_printed_approximate_1st_with_4th = get_relative_entropy(total_feat_printed_1st, total_feat_printed_4th)
    relative_entropy_printed_approximate_2nd_with_3rd = get_relative_entropy(total_feat_printed_2nd, total_feat_printed_3rd)
    relative_entropy_printed_approximate_2nd_with_4th = get_relative_entropy(total_feat_printed_2nd, total_feat_printed_4th) 
    relative_entropy_printed_approximate_3rd_with_4th = get_relative_entropy(total_feat_printed_3rd, total_feat_printed_4th)   
    
    print "Relative Entropy", relative_entropy_cursive_approximate_3rd_with_4th, relative_entropy_printed_approximate_1st_with_2nd, relative_entropy_printed_approximate_1st_with_3rd, relative_entropy_printed_approximate_1st_with_4th, relative_entropy_printed_approximate_2nd_with_3rd, relative_entropy_printed_approximate_2nd_with_4th, relative_entropy_printed_approximate_3rd_with_4th

    unusual_sample_cursive_3rd = most_unusual_sample("../cursive_3rd.p")
    unusual_sample_cursive_4th = most_unusual_sample("../cursive_4th.p")
    
    unusual_sample_printed_1st = most_unusual_sample("../printed_1st.p")
    unusual_sample_printed_2nd = most_unusual_sample("../printed_2nd.p")
    unusual_sample_printed_3rd = most_unusual_sample("../printed_3rd.p")
    unusual_sample_printed_4th = most_unusual_sample("../printed_4th.p")
    
    print "Unusual Sample", unusual_sample_cursive_3rd, unusual_sample_cursive_4th, unusual_sample_printed_1st, unusual_sample_printed_2nd, unusual_sample_printed_3rd, unusual_sample_printed_4th
