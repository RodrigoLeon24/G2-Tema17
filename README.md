# G2-Tema17

### **Nome:** Rodrigo Leon de Andrade Silva
### **Professor:** Alexandre Neves Louzadas
### **Matéria:** Linguagens de Programação

## Dashboard de Indicadores Econômicos do Brasil
## 1. Descrição do projeto

Este projeto apresenta uma análise interativa dos principais indicadores econômicos do Brasil, considerando o período de 2015 a 2024.

O projeto foi desenvolvido como avaliação G2 — Tema 17: Indicadores Econômicos do Brasil, da disciplina de Linguagem de Programação — Análise e Visualização de Dados com Python.

A aplicação permite analisar a evolução de indicadores econômicos, comparar variáveis, identificar períodos críticos e investigar possíveis relações entre diferentes aspectos da economia brasileira.

## Fluxo do projeto

```
simulacao_indicadores_economicos_brasil.csv
                    ↓
          Leitura e tratamento
                 Pandas
                    ↓
        Análise e visualização
       Matplotlib + Seaborn
                    ↓
             Persistência
             SQLAlchemy
                    ↓
              Banco SQLite
                    ↓
          Dashboard interativo
               Streamlit
                    ↓
            Publicação online
         Streamlit Cloud / GitHub
```

## 2. Problema de análise

O projeto busca compreender o comportamento da economia brasileira entre 2015 e 2024 por meio da análise de diferentes indicadores econômicos.

- A aplicação procura responder às seguintes questões:
- Como o PIB evoluiu ao longo do período analisado?
- Existe relação entre inflação e desemprego?
- Quais períodos apresentaram maior crescimento econômico?
- Existe relação entre taxa de juros e consumo das famílias?
- Quais indicadores apresentaram maior instabilidade?
- Como a renda média evoluiu ao longo dos anos?
- Como o câmbio se comportou durante o período?
- Quais períodos podem ser considerados críticos para a economia brasileira?
- Quais relações podem ser observadas entre os principais indicadores econômicos?

A análise dos dados permite transformar os valores da base em informações úteis para interpretação econômica e tomada de decisão.

## 3. Objetivos do projeto
Objetivo geral

Desenvolver uma aplicação analítica capaz de explorar e visualizar indicadores econômicos brasileiros entre 2015 e 2024.

Objetivos específicos

Analisar a evolução temporal dos indicadores;

Comparar diferentes indicadores econômicos;

Identificar períodos de crescimento e retração;

Investigar relações entre inflação e desemprego;

Investigar a relação entre juros e consumo;

Analisar a evolução do PIB;

Avaliar o comportamento do câmbio;

Identificar períodos econômicos críticos;

Calcular indicadores estatísticos;

Armazenar os dados em banco SQLite;

Disponibilizar os resultados por meio de um dashboard interativo.

## 4. Base de dados

O projeto utiliza um dataset simulado contendo indicadores econômicos brasileiros referentes ao período de 2015 a 2024.

Arquivo utilizado
dados/simulacao_indicadores_economicos_brasil.csv

Principais variáveis
Coluna	Descrição
ano	Ano da medição
trimestre	Trimestre da medição
data	Data de referência
pib	Produto Interno Bruto
inflacao	Índice de inflação
taxa_juros	Taxa de juros
taxa_desemprego	Percentual de desemprego
cambio_dolar	Cotação do dólar
renda_media	Renda média da população
consumo_familias	Índice de consumo das famílias
investimento	Índice de investimento
exportacoes	Volume de exportações
importacoes	Volume de importações
nivel_economico	Classificação do período econômico

O campo nivel_economico permite classificar os períodos como, por exemplo:

Crescimento
Estabilidade
Crise

## 5. Tecnologias utilizadas
Tecnologia	Função
Python	Linguagem principal do projeto
Pandas	Manipulação, limpeza e análise dos dados
Matplotlib	Criação de gráficos
Seaborn	Visualizações estatísticas
Streamlit	Desenvolvimento do dashboard interativo
SQLAlchemy	Integração com banco SQLite
SQLite	Persistência dos dados
Git	Controle de versão
GitHub	Armazenamento e publicação do código
## 6. Estrutura do projeto
projeto-indicadores-economicos/
│
├── README.md
├── requirements.txt
├── app.py
├── index.html
│
├── dados/
│   └── simulacao_indicadores_economicos_brasil.csv
│
├── database/
│   └── indicadores_economicos.sqlite
│
├── notebooks/
│   └── analise_indicadores_economicos.ipynb
│
└── imagens/

Descrição dos principais arquivos
Arquivo/Pasta	Função
`app.py`	Aplicação principal em Streamlit
`requirements.txt`	Dependências do projeto
`README.md`	Documentação do projeto
`index.html`	Página de apresentação para GitHub Pages
`dados/`	Armazenamento da base de dados
`database/`	Banco de dados SQLite
`notebooks/`	Notebook de análise exploratória
`imagens/`	Imagens utilizadas na documentação
## 7. Dashboard

O dashboard foi desenvolvido utilizando Streamlit e permite explorar os indicadores econômicos de forma interativa.

Funcionalidades

O sistema apresenta:

KPIs econômicos;

filtros interativos;

análise temporal;

comparação entre indicadores;

gráficos estatísticos;

identificação de períodos críticos;

consultas utilizando SQL;

visualização dos dados armazenados no SQLite;

interpretação dos resultados.

Abas do dashboard

A aplicação está organizada nas seguintes áreas:
 
#### 1. Visão Geral
#### 2. Relações Econômicas
#### 3. Períodos Críticos
#### 4. Consulta SQL
#### 5. Dados

## 8. Filtros interativos

O dashboard permite filtrar os dados de acordo com diferentes critérios.

Filtros disponíveis

Ano;

Nível econômico.

Os filtros são aplicados aos dados utilizados nas análises e também aos dados apresentados na consulta do banco SQLite.

Exemplo:

Ano
☑ 2020
☑ 2021
☐ 2022

Nível econômico
☑ Crise
☐ Estabilidade
☐ Crescimento


Dessa forma, o usuário consegue analisar somente os períodos que deseja investigar.

## 9. KPIs utilizados

O dashboard apresenta indicadores-chave de desempenho econômico.

KPI	Descrição
PIB médio	Média do Produto Interno Bruto no período selecionado
Inflação média	Média do indicador de inflação
Desemprego médio	Média da taxa de desemprego
Juros médio	Média da taxa de juros
Dólar médio	Média da cotação do dólar
Crescimento médio	Média do crescimento econômico

Os KPIs são recalculados de acordo com os filtros selecionados pelo usuário.

## 10. Análises realizadas
#### 10.1 Evolução do PIB

A análise temporal do PIB permite observar períodos de crescimento e retração da atividade econômica.

O gráfico de linha facilita a identificação de mudanças no comportamento do indicador ao longo dos anos.

#### 10.2 Evolução da inflação

A evolução da inflação é analisada temporalmente para identificar períodos de maior ou menor pressão inflacionária.

#### 10.3 Evolução do desemprego

A taxa de desemprego é analisada para identificar mudanças no mercado de trabalho durante o período estudado.

#### 10.4 Inflação × desemprego

É utilizado um gráfico de dispersão para investigar a relação entre inflação e desemprego.

Também é calculado o coeficiente de correlação entre os dois indicadores.

A correlação indica associação entre variáveis, mas não significa necessariamente relação de causa e efeito.

#### 10.5 Juros × consumo

A relação entre taxa de juros e consumo das famílias é investigada por meio de gráfico de dispersão e correlação.

Essa análise permite verificar se períodos de juros maiores estão associados a alterações no comportamento do consumo.

#### 10.6 Análise do câmbio

A cotação do dólar é analisada para observar sua evolução durante o período estudado e identificar momentos de maior valorização ou desvalorização cambial.

#### 10.7 Períodos críticos

São identificados períodos em que o crescimento econômico apresenta valores negativos.

Quando disponível na base, o indicador de crescimento econômico é utilizado diretamente para identificar esses períodos.

## 11. Visualizações

O projeto utiliza diferentes técnicas de visualização para facilitar a interpretação dos dados.

Principais visualizações

Gráficos de linha;

Gráficos de dispersão;

Gráficos comparativos;

Gráficos de evolução temporal;

Tabelas de dados;

Indicadores numéricos;

Visualizações estatísticas.

As visualizações são construídas principalmente utilizando:

Matplotlib
Seaborn

## 12. Banco de dados SQLite

O projeto também utiliza um banco de dados SQLite para demonstrar a persistência e consulta dos dados.

O banco está localizado em:

`database/indicadores_economicos.sqlite`


A tabela principal utilizada pela aplicação é:

`indicadores_economicos`


A integração é realizada utilizando SQLAlchemy.

Exemplo da consulta utilizada:

`SELECT *
FROM indicadores_economicos;`


Também são realizadas consultas agregadas para calcular médias dos indicadores econômicos.

## 13. Notebook de análise

O notebook está localizado em:

`notebooks/analise_indicadores_economicos.ipynb`

O notebook apresenta as etapas de análise exploratória dos dados.

Estrutura do notebook

Introdução;

Contextualização econômica;

Explicação da base;

Leitura dos dados;

Limpeza e preparação;

Engenharia de atributos;

Cálculo dos KPIs;

Visualizações;

Interpretação dos resultados;

Conclusão.

## 14. Como executar localmente
#### 14.1 Clonar o repositório
`git clone https://github.com/RodrigoLeon24/g2-tema17.git`


Depois entre na pasta:

cd g2-tema17

#### 14.2 Instalar as dependências

Execute:

`pip install -r requirements.txt`


As principais bibliotecas utilizadas são:

`pandas`
`matplotlib`
`seaborn`
`streamlit`
`sqlalchemy`

#### 14.3 Executar o dashboard

Execute:

`streamlit run app.py`


O Streamlit abrirá o dashboard no navegador.

#### 14.4 Executar o notebook

Para abrir o notebook utilizando Jupyter:

`jupyter notebook`


Depois acesse:

`notebooks/analise_indicadores_economicos.ipynb`


Também é possível abrir o arquivo utilizando VS Code ou Google Colab.

## 15. Publicação

O projeto foi planejado para ser disponibilizado em três plataformas.

GitHub

Utilizado para:

armazenar o código-fonte;

versionar o projeto;

disponibilizar a documentação;

armazenar a base e o notebook.

GitHub Pages

Utilizado para disponibilizar uma página de apresentação do projeto.

Arquivo:

`index.html`

`Streamlit Cloud`

Utilizado para disponibilizar o dashboard de forma online.

O aplicativo é executado a partir do arquivo:

`app.py`

## 16. Entregas do projeto

As entregas previstas para o projeto são:

Link do repositório GitHub:'https://github.com/RodrigoLeon24/G2-Tema17';

Link da página GitHub Pages: 'https://rodrigoleon24.github.io/G2-Tema17/';

Link do dashboard no Streamlit: 'https://g2-tema17-9xssszvfx5pn4eapvjnwsf.streamlit.app/';

Notebook '[notebook/G1_TRABALHO_PRATICO_RODRIGO_LEON.ipynb](https://github.com/RodrigoLeon24/G2-Tema17/blob/main/notebook/G1_TRABALHO_PRATICO_RODRIGO_LEON.ipynb)';

Código '[app.py](https://github.com/RodrigoLeon24/G2-Tema17/blob/main/app.py)';

Base de dados utilizada 'https://github.com/RodrigoLeon24/G2-Tema17/blob/main/dados/simulacao_indicadores_economicos_brasil.csv'.

## 17. Critérios de análise

O projeto considera os seguintes aspectos:

## Tratamento dos dados

Verificação, limpeza, conversão de tipos e preparação da base para análise.

## KPIs

Cálculo de indicadores relevantes para interpretação econômica.

## Visualizações

Utilização de gráficos adequados para representar tendências, comparações e relações entre variáveis.

## Dashboard

Desenvolvimento de uma aplicação interativa utilizando Streamlit.

## Interpretação

Análise dos resultados encontrados e identificação de tendências e períodos críticos.

## Organização

Estruturação profissional dos arquivos, banco de dados, notebook e documentação.

### 18. Conclusão

O projeto demonstra como ferramentas de análise de dados podem ser utilizadas para investigar o comportamento da economia brasileira.

A combinação de Python, Pandas, Matplotlib, Seaborn, SQLAlchemy, SQLite e Streamlit permite transformar uma base de dados econômicos em uma aplicação analítica interativa.

A análise dos indicadores possibilita observar tendências, identificar períodos de crescimento ou retração e investigar relações entre diferentes variáveis econômicas.

Além da construção dos gráficos e indicadores, o projeto busca desenvolver a capacidade de interpretar dados e comunicar resultados de forma clara, transformando informações econômicas em conhecimento útil para análise e tomada de decisão.

### 19. Autor

Projeto G2 — Tema 17

Indicadores Econômicos do Brasil

Desenvolvido como projeto acadêmico da disciplina de Linguagem de Programação — Análise e Visualização de Dados com Python.