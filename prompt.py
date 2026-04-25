from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
  template="""
  You are an expert writing assistant.

  Your task is to refine and improve the given text while keeping its original meaning.

  Instructions:
  - Improve clarity and readability
  - Fix grammar and spelling mistakes
  - Make the tone professional and natural
  - Keep the message concise
  - Do NOT change the original intent
  - Do NOT add new information

  Input Text:
  {text}

  Output:
  Return only the refined version of the text.
  """,
  input_variables=["text"]
)
