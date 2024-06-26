import streamlit as st
from textsum.summarize import Summarizer

def main():
    st.title("Book-ML📖")

    # Input text area for user to enter text
    user_input = st.text_area("Drop your text here, and let the magic happen! ✨")

    if st.button("Summarize 📚"):
        if user_input:
            # Summarize the user input
            summary = summarize_text(user_input)

            # Create containers for the original and summarized text
            with st.container():
                st.subheader("Original Text:")
                st.text(user_input)

            with st.container():
                st.subheader("Summarized Text:")
                st.text(summary)
        else:
            st.warning("Please enter some text to summarize.")

def summarize_text(text):
    model_name = "pszemraj/led-base-book-summary"
    summarizer = Summarizer(
        model_name_or_path=model_name,
        token_batch_length=4096
    )
    summarized_text = summarizer.summarize_string(text)
    return summarized_text


# Create or connect to the SQLite database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a user_data table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        weight INTEGER,
        activity_level TEXT,
        climate TEXT,
        day INTEGER,
        water_intake INTEGER
    )
''')
conn.commit()

def get_personalized_recommendation(user_data):
    # Dummy polynomial regression model for demonstration purposes
    X = user_data[['age', 'weight', 'day']]
    y = user_data['water_intake']

    degree = 2  # You can adjust the degree based on your data
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X, y)

    user_input = user_data[['age', 'weight', 'day']]
    recommendation = model.predict(user_input)

    # Make a recommendation based on the prediction (replace with your actual logic)
    if recommendation[-1] > 2000:
        result = "You are doing well in maintaining hydration!"
    else:
        result = "Consider adjusting your water intake for better hydration."

    return result


if __name__ == "__main__":
    main()
