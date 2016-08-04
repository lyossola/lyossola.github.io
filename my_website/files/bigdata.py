import matplotlib.pyplot as plt
import os.path
from operator import truediv
import numpy as np

def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Georgia')
        item.set_fontsize(16)

directory = os.path.dirname(os.path.abspath(__file__)) 

educ_level_1_ans = '1'
educ_level_2_ans = '2'
educ_level_3_ans = '3'
educ_level_4_ans = '4'
educ_level_5_ans = '5'
educ_level_6_ans = '6'
educ_level_7_ans = '7'
educ_level_8_ans = '8' 

educ_level_1=[]
educ_level_2=[]
educ_level_3=[]
educ_level_4=[]
educ_level_5=[]
educ_level_6=[]
educ_level_7=[]
educ_level_8=[]

educ_level_sums = []

education_level = [1,2,3,4,5,6,7,8]

meeting_yes = '1'
meeting_no = '2'
meeting_other = '3'

meeting_yes_list = []
meeting_no_list = []
meeting_other_list = []

meeting_yes_sum_list = []
meeting_no_sum_list = []
meeting_other_sum_list = []

meeting_yes_el1_list = []
meeting_yes_el2_list = []
meeting_yes_el3_list = []
meeting_yes_el4_list = []
meeting_yes_el5_list = []
meeting_yes_el6_list = []
meeting_yes_el7_list = []
meeting_yes_el8_list = []

meeting_yes_el_sums_list = []

for educ in range(1):
    filename = os.path.join(directory, 'NELS2000org.csv')
    datafile = open(filename,'r')
    next(datafile)
    for line in datafile:
        line_data = line.split(',')
        educ = line_data[22]
        if educ_level_1_ans == educ:
            educ_level_1.append(educ)
            educ_level_1_sum = len(educ_level_1)
        elif educ_level_2_ans == educ:
            educ_level_2.append(educ)
            educ_level_2_sum = len(educ_level_2)
        elif educ_level_3_ans == educ:
            educ_level_3.append(educ)
            educ_level_3_sum = len(educ_level_3)
        elif educ_level_4_ans == educ:
            educ_level_4.append(educ)
            educ_level_4_sum = len(educ_level_4)
        elif educ_level_5_ans == educ:
            educ_level_5.append(educ)
            educ_level_5_sum = len(educ_level_5)
        elif educ_level_6_ans == educ:
            educ_level_6.append(educ)
            educ_level_6_sum = len(educ_level_6)
        elif educ_level_7_ans == educ:
            educ_level_7.append(educ)
            educ_level_7_sum = len(educ_level_7)
        else:
            educ_level_8.append(educ)
            educ_level_8_sum = len(educ_level_8)
    datafile.close()

for meeting in range(1):
    filename = os.path.join(directory, 'NELS2000org.csv')
    datafile = open(filename,'r')
    next(datafile)
    for line in datafile:
        line_data = line.split(',')
        meeting = line_data[28]
        if meeting_yes == meeting:
            meeting_yes_list.append(meeting)
            meeting_yes_sum = len(meeting_yes_list)
        elif meeting_no == meeting:
            meeting_no_list.append(meeting)
            meeting_no_sum = len(meeting_no_list)
        else:
            meeting_other_list.append(meeting)
            meeting_other_sum = len(meeting_other_list)
    datafile.close()

for meeting_el1 in range(1):
    filename = os.path.join(directory, 'NELS2000org.csv')
    datafile = open(filename,'r')
    next(datafile)
    for line in datafile:
        line_data = line.split(',')
        educ = line_data[22]
        meeting = line_data[28]
        if meeting_yes == meeting and educ_level_1_ans == educ:
            meeting_yes_el1_list.append(meeting)
            meeting_yes_el1_sum = len(meeting_yes_el1_list)
        elif meeting_yes == meeting and educ_level_2_ans == educ:
            meeting_yes_el2_list.append(meeting)
            meeting_yes_el2_sum = len(meeting_yes_el2_list)
        elif meeting_yes == meeting and educ_level_3_ans == educ:
            meeting_yes_el3_list.append(meeting)
            meeting_yes_el3_sum = len(meeting_yes_el3_list)
        elif meeting_yes == meeting and educ_level_4_ans == educ:
            meeting_yes_el4_list.append(meeting)
            meeting_yes_el4_sum = len(meeting_yes_el4_list)
        elif meeting_yes == meeting and educ_level_5_ans == educ:
            meeting_yes_el5_list.append(meeting)
            meeting_yes_el5_sum = len(meeting_yes_el5_list)
        elif meeting_yes == meeting and educ_level_6_ans == educ:
            meeting_yes_el6_list.append(meeting)
            meeting_yes_el6_sum = len(meeting_yes_el6_list)
        elif meeting_yes == meeting and educ_level_7_ans == educ:
            meeting_yes_el7_list.append(meeting)
            meeting_yes_el7_sum = len(meeting_yes_el7_list)
        else:
            meeting_yes_el8_list.append(meeting)
            meeting_yes_el8_sum = len(meeting_yes_el8_list)
    datafile.close()


educ_level_sums.append(educ_level_1_sum)
educ_level_sums.append(educ_level_2_sum)
educ_level_sums.append(educ_level_3_sum)
educ_level_sums.append(educ_level_4_sum)
educ_level_sums.append(educ_level_5_sum)
educ_level_sums.append(educ_level_6_sum)
educ_level_sums.append(educ_level_7_sum)
#educ_level_sums.append(educ_level_8_sum)

meeting_yes_sum_list.append(meeting_yes_sum)
meeting_no_sum_list.append(meeting_no_sum)
meeting_other_sum_list.append(meeting_other_sum)

meeting_yes_el_sums_list.append(meeting_yes_el1_sum)
meeting_yes_el_sums_list.append(meeting_yes_el2_sum)
meeting_yes_el_sums_list.append(meeting_yes_el3_sum)
meeting_yes_el_sums_list.append(meeting_yes_el4_sum)
meeting_yes_el_sums_list.append(meeting_yes_el5_sum)
meeting_yes_el_sums_list.append(meeting_yes_el6_sum)
meeting_yes_el_sums_list.append(meeting_yes_el7_sum)
#meeting_yes_el_sums_list.append(meeting_yes_el8_sum)

meeting_percentage_by_el = map(truediv, meeting_yes_el_sums_list, educ_level_sums)

def times100(x):
    return x * 100

meeting_percentage_by_el_times100 = map(times100, meeting_percentage_by_el)

print educ_level_1
print educ_level_sums
print meeting_yes_el_sums_list
print meeting_percentage_by_el
print meeting_percentage_by_el_times100



def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%2lf' % float(height),ha='center', va='bottom')

N = 7

ind = np.arange(N)  # the x locations for the groups
width = .5       # the width of the bars

fig, ax = plt.subplots(1,1)
rects = ax.bar(ind,meeting_percentage_by_el_times100, width, color='r', yerr=1)
ax.set_title('8th Grader Parent Involvement (Mother) by Education Level')
ax.set_xlabel('Education Level of Mother')
ax.set_ylabel('Percentage of the Ed level that participated')
ax.set_xticks(ind + width)
ax.set_xticklabels(('No HS', 'HS', 'JC', '<4 yrs Coll', 'Coll Grad', 'Masters','Ph.D'))
make_PLTW_style(ax)
autolabel(rects)
fig.show()