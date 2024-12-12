### Apresentação do Projeto: Identificação de Plantas por Imagem  

Este projeto utiliza aprendizado de máquina e redes neurais convolucionais (CNN) para identificar diferentes categorias de plantas a partir de imagens. A seguir, apresentamos uma visão geral do projeto e o link para acesso aos arquivos utilizados e gerados durante o desenvolvimento.

---

#### **Descrição do Projeto**  
- **Objetivo**: Classificar imagens de plantas em 8 categorias:  
  - *Daisy*, *Dandelion*, *Rose*, *Sunflower*, *Tulip*, *Orchid*, *Lavender*, *Hydrangea*.  
- **Tecnologias Utilizadas**:  
  - Linguagem: Python  
  - Bibliotecas: TensorFlow, NumPy, Matplotlib, OpenCV, Scikit-learn  
- **Arquitetura do Modelo**:  
  - Rede Neural Convolucional (CNN) com múltiplas camadas de convolução, pooling e densas.  
- **Resultado**:  
  - Modelo treinado com precisão de **96%** no conjunto de teste.  

---

#### **Conteúdo do Projeto**  

Acesso aos **[arquivos](https://drive.google.com/drive/u/2/folders/10GnSyr6heh_wUFy9MQA39cm5VyOTo1ST)** do projeto.

##### Estrutura dos Arquivos:  
1. **`data.pickle`**  
   - Arquivo contendo os dados pré-processados (imagens e rótulos).  

2. **Dataset**  
   - Conjunto de imagens utilizado para treinar e avaliar o modelo.  

3. **Modelo (`my_model.h5`)**  
   - Modelo treinado e salvo, pronto para ser reutilizado em predições futuras.  

4. **Output de Testes**  
   - Arquivo com os resultados de testes e a validação do modelo, indicando uma precisão de **96%**.  

---

#### **Demonstração**  
O projeto inclui visualizações das predições realizadas pelo modelo. As imagens de teste são exibidas com as categorias reais e previstas, facilitando a validação visual do desempenho.

---

#### **Como Utilizar**  
1. Faça o download dos arquivos disponíveis no Google Drive.  
2. Execute os seguintes scripts na ordem:  
   - **`utils.py`**: Para pré-processamento de dados (se necessário).  
   - **`myclassifier.py`**: Para treinar o modelo (caso deseje replicar o treinamento).  
   - **`detecp.py`**: Para avaliar o modelo e visualizar as predições.  

---

#### **Resultados Alcançados**  
- **Acurácia**: 96% no conjunto de teste.  
- **Aplicabilidade**: O modelo pode ser expandido para classificar novas categorias de plantas com a adição de mais dados.  

---

#### **Apresentação**  
- **[Vídeo demonstrativo](../presentation/will_flor.zip)**
- **[Apresentação em slides](../presentation/Apresentação%20de%20Proposta%20para%20Visão%20Computacional%20e%20Realidade%20Aumentada.pdf)**