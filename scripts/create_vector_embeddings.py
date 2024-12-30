from app import settings
from langchain_neo4j import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI

kg = Neo4jGraph(
    url=settings.NEO4J_URI,
    username=settings.NEO4J_USERNAME,
    password=settings.NEO4J_PASSWORD,
)

crimes = kg.query("""
    MATCH (crime: Crime) WHERE crime.charge IS NOT NULL RETURN crime
""")

crimes = [ crime["crime"] for crime in crimes ]

for crime in crimes:
    kg.query("""
        MATCH (c:Crime {id: $crime_id})
        WITH c, genai.vector.encode(
            c.charge,
            "OpenAI",
            {
                token: $openai_key,
                endpoint: $openai_endpoint
            }) AS vector
        CALL db.create.setNodeVectorProperty(c, "textEmbedding", vector)
        """,
        params={
            "crime_id": crime["id"],
            "openai_key": settings.OPENAI_API_KEY,
            "openai_endpoint": settings.LANGCHAIN_ENDPOINT
        }
    )
