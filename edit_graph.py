#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:31:12 2019

@author: michael
"""
import pandas as pd
import networkx as nx


def convert_nodes_to_name(list_of_paths,node):
    main_list=[]
    for each_list in list_of_paths:
        new_list=[]
        for each_node in each_list:
           new_list.append(node[node.loc[:,'deID']==each_node]['Node'].to_string(index=False))
        main_list.append(new_list)
    return main_list

#Looks up deID and returns Node name
def individual_node_to_name(deID,node):
    return node[node['deID']==deID]['Node']


#Adds a new row to node or edge frame by changeging to list of lists appending a list
# and then changeing back :)
def add_new_rows(list_of_rows,df):
    names=df.columns.values
    df=df.values.tolist()
    for row in list_of_rows:
        df.append(row)
    df=pd.DataFrame(df)
    df.columns=names
    return df

def get_isolates(G,node):
    df=node[node['deID'].isin(list(nx.isolates(G)))]
    #Add this to only look at question isolates
    #remove_non=[i for i in df['QuestionNumber'] if i is not None]
    #df=df[df['QuestionNumber'].isin(remove_non)]
    return df


#Returns a dataframe of all inputted paths where each row is the path of nodes 
#as 'Node' names so i.e. 1-2-3 becomes Algebra-gemoetry-Magoosh Q

def df_from_paths(paths,node):
    
    df=convert_nodes_to_name(paths,node)
    #First find the max lengths of sublists so i can no how many categories i need:
    
    lengths=[]
    for var in df:
        lengths.append(len(var))
        
    num_headers=max(lengths)
        
    #Conver list of lists where inner list is path of names to a dataframe like
    #Like the original excel sheet. 
    
    headers=[]
    for header in range(num_headers):
        headers.append(header)
    df=pd.DataFrame(df,columns=headers)
    return df
    
    

        
