# Offshore chatbot 🤖

We are exploring the possibility to build a chatbot with an open source Large Language Model, locally on a 'every day' laptop (no GPU). Ultimately, we would like to attempt to 'fine-tune' the chatbot with some public data, related to the energy industry on the continental shelf of Norway. 

Laptop configuration:
- ThinkPad (Lenovo) T14s
- Processor: 13th Gen Intel(R) Core(TM) i7-1355U, 1.70 GHz
- RAM: 32 GB
- Operating system: Windows 11 Pro

## Results

We tried two different approaches:
1) Implementing only a 7 billion parameters large language model from Huggingface (see below under 'Data source').
2) Adding a document as text file with a selection of field information from NOD (Norwegian Offshore Directorate), in order to attempt 'fine-tuning'.

For the approach 1), the chatbot was only able to answer to generic questions, and for more detailed questions about specific fields, it was unable to answer anything. Also for the more generic questions that we asked, the information returned in the reply was not 100% reliable. The reply time was about 25 seconds.

For the approach 2), the chatbot was able to answer to much more specific questions about the selection of fields we compiled in the provided text file. Although the quality of the answers from the chatbox were satisfactory, the reply time was quite mediocre with waiting time over several minutes (~10 min). 

## Conclusions

Using a relatively small open source language model locally for generic purpose seems possible, still with some waiting time though (approximatively 20-25 seconds).
As soon as we tried to implement some extra document to attempt fine-tuning, the processing time increased exponentially: 10 minutes or more, depending of the length of the document. In this case, using a laptop computer with only CPU is not recommended. Moving over to a machine with GPU (or using google colab?) is necessary.

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
Huggingface language model (7 billion parameters): llama-2-7b-chat.Q2_K.gguf (size: 2.7 GB)</br>
--> https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf </br>

FIELD data for Norwegian continental shelf:</br>
https://factpages.sodir.no/en/field/TableView/Description </br>
Note that we had to compile a short sample of this table in a text file with only 5 fields for our project! </br>
(see in the data/sodir subfolder)

## Examples
Using ONLY the LLM, we see that the first answer is a bit strange (I don't think that the Gjoa field exists?), and when trying to dig a bit deeper, chatbot get stuck:

![screenshot_chatbot_question03](https://github.com/AnneEstoppey/Offshore_chatbot/assets/35219455/588535ec-833b-49f6-81f4-1a747f296d43)

##
Adding an extra document containing more detailed information:

![screenshot_chatbot_question04](https://github.com/AnneEstoppey/Offshore_chatbot/assets/35219455/8fd2cfba-872e-433b-9e0b-a0133ff6fc29)


## References
https://kavitmht.medium.com/create-a-chatbot-using-hugging-face-and-streamlit-9cbd9b90052b</br>
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF</br>
https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp.html</br>
https://medium.com/@fradin.antoine17/3-ways-to-set-up-llama-2-locally-on-cpu-part-1-5168d50795ac</br>
https://stackoverflow.com/questions/77267346/error-while-installing-python-package-llama-cpp-python</br>
