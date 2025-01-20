# API Vitivinicultura Embrapa  

Este projeto foi desenvolvido por **Diego de Faria do Nascimento** como parte da avaliação do curso de Pós-Graduação em **Machine Learning Engineering** do Pos Tech FIAP.  

---

## 📄 Descrição  

A **API Vitivinicultura Embrapa** é uma API pública projetada para facilitar a consulta aos dados do site da **Embrapa**, permitindo a consulta de dados disponibilizados ns seguintes abas do website da Embrapa:  

- **Produção**  
- **Processamento**  
- **Comercialização**  
- **Importação**  
- **Exportação**  

O projeto foi desenvolvido em **Python**, utilizando:  
- **Flask**: Para construção da API REST e definição de rotas.  
- **BeautifulSoup**: Para extração de dados por meio de técnicas de Web Scraping.  

---


## 🚀 MVP - Deploy da API  

A API foi implantada como um MVP e está acessível no seguinte link:  

👉 [**API Vitivinicultura Embrapa**](https://api-vitivinicultura-embrapa.vercel.app/)  

A documentação completa da API (API Docs) foi gerada utilizando **Swagger** e está disponível no endpoint abaixo:  

👉 [**API Docs**](https://api-vitivinicultura-embrapa.vercel.app/apidocs/)  

### Endpoints Disponíveis  

| Método | Endpoint                     | Descrição                                     |  
|--------|------------------------------|---------------------------------------------|  
| GET    | `https://api-vitivinicultura-embrapa.vercel.app/producao`                 | Endpoint para buscar dados de produção por ano.                 |  
| GET    | `https://api-vitivinicultura-embrapa.vercel.app/processamento`            | Endpoint para buscar dados de processamento por ano e subopção.         |  
| GET    | `https://api-vitivinicultura-embrapa.vercel.app/comercializacao`          | Endpoint para buscar dados de comercialização por ano.           |  
| GET    | `https://api-vitivinicultura-embrapa.vercel.app/importacao`               | Endpoint para obtenção dos dados de importação por ano e subopção.               |  
| GET    | `https://api-vitivinicultura-embrapa.vercel.app/exportacao`               | Endpoint para obtenção dos dados de exportação por ano e subopção.               |  


### **Autenticação - Basic Auth**  

Para acessar a API, é necessário autenticar-se utilizando **Basic Auth**.  

#### **Credenciais de Acesso (exemplo)**  
- **Usuário**: `admin`  
- **Senha**: `@pI_mbr@p4`  

---


## 🛠️ Arquitetura do Projeto  

O fluxo do projeto é composto pelas seguintes etapas:  

### **1. Coleta de Dados**  
- Os dados são extraídos diretamente do site da Embrapa utilizando Web Scraping.  
- Em casos de instabilidade no site, a API consulta dados armazenados localmente em arquivos CSV previamente baixados.  

### **2. Transformação e Disponibilização**  
- As informações extraídas são processadas e disponibilizadas no formato **JSON** através das rotas da API.  

### **3. Integração com Pipeline de Machine Learning**  
- Um pipeline de Machine Learning consome os dados fornecidos pela API para:  
  - **Pré-processamento**: Limpeza e transformação dos dados.  
  - **Treinamento de Modelos**: Construção de modelos de Machine Learning.  
  - **Armazenamento**: Persistência dos resultados em um banco de dados.  

### **4. Sistema de Previsão**  
- O modelo treinado é disponibilizado em um **Sistema de Previsão para Vitivinicultura**, permitindo que usuários finais acessem previsões e insights de forma prática e eficiente.  


![Imagem com a Arquitetura do projeto.](https://github.com/dfnascimento/API_Vitivinicultura_Embrapa/blob/main/arquitetura.png)
---


## 🚀 Tecnologias Utilizadas  

- **Python**  
- **Flask**  
- **BeautifulSoup**
- **Pandas**
- **Flasgger**

---

## 📝 Como Executar o Projeto  

### Pré-requisitos  
Certifique-se de ter o **Python 3.9+** instalado em sua máquina.  

### Passos  

1. Clone o repositório:  
   ```
   git clone https://github.com/dfnascimento/API_Vitivinicultura_Embrapa.git
   cd API_Vitivinicultura_Embrapa
   ```
2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
    ```
    python app.py
    ```
5. Acesse a API no navegador ou via ferramentas como Postman:

    ```
    http://localhost:5000

    ```

---

## 📞 Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: df.nascimento93@gmail.com
