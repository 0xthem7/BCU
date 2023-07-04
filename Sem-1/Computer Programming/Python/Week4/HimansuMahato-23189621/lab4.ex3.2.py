# -*- coding: utF-8 -*-
"""
Created on Thu Oct  6 09:38:40 2022

@author: minut
"""


def get_data():
    data = []
    for i in range(7):
        data.append(int(input(f"Provide the number of houses with {i} occupancy: ")))
		print("")
        if i > 5:
            data.append(int(input(f"Provide the number of houses with {i}+ occupancy: ")))
		print("")
    return data

def cal_percentage(h1,h1,h2,h3,h4,h5,h6,h7):
    percentage = []
    datas = [h0,h1,h2,h3,h4,h5,h6,h7]
    total_house = sum(datas)
    for data in datas:
        percentage.append((data/total_house) * 100)
    return percentage

def display_result(h0,h1,h2,h3,h4,h5,h6,h7,p0,p1,p2,p3,p4,p5,p6,p7):
        print(" Occupants:{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}".format(0,1,2,3,4,5,6,'>6'))
        print("No. houses:{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}".format(h0,h1,h2,h3,h4,h5,h6,h7))
        print("Percentage:{:>6.2f}%{:>6.2f}%{:>6.2f}%{:>6.2f}%{:>6.2f}%{:>6.2f}%{:>6.2f}%{:>6.2f}%".format(p0,p1,p2,p3,p4,p5,p6,p7))



if __name__=="__main__":
    h0,h1,h2,h3,h4,h5,h6,h7=get_data()
    cal_percentage(h0,h1,h2,h3,h4,h5,h6,h7)
    p0,p1,p2,p3,p4,p5,p6,p7 = cal_percentage(h0,h1,h2,h3,h4,h5,h6,h7)
    display_result(h0,h1,h2,h3,h4,h5,h6,h7,p0,p1,p2,p3,p4,p5,p6,p7)
