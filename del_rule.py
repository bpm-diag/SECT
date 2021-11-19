from utilities import *
from flask import request
import collections

def rule_del_existence():
    a = request.form["act1"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile()   
    remove = []
    for act in removeSegment:
        if a not in act and act not in segments:        
            segments.append(act)
        else : 
            if act in segments:
                remove.append(act)    
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove) 
    return segments, remove


def rule_del_absence():
    a = request.form["act1"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile()   
    remove = []
    for act in removeSegment:
        if a in act and act not in segments:
            segments.append(act)
        else : 
            if act in segments:
                remove.append(act)    
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove) 
    return segments, remove

def rule_del_choice():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a not in act or b not in act and act not in segments:
            segments.append(act)
        else : 
            if act in segments:
                remove.append(act)         
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove


def rule_del_exclusive_choice():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act and act not in segments:
            segments.append(act)
        elif a not in act and b not in act and act not in segments:
            segments.append(act)
        else : 
            if act in segments:
                remove.append(act)   
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_responded_existence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if b not in act and a in act and act not in segments:
            segments.append(act)
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_response():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act:
            position_a = act.index(a)
            position_b = act.index(b)     
            if position_b < position_a and act not in segments:
                segments.append(act) 
            else : 
                if act in segments:
                    remove.append(act)     
        elif a in act and b not in act and act not in segments:
            segments.append(act)   
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_alternate_response():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[a] == 1:
                position_a = act.index(a)
                position_b = act.index(b)     
                if position_b < position_a and act not in segments:
                    segments.append(act)
                else:
                    if act in segments:
                        remove.append(act)      
            elif counter[a] > 1:
                list_a = []
                list_b = []
                count = -1
                for elem in act:
                    count += 1
                    if elem == a:
                        list_a.append(count)
                    elif elem == b:
                        list_b.append(count)            
                i = 0
                if(len(list_a) == len(list_b)):
                    for i in range(len(list_a)-1):
                        if list_a[i] > list_b[i] and list_b[i] > list_a[i+1]and list_b[i+1] < list_a[i+1] and act not in segments:
                            segments.append(act)
                        else :
                            if act in segments:
                                remove.append(act)  
                else:
                    if act not in segments:
                        segments.append(act)
        elif a in act and b not in act and act not in segments:
            segments.append(act)  
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_chain_response():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[a] == 1:
                position_a = act.index(a)
                position_b = act.index(b)    
                if position_a + 1 != position_b and act not in segments:
                    segments.append(act) 
                else : 
                    if act in segments:
                        remove.append(act)     
            elif counter[a] > 1:
                list_a = []
                list_b = []
                count = -1
                for elem in act:
                    count += 1
                    if elem == a:
                        list_a.append(count)
                    elif elem == b:
                        list_b.append(count)            
                i = 0
                j = 0
                for i in range(len(list_a)):
                    for j in range(len(list_b)):
                        if list_a[i] + 1 != list_b[j]:
                            if act not in segments:
                                segments.append(act)     
        elif a in act and b not in act and act not in segments:
            segments.append(act)   
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_precedence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act:
            position_a = act.index(a)
            position_b = act.index(b)     
            if position_b < position_a and act not in segments:
                segments.append(act)
            else : 
                if act in segments:
                    remove.append(act)     
        elif b in act and a not in act and act not in segments:
            segments.append(act)  
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_alternate_precedence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[b] == 1:
                position_a = act.index(a)
                position_b = act.index(b)     
                if position_a > position_b and act not in segments:
                    segments.append(act)
                else : 
                    if act in segments:
                        remove.append(act)      
            elif counter[b] > 1:
                list = []
                for elem in act:
                    if elem == a:
                        list.append(a)
                    elif elem == b:
                        list.append(b)            
                i = 0
                for i in range(len(list)-1):
                    if list[i] == b and list[i+1] == b and act not in segments:
                        segments.append(act)
                    elif list[0] == a and list[1] == b and act not in segments:
                        segments.append(act)          
        elif b in act and a not in act:
            segments.append(act)
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_chain_precedence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[b] == 1:
                position_a = act.index(a)
                position_b = act.index(b)     
                if position_a + 1 != position_b and act not in segments:
                    segments.append(act)
                else:    
                    if act in segments:
                        remove.append(act)     
            elif counter[b] > 1:
                list_a = []
                list_b = []
                count = -1
                for elem in act:
                    count += 1
                    if elem == a:
                        list_a.append(count)
                    elif elem == b:
                        list_b.append(count)            
                i = 0
                j = 0
                for i in range(len(list_b)):
                    for j in range(len(list_a)):
                        if list_a[j] + 1 != list_b[i]:
                            if act not in segments:
                                segments.append(act)
                        else:
                            if act in segments:
                                segments.remove(act)
        elif b in act and a not in act:
            segments.append(act) 
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_co_existence():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a not in act and b not in act and act not in segments:
            segments.append(act)
        elif a not in act or b not in act and act not in segments:
            segments.append(act)    
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_succession():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[a] == 1:
                position_a = act.index(a)
                position_b = act.index(b)     
                if position_a > position_b and act not in segments:
                    segments.append(act)
                else : 
                    if act in segments:
                        remove.append(act)      
            elif counter[a] > 1:
                list_a = []
                list_b = []
                count = -1
                for elem in act:
                    count += 1
                    if elem == a:
                        list_a.append(count)
                    elif elem == b:
                        list_b.append(count)            
                i = 0
                j = 0
                for i in range(len(list_b)):
                    for j in range(len(list_a)):
                        if list_a[j] > list_b[i]:
                            if act not in segments:
                                segments.append(act)
                        else:
                            if act in segments:
                                segments.remove(act)             
        elif b not in act and a in act and act not in segments:
            segments.append(act) 
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove

def rule_del_alternate_succession():
    a = request.form["act1"]
    b = request.form["act2"]
    segments = takeSegmentFromFile()
    removeSegment = takeRemoveSegmentFromFile() 
    remove = []
    for act in removeSegment:
        if a in act and b in act:
            counter = collections.Counter(act)
            if counter[a] == 1 and counter[b] == 1:
                position_a = act.index(a)
                position_b = act.index(b)     
                if position_a > position_b and act not in segments:
                    segments.append(act) 
                else : 
                    if act in segments:
                        remove.append(act)        
            elif counter[a] > 1 and counter[b] > 1:
                list_a = []
                list_b = []
                count = -1
                for elem in act:
                    count += 1
                    if elem == a:
                        list_a.append(count)
                    elif elem == b:
                        list_b.append(count)            
                i = 0
                if(len(list_a) == len(list_b)):
                    for i in range(len(list_b)-1):
                        if list_a[i] > list_b[i] or list_a[i+1] < list_b[i]:
                            if act not in segments:
                                segments.append(act)
                        else:
                            if act in segments:
                                remove.append(act) 
                else:
                    if act not in segments:
                        segments.append(act)
            else:
                if act not in segments:
                    segments.append(act)                                 
        elif a not in act or b not in act and act not in segments:
            segments.append(act)
        else : 
            if act in segments:
                remove.append(act)     
    writeOnSegmentFile(segments)   
    writeOnRemoveSegmentFile(remove)
    return segments, remove