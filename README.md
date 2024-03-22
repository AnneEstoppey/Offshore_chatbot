# Offshore chatbot 🤖

We are exploring the possibility to build a chatbot with an open source Large Language Model, locally on a 'every day' laptop (no GPU). Ultimately, we would like to 'fine-tune' the chatbot with extra public data, related to the energy industry on the continental shelf of Norway. 

## Steps

1) Create the chatbot and test it on local - DONE
2) Add extra data (public) for fine-tuning for offshore activities on Norwegian continental shelf - under construction

## Install - requirements
We installed a brand new Python environment from conda, Python version: **3.11.3**

We installed all the following libraries from PIP (at the time of creating the chatbot, we didn't succeed to install the 'llama' libraries from conda!)
- langchain
- llama-index
- llama-index-llms-llama-cpp
- llama-cpp-python
- streamlit

**NOTE**: if you are using Windows, you will have to install Visual Studio Installer, and then install the Desktop development with C++, in order to be able to install and use the python libraries related to 'llama-ccp'.

## Data source
LLM:
Huggingface language model (7 billion parameters): llama-2-7b-chat.Q2_K.gguf (size: 2.7 GB)

--> please check in the references below as we have not included this model in this repo, you will have to download it from huggingface.

## Example - first run!
This is a first try to interact with the chatbot, directly towards the LLM, NO fine-tuning... Some facts are not exactly correct, but not too bad for a model of that size, working locally from my laptop!

![screenshot_chatbot_question01](https://github.com/AnneEstoppey/Offshore_chatbot/assets/35219455/3cbc99c9-af20-40b2-b101-2ef23870ed92)

## References
https://kavitmht.medium.com/create-a-chatbot-using-hugging-face-and-streamlit-9cbd9b90052b
https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp.html
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
https://medium.com/@fradin.antoine17/3-ways-to-set-up-llama-2-locally-on-cpu-part-1-5168d50795ac
https://stackoverflow.com/questions/77267346/error-while-installing-python-package-llama-cpp-python
