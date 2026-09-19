# 🦺 Sistema de Visão Computacional para Segurança do Trabalho

### Detecção de EPIs e Segmentação de Pessoas em Canteiros de Obras

## 📌 Sobre o projeto

Este projeto apresenta o desenvolvimento de um **sistema de visão computacional aplicado à segurança do trabalho em canteiros de obras**, utilizando técnicas de aprendizado profundo para detectar equipamentos de proteção individual (EPIs) e segmentar trabalhadores presentes nas imagens.

O sistema foi desenvolvido como parte da atividade de sistematização da disciplina de **Visão Computacional e Reconhecimento de Padrões**, seguindo um pipeline completo de desenvolvimento:

```text
Dataset
   ↓
Análise exploratória
   ↓
Preparação dos dados
   ↓
Detecção de objetos
   ↓
Segmentação
   ↓
Avaliação
   ↓
Análise de erros
   ↓
Inferência em vídeo
```

O projeto tem como foco principal a identificação de:

* 👷 Pessoas;
* 🪖 Capacetes de segurança;
* 🦺 Coletes de segurança.

A solução combina **detecção de objetos** e **segmentação**, permitindo não apenas localizar os elementos presentes na cena, mas também representar de forma mais precisa a região ocupada pelos trabalhadores.

---

# 🎯 1. Objetivo

## Objetivo geral

Desenvolver e avaliar um sistema de visão computacional baseado em aprendizado profundo capaz de **detectar equipamentos de proteção individual e segmentar pessoas em imagens de canteiros de obras**, demonstrando seu funcionamento também em vídeo.

## Objetivos específicos

* Selecionar um dataset público com pelo menos 300 imagens anotadas;
* Realizar análise exploratória dos dados;
* Preparar os dados para treinamento;
* Treinar um detector moderno baseado em YOLO;
* Desenvolver um modelo de segmentação;
* Avaliar os modelos utilizando métricas apropriadas;
* Analisar falsos positivos e falsos negativos;
* Comparar detecção e segmentação;
* Executar inferência em imagens novas;
* Executar inferência em vídeo;
* Documentar todo o processo de desenvolvimento;
* Disponibilizar o projeto de forma reproduzível.

---

# 🏗️ 2. Problema

Canteiros de obras apresentam grande quantidade de trabalhadores, máquinas, equipamentos e estruturas, tornando o monitoramento contínuo das condições de segurança um desafio.

Entre os equipamentos de proteção individual utilizados nesses ambientes estão capacetes e coletes de segurança.

A proposta deste projeto é investigar como técnicas modernas de visão computacional podem auxiliar na identificação automática desses elementos em imagens e vídeos.

### Problema de visão computacional

> Como desenvolver um sistema capaz de identificar trabalhadores e equipamentos de proteção individual em imagens de canteiros de obras e segmentar os trabalhadores presentes na cena?

---

# 💡 3. Solução proposta

A solução será composta por duas tarefas principais.

### 🔎 Detecção de objetos

Utilização de um detector baseado em **YOLO** para localizar:

```text
Person
Helmet
Safety Vest
```

O detector produzirá:

* classe;
* bounding box;
* confiança da predição.

### 🎭 Segmentação

Utilização de um modelo de segmentação para produzir máscaras dos trabalhadores.

A segmentação permitirá representar a região ocupada pela pessoa de maneira mais precisa do que uma simples bounding box.

---

# 🧠 4. Arquitetura da solução

```text
                         ┌────────────────────┐
                         │      DATASET       │
                         └──────────┬─────────┘
                                    │
                                    ▼
                         ┌────────────────────┐
                         │       EDA          │
                         │ Análise dos dados  │
                         └──────────┬─────────┘
                                    │
                                    ▼
                         ┌────────────────────┐
                         │ Pré-processamento  │
                         └──────────┬─────────┘
                                    │
                       ┌────────────┴────────────┐
                       │                         │
                       ▼                         ▼
             ┌──────────────────┐      ┌──────────────────┐
             │    DETECÇÃO      │      │   SEGMENTAÇÃO    │
             │      YOLO        │      │ YOLO-seg /       │
             │                  │      │ Mask R-CNN       │
             └────────┬─────────┘      └────────┬─────────┘
                      │                         │
                      └────────────┬────────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │     AVALIAÇÃO      │
                         │ mAP / IoU / P/R    │
                         └──────────┬─────────┘
                                    │
                                    ▼
                         ┌────────────────────┐
                         │ ANÁLISE DE ERROS   │
                         └──────────┬─────────┘
                                    │
                                    ▼
                         ┌────────────────────┐
                         │ INFERÊNCIA VÍDEO   │
                         └────────────────────┘
```

---

# 📊 5. Dataset

## Dataset utilizado

**Nome:** `Construction Site Safety`

**Fonte:** `Kaggle — snehilsanyal/construction-site-safety-image-dataset-roboflow`

**Link:** `https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow`

**Total de imagens:** `[2.834]`

**Formato das anotações:** `YOLO (arquivos .txt)`

### Requisitos

O dataset deve possuir:

* ✅ mínimo de 300 imagens;
* ✅ imagens do domínio de construção civil;
* ✅ anotações;
* ✅ classes relacionadas aos objetos de interesse;
* ✅ dados suficientes para treinamento, validação e teste.

---

## 📦 Distribuição dos dados

| Conjunto    | Imagens | Percentual |
| ----------- | ------: | ---------: |
| Treinamento |   `[2.123]` |     `[ 74,9 ]%` |
| Validação   |   `[ 580 ]` |     `[ 20,5% ]%` |
| Teste       |   `[ 131     ]` |     `[ 4,6% ]%` |
| **Total**   | **[ 2.834 ]** |   **100%** |

A divisão dos dados será realizada com seed fixa para favorecer a reprodutibilidade dos experimentos.

---

# 🏷️ 6. Classes

As principais classes utilizadas no projeto são:

| Classe        | Descrição             | Tarefa                 |
| ------------- | --------------------- | ---------------------- |
| `Capacete`    | Capacete de segurança | Detecção               |
| `Máscara`     | Máscara | Detecção    |                        |
| `Sem Capacete`| Ausência de capacete  | Detecção               |
| `Sem Máscara` | Ausência de máscara   | Detecção               |
| `Sem Colete`  | Ausência de colete    | Detecção               |
| `Pessoa`      | Pessoa/trabalhador   | Detecção                |
| `Cone de Sinalização` | Cone de sinalização   | Detecção       |
| `Colete Refleto` | Colete refletor   | Detecção                |
| `Maquinaria` | Maquinaria   | Detecção                         |
| `Veículo` | Veículo   | Detecção                               |

> A versão utilizada no notebook contém 10 classes: Capacete, Máscara, Sem Capacete, Sem Máscara, Sem Colete, Pessoa, Cone de Sinalização, Colete Refletor, Maquinaria, Veículo.

---

# 🔍 7. Análise exploratória

Antes do treinamento dos modelos será realizada uma análise exploratória para compreender as características do dataset.

Serão analisados:

* quantidade de imagens;
* quantidade de objetos;
* distribuição das classes;
* resolução das imagens;
* tamanho dos objetos;
* distribuição das bounding boxes;
* imagens duplicadas;
* imagens inválidas;
* condições de iluminação;
* oclusões;
* desbalanceamento.

---

# ⚙️ 8. Tecnologias utilizadas

| Tecnologia            | Utilização                        |
| --------------------- | --------------------------------- |
| Python                | Linguagem principal               |
| PyTorch               | Framework de Deep Learning        |
| Ultralytics           | Treinamento dos modelos YOLO      |
| YOLO                  | Detecção de objetos               |
| YOLO-seg / Mask R-CNN | Segmentação                       |
| OpenCV                | Processamento de imagens e vídeos |
| NumPy                 | Manipulação numérica              |
| Matplotlib            | Visualização                      |
| Pandas                | Análise dos dados                 |
| Google Colab          | Ambiente de treinamento           |
| Git / GitHub          | Versionamento                     |

---

# 🧪 9. Metodologia

## 9.1 Preparação dos dados

As imagens serão verificadas e preparadas para o treinamento dos modelos.

As etapas incluem:

1. carregamento do dataset;
2. verificação das imagens;
3. verificação das anotações;
4. conversão de formato, quando necessário;
5. divisão em treino, validação e teste;
6. aplicação de técnicas de aumento de dados;
7. preparação dos arquivos de configuração.

---

## 9.2 Detecção de objetos

O detector será treinado utilizando **fine-tuning** de um modelo pré-treinado.

### Modelo

```text
Modelo: [YOLOv8]
```

### Classes

```text
Capacete
Máscara
Sem Capacete
Sem Máscara
Sem Colete
Pessoa
Cone de Sinalização
Colete Refletor
Maquinaria
Veículo
```

### Hiperparâmetros

| Parâmetro     | Valor |
| ------------- | ----: |
| Modelo        | `[ YOLOv8m ]` |
| Épocas        | `[40]` |
| Batch size    | `[16]` |
| Image size    | `[640]` |
| Learning rate | `[0.01 (lr0 padrão registrado pelo Ultralytics)]` |
| Optimizer     | `[auto]` |
| Seed          | `[42]` |
| GPU           | `[Tesla T4 (14913 MiB)]` |

---

# 🎭 9.3 Segmentação

Para a segmentação será utilizado:

```text
Modelo: [YOLO-seg / Mask R-CNN / outro]
```

O objetivo será gerar máscaras para os trabalhadores presentes nas imagens.

A segmentação será utilizada para comparar a representação de uma pessoa por:

```text
Detecção
      ↓
Bounding Box
```

versus:

```text
Segmentação
      ↓
Máscara da pessoa
```

---

# 📏 10. Métricas

## Detecção

Serão utilizadas:

### Precision

Mede a proporção das detecções positivas que são realmente corretas.

```text
Precision = TP / (TP + FP)
```

### Recall

Mede a capacidade do modelo de encontrar os objetos existentes.

```text
Recall = TP / (TP + FN)
```

### mAP@0.5

Avalia a precisão média considerando IoU igual a 0,5.

### mAP@0.5:0.95

Avalia o modelo considerando múltiplos limiares de IoU entre 0,5 e 0,95.

---

## Segmentação

A principal métrica será:

### IoU — Intersection over Union

```text
IoU = Área da interseção / Área da união
```

Quando apropriado, também será analisado o Dice Score.

---

# 📈 11. Resultados

> Esta seção será preenchida após o treinamento e avaliação final.

## Detecção

| Classe      |      Images   |  Instances       |  Box(P    |    R       |  mAP50-95 ) | AP@0.5:0.95 |
| ----------- |-------------  |  --------------- |--------   | ---------- | ----------  |  ---------- |
|  Capacete   |          30   |      110         |   0.962   |   0.913    |    0.97     |  0.649      |
|  Máscara    |          16   |       28         |   0.937   |   0.75     |    0.799    |  0.552      |
|  Sem Capacete |        25   |       41         |   0.866   |   0.634    |    0.595    |  0.361      |
|  Sem Máscara |         30   |       79         |   0.928   |   0.81     |    0.892    |  0.455      |
|  Sem Colete  |         36   |       90         |   1       |    0.818   |     0.844   |  0.551      |
|  Pessoa      |         59   |      174         |   0.933   |   0.845    |    0.912    |  0.593      |
|  Cone de Sinalização |  8   |       92         |   0.775   |   0.511    |    0.507    |  0.232      | 
|  Colete Refletor |     22   |       61         |   0.883   |   0.868    |    0.916    |  0.674      |
|  Maquinaria  |         22   |       44         |   0.925   |   0.837    |    0.882    |  0.665      |
|  Veículo    |          15   |       41         |   0.827   |   0.816    |    0.86     |  0.543      |
---


# 📊 12. Matriz de confusão

A matriz de confusão será utilizada para analisar as classes que apresentam maior dificuldade de classificação.

![Matriz de confusão](docs/images/confusion_matrix.png)

> Resultado será adicionado após o treinamento.

---

# 🔎 13. Análise de erros

A avaliação do modelo não será baseada somente nas métricas numéricas.

Serão analisados exemplos de:

### ❌ Falsos positivos

Situações em que o modelo identifica incorretamente determinado objeto.

![Falso positivo](docs/images/false_positive_01.png)

**Análise:** `[PREENCHER]`

---

### ❌ Falsos negativos

Situações em que um objeto existente não é identificado.

![Falso negativo](docs/images/false_negative_01.png)

**Análise:** `[PREENCHER]`

---

## Possíveis causas dos erros

Serão investigados fatores como:

* oclusão;
* baixa iluminação;
* objetos pequenos;
* baixa resolução;
* distância da câmera;
* sobreposição entre pessoas;
* objetos parcialmente visíveis;
* características semelhantes entre objeto e ambiente;
* distribuição desigual das classes.

---

# 🆚 14. Detecção × Segmentação

Uma das análises centrais do projeto será comparar os resultados obtidos pelas duas técnicas.

| Característica      | Detecção                    | Segmentação      |
| ------------------- | --------------------------- | ---------------- |
| Representação       | Bounding box                | Máscara          |
| Localização         | Aproximada                  | Pixel a pixel    |
| Informação espacial | Menor                       | Maior            |
| Complexidade        | Menor                       | Maior            |
| Custo computacional | Geralmente menor            | Geralmente maior |
| Contorno            | Não representa precisamente | Representa       |
| Aplicação           | EPIs e pessoas              | Pessoas          |


Os resultados reais serão apresentados nesta seção após o treinamento.

---

# 🎥 15. Inferência em vídeo

Como etapa final, o sistema será aplicado a um vídeo real ou representativo de um canteiro de obras.

### Requisitos

* duração mínima: **30 segundos**;
* cenário relacionado ao projeto;
* processamento pelo modelo treinado;
* resultado gravado em vídeo.


### 🎬 Demonstração

**Vídeo-pitch:** `[https://www.youtube.com/watch?v=ofIVM01xJx8]`

---

# 🚀 16. Como executar o projeto

## Requisitos

Recomenda-se utilizar:

* Google Colab com GPU;
* Python 3.x;
* Git;
* acesso ao dataset.

---

## 16.1 Clonar o repositório

```bash
git clone [https://github.com/pedrohsmoura/sistematizacao-visao-computacional.git]
cd [sistematizacao-visao-computacional]
```

---

## 16.2 Instalar dependências

```bash
pip install 
```

---

## 16.3 Abrir o notebook

O notebook principal está disponível em:

```text
notebooks/
└── visao_computacional_sistemarizacao_sec_trab.ipynb
```

Também é possível executar diretamente pelo Google Colab:

---


# 🧪 17. Reprodutibilidade

Para garantir a reprodução dos experimentos serão registrados:

* versão do Python;
* versões das bibliotecas;
* modelo utilizado;
* pesos iniciais;
* seed;
* hiperparâmetros;
* tamanho das imagens;
* batch size;
* número de épocas;
* dataset utilizado;
* divisão dos dados;
* hardware utilizado.

Sempre que possível, os experimentos serão executados utilizando seeds fixas.

---

# 📚 18. Referências

### YOLO / Ultralytics

> Ultralytics. **Ultralytics YOLO Documentation**.

### PyTorch

> PyTorch. **PyTorch Documentation**. 

### OpenCV

> OpenCV. **OpenCV Documentation**. 

---

# 🤖 19. Uso de Inteligência Artificial

Ferramentas de inteligência artificial generativa foram utilizadas como apoio durante o desenvolvimento do projeto.

A utilização ocorreu principalmente para:

* organização da documentação;
* esclarecimento de conceitos técnicos;
* apoio na revisão de código;
* identificação de possíveis erros;
* estruturação de explicações;
* apoio à organização do projeto.

As decisões sobre dataset, configuração dos experimentos, execução dos modelos, obtenção das métricas e análise dos resultados foram realizadas e verificadas pelos integrantes do grupo.

Os resultados apresentados no projeto correspondem aos experimentos efetivamente executados pelo grupo.

---

# ⚠️ 20. Limitações

O sistema desenvolvido possui limitações relacionadas principalmente à qualidade e diversidade do dataset utilizado.

Situações pouco representadas nos dados, como diferentes condições de iluminação, oclusões, distâncias elevadas, baixa resolução e ângulos de câmera distintos, podem afetar o desempenho dos modelos.

Além disso, o protótipo deve ser considerado uma ferramenta experimental de apoio ao monitoramento e não um substituto para procedimentos oficiais de segurança do trabalho ou para a atuação de profissionais especializados.

---

# 🔮 21. Trabalhos futuros

Como possíveis extensões do projeto, podem ser consideradas:

* inclusão de outros EPIs;
* utilização de datasets maiores;
* coleta de imagens em ambientes reais;
* treinamento com diferentes condições climáticas;
* rastreamento dos trabalhadores;
* utilização de **ByteTrack**;
* utilização de **DeepSORT**;
* geração automática de alertas;
* integração com câmeras de monitoramento;
* execução em dispositivos de borda;
* criação de dashboard;
* criação de aplicação web;
* publicação no **Hugging Face Spaces**;
* desenvolvimento de interface utilizando **Gradio**.

---

# 🏆 22. Conclusão

Este projeto apresenta uma abordagem de visão computacional aplicada à segurança do trabalho em canteiros de obras, combinando detecção de objetos e segmentação de pessoas.

A proposta busca demonstrar, de maneira prática, como modelos modernos de aprendizado profundo podem ser adaptados a um problema específico por meio de fine-tuning e avaliados utilizando métricas quantitativas e análise qualitativa.

O projeto também contempla a aplicação dos modelos em vídeo, aproximando o experimento de uma situação de utilização prática.

Ao final, espera-se disponibilizar um sistema funcional, documentado e reproduzível, acompanhado de código, notebook, resultados experimentais e demonstração em vídeo.

---

## 📎 Links do projeto

| Recurso                 | Link     |
| ----------------------- | -------- |
| 📓 Google Colab         | `[LINK]` |
| 💻 GitHub               | `[LINK]` |
| 🎥 Vídeo-pitch          | `[LINK]` |
| 🎬 Vídeo com inferência | `[LINK]` |
| 📊 Dataset              | `[LINK]` |
| 📄 Relatório técnico    | `[LINK]` |

---

<p align="center">

**🦺 Segurança do Trabalho · Visão Computacional · Deep Learning**

Desenvolvido como projeto acadêmico da Pós-graduação em Visão Computacional e Reconhecimento de Padrões.

</p>
