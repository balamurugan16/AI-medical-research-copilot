# MediCopilot

Reading through medical research papers, clinical trials, and drug trials will be very informative for research purposes. But retaining all the key information out of them will be very challenging. Also, reading does takes a lot of time. To make this process easy, I created this tool called ***MediCopilot***

## Features
### Let's you load articles into the application which should be analysed.
![Home page](https://raw.githubusercontent.com/balamurugan16/AI-medical-research-copilot/main/screenshots/home.png)
### Has a chat window where you can chat with Medicopilot about your articles.
![chat page](https://raw.githubusercontent.com/balamurugan16/AI-medical-research-copilot/main/screenshots/chat.png)
### Creates a summary on any subject with the articles you have provided.
![summary page](https://raw.githubusercontent.com/balamurugan16/AI-medical-research-copilot/main/screenshots/summary.png)

## Tools used
1. Python
2. Streamlit (UI)
3. Langchain
4. Azure OpenAI
5. ChromaDB

## Environment variables
Checkout the `.env.example` file for the `.env` file setup.
Azure OpenAI can be swapped with OpenAI models too!

## Limitations
Currently only articles from the following sites are supported since the web scraping depends on the html page structure, I have a pre defined data loader to tackle each site.
1. Pubmed
2. Drugbank
3. Dailymed
4. FDA

## How to run?

1. Initialize `pipenv` and install dependencies
```
pipenv shell
pipenv install
```
2. Run the streamlit app
```
pipenv run streamlit run Home.py
```

## Requirements
1. Python 3.12
2. Azure OpenAI