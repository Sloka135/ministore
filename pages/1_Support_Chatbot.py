import streamlit as st
from openai import OpenAI

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬",
    layout="wide"
)

# --------------------------------------------------
# OPENAI CLIENT
# --------------------------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# --------------------------------------------------
# PRODUCT CATALOG
# --------------------------------------------------
STORE_CATALOG = """
MiniStore Product Catalog

1. Wireless Bluetooth Headphones
   Price: $79.99
   Description: Premium noise-cancelling headphones with immersive sound quality.

2. Smart Fitness Watch
   Price: $129.99
   Description: Track heart rate, steps, workouts, sleep, and notifications.

3. Premium Coffee Maker
   Price: $89.99
   Description: Brew café-style coffee every morning with ease.

4. Ergonomic Office Chair
   Price: $249.99
   Description: Maximum comfort and lumbar support for long work sessions.

5. Running Shoes Pro
   Price: $99.99
   Description: Lightweight running shoes designed for comfort and speed.

6. Leather Travel Backpack
   Price: $69.99
   Description: Stylish backpack with laptop compartment and premium finish.
"""

# --------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------
SYSTEM_PROMPT = f"""
You are the official customer support representative for MiniStore.

Your role is to provide professional, friendly, and accurate customer support.

You may ONLY answer questions related to:

• Products
• Product recommendations
• Product pricing
• Orders
• Order status
• Delivery and shipping
• Refunds
• Returns
• Payment methods
• Store policies

MiniStore Product Catalog:

{STORE_CATALOG}

Rules:

1. Stay focused on MiniStore support topics only.

2. If the user asks unrelated questions
   (sports, politics, coding, history, celebrities, etc.),
   politely respond:

   "I'm here to assist with MiniStore products,
   orders, delivery, refunds, returns, and payments.
   Please ask a store-related question."

3. Use product information from the catalog when answering.

4. Never invent products that are not listed.

5. Be concise, professional, and helpful.

6. If you do not know the answer,
   politely explain that the information is unavailable.
"""

# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------
st.title("💬 MiniStore Support Chatbot")

st.write(
    "Ask questions about products, orders, delivery, "
    "returns, refunds, and payment methods."
)

# --------------------------------------------------
# SESSION STATE FOR CHAT HISTORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------
prompt = st.chat_input(
    "Ask a MiniStore support question..."
)

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Build conversation
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3
        )

        assistant_reply = (
            response.choices[0]
            .message
            .content
        )

    except Exception:
        assistant_reply = (
            "MiniStore AI Support is currently unavailable. "
            "Please try again later."
        )

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)