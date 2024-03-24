# Offshore chatbot 🤖

We are exploring the possibility to build a chatbot with an open source Large Language Model, locally on a 'every day' laptop (no GPU). Ultimately, we would like to 'fine-tune' the chatbot with extra public data, related to the energy industry on the continental shelf of Norway. 

## Results

We tried two different approaches:
1) Implementing only a 7 billion parameters large language model from Huggingface (see below under 'Data source').
2) Adding a document as text file with a selection of field information from SODIR (Continental Shelf Directorate, Norway).

For the approach 1), the chatbot was only able to answer to generic questions, and for more detailed questions about specific fields, it was unable to answer anything. Also for the more generic questions we asked, the information returned in the reply was not 100% reliable. The reply time was about 25 seconds.

For the approach 2), the chatbot was able to answer to much more specific questions about the selection of fields we compiled in the provided text file. Although the quality of the answers from the chatbox are satisfactory, the reply time is quite mediocre with waiting time over several minutes (~10 min). 

## Install - requirements
We created a brand new Python environment from conda, Python version: **3.11.3**

We installed all the following libraries from PIP (at the time of creating the chatbot, we didn't succeed to install the 'llama' libraries from conda!)
- langchain
- llama-index
- llama-index-llms-llama-cpp
- llama-cpp-python
- streamlit

**NOTE**: if you are using Windows, you will have to install Visual Studio Installer, and then install the Desktop development with C++, in order to be able to install and use the python libraries related to 'llama-cpp' (where 'cpp' stands for 'C++').

## Data source
LLM:
Huggingface language model (7 billion parameters): llama-2-7b-chat.Q2_K.gguf (size: 2.7 GB)
--> please check in the references below as we have not included this model in this repo, you will have to download it from huggingface.

FIELD data for Norwegian continental shelf:
https://factpages.sodir.no/en/field/TableView/Description </br>
Note that we had to compile a short sample of this table in a text file with only 5 fields for our project! </br>
(see in the data/sodir subfolder)

## Example - first run!
This is a first try to interact with the chatbot, directly towards the LLM, NO fine-tuning... Some facts are not exactly correct, but not too bad for a model of that size, working locally from my laptop!

![screenshot_chatbot_question01](https://github.com/AnneEstoppey/Offshore_chatbot/assets/35219455/3cbc99c9-af20-40b2-b101-2ef23870ed92)

## References
https://kavitmht.medium.com/create-a-chatbot-using-hugging-face-and-streamlit-9cbd9b90052b
https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp.html
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
https://medium.com/@fradin.antoine17/3-ways-to-set-up-llama-2-locally-on-cpu-part-1-5168d50795ac
https://stackoverflow.com/questions/77267346/error-while-installing-python-package-llama-cpp-python
