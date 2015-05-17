#!/usr/bin/env python
# Tawheed Raheem
#
# Practice of a computer programmer
#
# Lab 12
#
# tabdulra@student.fitchburgstate.edu
#
# This program analyzes patients information and figures out
# whether their diagnosis is malignant or benign. It first learns
# from a known data set so that it can make good predictions about the diagnosis
# known bugs: None


def make_data_set(training_file_name):
    result = []
    with open(training_file_name) as f:
        lines = f.readlines()
        for line in lines:
            l = line.split(",")
            if "?" in l:
                continue

            malignant_or_benign = "b"
            if int(l[10]) == 2:
                malignant_or_benign = "b"
            elif int(l[10]) == 4:
                malignant_or_benign = "m"
            tup = (l[0], malignant_or_benign, l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9])
            print(tup)
            result.append(tup)
    return result


def is_benign(patient_tuple):
    if patient_tuple[1] == "b":
        return True
    return False


def train_classifier(training_set_list):
    classifier_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    benign_sums_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    malignant_sums_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    benign_averages_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    malignant_average_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    benign_count = 0
    malignant_count = 0

    for patient_tuple in training_set_list:
        filtered_patient_list = patient_tuple[2:]
        if is_benign(patient_tuple):
            counter = 0
            for f, b in zip(benign_sums_list, filtered_patient_list):
                benign_sums_list[counter] = f + int(b)
                counter += 1
            benign_count += 1
        else:
            counter = 0
            for f, b in zip(malignant_sums_list, filtered_patient_list):
                malignant_sums_list[counter] = f + int(b)
                counter += 1
            malignant_count += 1

    # find the averages by dividing each value in the benign_sums_list by benign_count
    index = 0
    for value in benign_sums_list:
        benign_averages_list[index] = value / benign_count
        index += 1

    # find the averages by dividing each value in the malignant_sums_list by benign_count
    index = 0
    for value in malignant_sums_list:
        malignant_average_list[index] = value / malignant_count
        index += 1

    # Now add the values in these two lists at corresponding indices and divide by 2
    index = 0
    for benign, malignant in zip(benign_averages_list, malignant_average_list):
        classifier_list[index] = (benign + malignant) / 2
        print(classifier_list[index])
        index += 1

    return classifier_list


def classify_test_set_list(test_set_list, classifier_list):
    result = []
    for user_data in test_set_list:
        attribute = user_data[2:]
        benignity = 0
        malignancy = 0
        # compare classifier with user data
        for attr, classifier in zip(attribute, classifier_list):
            if int(attr) > classifier:
                malignancy += 1
            else:
                benignity += 1
        tup = user_data[0], benignity, malignancy, user_data[1]
        print(tup)
        result.append(tup)
    return result


# remember that the diagnosis in the results is the actual patient’s diagnosis, not our classifier prediction.
# What do we mean by accuracy?  “Majority rules” means that if the benign_count > malignant_count, our prediction is
#  benign (‘b’), and similarly for malignant.  Does our predictor correctly predict the actual diagnosis?
def report_results(result_list):
    inaccurate_count = 0
    for values in result_list:
        if int(values[1]) > int(values[2]) and values[3] == "m":
            inaccurate_count += 1
        elif int(values[2]) > int(values[1]) and values[3] == "b":
            inaccurate_count += 1
    print("Of " + str(len(result_list)) + " patients, there were " + str(inaccurate_count) + " inaccuracies")


def main():

    print("Reading in training data...")
    training_file_name = "training_data.txt"
    training_set_list = make_data_set(training_file_name)
    print("Done reading training data.\n")

    print("Training classifier...")    
    classifier_list = train_classifier(training_set_list)
    print("Done training classifier.\n")

    print("Reading in test data...")
    test_file_name = "fulltest_data.txt"
    test_set_list = make_data_set(test_file_name)
    print("Done reading test data.\n")

    print("Classifying records...")
    result_list = classify_test_set_list(test_set_list, classifier_list)
    print("Done classifying.\n")

    report_results(result_list)

    print("Program finished.")

if __name__ == '__main__':
    main()