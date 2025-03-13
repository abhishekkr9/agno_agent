from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.models.ollama import Ollama
from agno.tools.website import WebsiteTools

MODEL_ID = "llama3.2:latest"

newsAgent = Agent(
    model=Ollama(id=MODEL_ID),
    tools=[WebsiteTools()],
    show_tool_calls=True,
    instructions="Use News Agent to gather news from the different sources:",
    description="You are an investor from India and you want to invest in Indian listed companies. You want to know about the news and how it has impacted the stock prices of the companies.",
)

web_agent=Agent(
    model=Ollama(id="llama3.2:latest"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    description="You are a investor trying to gather information on a company to make an informed decision. You want to know about the company's financials, news, and any other relevant information.",
    instructions=[
        "If there is any more information to be found, which is not sufficient to answer the question, use the Google Search tool to find it and make sure to gather from reliable and well known sources.",
        "Prioritize financial news websites, company websites, and reputable news outlets.",
    ],
)

finance_agent = Agent(
    model=Ollama(id="llama3.2:latest"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True)],
    show_tool_calls=True,
    markdown=True,
    description="You are an investor from India and you want to invest in indian listed companies priced below Rs. 500 per share based on their stock price, analyst recommendations and stock fundamentals. You also want to see trends on past, present and future news and how they have impacted the stock prices.",
    instructions=[
        "Format your response using markdown and use tables to display data where possible.",
        "Focus on Indian listed companies with stock prices below Rs. 500 per share.",
        "Prioritize companies with strong analyst recommendations and positive stock fundamentals (e.g., low P/E ratio, high growth potential).",
        "Analyze trends in past, present, and future news to understand their impact on stock prices.",
        "Only use financial data from reliable sources.",
    ],
)

agent_team=Agent(
    team=[ finance_agent, newsAgent, web_agent],
    model=Ollama(id="llama3.2:latest"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Based on current scenario, which stocks are best to buy?", stream=True)