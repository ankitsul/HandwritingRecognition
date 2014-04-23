from PIL import Image
import ImageOps
import os
import numpy
from numpy.testing.utils import assert_equal
from numpy.core.numeric import dtype
import gzip
import pickle
import theano

def is_grayscale(features):
    for feature in features:
        if (isinstance(feature, int)):
            pass
        else:
            return False
    return True

def read_files(folders):
    size = 28, 28
    features_list = []
    for folderpath in folders:
        for root, dirs, files in os.walk(folderpath):
            path = root.split('/')
            for file in files:
                if "and " in file:
#                     print "@@@", os.path.join(root, file)
                    im = Image.open(os.path.join(root, file))
                    imagefit = ImageOps.fit(im, size, Image.ANTIALIAS)
                    features = list(imagefit.getdata())
                    assert_equal(len(features), 784)  
#                     print features
                    if(is_grayscale(features)):
                        features_list.append(features)
        
#     print features_list    
    print "!!!!!!", len(features_list)    
    return features_list

def cursive():
    folders_cursive_3rd = ["/home/ankitsul/Courses/AML/project/datasets/Images/3rd Grade/Mrs. Dantas - 3/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/3rd Grade/Mrs. Quirk - 3/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/3rd Grade/Mrs Swalve - 3/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/3rd Grade/Ms. Eboldt - 3/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade/3 grade cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade (2)/Class 1/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade (2)/Class 2/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade (2)/Class 3/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade (2)/Class 4/Cursive/"]
    folders_cursive_4th = ["/home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/4th Grade/Mrs. Filler - 4 i think/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/4th Grade/Mrs. Koehnen - 4/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/4th Grade/Mrs. March - 4/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/4th Grade/Mrs Jankowski - 4/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Red_Rock_2nd_4th_Grade/Fourth Grade/4th grade cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Royal_Oaks_2nd_4th_Grade/4th Grade/Mr. Anderson - 4/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Royal_Oaks_2nd_4th_Grade/4th Grade/Mr Gonzalez 4th/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Royal_Oaks_2nd_4th_Grade/4th Grade/Mrs. Birkel 4th/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Woodbury_2nd_4th_Grade/Fourth Grade/Class 1/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Woodbury_2nd_4th_Grade/Fourth Grade/Class 2/Cursive/", "/home/ankitsul/Courses/AML/project/datasets/Images/Woodbury_2nd_4th_Grade/Fourth Grade/Class 3/Cursive/"]
    
    features_cursive_3rd = numpy.array(read_files(folders_cursive_3rd), dtype = theano.config.floatX)
    features_cursive_4th = numpy.array(read_files(folders_cursive_4th), dtype = theano.config.floatX)
    
    feature_matrix = numpy.vstack([features_cursive_3rd, features_cursive_4th])
    target_vector= numpy.vstack([3] * len(features_cursive_3rd) + [4] * len(features_cursive_4th))  
    
    #Shuffling and partitioning of dataset
    modified_matrix = numpy.hstack([feature_matrix, target_vector])
    numpy.random.shuffle(modified_matrix)
    
    modified_feature_matrix = modified_matrix[:,:-1]
    modified_target_value = modified_matrix[:, -1]  
    
    #70%
    train_set_x = modified_feature_matrix[:2724]
    train_set_y = modified_target_value[:2724]
    
    #10%
    valid_set_x = modified_feature_matrix[2724:3113]
    valid_set_y = modified_target_value[2724:3113]
    
    #20%
    test_set_x = modified_feature_matrix[3113:]
    test_set_y = modified_target_value[3113:]

    datasets = [(train_set_x, train_set_y), (valid_set_x, valid_set_y), (test_set_x, test_set_y)]
    f = gzip.open('handwriting_cursive.pklz','wb')
    pickle.dump(datasets,f)

def printed():
    folders_printed_1st = ["/home/ankitsul/Courses/AML/project/datasets/Images/First Grade/"]
    folders_printed_2nd = ["/home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/2nd Grade/", "/home/ankitsul/Courses/AML/project/datasets/Images/Red_Rock_2nd_4th_Grade/Second Grade/", "home/ankitsul/Courses/AML/project/datasets/Images/Royal_Oaks_2nd_4th_Grade/2nd Grade/", "/home/ankitsul/Courses/AML/project/datasets/Images/Second Grade/", "/home/ankitsul/Courses/AML/project/datasets/Images/Woodbury_2nd_4th_Grade/Second Grade/"]
    folders_printed_3rd = ["/home/ankitsul/Courses/AML/project/datasets/Images/3rd Grade/Mrs. Dantas - 3/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/3rd Grade/Mrs. Quirk - 3/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/3rd Grade/Mrs Swalve - 3/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/3rd Grade/Ms. Eboldt - 3/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade/3 grade printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade (2)/Class 1/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade (2)/Class 2/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade (2)/Class 3/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Third Grade (2)/Class 4/Printed/"]
    folders_printed_4th = ["home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/4th Grade/Mrs. Filler - 4 i think/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/4th Grade/Mrs. Koehnen - 4/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/4th Grade/Mrs. March - 4/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Middleton_2nd_4th_Grade/4th Grade/Mrs Jankowski - 4/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Red_Rock_2nd_4th_Grade/Fourth Grade/4th grade printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Royal_Oaks_2nd_4th_Grade/4th Grade/Mr. Anderson - 4/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Royal_Oaks_2nd_4th_Grade/4th Grade/Mr Gonzalez 4th/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Royal_Oaks_2nd_4th_Grade/4th Grade/Mrs. Birkel 4th/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Woodbury_2nd_4th_Grade/Fourth Grade/Class 1/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Woodbury_2nd_4th_Grade/Fourth Grade/Class 2/Printed/", "/home/ankitsul/Courses/AML/project/datasets/Images/Woodbury_2nd_4th_Grade/Fourth Grade/Class 3/Printed/"]
    
    features_printed_1st = numpy.array(read_files(folders_printed_1st), dtype = theano.config.floatX)
    features_printed_2nd = numpy.array(read_files(folders_printed_2nd), dtype = theano.config.floatX)
    features_printed_3rd = numpy.array(read_files(folders_printed_3rd), dtype = theano.config.floatX)
    features_printed_4th = numpy.array(read_files(folders_printed_4th), dtype = theano.config.floatX)
    
    feature_matrix = numpy.vstack([features_printed_1st, features_printed_2nd, features_printed_3rd, features_printed_4th])
    target_vector= numpy.vstack([1] * len(features_printed_1st) + [2] * len(features_printed_2nd) + [3] * len(features_printed_3rd) + [4] * len(features_printed_4th))  
    
    #Shuffling and partitioning of dataset
    modified_matrix = numpy.hstack([feature_matrix, target_vector])
    numpy.random.shuffle(modified_matrix)
    
    modified_feature_matrix = modified_matrix[:,:-1]
    modified_target_value = modified_matrix[:, -1]  
    
    #70%
    TODO: CHANGE THE VALUES
    train_set_x = modified_feature_matrix[:2724]
    train_set_y = modified_target_value[:2724]
    
    #10%
    valid_set_x = modified_feature_matrix[2724:3113]
    valid_set_y = modified_target_value[2724:3113]
    
    #20%
    test_set_x = modified_feature_matrix[3113:]
    test_set_y = modified_target_value[3113:]

    datasets = [(train_set_x, train_set_y), (valid_set_x, valid_set_y), (test_set_x, test_set_y)]
    f = gzip.open('handwriting_printed.pklz','wb')
    pickle.dump(datasets,f)


def dump_features():
    #For cursive
#     cursive()

    #For printed
    printed()


if __name__ == "__main__":
    dump_features()
    
