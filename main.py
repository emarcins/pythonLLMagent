from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms import openai

load_dotenv()

#setting of the Pandas data from csv file
university_path = os.path.join("data", "university.csv")
university_df = pd.read_csv(university_path)

#querying Pandas data and updating prompts
university_query_engine = PandasQueryEngine(df=university_df, verbose=True, instruction_str=instruction_str)
university_query_engine.update_prompts({"pandas_prompt": new_prompt})

#tool which can help specify data, building agent capabilities
tools = [
    note_engine,
    QueryEngineTool(query_engine=university_query_engine, metadata=ToolMetadata(
        name="university-data",
        description="this gives an information about the ranks of the best world University"
    ))
]

#sort of the using larg language model
llm = openai(model="gpt-3.5-turbo-0613")

#sort of the AI Agent tool
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

#while loop which gives the possibility of start the work of Agent. Place to input your query.
while(prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)