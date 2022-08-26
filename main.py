from pytrials.client import ClinicalTrials
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
import pytrials


ct = ClinicalTrials()
print(ct.study_fields)
#Get 50 Studies related to Medical Devices in JSON
# json_studies = ct.get_full_studies(search_expr="Medical+Devices", max_studies=50)
# print(json_studies)
#Get the NCTId, Condition and Breaf titile fields from 500 studies related to medical devices in CSV
medical_devices_fields = ct.get_study_fields(
    search_expr="Medical+Devices",
    fields = ["NCTId","Condition","BriefTitle","StartDate","CompletionDate"],
    max_studies=500,
    fmt="csv"
)
# print(medical_devices_fields)
#Get the counts of studies related to medical devices
#ClincialTrials limits API queries to 1000 recors
#Count of studies may be useful to build loops when you want to retreive more than 1000 studies


study_count = ct.get_study_count(search_expr="Medical+Devices")
print(study_count)
#read the csv in Pandas
import pandas as pd

test = pd.DataFrame.from_records(medical_devices_fields[1:],columns=medical_devices_fields[0])

# print(test)

def Get_API_data(search_string,field_options):
    print("not done")
    print(search_string)
    print(field_options)
    medical_devices_fields2 = ct.get_study_fields(
        search_expr=search_string,
        fields=field_options,
        max_studies=500,
        fmt="csv"
    )
    print(medical_devices_fields2)

#create Object
root = Tk()

#adjust the size
root.geometry("200x200")
show_list = []
#change label text
def show():
    if clicked.get() in show_list:
        return
    else:
        show_list.append(clicked.get())
        label.config( text = show_list)
        print(show_list)

#create a search bar
search_entry = tk.Entry(root)
search_entry.pack()

#dropdown menu options
options = ct.study_fields

# datatype of menu text
clicked = StringVar()
search_entry0 = StringVar()

#initial menu setup
clicked.set( "NCTId" )

#create dropdown menu
drop = OptionMenu( root, clicked, *options)
drop.pack()

#Create button, it will change label text
Add_Field = Button( root, text = "Add Field", command = show ).pack()

#Create label
label = Label( root, text = "  " )
label.pack()

Search_and_save = Button(root, text = "search and save", command = Get_API_data(field_options=show_list,search_string=search_entry.get()))
Search_and_save.pack()
#Create button for publishin

#execute tkinter
root.mainloop()