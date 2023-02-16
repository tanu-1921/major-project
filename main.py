from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


#-----------------------------------------------------------------------------------------------------------------------



#dataset
diabetes_dataset = pd.read_csv("correct.csv")


x=diabetes_dataset.drop(columns="Outcome",axis=1)
y=diabetes_dataset["Outcome"]
scaler=StandardScaler()
scaler.fit(x)
standardized_data=scaler.transform(x)
x=standardized_data
y=diabetes_dataset["Outcome"]
x_train ,x_test ,y_train ,y_test =train_test_split(x,y,stratify=y,random_state=2)
classifier=svm.SVC(kernel="linear")
classifier.fit(x_train,y_train)


#----------------------------------------------------------------------------------------------------------------------------------

def myrest():
    for i in root.winfo_children():
        if isinstance(i,Entry):
            i.delete(0,"end")
    lableout10.destroy()
    
    if co >0:
        lableout11.destroy()
    else:
        lableout100.destroy()


root=Tk()
#root work
root.minsize(680,550)
root.maxsize(680,550)
#root.geometry("650x550")
root.configure(background="#999999")



# heading part
heading=Label(root,text="Disease Prediction",font=("Arial", 25), foreground="black",background="#999999",padx=15,pady=15)
heading.grid(row=0,column=1)

name=Label(root,text="Enter Patient Name",font=("Arial", 18), foreground="black",background="#999999",padx=15,pady=15)
name.grid(row=1,column=0)
e=Entry(root, width = 20,font=("Arial",14))
e.grid(row=1,column=1)



#lable inputs
age=Label(root,text="Enter your Age   ",font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
age.grid(row=2,column=0)
question5 = Entry(root,width=20,font=("Arial",14))
question5.grid(row=2, column=1)

lableglucose=Label(root,text="Glucose             ",font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
lableglucose.grid(row=3,column=0)
question1 = Entry(root,width=20,font=("Arial",14))
question1.grid(row=3, column=1)

lablebp=Label(root,text="Blood Pressure  ",font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
lablebp.grid(row=4,column=0)
question2 = Entry(root,width=20,font=("Arial",14))
question2.grid(row=4, column=1)

lableinsulin=Label(root,text="Insulin                ",font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
lableinsulin.grid(row=5,column=0)
question3 = Entry(root,width=20,font=("Arial",14))
question3.grid(row=5, column=1)

lablebmi=Label(root,text="BMI                    ",font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
lablebmi.grid(row=7,column=0)
question4=Entry(root,width=20,font=("Arial",14))
question4.grid(row=7,column=1)




#lable for outputs
lableout1=Label(root,text="The person is                ",font=("Arial",16),foreground="red",background="#999999",padx=15,pady=15)
lableout1.grid(row=8,column=0)
lableout2=Label(root,text="Percentage of Accuracy",font=("Arial",16),foreground="red",background="#999999",padx=15,pady=15)
lableout2.grid(row=9,column=0)



#----------------------------------------------------------------------------------------------------------------------------




def submit():
    global lableout100 ,lableout11 , lableout10 , co
    input_data=(question1.get(),question2.get(),question3.get(),question4.get(),question5.get())
    count=0
    for i in input_data:
        k=str(i)
        if len(k)==0:
            count+=1
    if count>0:
        messagebox.showwarning("Warning","Please fill all the fields")
    else:
        input_data_as_nupyarray= np.asarray(input_data)
        input_data_reshaped=input_data_as_nupyarray.reshape(1,-1)
        std_data=scaler.transform(input_data_reshaped)
        prediction=classifier.predict(std_data)
        co=0
        if prediction[0]==1:
            lableout11=Label(root,text="Diabetic",font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
            lableout11.grid(row=8,column=1)
            co+=1
            #for accuracy score
            x_train_prediction=classifier.predict(x_train)
            training_data_accuracy = accuracy_score(x_train_prediction,y_train)
            printaccuracy=round( training_data_accuracy,4)*100
            lableout10=Label(root,text=printaccuracy,font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
            lableout10.grid(row=9,column=1)
        else:
            lableout100=Label(root,text="Nondiabetic",font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
            lableout100.grid(row=8,column=1)
    
            #for accuracy score
            x_train_prediction=classifier.predict(x_train)
            training_data_accuracy = accuracy_score(x_train_prediction,y_train)
            printaccuracy=round( training_data_accuracy,4)*100
            lableout10=Label(root,text=printaccuracy,font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
            lableout10.grid(row=9,column=1)


#------------------------------------------------------------------------------------------------------------------------------------

#reset and submit button
btn1=Button(root,text="Reset",font=("Arial",12),foreground="white",background="red",padx=5,pady=5,width=10,command=myrest)
btn1.grid(row=8,column=3)
btn2=Button(root,text="submit",font=("Arial",12),foreground="Black",background="#72fc56",padx=5,pady=5,command=submit,width=10)
btn2.grid(row=9,column=3)


root.mainloop()

