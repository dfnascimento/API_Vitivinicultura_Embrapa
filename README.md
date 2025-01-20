# API Vitivinicultura Embrapa 

Esse projeto foi desenvolvido por Diego de Faria do Nascimento como atividade parte da avaliação da Pós-Graduação de Machine Learning Engineering do Pos Tech FIAP

## Descrição: 

Trata-se de uma API pública para consulta aos dados do site da Embrapa, abrangendo informações das seções de Produção, Processamento, Comercialização, Importação e Exportação.

A API foi desenvolvida na liguagem de programação Python utilizando as bibliotecas Flask para a construção da API REST e definição das rotas, Beautiful Soap para a consulta e extração dos dados do site da embrapa com utilização das técnicas de Webscrapping.




## Arquitetura do Projeto:

O fluxo dp projeto envolve as seguintes etapas:

* Coleta de dados: a partir do uso da API REST Vitivinicultura da Embrapa serão coletados via webscrapping os dados do site da Embraba, em caso de instabilidade no link de acesso para embraba, a consulta ira ocorrer em arquivos csv baixados do site da embrapa e disponiveis offline
* Transformação e disponibilização: Os dados serão consultados via chamada de API Rest e disponibilizados no formado JSON
* Integração com Pipeline de Machine Learning: um pipeline de machine learning irá consuir os dados por intermedio da API e irá fazer o pre-processamento, tratamento do modelo de Machine Learning, gravação em um banco de dados com atuação de um Cientista de Dados .
* O Pipeline de Machine Learning irá disponibilizar o modelo de Machine Learning em um Sistema de Previsão para Vitivinicultura que será utilizado pelo usuário final. 


![Imagem com a Arquitetura do projeto.](https://github.com/dfnascimento/API_Vitivinicultura_Embrapa/blob/main/arquitetura.png)****

