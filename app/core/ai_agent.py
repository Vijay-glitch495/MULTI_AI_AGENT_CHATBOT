from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage,HumanMessage

from app.config import settings

def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt=None):
   
    llm = ChatGroq(model=llm_id)
    
    tools = [TavilySearch(max_results=2)] if allow_search else []
    
    agent = create_react_agent(
        model=llm,
        tools=tools
    )
    
    # Wrap user query as a HumanMessage
    state = {"messages": [HumanMessage(content=msg) for msg in query]}
    
    response = agent.invoke(state)
    
    messages = response.get("messages")
    
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)]
    
    return ai_message[-1] if ai_message else "No response from AI"

    
    
#Example response might look like:
#  response["messages"] = [
#    HumanMessage(content="Search: Who is CEO of OpenAI?"),
#    AIMessage(content="Searching online..."),       # intermediate step
#    AIMessage(content="The CEO of OpenAI is Sam Altman.")   # final answer
# ]


    
    
    