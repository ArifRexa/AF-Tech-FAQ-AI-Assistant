
# FAQ Retrieval System with OpenAI and FAISS

This project is a FAQ retrieval system built using OpenAI embeddings and FAISS for vector storage. The system allows users to query a collection of FAQs and retrieve relevant answers based on semantic similarity.

## Features

- **OpenAI Embeddings:** Leverages OpenAI's powerful embeddings to semantically encode FAQ entries.
- **FAISS Vector Store:** Efficiently stores and retrieves vectorized FAQs using Facebook's FAISS library.
- **Contextual Answer Generation:** Answers are generated with context from the original FAQ documents, ensuring accuracy and relevance.
- **CSV Data Loading:** Easily load FAQ data from a CSV file for quick setup and updates.
- **Query Logging:** Logs all user queries and responses for analysis and system improvement.
- **Interactive FAQ Management:** Administrators can update or add new FAQs through a simple UI.
- **Feedback Mechanism:** Users can provide feedback on the quality of the answers to help improve the system.
- **Multi-language Support:** Allows queries in multiple languages by integrating with a translation API.
- **Customizable Response Length:** Users can choose between short, medium, and detailed answers based on their needs.
- **Scheduled Re-indexing:** Automatically updates the FAISS index at regular intervals to include new FAQs.
- **Chatbot Integration:** Seamlessly integrates with a chatbot interface for a conversational FAQ experience.
- **Real-time Analytics Dashboard:** Monitor usage statistics and system performance through a dedicated dashboard.

## Setup

### Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- [FAISS](https://github.com/facebookresearch/faiss) (Install with `pip install faiss-cpu` or `pip install faiss-gpu` if you have a CUDA-enabled GPU)
- OpenAI API Key
- (Optional) Google API Key for translation and other integrations

### Installation

1. **Clone the repository:**

    \`\`\`bash
    git clone https://github.com/your-username/faq-retrieval-system.git
    cd faq-retrieval-system
    \`\`\`

2. **Install dependencies:**

    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

3. **Set up environment variables:** Create a \`.env\` file in the root directory of your project with the following content:

    \`\`\`env
    OPENAI_API_KEY=your-openai-api-key
    SERPAPI_API_KEY=your-serpapi-api-key
    GOOGLE_API_KEY=your-google-api-key
    \`\`\`

4. **Prepare the CSV data:**

    - Place your FAQ data in a CSV file named \`codebasics_faqs.csv\` in the root directory.
    - The CSV should have a column named \`prompt\` that contains the questions or prompts.

5. **Create the vector database:**

    \`\`\`bash
    python your_script.py
    \`\`\`

## Usage

### Running the System:

\`\`\`bash
python your_script.py
\`\`\`

### Query the System: Use the \`chain.invoke()\` method to query the system:

\`\`\`python
result = chain.invoke("Your question here")
print(result)
\`\`\`

### Example

\`\`\`python
result = chain.invoke("Do you have a JavaScript course?")
print(result)
\`\`\`

## Features You Can Add

This project can be extended with additional features such as:

- **Context Highlighting:** Show where in the document the answer was found.
- **Multi-language Support:** Use a translation API to handle queries in different languages.
- **Feedback Collection:** Allow users to rate the quality of the answers.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://openai.com/) for their powerful API.
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search.
- [LangChain](https://langchain.com/) for the foundational libraries that made this project possible.
