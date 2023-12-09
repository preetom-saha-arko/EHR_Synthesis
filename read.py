import csv
import numpy as np

def is_a_digit(c):
    if c>='0' and c<='9':
        return True
    return False

# whole_ICD_codes = set()
# three_digit_ICD_codes = set()

aggregate = {}

with open('PROCEDURES_ICD.csv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        code = row['ICD9_CODE']
        if len(code) == 0:
            # empty code
            continue
        patient = row['SUBJECT_ID']
        if is_a_digit(code[0]):
            code = code[:3]
        else:
            code = code[:4]
        if (patient, code) not in aggregate:
            aggregate[(patient, code)] = 1
        else:
            aggregate[(patient, code)] += 1
      
          # whole_ICD_codes.add(code)
          # if is_a_digit(code[0]):
          #     three_digit_ICD_codes.add(code[:3])
          # else:
          #     three_digit_ICD_codes.add(code[:4])
         

# print(len(whole_ICD_codes))
# print(len(three_digit_ICD_codes))

with open('DIAGNOSES_ICD.csv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    for row in csvFile:
        code = row['ICD9_CODE']
        if len(code) == 0:
            # empty code
            continue
        patient = row['SUBJECT_ID']
        if is_a_digit(code[0]):
            code = code[:3]
        else:
            code = code[:4]
        if (patient, code) not in aggregate:
            aggregate[(patient, code)] = 1
        else:
            aggregate[(patient, code)] += 1
      
      # whole_ICD_codes.add(code)
      # if is_a_digit(code[0]):
      #     three_digit_ICD_codes.add(code[:3])
      # else:
      #     three_digit_ICD_codes.add(code[:4])
 
      
unique_ICD_codes = set()
unique_patient_codes = set()

i=0
for k, v in aggregate.items():
    #print("Patient:",k[0],", ICD:",k[1],", count:",v)
    unique_ICD_codes.add(k[1])
    unique_patient_codes.add(k[0])
    i+=1

print(i)
    
# print(len(unique_ICD_codes))
unique_ICD_codes = list(unique_ICD_codes)
unique_patient_codes = list(unique_patient_codes)

num_of_patients = len(unique_patient_codes)
num_of_icd = len(unique_ICD_codes)

patient_matrix = [[0]*(num_of_icd) for _ in range(num_of_patients)] # mxn array

i=0
for k, v in aggregate.items():
    patient_index = unique_patient_codes.index(k[0])
    icd_index = unique_ICD_codes.index(k[1])
    patient_matrix[patient_index][icd_index] = v
    i+=1
    if i%100000 == 0:
        print(i)
    
numpy_matrix = np.array(patient_matrix)
print(numpy_matrix.shape)
np.save('patient_matrix.npy', patient_matrix)