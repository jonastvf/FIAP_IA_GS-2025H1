# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Grupo de SP e Interior

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/jonastadeufernandes">Jonas T V Fernandes</a>
- <a href="https://www.linkedin.com/in/rannaleslie">Ranna Leslie</a>
- <a href="https://www.linkedin.com/in/raphaelsilva-phael">Raphael da Silva</a> 
- <a href="https://www.linkedin.com/in/raphael-dinelli-8a01b278/">Raphael Dinelli Neto</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Levi Passos Silveira Marques</a>


## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>


## 📜 Descrição

**Sistema de gestão e monitoramento de deslizamentos (SMD)**

**1. O que:**

Criar um Eco-sistema gerenciador de áreas de risco de deslizamento de terras, capaz de monitorar em escala local áreas com risco de deslizamento em suas dimensões geologicas, climáticas e humana. 

**2. Porque:**

Atualmente, entidades que realizam o manejo de áreas de risco de deslizamento como a Defesa Civil, tem dificuldade de realizar o manejo e gestão das áreas de risco em suas diferentes dimensões. Dado que os sistemas de monitoramento atuais oferecem apenas imagens via satélite, agregadas no nível do município ou regionalidade. 

O sistema terá por príncipio oferecer a gestão do risco em menor escala, integrando tecnologias e diferentes camadas de dados que permitam a tomada de decisão ágil e manejo adequado do impacto.

**3. Onde, quando e para quem?**

O sistema será desenvolvido pensando em áreas de risco já conhecidas pela Defesa Civil, especialmente em contextos urbanos ou de maior densidade populacional. O objetivo é permitir o manejo adequado dos diferentes impactos quando um sinistro ocorre nesta área. 

Ele deverá ser capaz de descrever e medir condições de risco como: tipo do solo, curvas de nível do terreno, microclima, precipitação local, densidade de ocupação, domicilios (por raio de deslizamento), números de familias da região, condições de ocupação do espaço, tipo de residencias, residentes portadores de necessidades especiais, vibração do terreno, movimentações de solo, vento, umidade do solo e outras condições. 

O sistema deverá ser capaz de armazenar estas informações, gerar predições, alertas e calculos de impacto para simulação de ações coordenadas. 

Por se tratar de zonas de risco conhecidas, prevemos o engajamento da comunidade habitante do local por meio de alertas por celular, mas também alarmes que soem localmente. Futuramente, também imaginamos outras estratégias possíveis de engajamento da comunidade.

**4. Como?**

O sistema será composto por:

- Banco de dados: armazenará todas as informações relevantes das áreas de risco e também do app
- Sensores IOT: implantados localmente, enviam informações via internet e rádio
- Sistema de Alerta: compõe uma rede de alertas, com app, mensagens, avisos sonoros locais entre outros
- Algoritimos de IA: a partir dos dados são capazes de prever condições em que o sinistro pode ocorrer, poderá ser treinado a priori (por meio de estudos técninos e simulações) e a posteri (por dados de outros sinistros).
- Ingestor de dados: recebe informações de outras fontes para melhorar as predições, exemplos: sistemas meterologicos, mapas e satélites. 

**5. Arquitetura da solução**

A imagem abaixo representa a arquitetura proposta do sistema, integrando sensores, banco de dados e modelos de IA:

![Imagem do WhatsApp de 2025-06-05 à(s) 13 03 33_490367c7](https://github.com/user-attachments/assets/9dcb66d5-f2ff-4ce0-9013-e1cead20739c)


## 💽 Fontes de dados: 

- [Data GEO](https://datageo.ambiente.sp.gov.br/temas): Sistema ambiental do governo estadual de São Paulo
   - [Areas de risco de deslizamentos - Mapas](https://datageo.ambiente.sp.gov.br/coffey?_48_INSTANCE_KDzpt1cNV1RS_iframe_text=deslizamentos&enviar=Consultar&p_p_id=48_INSTANCE_KDzpt1cNV1RS&_48_INSTANCE_KDzpt1cNV1RS_iframe_avancado=false#_48_INSTANCE_KDzpt1cNV1RS_%3Dhttps%253A%252F%252Fdatageo.ambiente.sp.gov.br%252Fgeoportal%252Fcatalog%252Fsearch%252Fsearch.page%253Ftext%253Ddeslizamentos%2526avancado%253Dfalse)

- [Google Sheets](https://docs.google.com/spreadsheets/): Ferramenta online de planilhas
 
- [Planilha de Monitoramento do Global Solution - Google Sheets](https://docs.google.com/spreadsheets/d/1H1zP9-9wuWSaKQ42PPWfBeWI3orkBrMcKRiPaCnG0vY/edit?usp=sharing)
 
- Dados sintéticos de treino e teste para o algoritmo GWR: dada natureza do projeto, precisávamos gerar uma massa de dados para treinar o nosso modelo IA, mas não tinhamos o historico das métricas associadas aos nossos sensores disponíveis. Assim, optamos pela abordagem de criar dados sintéticos: treinamos o agente de IA Manus com o nosso MER, a proposta de trabalho da GS, nossa proposta de trabalho e os dados do Data GEO (acima). Posteriormente, solicitamos a ele que criasse 2 fontes de dados, uma para treino e outra para teste, combinando os dados das zonas de risco conhecidas e simulando os dados para as principais métricas e dimensões que compõem o modelo GWR que treinamos. O prompt está disponível [aqui](https://manus.im/share/ipbIW97xOv31p6r8YH0Ohb?replay=1).

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

### 📈 Monitoramento IoT com ESP32 e Google Sheets

O projeto foi desenvolvido na <a href="https://wokwi.com">Wokwi</a> junto com extensão para Visual Studio Code, utilizando as extensões <a href="https://platformio.org">PlatformIO</a>, para executar o circuito e compilar o código dentro do VS Code.

#### 🔧 Etapa para executar o projeto

**1. Instalar as extensões no VS Code necessárias para execução** 
- [C/C++ (ms-vscode.cpptools)](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [PlatformIO IDE (platformio.platformio-ide)](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)
- [Wokwi for VS Code (wokwi.wokwi-vscode)](https://marketplace.visualstudio.com/items?itemName=wokwi.wokwi-vscode)


```bash
code --install-extension ms-vscode.cpptools
code --install-extension platformio.platformio-ide
code --install-extension wokwi.wokwi-vscode
```


**2. O arquivo está presente na seguinte caminho:**

```sheel
FIAP_IA_GS-2025H1/src/ESP32
```

Dentro da pasta `src` está o arquivo `main.cpp`, onde se encontra o código principal do projeto.<br>
Em `diagram.json` está o circuito eletrônico do projeto.

Devido a plataforma **Wokwi** ser limitadas em sesnores especifícos, utilizamos:
- Potênciomentros simulando um sensor de vibração, onde ele detecta as vibrações no eixo X, Y e Z.
- Módulo LDR simula sensor de vento, quanto menor a luminosidade, maior o vento capturado no sensor.
- Módulo DHT22 utilizado para controle de temperatura e umidade.
- Chave Táctil (Push Button) para simular detecção de presença de chuva, onde botão precionado significa que está chovendo e envia valor TRUE, se não FALSE.
<br><br>

**3. ESP32 conectado com Google Sheets (Planilha do Google)**

O ESP32 conecta com Google Sheets, enviando os dados recebidos pelo sensor. Para isso é utilizado o conceito de *IoT (Internet of Things)* ou Internet das Coisas. Para isso, utilizamos o módulo WiFi do ESP32 e bibliotecas que possibilita a conexão com a internet. No caso a `WiFi.h`, `HTTPClient` e `WiFiUdp.h`.

Para conectar com o Google Sheets utilizamos a função ***Apps Script***, e adicionando o código de implementação e inserção dos dados vindo pelo ESP32 a planilha, sendo comunicados através de um link http. O script está disponibilizado no caminho
```sheel
FIAP_IA_GS-2025H1/documents/other/readme.md
```
Ao simular, ele conecta-se com ao WiFI e logo em seguida, num *delay* de 3 segundos ele vai enviando e inserindo dados dos sensores a planilha do Google Sheets.
<hr> 


### 🤖 Modelo GWR

O sistema de previsão e alertas foi construido no R, utilizando o modelo de Machine Learning chamado Regressão Geográficamente Ponderada (GWR). A escolha do modelo se deu pela natureza do problema, prever riscos de deslizamento em diferentes áreas partindo em um mesmo conjunto de variáveis monitoradas. Assim, entendemos que a ponderação do modelo seria mais adequada a dispersão do fenômeno a ser observado em cada área.  

#### 🔧 Etapa para executar o projeto

**1. Instalar as packages e libraries** 

Os pacotes e bibliotecas necessárias para rodar o modelo estão todas no código. O ponto de atenção se dá pelos dados, para os quais será necessário realizar uma alteração do caminho de acesso aos "csvs". Os dados estão divididos em treino e teste, e se encontram disponíveis na pasta src/Dados deste repositório. 


**2. O arquivo está presente na seguinte caminho:**

O modelo está disponível na pasta src/Modelo GWR deste repositório. Na pasta, é possível encontrar o script em R, mas também o html que contém o mapa gerado apartir das saídas do modelo, e nossa interpretação do níveis de risco e seu indicativo de monitoramento. 


## 🗃 Histórico de lançamentos

* 1.0.0 - 02/06/2025
   
## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


