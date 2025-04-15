import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
from dotenv import load_dotenv

load_dotenv()

BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
BLOB_ACCOUNT_NAME = os.getenv("BLOB_ACCOUNT_NAME")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

st.title("Cadastro de Produtos")

product_name = st.text_input("Nome do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_description = st.text_area("Descrição do Produto")
product_image = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

def upload_blob(file):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(BLOB_CONTAINER_NAME)
        blob_name = f"{uuid.uuid4()}/{file.name}"
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file, overwrite=True)
        return f"https://{BLOB_ACCOUNT_NAME}.blob.core.windows.net/{BLOB_CONTAINER_NAME}/{blob_name}"
    except Exception as e:
        st.error(f"Erro ao fazer upload da imagem: {e}")
        return None

def insert_product(name, price, description, image_url):
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES (%s, %s, %s, %s)",
            (name, price, description, image_url)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Erro ao salvar produto: {e}")
        return False

def list_products():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Produtos")
        products = cursor.fetchall()
        conn.close()
        return products
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []

def show_products():
    products = list_products()
    if products:
        cards_per_row = 3
        cols = st.columns(cards_per_row)
        for i, product in enumerate(products):
            col = cols[i % cards_per_row]
            with col:
                st.markdown(f"### {product['nome']}")
                st.write(f"**Descrição:** {product['descricao']}")
                st.write(f"**Preço:** R$ {product['preco']:.2f}")
                if product["imagem_url"]:
                    st.markdown(f'<img src="{product["imagem_url"]}" width="200" height="200">', unsafe_allow_html=True)
                st.markdown("---")
            if (i + 1) % cards_per_row == 0 and (i + 1) < len(products):
                cols = st.columns(cards_per_row)
    else:
        st.info("Nenhum produto encontrado.")

if st.button('Salvar Produto'):
    if product_image is not None:
        image_url = upload_blob(product_image)
        if image_url and insert_product(product_name, product_price, product_description, image_url):
            st.success("Produto salvo com sucesso!")
    else:
        st.warning("Por favor, envie uma imagem do produto.")

st.header("Produtos Cadastrados")

if st.button('Listar Produtos'):
    show_products()
