# 📊 Análise e Modelagem Preditiva de Impactos Socioeconômicos em Minas Gerais

Este projeto tem como objetivo desenvolver um modelo de *Machine Learning* capaz de **avaliar, prever e visualizar os agentes e fenômenos que mais impactam o desenvolvimento socioeconômico**, utilizando como variável-alvo o **Índice de Desenvolvimento Humano (IDH)** das regiões do estado de Minas Gerais.

Todo o processo foi conduzido seguindo uma **metodologia estruturada**, desde a formulação do problema até a análise da importância das variáveis, garantindo coerência estatística, interpretabilidade e robustez dos resultados.


Foi adotado um método de 7 etapas para a construção do modelo:
- 1° Definição do objetivo
- 2° Coleta dos dados
- 3° Análise dos dados
- 4° Tratamento dos dados
- 5° Escolha do algoritmo
- 6° Treinamento e Teste
- 7° Ajuste de hiperparâmetros
---

## 1️⃣ Definição do Objetivo

O desenvolvimento do modelo partiu da seguinte questão central:

> **Como poderíamos avaliar e prever/visualizar os agentes e fenômenos que mais causam impactos socioeconômicos no Brasil?**

Para tornar o problema tratável e mensurável, o estudo foi delimitado ao **estado de Minas Gerais**, utilizando dados agregados por Regiões Integradas de Segurança Pública (RISP).  
O **IDH** foi escolhido como variável-alvo por ser um **indicador consolidado**, amplamente utilizado para representar condições socioeconômicas, incorporando dimensões de **renda, educação e saúde**.

---

## 2️⃣ Coleta dos Dados

Os dados utilizados neste projeto foram coletados a partir de fontes públicas e organizados em um dataset estruturado, contendo indicadores como:

- Renda média
- Taxas educacionais
- Indicadores criminais
- Expectativa de vida
- Variáveis demográficas e socioeconômicas

Todo o processo de coleta está documentado no repositório:

🔗 **https://github.com/jvrezendem/analise_socioeconomica_mg**

---

## 3️⃣ Análise Exploratória dos Dados

A etapa de análise exploratória teve como objetivos principais:

- Compreender a distribuição das variáveis
- Identificar padrões e correlações
- Detectar possíveis inconsistências ou valores atípicos
- Avaliar relações iniciais entre os indicadores e o IDH

Essa análise permitiu observar que muitos fenômenos socioeconômicos apresentam **relações não triviais**, frequentemente mediadas por interações entre variáveis.
---

## 4️⃣ Tratamento dos Dados e Engenharia de Atributos

### 4.1 Limpeza e Preparação
Foram realizadas etapas de:
- Remoção de colunas não informativas ou identificadoras (ex: latitude, longitude, códigos administrativos)
- Padronização de nomes
- Garantia de consistência entre variáveis

### 4.2 Engenharia de Atributos
Uma etapa fundamental do projeto foi a **engenharia de atributos**, que permitiu enriquecer o dataset original com novas variáveis derivadas, como:

- Relações entre criminalidade e renda
- Relações entre criminalidade e educação
- Interações entre expectativa de vida e renda
- Indicadores normalizados por população

Esses atributos derivados permitiram capturar **relações socioeconômicas mais profundas**, que não seriam observáveis apenas com variáveis brutas.

📌 *(Inserir diagrama ou tabela de engenharia de atributos)*  
📂 **assets/feature_engineering/**

---

## 5️⃣ Escolha do Algoritmo

### 5.1 Modelos Avaliados
Foram testados **quatro algoritmos de regressão**, utilizando tanto **split fixo** quanto **validação cruzada**:

- Regressão Linear
- Regressor baseado em Árvore de Decisão
- Rede Neural (MLP)
- **Ridge Regressor**

### 5.2 Algoritmo Escolhido — Ridge Regressor
O **Ridge Regressor** foi selecionado por apresentar:

- Melhor desempenho médio
- Maior estabilidade
- Menor sensibilidade à multicolinearidade
- Boa capacidade de generalização em **datasets pequenos**

O Ridge é uma regressão linear com **regularização L2**, que penaliza coeficientes excessivamente altos, reduzindo overfitting (quando o modelo "decora" os dados de treinamento) e tornando o modelo mais robusto.

### 5.3 Validação Cruzada
Foi adotada a **validação cruzada K-Fold (K=5)** por:

- Reduzir dependência de um único split
- Permitir avaliação mais confiável do erro
- Ser especialmente adequada para bases de dados pequenas

A validação Cruzada (Cross Validation) realiza a divisão dos daddos de treino e test multiplas vezes, garantindo que todo o conjunto de dados seja usado para treinamento e teste em momentos diferentes.
O método K-Fold separa o conjunto de dados em *k* subconjuntos (os folds). Os dados são divididos em *k* partes iguais e o modelo é treinado *k* vezes.


📌 *(Inserir gráfico comparando split fixo vs cross-validation)*  
📂 **assets/model_comparison/**

---

## 6️⃣ Treinamento e Teste do Modelo

### 6.1 Variável-Alvo
- **IDH** foi escolhido como target por sintetizar múltiplas dimensões socioeconômicas e ser amplamente reconhecido.

### 6.2 Variáveis Preditivas
Foram utilizadas todas as variáveis socioeconômicas relevantes, com exceção de:
- Colunas identificadoras
- Variáveis geográficas (latitude/longitude)
- Códigos administrativos

### 6.3 Normalização
Os dados foram padronizados utilizando **StandardScaler**, sempre ajustado **apenas no conjunto de treino**, evitando vazamento de informação.

### 6.4 Processo de Treinamento
Em cada fold:
- O modelo foi treinado
- O erro foi avaliado
- As previsões foram armazenadas para análise comparativa

📌 *(Inserir scatter plot IDH real vs previsto)*  
📂 **assets/predictions/**

---

## 7️⃣ Ajuste de Hiperparâmetros

Foi realizado um teste sistemático de diferentes valores do hiperparâmetro **α (alpha)** do Ridge Regressor.

- O alpha controla a intensidade da regularização
- Valores baixos → modelo mais flexível
- Valores altos → modelo mais conservador

A escolha do alpha foi baseada no **menor erro médio (MAE)** obtido via validação cruzada, buscando equilíbrio entre viés e variância.

📌 *(Inserir gráfico Alpha vs MAE)*  
📂 **assets/hyperparameter_tuning/**

---

## 8️⃣ Importância das Variáveis

Após a definição do modelo final, foram aplicados dois métodos complementares para avaliar a importância das variáveis na predição do IDH.

### 8.1 LOFO (Leave-One-Feature-Out)
Nesse método:
- Uma variável é removida por vez
- O modelo é reavaliado
- Observa-se o quanto o erro aumenta

O LOFO mede a **importância estrutural** da variável no modelo.

### 8.2 Importância por Permutação
Nesse método:
- Os valores de uma variável são embaralhados
- O modelo treinado é mantido
- Mede-se o aumento do erro

Esse método avalia **quanto o modelo depende da informação daquela variável**, preservando a distribuição original.

A utilização conjunta dos dois métodos permite:
- Maior robustez
- Comparação entre importância estrutural e informacional
- Redução de vieses de interpretação

📌 *(Inserir gráfico de barras comparando LOFO vs Permutação)*  
📂 **assets/feature_importance/**

---

## 🧠 Conclusão

Os resultados indicam que o modelo Ridge Regressor, aliado à validação cruzada e à engenharia de atributos, é capaz de **capturar padrões socioeconômicos relevantes**, mesmo em um conjunto de dados reduzido.

A análise de importância das variáveis evidencia que **renda, educação e indicadores sociais compostos** exercem papel central na definição do IDH, reforçando achados da literatura socioeconômica.

---