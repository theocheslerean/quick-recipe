import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Streamlit app title and description
st.title("Recipe Suggestion App")
st.write("Enter the ingredients you have and your preferences, and we'll suggest a recipe!")

# User input
ingredients = st.text_area("Enter the ingredients you have (comma-separated)", "")
meal_type = st.selectbox("Select meal type", ["Breakfast", "Lunch", "Dinner"])
diet_preference = st.selectbox("Select dietary preference", ["Any", "Vegetarian", "Gluten-free"])
language = st.selectbox("Select language", ["English", "German", "Romanian"])

# Generate recipe suggestion
if st.button("Get Recipe"):
    
    if ingredients:
        
        lang_suffix = f'Write the instructions in {language.lower()}' if language.lower() != 'english' else ''
        
        prompt = f"You are a world renowned cook working at a 3-star Michelin restaurant. I am your wife and you like to make me happy by cooking simple stuff for me in your free time. Since you don't have time today I will give you a list of ingredients that are still in our fridge and you will give me a simple recipe that you believe I can make and which I will enjoy eating. I have the following ingredients: {ingredients}. I'd love to eat something for {meal_type.lower()} that's {diet_preference.lower()} using these ingredients. Write as a short paragraph, don't use bullet points, and try not to give me bad advice that will make me sick. Try to keep it short and not go overboard with complicated stuff.{lang_suffix}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        suggested_recipe = response.choices[0].text.strip()
        st.subheader("Suggested Recipe:")
        st.write(suggested_recipe)
    else:
        st.warning("Please enter the ingredients you have.")
