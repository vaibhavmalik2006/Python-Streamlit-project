import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", layout="centered")

st.title("🧪 Scientific Calculator")

# Input
expression = st.text_input("Enter expression (e.g., sin(30) + log(100)): ", "")

# Help note
with st.expander("ℹ️ Supported Functions"):
    st.markdown("""
    - **Basic**: `+`, `-`, `*`, `/`, `**` (power), `%`
    - **Trigonometry**: `sin(x)`, `cos(x)`, `tan(x)` (x in degrees)
    - **Inverse Trigonometry**: `asin(x)`, `acos(x)`, `atan(x)`
    - **Logarithms**: `log(x)` (base 10), `ln(x)` (natural log)
    - **Square root**: `sqrt(x)`
    - **Constants**: `pi`, `e`
    """)

# Safe dictionary for eval
safe_dict = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "asin": lambda x: math.degrees(math.asin(x)),
    "acos": lambda x: math.degrees(math.acos(x)),
    "atan": lambda x: math.degrees(math.atan(x)),
    "log": math.log10,
    "ln": math.log,
    "sqrt": math.sqrt,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "round": round,
    "__builtins__": {}
}

# Evaluate button
if st.button("Calculate"):
    try:
        result = eval(expression, {"__builtins__": None}, safe_dict)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")
