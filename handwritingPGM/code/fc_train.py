import re
from math import log

import SETTINGS
from util import read_file, parse_data, get_similarity_score, get_feature_map


def get_features(folderpath):
    features = []
    fileData = read_file(folderpath)
    # For each line
    for dataVar in fileData:
        parsed_data = parse_data(dataVar)
        # If list is not empty
        if parsed_data != None:
            features.append(parsed_data)
    return features


def calculate_mean(features):
    sumList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for features in features:
        # features = [ int(x) for x in features ]
        for i in range(len(features)):
            sumList[i] = sumList[i] + features[i]
        
    meanList = [x / len(features) for x in sumList]
        
    return meanList    


def get_similar_samples(features, mean_feature):
    scores = []
    
    for feature in features:
        score = get_similarity_score(feature, mean_feature)
        scores.append(score)
    
    # Return top n scores - use heapq 
    
    return scores


def get_entropy(features):
    s = 0
    no_samples = len(features)
    
    feature_map = get_feature_map(features)
    for feature in features:
        s += log(float(feature_map[tuple(feature)]) / no_samples)

    s = s / no_samples
    s = -s
    return s    
    


if __name__ == "__main__":
    total_feat_cursive_3rd = get_features(SETTINGS.file_path_cursive_3rd)
    total_feat_cursive_4th = get_features(SETTINGS.file_path_cursive_4th)
        
    total_feat_printed_1st = get_features(SETTINGS.file_path_printed_1st)
    total_feat_printed_2nd = get_features(SETTINGS.file_path_printed_2nd)
    total_feat_printed_3rd = get_features(SETTINGS.file_path_printed_3rd)
    total_feat_printed_4th = get_features(SETTINGS.file_path_printed_4th)
    
    print "Features", len(total_feat_cursive_3rd), len(total_feat_cursive_4th), len(total_feat_printed_1st), len(total_feat_printed_2nd), len(total_feat_printed_3rd), len(total_feat_printed_4th)
      
    # Calculating mean    
    mean_cursive_3rd = calculate_mean(total_feat_cursive_3rd)
    mean_cursive_4th = calculate_mean(total_feat_cursive_4th)
      
    mean_printed_1st = calculate_mean(total_feat_printed_1st)
    mean_printed_2nd = calculate_mean(total_feat_printed_2nd)
    mean_printed_3rd = calculate_mean(total_feat_printed_3rd)
    mean_printed_4th = calculate_mean(total_feat_printed_4th)
    
    
    # Finding samples which are closest to the mean
    similar_scores_mean_cursive_3rd = get_similar_samples(total_feat_cursive_3rd, mean_cursive_3rd)
    similar_scores_mean_cursive_4th = get_similar_samples(total_feat_cursive_4th, mean_cursive_4th)
    
    similar_scores_mean_printed_1st = get_similar_samples(total_feat_printed_1st, mean_printed_1st)
    similar_scores_mean_printed_2nd = get_similar_samples(total_feat_printed_2nd, mean_printed_2nd)
    similar_scores_mean_printed_3rd = get_similar_samples(total_feat_printed_3rd, mean_printed_3rd)
    similar_scores_mean_printed_4th = get_similar_samples(total_feat_printed_4th, mean_printed_4th)
    
    print "Similarity scores", len(similar_scores_mean_cursive_3rd), len(similar_scores_mean_cursive_4th), len(similar_scores_mean_printed_1st), len(similar_scores_mean_printed_2nd), len(similar_scores_mean_printed_3rd), len(similar_scores_mean_printed_4th)
    
    
    entropy_cursive_3rd = get_entropy(total_feat_cursive_3rd)
    entropy_cursive_4th = get_entropy(total_feat_cursive_4th)
    
    entropy_printed_1st = get_entropy(total_feat_printed_1st)
    entropy_printed_2nd = get_entropy(total_feat_printed_2nd)
    entropy_printed_3rd = get_entropy(total_feat_printed_3rd)
    entropy_printed_4th = get_entropy(total_feat_printed_4th)
    
    print "Entropy", entropy_cursive_3rd, entropy_cursive_4th, entropy_printed_1st, entropy_printed_2nd, entropy_printed_3rd, entropy_printed_4th
    
    
