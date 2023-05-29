
from dotenv import load_dotenv
import streamlit as st
import openai
import credentials

openai.api_key = credentials.api_key


def generate_product_description(product_name):
    prompt = f"Generate a product description for {product_name}."
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        description = response.choices[0].text.strip()
    except Exception as ex:
        print("error:", ex)
        return "", []
    return description, response.choices



def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")

    # upload file
    suggested_product_description, choices = generate_product_description("Brushed Silver Tungsten Ring")


if __name__ == '__main__':
    main()


