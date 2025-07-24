import streamlit as st
from Bank import Bank  # Assuming the class above is in bank.py

st.title("🏦 Welcome to Simple Bank System")

bank = Bank()

menu = ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Create Account":
    st.header("Create Your Account")
    name = st.text_input("Enter Your Name")
    age = st.number_input("Enter Your Age", min_value=0)
    email = st.text_input("Enter Your Email")
    pin = st.text_input("Set 4-digit PIN", type="password")

    if st.button("Create Account"):
        result = bank.create_account(name, age, email, pin)
        if "Account created successfully" in result:
            st.success(result)
            st.subheader(f"Welcome, {name}! 🎉")
        else:
            st.error(result)

elif choice == "Deposit":
    st.header("Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1.0)

    if st.button("Deposit"):
        st.info(bank.deposit_money(acc, int(pin), amount))

elif choice == "Withdraw":
    st.header("Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1.0)

    if st.button("Withdraw"):
        st.info(bank.withdraw_money(acc, int(pin), amount))

elif choice == "Show Details":
    st.header("Show Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        details = bank.show_details(acc, int(pin))
        if isinstance(details, dict):
            st.json(details)
        else:
            st.error(details)

elif choice == "Update Details":
    st.header("Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        st.success(bank.update_details(acc, int(pin), name, email, new_pin))

elif choice == "Delete Account":
    st.header("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        st.warning(bank.delete_account(acc, int(pin)))
