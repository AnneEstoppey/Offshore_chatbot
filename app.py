import streamlit as st
from llama_index.core import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)
from langchain.schema import(SystemMessage, HumanMessage, AIMessage)


def init_page() -> None:
  """Initialize the page."""
  st.set_page_config(
    page_title="Personal Chatbot"
  )
  st.header("Personal Chatbot")
  st.sidebar.title("Options")


def select_llm() -> LlamaCPP:
  """Select the LLM model."""
  return LlamaCPP(
    model_path="./data/llm/llama-2-7b-chat.Q2_K.gguf",
    temperature=0.1,
    max_new_tokens=500,
    context_window=3900,
    generate_kwargs={},
    model_kwargs={"n_gpu_layers":1},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True,
  )


def init_messages() -> None:
  """Initialize the messages."""
  clear_button = st.sidebar.button("Clear Conversation", key="clear")
  if clear_button or "messages" not in st.session_state:
    st.session_state.messages = [
      SystemMessage(
        content="you are a helpful AI assistant. Write your answer in markdown format."
      )
    ]


def get_answer(llm, messages) -> str:
  """Get the answer from the LLM model."""
  response = llm.complete(messages)
  return response.text


def main() -> None:
  """Main function."""
  init_page()
  llm = select_llm()
  init_messages()

  if user_input := st.chat_input("Input your question!"):
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Bot is typing ..."):
      answer = get_answer(llm, user_input)
      print(answer)
    st.session_state.messages.append(AIMessage(content=answer))
    
  messages = st.session_state.get("messages", [])
  for message in messages:
    if isinstance(message, AIMessage):
      with st.chat_message("assistant"):
        st.markdown(message.content)
    elif isinstance(message, HumanMessage):
      with st.chat_message("user"):
        st.markdown(message.content)

if __name__ == "__main__":
  main()
