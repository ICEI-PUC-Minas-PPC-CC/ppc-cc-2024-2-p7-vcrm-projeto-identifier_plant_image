### Plano de Testes de Software  

Este documento apresenta o plano de testes elaborado para o projeto de identificação de plantas por imagem, com o objetivo de garantir a qualidade e o correto funcionamento do sistema em diferentes cenários.

---

#### **1. Objetivo**  
Validar as funcionalidades principais do sistema, desde o pré-processamento de dados até a avaliação e predição do modelo de classificação. O plano de testes visa identificar erros e garantir que o sistema atenda aos requisitos especificados.

---

#### **2. Escopo do Teste**  
- **Componentes Cobertos**:  
  - Funções de utilitários (`utils.py`).  
  - Treinamento do modelo (`myclassifier.py`).  
  - Avaliação e predição (`detecp.py`).  
- **Componentes Excluídos**:  
  - Alterações na arquitetura do modelo.  
  - Inclusão de novas categorias de plantas.

---

#### **3. Tipos de Testes**  
- **Teste de Unidade**:  
  Verificar se as funções individuais funcionam conforme o esperado.  
- **Teste de Integração**:  
  Garantir que os módulos interagem corretamente, como o carregamento de dados e o treinamento do modelo.  
- **Teste de Validação**:  
  Avaliar a precisão do modelo com base no conjunto de teste.  
- **Teste de Usabilidade**:  
  Certificar-se de que as visualizações geradas são compreensíveis e úteis.  

---

#### **4. Casos de Teste**

| **ID do Teste** | **Descrição**                                                   | **Entrada**              | **Saída Esperada**                                           | **Status** |
|------------------|-----------------------------------------------------------------|--------------------------|-------------------------------------------------------------|------------|
| **UT-01**        | Verificar carregamento de imagens e rótulos (`make_data`)       | Diretório de imagens     | Arquivo `data.pickle` com dados pré-processados             | Testado |
| **UT-02**        | Testar a normalização de imagens (`load_data`)                 | Arquivo `data.pickle`    | Matriz de imagens com valores normalizados                 | Testado |
| **IT-01**        | Testar treinamento do modelo CNN                               | Dados normalizados       | Arquivo `my_model.h5` salvo corretamente                   | Testado |
| **IT-02**        | Verificar a avaliação do modelo no conjunto de teste           | Dados de teste           | Métrica de precisão (e.g., >85% accuracy)                  | Testado |
| **VT-01**        | Validar previsões para imagens de teste                        | Conjunto de imagens      | Gráfico `.png` com previsões corretas                | Testado |
| **UT-03**        | Testar comportamento com dados corrompidos ou ausentes         | Arquivo de dados inválido| Tratamento de exceção sem travar o sistema                 | A ser testado |

---

#### **5. Critérios de Aceitação**
- O sistema deve atingir uma precisão mínima de **85%** no conjunto de teste.  
- Todas as funções devem lidar com entradas inválidas sem causar interrupções no sistema.  
- O modelo deve ser treinado e salvo corretamente no arquivo `my_model.h5`.  
- As visualizações geradas devem ser claras e condizentes com as previsões realizadas.  

---

#### **6. Ferramentas Utilizadas**
- **Frameworks de Teste**:  
  - *pytest* para automação de testes de unidade e integração.  
- **Bibliotecas de Suporte**:  
  - *TensorFlow*, *NumPy*, *Matplotlib* e *OpenCV* para validação funcional.  

---

#### **7. Riscos e Mitigações**
- **Risco**: Dados de treinamento insuficientes ou não balanceados.  
  - **Mitigação**: Realizar aumento de dados (*data augmentation*) para evitar sobreajuste.  
- **Risco**: Tempo de treinamento elevado.  
  - **Mitigação**: Utilizar GPU para acelerar o treinamento.  
- **Risco**: Modelo incapaz de generalizar para novas imagens.  
  - **Mitigação**: Implementar validação cruzada e ajustar hiperparâmetros.  

---

#### **8. Aprovação**
O sistema será considerado aprovado quando todos os casos de teste forem executados com sucesso e os critérios de aceitação forem atendidos.
