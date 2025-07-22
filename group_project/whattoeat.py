import streamlit as st

# App Title
st.title("🍽️ What to Eat")

# Input Section
st.header("Tell us what you're craving!")

location = st.text_input("📍 Enter your location:")
budget = st.number_input("💸 What's your budget? (RM)", min_value=0.0, step=1.0)
preference = st.text_input("😋 What kind of food do you prefer?")
craving = st.text_input("🤤 Any specific craving?")
calories = st.number_input("🔥 Max calories?", min_value=0)
nutrients = st.text_input("🥦 Any nutrients you're focusing on? (e.g. protein, fiber)")

# Show user input summary
st.subheader("✅ Your Input Summary:")
st.write(f"**Location:** {location}")
st.write(f"**Budget:** RM{budget}")
st.write(f"**Preference:** {preference}")
st.write(f"**Craving:** {craving}")
st.write(f"**Calories:** {calories} kcal")
st.write(f"**Nutrients:** {nutrients}")

# Output Placeholder
if st.button("🍜 Show me what to eat"):
    # You will add real logic later; this is a placeholder
    st.success("Here's a recommendation for you!")
    st.write("**🍔 Food:** Grilled Chicken Wrap")
    st.write("**💸 Price:** RM12.50")
    st.write("**📍 Nearest Store:** Healthy Bites, Jalan ABC")
    st.write("**⭐ Rating:** 4.5/5")
    st.write("**🔥 Calories:** 450 kcal")