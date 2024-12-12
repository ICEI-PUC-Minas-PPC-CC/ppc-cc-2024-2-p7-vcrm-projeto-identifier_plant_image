### Programação de Funcionalidades  

Este projeto foi estruturado com base em módulos que desempenham funções específicas para a identificação de plantas por meio de imagens. A seguir, apresentamos a programação das funcionalidades divididas por arquivos:

---

#### **1. `utils.py` - Utilitários para Manipulação de Dados**  
Este módulo é responsável por coletar, processar e preparar os dados necessários para o treinamento e teste do modelo.  

##### Funcionalidades:  
- **`make_data()`**  
  - Carrega as imagens de diferentes categorias a partir do diretório `data/flowers`.  
  - Pré-processa as imagens (redimensionamento, conversão de cores e normalização).  
  - Associa cada imagem ao rótulo correspondente com base na categoria.  
  - Salva os dados pré-processados no arquivo `data.pickle`.  

- **`load_data()`**  
  - Carrega os dados armazenados no arquivo `data.pickle`.  
  - Separa as imagens (*features*) e os rótulos (*labels*).  
  - Normaliza os valores das imagens para o intervalo `[0, 1]`.  
  - Retorna os dados prontos para o treinamento ou avaliação do modelo.  

---

#### **2. `myclassifier.py` - Treinamento do Classificador**  
Este módulo cuida da construção e treinamento do modelo de rede neural convolucional (CNN).  

##### Funcionalidades:  
- **Carregamento dos Dados**  
  - Utiliza a função `load_data()` para carregar as imagens e rótulos.  
  - Divide os dados em conjuntos de treinamento e teste (90% treinamento, 10% teste).  

- **Construção do Modelo**  
  - Define a arquitetura de uma CNN utilizando o *TensorFlow*.  
  - Inclui camadas convolucionais, pooling e densas, culminando em uma saída de 8 classes (*softmax*).  

- **Treinamento do Modelo**  
  - Compila o modelo com o otimizador Adam e a função de perda `sparse_categorical_crossentropy`.  
  - Treina o modelo por 10 épocas com um *batch size* de 100.  
  - Salva o modelo treinado no arquivo `my_model.h5` para reutilização.  

---

#### **3. `detect.py` - Avaliação e Predição**  
Este módulo realiza a avaliação do modelo e apresenta previsões em imagens do conjunto de teste.  

##### Funcionalidades:  
- **Carregamento do Modelo e Dados**  
  - Carrega o modelo treinado a partir do arquivo `my_model.h5`.  
  - Utiliza `load_data()` para obter o conjunto de dados.  

- **Avaliação do Modelo**  
  - Avalia o modelo utilizando o conjunto de teste e apresenta métricas de desempenho, como *accuracy*.  

- **Visualização de Previsões**  
  - Gera previsões para imagens do conjunto de teste.  
  - Exibe 9 imagens em um gráfico com as classes reais e preditas para validação visual.  
  - Salva o gráfico gerado em arquivos `.png`.  

---

### Organização dos Arquivos  
| Arquivo          | Funcionalidade Principal                                      |  
|-------------------|---------------------------------------------------------------|  
| **`utils.py`**    | Pré-processamento das imagens e gerenciamento de dados.       |  
| **`myclassifier.py`** | Construção, treinamento e salvamento do modelo CNN.         |  
| **`detect.py`**   | Avaliação do modelo e visualização das previsões.             |  
