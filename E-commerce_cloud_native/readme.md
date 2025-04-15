######################

E-commerce Cloud Native
📝 Descrição
Este projeto implementa uma aplicação de e-commerce utilizando arquitetura cloud native, integrando serviços Azure com uma interface de cadastro de produtos. A solução oferece uma forma escalável e moderna de gerenciar um catálogo de produtos em ambiente cloud.
🚀 Tecnologias Utilizadas

Python
Azure Blob Storage
SQL Server
Streamlit (para interface de Usuário)
dotenv (para gerenciamento de variáveis de ambiente)

📊 Demonstração
Aqui estão algumas capturas de tela do projeto em funcionamento:
Mostrar Imagem
Estrutura do projeto no VS Code com os principais arquivos
Mostrar Imagem
Interface de cadastro de produtos implementada com Streamlit
Mostrar Imagem
Diagrama da integração com serviços Azure
⚙️ Instalação e Execução

# Clone este repositório

git clone https://github.com/seu-usuario/e-commerce-cloud-native.git

# Acesse a pasta do projeto

cd e-commerce-cloud-native

# Instale as dependências

pip install -r requirements.txt

# Configure as variáveis de ambiente

# Crie um arquivo .env com as seguintes variáveis:

# BLOB_CONNECTION_STRING=sua_connection_string

# BLOB_CONTAINER_NAME=nome_do_container

# BLOB_ACCOUNT_NAME=nome_da_conta

# SQL_SERVER=seu_servidor_sql

# SQL_DATABASE=sua_database

# SQL_USER=seu_usuario

# SQL_PASSWORD=sua_senha

# Execute a aplicação

python main.py
🔍 Funcionalidades

Cadastro de Produtos: Interface para adicionar e gerenciar produtos no catálogo
Armazenamento em Nuvem: Utilização do Azure Blob Storage para armazenar imagens e dados de produtos
Banco de Dados SQL: Persistência de dados estruturados em SQL Server
Gestão Segura de Credenciais: Utilização de variáveis de ambiente para proteger informações sensíveis

💡 Aprendizados
Durante o desenvolvimento deste projeto, aprendi:

Como integrar aplicações Python com serviços de nuvem Azure
Boas práticas para gestão de credenciais em aplicações cloud
Configuração de conexões seguras com bancos de dados SQL
Desenvolvimento de interfaces de usuário com Streamlit
Implementação de arquitetura cloud native para aplicações escaláveis

🧩 Desafios Enfrentados
Os principais desafios que enfrentei e como os solucionei:

Configuração do ambiente Azure: Aprendi a navegar pelo portal Azure e configurar corretamente permissões e serviços.
Gestão segura de credenciais: Implementei o uso de variáveis de ambiente e arquivos .env para não expor credenciais no código.
Integração de múltiplos serviços: Desenvolvi uma arquitetura que permite a comunicação eficiente entre o front-end, banco de dados e storage.

🔮 Melhorias Futuras
Ideias para aprimorar este projeto no futuro:

Implementar autenticação e autorização de usuários
Adicionar funcionalidades de busca e filtragem de produtos
Criar um painel de análise de vendas e comportamento de usuários
Migrar para uma arquitetura de microsserviços
Implementar CI/CD para deploy automático

👨‍💻 Autor

[![LinkedIn](https://img.shields.io/badge/LinkedIn-lindembergs-blue?logo=linkedin)](https://www.linkedin.com/in/lindembergs/)
[![GitHub](https://avatars.githubusercontent.com/u/101612031?v=4)](https://github.com/lindembergs)
[![Whatsapp](<https://img.shields.io/badge/Whatsapp-(83)%99308--8753-%237289DA?logo=whatsapp>)](https://wa.me/+5583993088753)

📄 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
