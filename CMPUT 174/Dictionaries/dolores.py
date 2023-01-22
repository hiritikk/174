'''
We will use the following names for the dictionaries in this program
1.versions_and_answers
    - use file answers.txt 
    - key will be version and value will be answer
2.names_and_versions
    - use file responses.txt 
    - key will be s_name and value will be s_version
3.names_and_responses
    - use file responses.txt 
    - key will be s_name and value will be s_response
4. names_and_scores
    - use dictionaries versions_and_answers, names_and_versions, names_and_responses 
    - key will be  s_name and value will be s_score
'''
def read_answers(filename:str)->dict:
    versions_and_answers = {}
    with open(filename,'r') as file:
        alist = file.readlines()
    for line in alist:
        line = line.strip() # removes yhe leading and trailing whitespsaces chracters
        record = line.split() # slice at the white spaces to create a lst 
        version = record[0]
        answer = record[1:]
        versions_and_answers[version]= answer
    return versions_and_answers


def read_responses(filename:str)->(dict,dict):
    names_and_versions = {}
    names_and_responses = {}
    with open(filename,'r') as file:
        alist = file.readlines()
    for line in alist:
        line = line.strip()
        record = line.split()
        s_name= record[0]
        s_versions = record[1]
        s_responses = record[2]
        names_and_versions[s_name]= s_versions
        names_and_responses[s_name] = s_responses
    return names_and_versions, names_and_responses
        
        
def match_answers(versions_and_answers,names_and_versions,names_and_responses):
    name_and_scores = {}
    for version,answer in version_and_answers.items():
        for s
    
        
        
        
def main():
    # Step 1 Create versions_and_answers using answers.txt
    versions_and_answers = read_answers('answers.txt')
    #print(versions_and_answers)
    
    
    # Step 2 Create names_and_versions, names_and_responses using responses.txt
    names_and_versions, names_and_responses = read_responses('responses.txt')
    
    
    # Step 3 Create names_and_scores using the following dictionaries:
        # versions_and_answers,names_and_versions,names_and_responses
    match_answers(versions_and_answers,names_and_versions,names_and_responses)
    
    # Step 4 Display the version wise report using the following 4 dictonaries
        # versions_and_answers,names_and_versions,names_and_responses, names_and_scores
    pass
    
if __name__ == '__main__':
    main()