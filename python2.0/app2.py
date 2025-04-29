import streamlit as st
import sqlite3

# --- DB Setup ---
def create_db():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
    ''')
    conn.commit()
    conn.close()

def add_account(name, balance):
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', (name, balance))
    conn.commit()
    conn.close()

def get_all_accounts():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute('SELECT * FROM accounts')
    data = c.fetchall()
    conn.close()
    return data

def update_balance(acc_no, amount, is_deposit=True):
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute('SELECT balance FROM accounts WHERE acc_no=?', (acc_no,))
    result = c.fetchone()
    if result:
        new_balance = result[0] + amount if is_deposit else result[0] - amount
        if new_balance < 0:
            conn.close()
            return False
        c.execute('UPDATE accounts SET balance=? WHERE acc_no=?', (new_balance, acc_no))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

# --- UI Logic ---
def main():
    st.title("🏦 Bank Management System")
    create_db()

    menu = ["Create Account", "View Accounts", "Deposit", "Withdraw"]
    choice = st.sidebar.selectbox("Select Action", menu)

    if choice == "Create Account":
        st.subheader("Create a New Bank Account")
        name = st.text_input("Account Holder Name")
        balance = st.number_input("Initial Deposit", min_value=0.0, step=10.0)
        if st.button("Create"):
            add_account(name, balance)
            st.success(f"Account created for {name} with ₹{balance:.2f}")

    elif choice == "View Accounts":
        st.subheader("All Bank Accounts")
        data = get_all_accounts()
        if data:
            st.table(data)
        else:
            st.info("No accounts found.")

    elif choice == "Deposit":
        st.subheader("Deposit Money")
        acc_no = st.number_input("Account Number", step=1)
        amount = st.number_input("Amount to Deposit", min_value=0.0, step=10.0)
        if st.button("Deposit"):
            if update_balance(acc_no, amount, is_deposit=True):
                st.success(f"Deposited ₹{amount:.2f} to Account #{acc_no}")
            else:
                st.error("Account not found.")

    elif choice == "Withdraw":
        st.subheader("Withdraw Money")
        acc_no = st.number_input("Account Number", step=1)
        amount = st.number_input("Amount to Withdraw", min_value=0.0, step=10.0)
        if st.button("Withdraw"):
            if update_balance(acc_no, amount, is_deposit=False):
                st.success(f"Withdrew ₹{amount:.2f} from Account #{acc_no}")
            else:
                st.error("Insufficient balance or account not found.")

if __name__ == '__main__':
    main()


