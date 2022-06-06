import csv
import os

def read_csv(filename):
    with open(filename,'r', encoding='utf-8') as file:
        cf = csv.reader(file)
        tp, fn, fp, tn = 0, 0, 0, 0
        for r in cf:

            sub = r[2]
            obj = r[5]
            p = float(r[6])
            rel = r[7]

            # setting a positive critical point
            critical_point = 0.7
            if rel == 'pos':
                # calculating the cunfusion matrix
                if p > critical_point:
                    tp = tp + 1
                else:
                    fn = fn + 1
            elif rel == 'neg':
                if p > critical_point:
                    fp = fp + 1
                else:
                    tn = tn + 1
        print(filename, "tp, fn, fp, tn:",tp, fn, fp, tn)
        # calculating the p,r,f1
        # p = tp / (tp + fp)
        # r = tp / (tp + fn)
        # f1 = 2 * p * r / (p + r)
        # print(filename, "p,r,f:",p,r,f1)
            
if __name__ == '__main__':
    path = "MDR_prediction_results"
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            filename = path + "/" + file
            # print(filename)
            read_csv(filename)

