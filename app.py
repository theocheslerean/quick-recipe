import streamlit as st
import streamlit.components.v1 as components
import openai

openai.api_key = st.secrets["openai_api_key"]
google_adsense_key =  st.secrets["google_adsense_key"]


st.set_page_config(page_title="QuickRecipe", page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)

# Streamlit app title and description
st.title("QuickRecipe")
st.write("Enter the ingredients you have and your preferences, and we'll suggest a recipe!")

# User input
ingredients = st.text_area("Enter the ingredients you have (comma-separated)", "")
meal_type = st.selectbox("Select meal type", ["Breakfast", "Lunch", "Dinner"])
diet_preference = st.selectbox("Select dietary preference", ["Any", "Vegetarian", "Gluten-free"])
language = st.selectbox("Select language", ["English", "German", "Romanian"])

col1, col2, _ = st.columns(3, gap='medium')

with col1:
    getrecipe_button = st.button("Get Recipe")
with col2:
    getfreaky_button = st.button("Feeling freaky today")

suggested_subheader = st.empty()
recipe_space = st.empty()

    # Generate recipe suggestion
if getrecipe_button:
        
        if ingredients:
            
            lang_suffix = f'Write the instructions in {language.lower()}' if language.lower() != 'english' else ''
            
            prompt = f"You are a world renowned cook working at a 3-star Michelin restaurant. I am your wife and you like to make me happy by cooking simple stuff for me in your free time. Since you don't have time today I will give you a list of ingredients that are still in our fridge and you will give me a simple recipe that you believe I can make and which I will enjoy eating. I have the following ingredients: {ingredients}. I'd love to eat something for {meal_type.lower()} that's {diet_preference.lower()} using these ingredients. Write as a short paragraph, don't use bullet points, and try not to give me bad advice that will make me sick. Try to keep it short and not go overboard with complicated stuff.{lang_suffix}"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=500
            )
            suggested_subheader.subheader("Suggested Recipe:")   
            suggested_recipe = response.choices[0].text.strip()
            recipe_space.write(suggested_recipe)
        else:
            st.warning("Please enter the ingredients you have.")

if getfreaky_button:
        
        if ingredients:
            
            lang_suffix = f'Write the instructions in {language.lower()}' if language.lower() != 'english' else ''
            
            prompt = f"You are a world renowned cook, always with a joke prepared. working at a 3-star Michelin restaurant. I am your wife and you like to make me happy by cooking simple stuff for me in your free time. Since you don't have time today I will give you a list of ingredients that are still in our fridge and you will give me a simple recipe that you believe I can make and which I will enjoy eating. I have the following ingredients: {ingredients}. I'd love to eat something for {meal_type.lower()} that's {diet_preference.lower()} using these ingredients and maybe one or two extra ones that you should propose that I buy before I prepare the food. Write me at the start a list of all ingredients that I need for this special recipe. Give me something that you think suits my ingredients, don't use bullet points, and try not to give me bad advice that will make me sick. Try to keep it short and not go overboard with complicated stuff. And be funny with your explanations. {lang_suffix}"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=500
            )
            suggested_subheader.subheader("Suggested Recipe:")   
            suggested_recipe = response.choices[0].text.strip()
            recipe_space.write(suggested_recipe)
        else:
            st.warning("Please enter the ingredients you have.")

HtmlFile = open('adsense.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(f"""
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-{google_adsense_key}"
     crossorigin="anonymous"></script>
<!-- quickrecipead -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-{google_adsense_key}"
     data-ad-slot="2301564086"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({{}});
</script>""", height=300)