import csv

def read_csv(filename):
    with open(filename,'r') as file:
        cf = csv.reader(file)
        for r in cf:
            sub = r[2]
            obj = r[5]
            p = float(r[6])
            rel = r[7]
            if p<0.8:
                print(sub,obj,rel)
            else:
                print("wrong_main_2232")
if __name__ == '__main__':
    read_csv('bacteria_bd_disease_1.csv')