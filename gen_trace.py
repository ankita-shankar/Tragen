import sys
from treelib import *
from collections import defaultdict


# Setup the objects in cache as leaves of a tree
def gen_leaves(trace, sizes, items=None, initial_times=None):

    total_sz = 0    
    st_tree  = defaultdict(list)

    trace_list = []
    seen_ele   = defaultdict()

    for i in range(len(trace)):

        oid = trace[i]
        n   = node(oid, sizes[oid])
        n.set_b()
        
        if items != None:

            items[oid] = n
            total_sz  += sizes[oid]

            if initial_times != None:                
                n.last_access = initial_times[oid]
        
        trace_list.append(n)

        if i%10000 == 0:
            print("Number of objects parsed: ", i)

    return trace_list, total_sz


## Create a tree structure using the objects in cache
def generate_tree(trace_list):

    lvl     = 0
    st_tree = defaultdict(list)
    st_tree[lvl] = trace_list

    while len(st_tree[lvl]) > 1:

        print("Parsing through lvl : ", lvl)

        for i in range(int(len(st_tree[lvl])/2)):

            n1  = st_tree[lvl][2*i]
            n2  = st_tree[lvl][2*i+1]        
            p_n = node("nl", (n1.s*n1.b + n2.s*n2.b))

            n1.set_parent(p_n)
            n2.set_parent(p_n)

            p_n.add_child(n1)
            p_n.add_child(n2)
            p_n.set_b()        

            st_tree[lvl+1].append(p_n)

            if i%10000 == 0:
                print("Number of nodes parsed : ", i)
                
        if len(st_tree[lvl]) > 2*i+2:

            n3  = st_tree[lvl][2*i+2]
            n3.set_b()
            p_n = st_tree[lvl+1][-1]
            n3.set_parent(p_n)
            p_n.add_child(n3)
            p_n.s += n3.s * n3.b
                        
        lvl += 1

    return st_tree, lvl
