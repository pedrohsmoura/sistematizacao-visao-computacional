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

**Nome:** `[PREENCHER]`

**Fonte:** `[Roboflow / Kaggle / COCO / outra]`

**Link:** `[PREENCHER]`

**Licença:** `[PREENCHER]`

**Total de imagens:** `[PREENCHER]`

**Formato das anotações:** `[YOLO / COCO / outro]`

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
| Treinamento |   `[ ]` |     `[ ]%` |
| Validação   |   `[ ]` |     `[ ]%` |
| Teste       |   `[ ]` |     `[ ]%` |
| **Total**   | **[ ]** |   **100%** |

A divisão dos dados será realizada com seed fixa para favorecer a reprodutibilidade dos experimentos.

---

# 🏷️ 6. Classes

As principais classes utilizadas no projeto são:

| Classe        | Descrição             | Tarefa                 |
| ------------- | --------------------- | ---------------------- |
| `Person`      | Pessoa/trabalhador    | Detecção + Segmentação |
| `Helmet`      | Capacete de segurança | Detecção               |
| `Safety Vest` | Colete de segurança   | Detecção               |

> A lista definitiva de classes será ajustada de acordo com o dataset selecionado.

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

### Distribuição das classes

![Distribuição das classes](docs/images/class_distribution.png)

### Exemplos do dataset

![Exemplos do dataset](docs/images/dataset_samples.png)

### Distribuição das imagens

![Distribuição dos dados](docs/images/dataset_distribution.png)

> As imagens acima serão adicionadas após a conclusão da análise exploratória.

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
Modelo: [YOLOv8 / YOLO11 / outro]
```

### Classes

```text
Person
Helmet
Safety Vest
```

### Hiperparâmetros

| Parâmetro     | Valor |
| ------------- | ----: |
| Modelo        | `[ ]` |
| Épocas        | `[ ]` |
| Batch size    | `[ ]` |
| Image size    | `[ ]` |
| Learning rate | `[ ]` |
| Optimizer     | `[ ]` |
| Seed          | `[ ]` |
| GPU           | `[ ]` |

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

| Classe      | Precision |  Recall |  AP@0.5 | AP@0.5:0.95 |
| ----------- | --------: | ------: | ------: | ----------: |
| Person      |     `[ ]` |   `[ ]` |   `[ ]` |       `[ ]` |
| Helmet      |     `[ ]` |   `[ ]` |   `[ ]` |       `[ ]` |
| Safety Vest |     `[ ]` |   `[ ]` |   `[ ]` |       `[ ]` |
| **mAP**     |   **[ ]** | **[ ]** | **[ ]** |     **[ ]** |

---

## Segmentação

| Classe    | Precision |  Recall |     IoU |    Dice |
| --------- | --------: | ------: | ------: | ------: |
| Person    |     `[ ]` |   `[ ]` |   `[ ]` |   `[ ]` |
| **Média** |   **[ ]** | **[ ]** | **[ ]** | **[ ]** |

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

### Comparação visual

```text
IMAGEM ORIGINAL

        ↓

┌─────────────────────┐
│      DETECÇÃO       │
│                     │
│  ┌───────────────┐  │
│  │    Pessoa     │  │
│  └───────────────┘  │
└─────────────────────┘

        VS.

┌─────────────────────┐
│     SEGMENTAÇÃO     │
│                     │
│    ███████          │
│   █████████         │
│    ███████          │
│      ███            │
└─────────────────────┘
```

Os resultados reais serão apresentados nesta seção após o treinamento.

---

# 🎥 15. Inferência em vídeo

Como etapa final, o sistema será aplicado a um vídeo real ou representativo de um canteiro de obras.

### Requisitos

* duração mínima: **30 segundos**;
* cenário relacionado ao projeto;
* processamento pelo modelo treinado;
* resultado gravado em vídeo.

### Informações

| Item               | Valor         |
| ------------------ | ------------- |
| Fonte              | `[PREENCHER]` |
| Duração            | `[PREENCHER]` |
| Resolução          | `[PREENCHER]` |
| FPS                | `[PREENCHER]` |
| Pessoas observadas | `[PREENCHER]` |

### 🎬 Demonstração

**Vídeo-pitch:** `[LINK DO YOUTUBE / GOOGLE DRIVE]`

**Vídeo com inferência:** `[LINK]`

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
git clone [URL_DO_REPOSITORIO]
cd [NOME_DO_REPOSITORIO]
```

---

## 16.2 Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 16.3 Abrir o notebook

O notebook principal está disponível em:

```text
notebooks/
└── projeto_seguranca_trabalho.ipynb
```

Também é possível executar diretamente pelo Google Colab:

**[ABRIR NO GOOGLE COLAB]**

---

## 16.4 Executar treinamento

```bash
python src/train_detection.py
```

Para o modelo de segmentação:

```bash
python src/train_segmentation.py
```

> Os comandos definitivos serão atualizados após a implementação do projeto.

---

# 📁 17. Estrutura do repositório

O projeto será organizado da seguinte maneira:

```text
seguranca-trabalho-visao-computacional/
│
├── README.md
│
├── requirements.txt
│
├── LICENSE
│
├── .gitignore
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_detection.ipynb
│   ├── 03_segmentation.ipynb
│   └── 04_evaluation_video.ipynb
│
├── src/
│   ├── data/
│   │   ├── prepare_dataset.py
│   │   └── validate_dataset.py
│   │
│   ├── detection/
│   │   ├── train.py
│   │   └── predict.py
│   │
│   ├── segmentation/
│   │   ├── train.py
│   │   └── predict.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│   │   └── confusion_matrix.py
│   │
│   └── video/
│       └── inference.py
│
├── configs/
│   ├── detection.yaml
│   └── segmentation.yaml
│
├── models/
│   └── README.md
│
├── results/
│   ├── figures/
│   ├── metrics/
│   ├── predictions/
│   └── videos/
│
├── docs/
│   ├── images/
│   └── relatorio.pdf
│
└── LICENSE
```

---

# 🧪 18. Reprodutibilidade

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

# 📌 19. Cronograma de desenvolvimento

| Fase   | Atividade                       | Status          |
| ------ | ------------------------------- | --------------- |
| Fase 1 | Definição do problema e dataset | 🟡 Em andamento |
| Fase 2 | Baseline de detecção            | ⚪ Pendente      |
| Fase 3 | Segmentação                     | ⚪ Pendente      |
| Fase 4 | Avaliação e vídeo               | ⚪ Pendente      |
| Fase 5 | Entrega e apresentação          | ⚪ Pendente      |

### Legenda

🟢 Concluído
🟡 Em andamento
⚪ Pendente

---

# 👥 20. Integrantes

| Integrante | Responsabilidades    |
| ---------- | -------------------- |
| `[Nome]`   | Dataset / EDA        |
| `[Nome]`   | Detecção             |
| `[Nome]`   | Segmentação          |
| `[Nome]`   | Avaliação            |
| `[Nome]`   | Vídeo / documentação |

> As responsabilidades podem ser compartilhadas entre os integrantes.

---

# 📚 21. Referências

### Dataset

> `[REFERÊNCIA DO DATASET]`

### YOLO / Ultralytics

> Ultralytics. **Ultralytics YOLO Documentation**. `[LINK]`

### PyTorch

> PyTorch. **PyTorch Documentation**. `[LINK]`

### OpenCV

> OpenCV. **OpenCV Documentation**. `[LINK]`

### Trabalhos científicos

> `[ADICIONAR ARTIGOS UTILIZADOS NO PROJETO]`

---

# 🤖 22. Uso de Inteligência Artificial

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

# ⚠️ 23. Limitações

O sistema desenvolvido possui limitações relacionadas principalmente à qualidade e diversidade do dataset utilizado.

Situações pouco representadas nos dados, como diferentes condições de iluminação, oclusões, distâncias elevadas, baixa resolução e ângulos de câmera distintos, podem afetar o desempenho dos modelos.

Além disso, o protótipo deve ser considerado uma ferramenta experimental de apoio ao monitoramento e não um substituto para procedimentos oficiais de segurança do trabalho ou para a atuação de profissionais especializados.

---

# 🔮 24. Trabalhos futuros

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

# 🏆 25. Conclusão

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
