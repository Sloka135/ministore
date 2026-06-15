import streamlit as st

# ------------------------------------------------
# Page Config
# ------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ------------------------------------------------
# Custom CSS
# ------------------------------------------------
st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding:40px;
    border-radius:15px;
    color:white;
    text-align:center;
    margin-bottom:25px;
}

.product-card {
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.product-title {
    font-size:20px;
    font-weight:bold;
}

.product-price {
    color:#10b981;
    font-size:22px;
    font-weight:bold;
}

/* Floating Support Button */
.support-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #2563eb;
    color: white;
    padding: 14px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 999;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

.support-btn:hover {
    background-color: #1d4ed8;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# Products
# ------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 89.99,
        "description": "Noise-cancelling wireless headphones.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch Pro",
        "price": 149.99,
        "description": "Fitness tracking and notifications.",
        "category": "Electronics"
    },
    {
        "name": "Classic Backpack",
        "price": 49.99,
        "description": "Durable backpack for daily use.",
        "category": "Fashion"
    },
    {
        "name": "Running Shoes",
        "price": 79.99,
        "description": "Comfortable lightweight running shoes.",
        "category": "Fashion"
    },
    {
        "name": "Coffee Maker",
        "price": 119.99,
        "description": "Automatic coffee machine.",
        "category": "Home"
    },
    {
        "name": "Desk Lamp",
        "price": 34.99,
        "description": "LED desk lamp with brightness control.",
        "category": "Home"
    }
]

# ------------------------------------------------
# Cart State
# ------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ------------------------------------------------
# Sidebar
# ------------------------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.selectbox(
    "Categories",
    categories
)

st.sidebar.markdown("---")

cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.write(f"Items: {len(st.session_state.cart)}")
st.sidebar.write(f"Total: ${cart_total:.2f}")

# ------------------------------------------------
# Hero
# ------------------------------------------------
st.markdown("""
<div class='hero'>
<h1>🛍️ MiniStore</h1>
<p>Your One-Stop Shop For Quality Products</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Featured Products")

# ------------------------------------------------
# Product Filter
# ------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# ------------------------------------------------
# Product Grid
# ------------------------------------------------
for i in range(0, len(filtered_products), 3):

    cols = st.columns(3)

    for col, product in zip(cols, filtered_products[i:i+3]):

        with col:

            st.markdown(f"""
            <div class='product-card'>
                <div class='product-title'>
                    {product["name"]}
                </div>
                <p>{product["description"]}</p>
                <div class='product-price'>
                    ${product["price"]}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "Add to Cart",
                key=product["name"]
            ):
                st.session_state.cart.append(product)
                st.success("Added to cart")

# ------------------------------------------------
# Floating Chat Button
# ------------------------------------------------
st.markdown("""
<a class="support-btn"
href="/Support_Chatbot"
target="_self">
💬 Support Chat
</a>
""", unsafe_allow_html=True)