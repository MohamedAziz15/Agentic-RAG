from config import Gemini_API_KEY, Groq_API_KEY, Open_router_API_KEY
from crewai_tools import WebsiteSearchTool

from crewai_tools import ScrapeWebsiteTool


# Example of initiating tool that agents can use 
# to search across any discovered websites
tool = WebsiteSearchTool()

# Example of limiting the search to the content of a specific website, 
# so now agents can only search within that website
tool = WebsiteSearchTool(website='https://computecheg.com/en/product/hp-zbook-15-g5-workstation-i7-8th/?srsltid=AfmBOoo8C_bs4GHFcFr1kGxP92qfthxG_p-FupQpj6vbMAqOE7VPtaso')


# tool = WebsiteSearchTool(
#     config=dict(
#         llm=dict(
#             provider="ollama", # or google, openai, anthropic, llama2, ...
#             config=dict(
#                 model="llama2",
#                 # temperature=0.5,
#                 # top_p=1,
#                 # stream=true,
#             ),
#         ),
#         embedder=dict(
#             provider="google", # or openai, ollama, ...
#             config=dict(
#                 model="models/embedding-001",
#                 task_type="retrieval_document",
#                 # title="Embeddings",
#             ),
#         ),
#     )
# )

# Extract the product information
text = tool.run()
print(text)


####################################################################################################################
# # Initialize the tool with the product page URL
# tool = ScrapeWebsiteTool(website_url='https://shop.example.com/product/12345')

# # Extract the product information
# text = tool.run()
# print(text)





