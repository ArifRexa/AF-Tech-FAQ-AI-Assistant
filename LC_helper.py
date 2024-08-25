from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
import logging
from dotenv import load_dotenv
from langchain_community.document_loaders.csv_loader import CSVLoader


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/faq_system.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
# Load environment variables from .env (especially OpenAI API key)
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Create OpenAI embeddings instance
openai_embeddings = OpenAIEmbeddings(api_key=openai_api_key)

vectordb_file_path = "faiss_index"

def create_vector_db():
    try:
        # Load data from the FAQ sheet
        logger.info("Loading CSV data")
        loader = CSVLoader(file_path='codebasics_faqs.csv', source_column="prompt", encoding='ISO-8859-1')
        data = loader.load()

        # Create a FAISS instance for vector database from 'data'
        logger.info("Creating FAISS vector database")
        vectordb = FAISS.from_documents(documents=data, embedding=openai_embeddings)

        # Save vector database locally
        logger.info("Saving vector database to local file")
        vectordb.save_local(vectordb_file_path)

    except Exception as e:
        logger.error(f"Failed to create vector database: {e}")
        raise


def get_qa_chain():
    try:
        logger.info("Loading vector database")
        # Load the vector database from the local folder
        vectordb = FAISS.load_local(vectordb_file_path, openai_embeddings, allow_dangerous_deserialization=True)

        # Create a retriever for querying the vector database
        logger.info("Creating retriever")
        retriever = vectordb.as_retriever(score_threshold=0.7)

        prompt_template = """Given the following context and a question, generate an answer based on this context only.
        In the answer, try to provide as much text as possible from the "response" section in the source document context without making many changes.
        If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.
    
        CONTEXT: {context}
    
        QUESTION: {question}"""

        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        chain = RetrievalQA.from_chain_type(llm=OpenAI(api_key=openai_api_key, temperature=0.1),
                                            chain_type="stuff",
                                            retriever=retriever,
                                            input_key="query",
                                            return_source_documents=True,
                                            chain_type_kwargs={"prompt": PROMPT})
        logger.info("QA chain created successfully")
        return chain
    except Exception as e:
        logger.error(f"Failed to create QA chain: {e}")
        raise

if __name__ == "__main__":
    # create_vector_db()
    # chain = get_qa_chain()
    # print(chain.invoke("Do you have a JavaScript course?"))
    try:
        logger.info("Starting FAQ Retrieval System")
        create_vector_db()
        chain = get_qa_chain()
        response = chain.invoke("Do you have a JavaScript course?")
        logger.info(f"Received response: {response}")

    except Exception as e:
        logger.critical(f"System encountered a critical error: {e}")