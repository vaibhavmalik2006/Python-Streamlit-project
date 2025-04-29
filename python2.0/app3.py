import streamlit as st
import sqlite3
from datetime import date

# --- DB Setup ---
def init_db():
    conn = sqlite3.connect('travel.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            traveler_name TEXT NOT NULL,
            destination TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT,
            cost REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_booking(name, destination, start_date, end_date, cost):
    conn = sqlite3.connect('travel.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO bookings (traveler_name, destination, start_date, end_date, cost)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, destination, start_date, end_date, cost))
    conn.commit()
    conn.close()

def get_all_bookings():
    conn = sqlite3.connect('travel.db')
    c = conn.cursor()
    c.execute('SELECT * FROM bookings')
    data = c.fetchall()
    conn.close()
    return data

def filter_bookings(keyword):
    conn = sqlite3.connect('travel.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bookings WHERE traveler_name LIKE ? OR destination LIKE ?", 
              (f'%{keyword}%', f'%{keyword}%'))
    data = c.fetchall()
    conn.close()
    return data

# --- App UI ---
def main():
    st.set_page_config(page_title="✈️ Travel Management", layout="centered")
    st.title("✈️ Travel Management System")
    init_db()

    menu = ["Add Booking", "View Bookings", "Search Bookings"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Add Booking":
        st.subheader("➕ Add New Travel Booking")
        name = st.text_input("Traveler Name")
        destination = st.text_input("Destination")
        start_date = st.date_input("Start Date", value=date.today())
        end_date = st.date_input("End Date", value=date.today())
        cost = st.number_input("Cost (₹)", min_value=0.0, step=100.0)

        if st.button("Add Booking"):
            add_booking(name, destination, str(start_date), str(end_date), cost)
            st.success(f"Booking for {name} to {destination} added successfully!")

    elif choice == "View Bookings":
        st.subheader("📋 All Bookings")
        data = get_all_bookings()
        if data:
            st.table(data)
        else:
            st.info("No bookings found.")

    elif choice == "Search Bookings":
        st.subheader("🔍 Search by Traveler or Destination")
        keyword = st.text_input("Enter keyword")
        if keyword:
            results = filter_bookings(keyword)
            if results:
                st.table(results)
            else:
                st.warning("No matching bookings found.")

if __name__ == '__main__':
    main()
