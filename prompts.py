from llama_index.core import PromptTemplate

#creating instruction prompt for the AI Agent
instruction_str = """\
    1. Convert the query to exectubale Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

#creating prompt template for the AI Agent
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression:  """
)

#context for the AI Agent engine
context="""
Purpose: The primary role of this agent is to assist user by providing accurate information about the rank of the best university of the world and details about that university like for example country of origin.   
"""