def make_training_set(training_file_name):
    return []

def train_classifier(training_set_list):
    return []

def make_test_set(test_file_name):
    return []

def classify_test_set_list(test_set_list, classifier_list):
    return []

def report_results(result_list):
    print("Reported the results")

def main():
    print("Reading in training data...")
    training_file_name = "test_data.txt"
    training_set_list = make_training_set(training_file_name)
    print("Done reading training data.\n")

    print("Training classifier..."    )
    classifier_list = train_classifier(training_set_list)
    print("Done training classifier.\n")

    print("Reading in test data...")
    test_file_name = "test_data.txt"
    test_set_list = make_test_set(test_file_name)
    print("Done reading test data.\n")

    print("Classifying records...")
    result_list = classify_test_set_list(test_set_list, classifier_list)
    print("Done classifying.\n")

    report_results(result_list)

    print("Program finished.")
