

**Stock Analysis Agents**
=========================

This project utilizes the Agno library to create a team of AI agents that provide comprehensive stock analysis and recommendations. The agents are designed to gather news, financial information, and analyst recommendations to help investors make informed decisions.

**Agents**
---------

The project consists of four agents:

* **News Agent**: Gathers news from various sources to provide an overview of market trends and company-specific news.
* **Web Agent**: Uses DuckDuckGo search to gather information on a company's financials, news, and other relevant information.
* **Finance Agent**: Analyzes Indian listed companies' stock prices, analyst recommendations, and fundamentals using YFinance tools.
* **Agent Team**: A team of the above three agents, which provides a comprehensive response to a question.

**Usage**
-----

To use the agents, simply run the code and ask a question, such as "Based on current scenario, which stocks are best to buy?" The agents will provide a response in real-time, including sources and data tables where applicable.

**Requirements**
------------

* Agno library
* YFinance library
* DuckDuckGo API (optional)

**Future Development**
-------------------

* Integrate additional data sources and APIs
* Improve agent training and fine-tuning
* Expand agent capabilities to include more advanced analysis and recommendations
