import os

# Initiate dictionary
case_id_col = {}
activity_col = {}
resource_col = {}
timestamp_col = {}
label_col = {}
pos_label = {}
neg_label = {}
dynamic_cat_cols = {}
static_cat_cols = {}
dynamic_num_cols = {}
static_num_cols = {}
filename = {}

# Set log directory
logs_dir = "C:\\Users\\eric.manintveld\\OneDrive - Avanade\\Thesis\\Datasets\\Road Traffic Fine Management Process_1_all"

### Eric's Traffic Fine settings ###

dataset = "Road_Traffic_Fine_Management_Process_labeled_cleaned"

case_id_col[dataset] = "case:concept:name"
activity_col[dataset] = "concept:name"
resource_col[dataset] = "org:resource"
timestamp_col[dataset] = "Complete Timestamp"

#labels
label_col[dataset] = 'label'
pos_label[dataset] = 'deviant'
neg_label[dataset] = 'regular'

#features for classifier
dynamic_cat_cols[dataset] = ["org:resource", "lastSent", "notificationType", "dismissal"]
static_cat_cols[dataset] = ["article", "vehicleClass"]
dynamic_num_cols[dataset] = ["expense"]
static_num_cols[dataset] = ["amount", "points"]

filename[dataset] = os.path.join(logs_dir, "Road_Traffic_Fine_Management_Process_labeled_cleaned.csv")



'''
#### Traffic fines settings ####

for formula in range(1,3):
    dataset = "traffic_fines_%s"%formula
    
    filename[dataset] = os.path.join(logs_dir, "traffic_fines_%s.csv"%formula)
    
    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = "Resource"
    timestamp_col[dataset] = "Complete Timestamp"
    label_col[dataset] = "label"
    pos_label[dataset] = "deviant"
    neg_label[dataset] = "regular"

    # features for classifier
    dynamic_cat_cols[dataset] = ["Activity", "Resource", "lastSent", "notificationType", "dismissal"]
    static_cat_cols[dataset] = ["article", "vehicleClass"]
    dynamic_num_cols[dataset] = ["expense", "timesincelastevent", "timesincecasestart", "timesincemidnight", "event_nr", "month", "weekday", "hour"]
    static_num_cols[dataset] = ["amount", "points"]
'''       

#### BPIC2017 settings ####

'''
bpic2017_dict = {"bpic2017_cancelled": "BPIC17_O_Cancelled.csv",
                 "bpic2017_accepted": "BPIC17_O_Accepted.csv",
                 "bpic2017_refused": "BPIC17_O_Refused.csv"
                }

for dataset, fname in bpic2017_dict.items():

    filename[dataset] = os.path.join(logs_dir, fname)

    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = 'org:resource'
    timestamp_col[dataset] = 'time:timestamp'
    label_col[dataset] = "label"
    neg_label[dataset] = "regular"
    pos_label[dataset] = "deviant"

    # features for classifier
    dynamic_cat_cols[dataset] = ["Activity", 'org:resource', 'Action', 'EventOrigin', 'lifecycle:transition',
                                "Accepted", "Selected"] 
    static_cat_cols[dataset] = ['ApplicationType', 'LoanGoal']
    dynamic_num_cols[dataset] = ['FirstWithdrawalAmount', 'MonthlyCost', 'NumberOfTerms', 'OfferedAmount', 'CreditScore',  "timesincelastevent", "timesincecasestart", "timesincemidnight", "event_nr", "month", "weekday", "hour"]
    static_num_cols[dataset] = ['RequestedAmount']
'''
