import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import csv

st.set_page_config(page_title="Student Management System",page_icon=":bar_chart:",layout="wide")

def load_sub():
    try:
        with open("subjects.json","r") as f:
            return json.load(f)
        
    except (FileNotFoundError,json.JSONDecodeError):
        return []
    
def save_sub(subjects):
    with open("subjects.json","w") as f:
        json.dump(subjects,f,indent=4)

def load_std_data(file_path):
   try:
      with open(file_path,"r") as f:
         return json.load(f)
      
   except (FileNotFoundError,json.JSONDecodeError):
      return []
   
def save_std_data(data):
   with open("data.json","w") as f:
      json.dump(data,f,indent=4)
   

st.title("Student Management System")
st.write("Welcome to the Student Management System. This application allows you to manage student records efficiently.")


menu=st.sidebar.selectbox('Menu',["Dashboard","Manage Subjects","Add Student","View Student","Search Student","Update Student","Delete Student","Top 3 Students","Subject Topper","Export data to CSV"])

if menu=="Manage Subjects":
   st.header("Manage Subjects")
   subjects=load_sub()
   new_subject=st.text_input("Enter new subject : ")

   if st.button("Add Subject"):

        new_subject = new_subject.strip()

        if not new_subject:

            st.error("Subject name cannot be empty!")

        elif new_subject in subjects:

            st.warning("Subject already exists")

        else:

             subjects.append(new_subject)

             save_sub(subjects)

             students=load_std_data("data.json")

             for student in students:

                 student["marks"][new_subject]=0

             save_std_data(students)

             st.success("Subject added successfully")

             st.rerun()
      

   st.subheader("Existing Subjects")
   if subjects:
      for sub in subjects:
         col1,col2=st.columns([4,1])
         col1.write(sub)
         if col2.button("Delete",key=f"delete_{sub}"):
            subjects.remove(sub)
            save_sub(subjects)

            students=load_std_data("data.json")

            for student in students:

               if sub in student["marks"]:

                  del student["marks"][sub]

            save_std_data(students)

            st.success("Subject deleted successfully")
            st.rerun()
   else:
      st.info("NO subjects found.")    

elif menu=="Add Student":

   st.header("+ Add Student")

   subjects=load_sub()

   if not subjects:

      st.warning(
         "No subjects found. Please add subjects first."
      )

   else:

      std_id=st.text_input(
         "Enter student ID : "
      )

      std_name=st.text_input(
         "Enter student name : "
      )

      marks={}

      for sub in subjects:

         marks[sub]=st.number_input(
            f"Enter marks for {sub} : ",
            min_value=0,
            max_value=100
         )

      if st.button("Add Student"):

         if not std_id.strip():

            st.error(
               "Student ID cannot be empty!"
            )

         elif not std_name.strip():

            st.error(
               "Student Name cannot be empty!"
            )

         else:

            students=load_std_data(
               "data.json"
            )

            exists=False

            for std in students:

               if std["id"]==std_id:

                  exists=True
                  break

            if exists:

               st.error(
                  "Student ID already exists!"
               )

            else:

               student={
                  "id":std_id,
                  "name":std_name,
                  "marks":marks
               }

               students.append(
                  student
               )

               save_std_data(
                  students
               )

               st.success(
                  "Student record added successfully"
               )

    

elif menu=="View Student":

   st.header("View Student")

   students=load_std_data("data.json")

   subjects=load_sub()

   if not students:

      st.info("No student records found. Please add students first.")

   else:

      table_data=[]

      for student in students:

         row={

            "ID":student["id"],

            "Name":student["name"]
         }

         total=0

         for sub in subjects:

            mark=student["marks"].get(sub,0)

            row[sub]=mark

            total+=mark

         avg=(total/len(subjects) )

         row["Average"]=round(avg,2)

         table_data.append(row)

      df=pd.DataFrame(table_data)

      st.dataframe(df,width="stretch")
      


elif menu=="Search Student":

   st.header("Search Student")

   std_id=st.text_input("Enter student ID to search : ")

   if st.button("Search"):

      students=load_std_data("data.json")

      found=False

      for student in students:

         if student["id"]==std_id:

            st.success("Student record found")

            st.write(f"**ID:** {student['id']}")

            st.write(f"**Name:** {student['name']}")

            st.subheader("Marks")

            total=0

            for subject,mark in student["marks"].items():

               st.write(f"**{subject}:** {mark}")

               total+=mark

            avg=(total/len(student["marks"]))

            st.write(f"**Average:** {avg:.2f}")


            fig,ax=plt.subplots(figsize=(5,3))

            subjects_graph=list(student["marks"].keys())

            marks_graph=list(student["marks"].values())

            bars=ax.bar(subjects_graph,marks_graph)

            ax.bar_label(bars)
            ax.set_ylim(0,max(marks_graph) + 15)

            ax.set_title(f"{student['id']} - {student['name']}")

            ax.set_ylabel("Marks")

            plt.grid(axis="y",linestyle="--",alpha=0.5)

            st.pyplot(fig)

            found=True

            break

      if not found:

         st.error("Student record not found")


elif menu=="Update Student":

   st.header("Update Student")

   students=load_std_data("data.json")

   std_id=st.text_input("Enter Student ID")

   if st.button("Load Student"):

      found=False

      for student in students:

         if student["id"]==std_id:

            st.session_state["student"] = student

            found=True

            break

      if not found:

         st.error("Student not found!")

   if "student" in st.session_state:

      student = st.session_state["student"]

      new_name = st.text_input("Student Name",value=student["name"])

      new_marks={}

      for subject,mark in student["marks"].items():

         new_marks[subject] = st.number_input(f"{subject}",min_value=0,max_value=100,value=int(mark))

      if st.button("Update Student"):

         for std in students:

            if std["id"] == student["id"]:

               std["name"] = new_name

               std["marks"] = new_marks

               break

         save_std_data(students)

         st.success("Student Updated Successfully!")

elif menu=="Delete Student":

   st.header("Delete Student")

   students=load_std_data("data.json")

   if not students:

      st.info("No student records found.")

   else:

      student_ids=[student["id"] for student in students]

      selected_id=st.selectbox("Select Student ID",student_ids)

      if st.button("Delete Student"):

         students=[student for student in students if student["id"]!=selected_id]

         save_std_data(students)

         st.success("Student Deleted Successfully!")

         st.rerun()


elif menu=="Dashboard":

   st.header("📊 Dashboard")

   students=load_std_data("data.json")

   if not students:

      st.info("No student records found.")

   else:

      total_students=len(students)

      class_avg=0

      topper_name=""

      topper_id=""

      topper_avg=0

      total_avg_sum=0

      for student in students:

         marks=list(student["marks"].values())

         avg=sum(marks)/len(marks)

         total_avg_sum+=avg

         if avg>topper_avg:

            topper_avg=avg

            topper_name=student["name"]

            topper_id=student["id"]

      class_avg=(total_avg_sum/total_students)

      col1,col2,col3=st.columns(3)

      col1.metric("Total Students",total_students)

      col2.metric("Class Average",f"{class_avg:.2f}")

      col3.metric("Topper Avg",f"{topper_avg:.2f}")

      st.success(f"🏆 Topper ID: {topper_id} | Name: {topper_name}")

      subjects=load_sub()

      if subjects:

         subject_avg=[]

         for subject in subjects:

            total=0

            count=0

            for student in students:

               total+=student["marks"].get(subject,0)

               count+=1

            subject_avg.append(total/count)

         fig,ax=plt.subplots(figsize=(5,3))

         bars=ax.bar(subjects,subject_avg)

         ax.bar_label(bars,fmt="%.1f")

         ax.set_ylim(0,max(subject_avg) + 15)

         ax.set_title("Subject-wise Average Marks")

         ax.set_ylabel("Average Marks")

         plt.grid(axis="y",linestyle="--",alpha=0.5)

         st.pyplot(fig)



elif menu=="Top 3 Students":

   st.header("🏆 Top 3 Students")

   students=load_std_data("data.json")

   if not students:

      st.info("No student records found.")

   else:

      rankings=[]

      for student in students:

         marks=list(student["marks"].values())

         avg=sum(marks)/len(marks)

         rankings.append((student["id"],student["name"],avg))

      rankings.sort(key=lambda x:x[2],reverse=True)

      for i,student in enumerate(rankings[:3],start=1):

         st.write(
            f"{i}. ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Avg: {student[2]:.2f}"
         )


elif menu=="Subject Topper":

   st.header("📚 Subject Topper")

   students=load_std_data("data.json")

   subjects=load_sub()

   if not students:

      st.info("No student records found.")

   else:

      for subject in subjects:

         topper_name=""

         topper_id=""

         highest_mark=-1

         for student in students:

            mark=student["marks"].get(subject,0)

            if mark>highest_mark:

               highest_mark=mark

               topper_name=student["name"]

               topper_id=student["id"]

         st.success(
            f"{subject} → "
            f"ID: {topper_id} | "
            f"Name: {topper_name} | "
            f"Marks: {highest_mark}"
         )


elif menu=="Export data to CSV":

   st.header("📄 Export CSV")

   students=load_std_data("data.json")

   subjects=load_sub()

   if not students:

      st.info("No student records found.")

   else:

      csv_data=[]

      for student in students:

         row={

            "ID":student["id"],

            "Name":student["name"]
         }

         total=0

         for subject in subjects:

            mark=student["marks"].get(subject,0)

            row[subject]=mark

            total+=mark

         avg=(total/len(subjects))

         row["Average"]=round(avg,2)

         csv_data.append(row)

      df=pd.DataFrame(csv_data)

      csv=df.to_csv(index=False)

      st.download_button(

         label="Download CSV",

         data=csv,

         file_name="students.csv",

         mime="text/csv"
         )
 