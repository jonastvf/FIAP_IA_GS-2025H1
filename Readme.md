# 📊 Sistema de Monitoramento Ambiental – API RESTful CRUD

## 🚀 1. Visão Geral
Este projeto entrega uma API RESTful robusta e escalável para gerenciamento de dados ambientais urbanos, desenvolvida com Python e Flask, integrada a um banco de dados MySQL, e totalmente containerizada com Docker para implantação ágil e confiável.

A API oferece operações completas de CRUD para entidades críticas como áreas monitoradas, sensores, incidentes e alertas, formando a base para soluções inteligentes de monitoramento ambiental e análise em tempo real.

## 🛠️ 2. Tecnologias Utilizadas

| Tecnologia   | Descrição                            | Versão Sugerida     |
|--------------|------------------------------------|---------------------|
| 🐍 Python    | Linguagem backend                   | 3.9+                |
| 🌐 Flask     | Framework web minimalista           | 2.x                 |
| 📦 Flask-RESTful | Extensão para criação simplificada de APIs | Última versão estável |
| 🗄️ MySQL    | Banco relacional para armazenamento| 8.0+                |
| 🐳 Docker    | Containerização e orquestração     | 20+                 |
| 🔗 SQLAlchemy| ORM para abstração do banco de dados| 1.4+               |
| 🧩 PyMySQL   | Driver Python para MySQL            | Última versão       |

## 🏗️ 3. Estrutura do Projeto
/
├── app.py # Aplicação Flask e definição de rotas
├── models.py # Modelos SQLAlchemy mapeando tabelas do MySQL
├── requirements.txt # Dependências Python
├── Dockerfile # Build da imagem Docker da aplicação
├── docker-compose.yml # Orquestração dos serviços (API + MySQL)
├── README.md # Documentação do projeto (você aqui 😉)
└── .env.example # Exemplo de variáveis de ambiente



## 🗄️ 4. Modelo de Dados e Entidades

| Tabela                 | Descrição                             |
|------------------------|-------------------------------------|
| 🌍 AREA_MONITORADA      | Áreas geográficas monitoradas        |
| 🚨 ALERTAS_DISPARADOS   | Alertas ambientais disparados        |
| ☀️ CLIMA_AREA          | Dados meteorológicos associados      |
| 🏠 DOMICILIOS_AREA      | Domicílios localizados nas áreas monitoradas |
| 👤 PESSOA_DOMICILIO     | Pessoas vinculadas a domicílios      |
| ⚠️ INCIDENTES_REGISTRADOS | Registro detalhado de incidentes  |
| 🌬️ SENSOR_VENTO        | Dados dos sensores de vento          |
| 🌀 SENSOR_VIBRACAO      | Dados dos sensores de vibração       |
| 🌧️ SENSOR_PLUVIOMETRICO | Dados pluviométricos                 |
| 💧 SENSOR_UMIDADE       | Dados de umidade do solo e ambiente  |

## ⚙️ 5. Guia de Instalação e Execução

### Pré-requisitos
- Docker e Docker Compose instalados (recomenda-se versões recentes)
- Git para clonar o repositório

### Passos

```bash
# Clonar o projeto
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Copiar arquivo de variáveis de ambiente e editar conforme necessário
cp .env.example .env
nano .env  # ou use seu editor preferido

# Construir e subir os containers
docker-compose up --build
A API ficará disponível em:
http://localhost:5000/

🔥 6. Endpoints REST (CRUD)
A API segue o padrão REST com endpoints estruturados para todas as entidades principais:

Ação	Método HTTP	Endpoint	Descrição
Criar	POST	/api/<entidade>	Insere um novo registro
Listar	GET	/api/<entidade>	Retorna todos os registros
Buscar por ID	GET	/api/<entidade>/<id>	Retorna registro específico
Atualizar	PUT	/api/<entidade>/<id>	Atualiza registro existente
Deletar	DELETE	/api/<entidade>/<id>	Remove registro

Exemplo: Área Monitorada
Método	Endpoint	Payload Exemplo (JSON)
POST	/api/area_monitorada	{ "nome": "Área Central", "descricao": "Zona urbana central" }
GET	/api/area_monitorada	—
GET	/api/area_monitorada/1	—
PUT	/api/area_monitorada/1	{ "descricao": "Área atualizada" }
DELETE	/api/area_monitorada/1	—

📋 7. Exemplo de Requisição e Resposta
Criar Sensor de Vento
bash
Copiar
Editar
POST /api/sensor_vento
Content-Type: application/json

{
  "area_id": 1,
  "velocidade": 15.3,
  "direcao": "NE"
}
Resposta HTTP 201 Created

json
Copiar
Editar
{
  "id": 25,
  "area_id": 1,
  "velocidade": 15.3,
  "direcao": "NE",
  "timestamp": "2025-06-06T15:30:00Z"
}
🐳 8. Docker e Orquestração
O Dockerfile define a imagem da aplicação Flask com todas as dependências.

O docker-compose.yml configura os serviços api e mysql, redes internas e volumes persistentes.

Variáveis de ambiente são usadas para configurar a conexão segura com o banco.

🛡️ 9. Boas Práticas Aplicadas
Código modular e organizado, facilitando manutenção e escalabilidade.

Uso de SQLAlchemy para evitar SQL Injection e aumentar portabilidade.

Respostas HTTP padronizadas com tratamento de erros consistente.

Containerização para garantir ambiente reprodutível.

Documentação clara para uso e manutenção do sistema.

📈 10. Próximos Passos
Implementar autenticação via JWT para segurança.

Adicionar testes unitários e de integração para garantir qualidade.

Criar documentação interativa via Swagger/OpenAPI.

Implementar filtros, paginação e ordenação nos endpoints GET.

Desenvolver dashboard frontend para visualização dos dados em tempo real.