# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/jonastadeufernandes">Jonas T V Fernandes</a>
- <a href="https://www.linkedin.com/in/rannaleslie">Ranna Leslie</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Raphael da Silva</a> 
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

Por se tratar de zonas de risco conhecidas, prevemos o engajamento da comunidade habitante do local por meio de um aplicativo que poderá compartilhar a predição de risco para população, oferecer informações e permitir que a comunidade envie fotos e alertas a defesa civil. O aplicativo também terá por objetivo estreitar a comunicação entre cidadãos e defesa civil. 

**4. Como?**

O sistema será composto por:

- Banco de dados ("datalake"): armazenará todas as informações relevantes das áreas de risco e também do app
- Sensores IOT: implantados localmente, enviam informações via internet e rádio
- Sistema de Alerta: compõe uma rede de alertas, com app, mensagens, avisos sonoros locais entre outros
- Algoritimos de IA: a partir dos dados são capazes de prever condições em que o sinistro pode ocorrer, poderá ser treinado a priori (por meio de estudos técninos e simulações) e a posteri (por dados de outros sinistros).
- Ingestor de dados: recebe informações de outras fontes para melhorar as predições, exemplos: sistemas meterologicos, mapas e satélites. 

## 💽 Fontes de dados: 

- [Data GEO](https://datageo.ambiente.sp.gov.br/temas): Sistema ambiental do governo estadual de São Paulo
   - [Areas de risco de deslizamentos - Mapas](https://datageo.ambiente.sp.gov.br/coffey?_48_INSTANCE_KDzpt1cNV1RS_iframe_text=deslizamentos&enviar=Consultar&p_p_id=48_INSTANCE_KDzpt1cNV1RS&_48_INSTANCE_KDzpt1cNV1RS_iframe_avancado=false#_48_INSTANCE_KDzpt1cNV1RS_%3Dhttps%253A%252F%252Fdatageo.ambiente.sp.gov.br%252Fgeoportal%252Fcatalog%252Fsearch%252Fsearch.page%253Ftext%253Ddeslizamentos%2526avancado%253Dfalse)

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*


## 🗃 Histórico de lançamentos

* 0.5.0 - 06/06/2024
   
## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


