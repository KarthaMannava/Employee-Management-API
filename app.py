import streamlit as st
import pandas as pd
from db import get_connection

st.set_page_config(page_title="Employee CRUD App", layout="centered")
st.title("👨‍💼 Employee Management System")

conn = get_connection()
cursor = conn.cursor()

# ---------------- CREATE ----------------
st.subheader("➕ Add Employee")

with st.form("add_employee"):
    name = st.text_input("Employee Name")
    email = st.text_input("Email")
    department = st.text_input("Department")
    salary = st.number_input("Salary", min_value=0.0, step=1000.0)
    submitted = st.form_submit_button("Add Employee")

    if submitted:
        cursor.execute(
            """
            INSERT INTO employee (emp_name, email, department, salary)
            VALUES (%s, %s, %s, %s)
            """,
            (name, email, department, salary)
        )
        conn.commit()
        st.success("Employee added successfully!")

# ---------------- READ ----------------
st.subheader("📋 Employee List")

cursor.execute("SELECT * FROM employee ORDER BY emp_id")
rows = cursor.fetchall()

df = pd.DataFrame(
    rows,
    columns=["ID", "Name", "Email", "Department", "Salary", "Created At"]
)

st.dataframe(df, use_container_width=True)

# ---------------- UPDATE ----------------
st.subheader("✏️ Update Employee")

emp_ids = df["ID"].tolist()
selected_id = st.selectbox("Select Employee ID", emp_ids)

if selected_id:
    cursor.execute("SELECT * FROM employee WHERE emp_id = %s", (selected_id,))
    emp = cursor.fetchone()

    with st.form("update_employee"):
        u_name = st.text_input("Name", emp[1])
        u_email = st.text_input("Email", emp[2])
        u_department = st.text_input("Department", emp[3])
        u_salary = st.number_input("Salary", value=float(emp[4]))
        update_btn = st.form_submit_button("Update")

        if update_btn:
            cursor.execute(
                """
                UPDATE employee
                SET emp_name=%s, email=%s, department=%s, salary=%s
                WHERE emp_id=%s
                """,
                (u_name, u_email, u_department, u_salary, selected_id)
            )
            conn.commit()
            st.success("Employee updated!")

# ---------------- DELETE ----------------
st.subheader("🗑️ Delete Employee")

del_id = st.selectbox("Select Employee to Delete", emp_ids, key="delete")

if st.button("Delete Employee"):
    cursor.execute("DELETE FROM employee WHERE emp_id = %s", (del_id,))
    conn.commit()
    st.warning("Employee deleted!")

cursor.close()
conn.close()
