from langchain_core.prompts import PromptTemplate

prompt_template = """answer the following question based on the context below.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Question: '{question}'
Context: '{context}'"""

def create_prompt_template(question: str, context: str) -> str:
    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template=prompt_template
    )
    return prompt.format(question=question, context=context)