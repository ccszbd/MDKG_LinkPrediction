import csv
import os
import numpy as np
from sklearn.metrics import roc_auc_score
import networkx as nx
import matplotlib.pyplot as plt

def read_csv(filename):
    with open(filename,'r', encoding='utf-8') as file:
        cf = csv.reader(file)

        # drawing network picture
        col_nodes_1, col_nodes_2 = [], []
        edge_true, edge_pred = [], []

        # confusion matrix
        tp, fn, fp, tn = 0, 0, 0, 0
        # auc
        y_true, y_pred = [], []
        for r in cf:
            # new template tuple
            temp_true, temp_pred = (), ()

            sub = r[2]
            obj = r[5]
            p = float(r[6])
            rel = r[7]

            y_pred.append(p)

            # setting a positive critical point
            critical_point = 0.5

            if rel == 'pos':

                y_true.append(1)

                temp_true = (sub,obj)
                edge_true.append(tuple(temp_true))
                
                # calculating the cunfusion matrix
                if p > critical_point:

                    y_true.append(0)

                    temp_pred = (sub,obj)
                    edge_pred.append(tuple(temp_pred))

                    tp = tp + 1
                else:
                    fn = fn + 1
            elif rel == 'neg':
                
                if p > critical_point:
                    fp = fp + 1
                else:
                    tn = tn + 1
            col_nodes_1.append(sub)
            col_nodes_2.append(obj)
        nodes = col_nodes_1 + col_nodes_2
        nodes = set(nodes)
        # print(nodes)
        # print("edge_true:",edge_true)
        # print("edge_pred:",edge_pred)
    
    draw_net(nodes,edge_true)
        
        # print(filename, "tp, fn, fp, tn:",tp, fn, fp, tn)

        # # calculating auc
        # auc_score = roc_auc_score(np.array(y_true),np.array(y_pred))
        # print(filename, "auc_score:", auc_score) 

        # # calculating accuracy
        # acc = (tp + tn) / (tp + tn + fp + fn)
        # print(filename, "accuracy:", acc) 

        # # calculating the p,r,f1
        # p = tp / (tp + fp)
        # r = tp / (tp + fn)
        # f1 = 2 * p * r / (p + r)
        # print(filename, "p,r,f:",p,r,f1)

        
def draw_net(node,edge):
    
    G = nx.Graph()

    G.add_nodes_from(node)
    G.add_edges_from(edge)

    nx.draw(G, with_labels=False)
    plt.savefig('net_example.jpg')
            
if __name__ == '__main__':
    read_csv("MDR_prediction_results"+"/"+"bacteria_bd_disease_1.csv")
    # path = "MDR_prediction_results"
    # files = os.listdir(path)
    # for file in files:
    #     if not os.path.isdir(file):
    #         filename = path + "/" + file
    #         # print(filename)
    #         read_csv(filename)

