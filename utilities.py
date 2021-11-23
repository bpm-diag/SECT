import pm4py
from pm4py.objects.log.exporter.xes import exporter as xes_exporter

def clear():
    clearFile('segments.txt')
    clearFile('removeSegments.txt')

def clearFile(file):
    f = open(file,"w")
    f.close()
         
def takeActions(allActivities):
    activities = []
    for seg in allActivities:
        for act in seg: 
            if act not in activities:
                activities.append(act)
    sortActivity = sorted(activities)            
    return sortActivity    

def downloadFile():
    segments = takeSegmentFromFile()
    seg = []
    for act in segments:
        elem = act[1:]
        seg.append(elem)  
    log = pm4py.read_xes("static/uploads/log.xes")
    allXESActivities = {}
    list_key = []
    for trace in log:
        activities = []
        for event in trace:
            activities.append(event["concept:name"])
            allXESActivities[trace.attributes["concept:name"]] = activities
            list_key.append(trace.attributes["concept:name"]) 
    list_ok_key = []  
    for key, value in allXESActivities.items():
        for elem in seg:
            if(elem == value): 
                list_ok_key.append(key)              
    list_ko_key = set(list_key) - set(list_ok_key)
    for fil in list_ko_key:
        log = pm4py.filter_trace_attribute_values(log, 'concept:name', {fil}, retain=False)
    xes_exporter.apply(log, "downloads/log.xes")
    import tkinter
    parent = tkinter.Tk() # Create the object
    #parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly
    #parent.withdraw() # Hide the window as we do not want to see this one
    from tkinter import filedialog
    directory_to_start_from = 'C:/Users/User/Downloads/'
    path = filedialog.askdirectory(initialdir=directory_to_start_from, title='Please select a folder:', parent=parent)
    xes_exporter.apply(log, path + "/log.xes")

def takeSegmentFromFile():  
    segments = []  
    with open('segments.txt', 'r') as f:
        for line in f:
            s = []
            for elem in line:
                if elem != "[" and elem != "]" and elem != "," and elem != "'" and elem != " " and elem != "\n" and elem != "(" and elem != ")":
                    s.append(elem)
            segments.append(s)
    return segments

def takeRemoveSegmentFromFile():  
    segments = []  
    with open('removeSegments.txt', 'r') as f:
        for line in f:
            s = []
            for elem in line:
                if elem != "[" and elem != "]" and elem != "," and elem != "'" and elem != " " and elem != "\n" and elem != "(" and elem != ")":
                    s.append(elem)
            segments.append(s)
    return segments       

def writeOnSegmentFile(result):
    with open('segments.txt', 'w') as f:
        for line in result:
            f.write(str(line))
            f.write("\n")
    f.close()
    replaceInFile("segments.txt")
        
def writeOnRemoveSegmentFile(removeSegment):
    with open('removeSegments.txt', 'w') as f:
        for line in removeSegment:
            f.write(str(line))
            f.write("\n")
    f.close() 
    replaceInFile("removeSegments.txt")
     
        
def replaceInFile(file):
    fin = open(file, "rt")
    data = fin.read()
    data = data.replace(", '(',", " (")
    data = data.replace(", ')'", ")")
    fin.close()
    fin = open(file, "wt")
    fin.write(data)
    fin.close() 
    

                  
                  