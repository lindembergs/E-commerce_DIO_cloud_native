import streaml as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
import json
from dotenv import load_dotenv

load_dotenv()

blobConnectionString = os.getenv("BLOB_CONNECTION_STRING")
blobContainerName = os.getenv("BLOB_CONTAINER_NAME")
blobaccountName = os.getenv("BLOB_ACCOUNT_NAME")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

st.title("Cadastro de Produtos")

product_name = st.text_input("Nome do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_description = st.text_area("Descrição do Produto")
product_image = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

def upload_blob(file, container_name, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(container_name)
    blob_name = f"{uuid.uuid4()}/{file.name}"
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file, overwrite=True)
    return f"https://{blobaccountName}.blob.core.windows.net/{container_name}/{blob_name}"

def insert_product(name, price, description, image_url):
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES (%s, %s, %s, %s)", (name, price, description, image_url))
        conn.commit()
        conn.close()
        return True


    except Exception as e:
        return_message = f"Erro ao salvar produto: {e}"
        return False
    
def list_products():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produtos")
        products = cursor.fetchall()
        conn.close()
        return products
    except Exception as e:
        return_message = f"Erro ao listar produtos: {e}"
        return []
    
def list_produtos_screen():
        products = list_products()
        if products:
        # Define o número de cards por linha
            cards_por_linha = 3
            # Cria as colunas iniciais
            cols = st.columns(cards_por_linha)
            for i, product in enumerate(products):
                col = cols[i % cards_por_linha]
                with col:
                    st.markdown(f"### {product['nome']}")
                    st.write(f"**Descrição:** {product['descricao']}")
                    st.write(f"**Preço:** R$ {product['preco']:.2f}")
                    if product["imagem_url"]:
                        html_img = f'<img src="{product["imagem_url"]}" width="200" height="200" alt="Imagem do produto">'
                        st.markdown(html_img, unsafe_allow_html=True)
                    st.markdown("---")
                # A cada 'cards_por_linha' produtos, se ainda houver produtos, cria novas colunas
                if (i + 1) % cards_por_linha == 0 and (i + 1) < len(products):
                    cols = st.columns(cards_por_linha)
        else:
            st.info("Nenhum produto encontrado.")
        

if st.button('Salvar Produto'):
    insert_product(product_name, product_price, product_description, upload_blob(product_image, blobContainerName, product_image.name))
    return_message = "Produto salvo com sucesso"

st.header("Produtos Cadastrados")

if st.button('Listar Produtos'):
    return_message = "Produtos listados com sucesso"