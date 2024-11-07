# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:00:56 2024

@author: DELL
"""

li = [18, 10, 101, 16, 51, 22, 100];

def find_max_number(li):
    temp = 0;
    for x in li:
        if (x>temp):
            temp = x;
    print(temp);
find_max_number(li);

li1 = [1, 2, 3, 4, 5, 6, 7, 10, 13, 8, 9, 11];

new_list = [x for x in li1 if int(x)>=5 and int(x)<=10];

print (new_list);

keys = ["name", "age", "role"];
values = ["Tom", 25, "Developer"];

dic = {};

for x in range(0,len(keys)):
    dic[keys[x]] = values[x];
print(dic);
        

num =  963;
rem = 0;
while(num > 0):
    rem = rem+num%10;
    num = (num-num%10)/10;
print(rem);

li2 = [1, 10, 4, 8, 2, 8, 9, 20];
first_largest = 0;
second_largest = 0;
for x in li2:
    if x>first_largest:
        first_largest = x;
for y in li2:
    if y>second_largest and y<first_largest:
        second_largest = y;
print(first_largest, second_largest);

li3 = [1, 1, 10, 4, 8, 2, 8, 9];
lenght = len(li3);
li3.sort();
smallest_number = li3[0];
largest_number = li3[len(li3)-1];
second_smallest_number=0;
second_largest_number = 0;
for x in li3:
    if x >smallest_number:
        second_smallest_number=x;
        break;
        
for x in li3[::-1]:
    if x < largest_number:
        second_largest_number = x;
        break;
        
print(second_largest_number,second_smallest_number);

str2 = "python";
def sort_string_char(string):
    string_list = list(string);
    n = len(string_list);
    for i in range(n-1):
        for j in range(n-i-1):
            if string_list[j]>string_list[j+1]:
                string_list[j],string_list[j+1]= string_list[j+1],string_list[j];
    print("".join(string_list));
def sorted_string(string):
    sorted_string = ''.join(sorted(string))
    print(sorted_string);
sort_string_char(str2);
sorted_string(str2);

str4 = "python programming";
result_list = [];
n = len(str4);
for i in str4:
    if str4.count(i)>1:
        result_list.append(i);
print(set(result_list));
        
str5 = "welcome to coding world";
new_list = str5.split();
for i in range(len(new_list)):
    new_list[i] = new_list[i].capitalize();
print(" ".join(new_list));

str6 = "I ekil gnimmargorp";
new_list = str6.split();
for i in range(len(new_list)):
    new_list[i]=new_list[i][::-1];
print(" ".join(new_list));

Sample_List = [[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]];

print(Sample_List[1][1]);
for i in range(len(Sample_List)-1):
    for j in range(len(Sample_List)-i-1):
        if Sample_List[j][1]>Sample_List[j+1][1]:
            Sample_List[j],Sample_List[j+1] = Sample_List[j+1],Sample_List[j];
print(Sample_List);
