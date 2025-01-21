import streamlit as st
from agents.coding_agent import ReflectionAgent
  

# Initialize ReflectionAgent
agent = ReflectionAgent()

# Configure Streamlit page
st.set_page_config(
    page_title="AI Coding Chatbot - Coding All You Need",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f9;
    }
    .message-user {
        background-color: black;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        text-align: left;
    }
    .message-bot {
        background-color: black;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        text-align: left;
    }
    .chat-history {
        max-height: 400px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 10px;
        background-color: black;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# App title and description
st.title("🤖 AI Coding Chatbot - Coding All You Need")
st.write("Ask me anything and I'll provide thoughtful responses with reflections.")

# Sidebar for configuration
st.sidebar.header("Agent Settings")
generation_prompt = st.sidebar.text_area(
    "Generation System Prompt",
    value="You are a programmer tasked with generating high-quality content for the user's requests.",
    height=150,
)
reflection_prompt = st.sidebar.text_area(
    "Reflection System Prompt",
    value="You are tasked with providing critique and suggestions to improve generated content.",
    height=150,
)
n_steps = st.sidebar.slider("Number of Reflection Steps", 1, 10, 3)



# Chat history display
st.markdown("### Chat History")
st.markdown('<div class="chat-history">', unsafe_allow_html=True)
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.markdown(f'<div class="message-user">👤 **You:** {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message-bot">🤖 **AI:** {message["content"]}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
# Main chat interface
st.markdown("### Code with the AI")
user_input = st.text_input("Type your message:", "")

if st.button("Send"):
    if user_input.strip():
        # Display user's message
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Generate AI response
        with st.spinner("Thinking..."):
            try:
                response = agent.run(
                    user_msg=user_input,
                    generation_system_prompt=generation_prompt,
                    reflection_system_prompt=reflection_prompt,
                    n_steps=n_steps,
                    verbose=0,
                )
                # Display AI's response
                st.session_state["messages"].append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
# Footer
st.markdown("---")
st.markdown(
    """
    **AI Chatbot** | Developed by [Waleed Ahmed](https://github.com/Ahmed546)  
    **LinkedIn** | [Waleed Ahmed](www.linkedin.com/in/waleedahmed003) 
    """
)
