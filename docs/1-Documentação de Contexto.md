### Apresentação do Projeto: Identificação de Plantas por Imagem  

Este projeto tem como objetivo principal identificar espécies de plantas a partir de imagens utilizando aprendizado de máquina e redes neurais convolucionais (CNN). O sistema foi projetado para processar e classificar imagens em oito categorias distintas com alta precisão.

---

#### **Introdução**  
A proposta envolve o uso de técnicas de visão computacional para identificar plantas com base em características visuais, como formato das folhas, tipos de flores e outras propriedades específicas. Essa solução automatizada visa superar os desafios da identificação manual, fornecendo um método acessível, rápido e confiável para diversos públicos, como pesquisadores, agricultores e entusiastas da jardinagem.

---

#### **Hierarquia do Diretório do Projeto**  

O projeto foi estruturado da seguinte forma:  
```
.
├── data
│   └── flowers
│       ├── daisy
│       ├── dandelion
│       ├── rose
│       ├── sunflower
│       ├── tulip
│       ├── orchid
│       ├── lavender
│       └── hydrangea
├── data.pickle
├── detec.py
├── myclassifier.py
├── my_model.h5
├── requirements.txt
└── utils.py
```

---

#### **Passos para Execução do Projeto**

1. **Instale as Dependências**  
   Antes de executar qualquer script, instale as dependências do projeto usando o seguinte comando no terminal:  
   
   > pip install -r requirements.txt

2. **Faça o Download dos Arquivos Necessários**  
   Acesse e faça o download dos seguintes arquivos no [Google Drive](https://drive.google.com/drive/u/2/folders/10GnSyr6heh_wUFy9MQA39cm5VyOTo1ST):  
   - **`data.pickle`**: Contém os dados pré-processados (imagens e rótulos).  
   - **`my_model.h5`**: Modelo treinado e salvo para classificação. 
   - **`data`** : Contém o dataset de imagens para treinamento e teste.

3. **Estruture o Diretório**  
   Certifique-se de que a estrutura de diretórios siga o padrão listado acima, colocando o dataset dentro da pasta `data/flowers`.

4. **Execute os Scripts**  
   - **`utils.py`**: Realiza o pré-processamento das imagens e cria o arquivo `data.pickle`.  
   - **`myclassifier.py`**: Treina o modelo utilizando CNN e salva o modelo treinado em `my_model.h5`.  
   - **`detec.py`**: Avalia o modelo, realiza predições no conjunto de teste e exibe os resultados.

---

#### **Resultados Alcançados**  
- **Acurácia do Modelo**: 96% no conjunto de teste.  
- **Validação Visual**: As predições são apresentadas com comparações entre a classe real e a prevista, permitindo uma análise visual do desempenho.  

---

#### **Link para os Arquivos do Projeto**  
[Acesse os arquivos necessários no Google Drive](https://drive.google.com/drive/u/2/folders/10GnSyr6heh_wUFy9MQA39cm5VyOTo1ST)  

Esses arquivos incluem o dataset, os dados pré-processados, o modelo treinado e as validações realizadas durante o desenvolvimento do projeto.