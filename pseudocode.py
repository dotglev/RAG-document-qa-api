# PROJECT PLAN: Document Q&A API

# --- API ENDPOINT 1: THE UPLOAD ROUTE (/upload) ---
# When a user sends a PDF file to this API endpoint:
# Step 1: Receive the uploaded PDF document from the user
# Step 2: Extract the raw text from all the pages of the PDF
# Step 3: Split the long text into smaller, readable chunks
# Step 4: Convert each text chunk into embeddings (lists of numbers)
# Step 5: Store the text chunks and their embeddings inside ChromaDB

# --- API ENDPOINT 2: THE QUESTION ROUTE (/ask) ---
# When a user sends a text question to this API endpoint:
# Step 6: Receive a specific question from the user
# Step 7: Search ChromaDB to find the text chunks most relevant to the question
# Step 8: Send the user question and the relevant chunks to the AI
# Step 9: Return the final generated answer back to the user

print("document Q AND A v1.0.0 Loaded!")