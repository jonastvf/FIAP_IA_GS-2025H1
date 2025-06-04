#packages
install.packages("spdep")
install.packages("sgwr")
install.packages("VIM")
install.packages("sp")
install.packages("sf")
install.packages("tmap")
install.packages("GWmodel")

#libraries
library(sp)
library(sf)
library(tmap)
library(GWmodel)

#dados de treino
setwd("C:/Users/Userv/OneDrive/Documentos/Fiap/4a Fase/GS1/Dados")
data <- read.csv2("C:/Users/Userv/OneDrive/Documentos/Fiap/4a Fase/GS1/Dados/deslizamentos_ficticio_espacial.csv")
names(data)

#TIPAGEM DATA FRAME DE TREINO

##check1
str(data$latitude)
str(data$longitude)

##dados coordenadas
data$latitude <- as.numeric(data$latitude)
data$longitude <- as.numeric(data$longitude)

##dados numericos
data$declividade_encosta_graus <- as.numeric(data$declividade_encosta_graus)
data$nivel_agua_profundidade_mt <- as.numeric(data$nivel_agua_profundidade_mt)
data$pressao_media_poros_kPa <- as.numeric(data$pressao_media_poros_kPa)
data$precipitacao_mm_24h <- as.numeric(data$precipitacao_mm_24h)
data$temperatura_media_c <- as.numeric(data$temperatura_media_c)
data$umidade_solo_percent <- as.numeric(data$umidade_solo_percent)
data$vibracao_terreno_hz <- as.numeric(data$vibracao_terreno_hz)

##dados temporais
data$timestamp <- as.POSIXct(data$timestamp, format = "%d/%m/%Y %H:%M", tz = "America/Sao_Paulo")

##fatores origem
data$tipo_solo <- as.factor(data$tipo_solo)

##Tratamento para converter em tipo coordenadas
coordenadas1 <- data[, c("longitude", "latitude")]	

#criando bd espacial para analises
dataSp <- SpatialPointsDataFrame(
    coords = coordenadas, 
    data = data, 
    proj4string = CRS("+proj=longlat +datum=WGS84 +no_defs")
) 

#fatores2
dataSp$tipo_solo <- as.factor(dataSp$tipo_solo)

#check2
class(dataSp)
summary(dataSp)

#MODELO

##Definindo a formula do GWR
formula_gwr <- risco_deslizamento ~ declividade_encosta_graus +
                                    presenca_agua_subterranea +
                                    nivel_agua_profundidade_mt +
                                    pressao_media_poros_kPa +
                                    precipitacao_mm_24h +
                                    temperatura_media_c +
                                    umidade_solo_percent +
                                    vibracao_terreno_hz +
                                    densidade_ocupacao_pessoas_km2

##Definindo a largura da Banda ótima (bw)
bw <- bw.gwr(
    formula = formula_gwr, 
    data = dataSp, 
    adaptive = TRUE, 
    kernel =  "bisquare"
)

cat("A largura da banda otimizada (nro de vizinhos) é:", bw, "\n")


##Ajustando o modelo
modelo_gwr <- gwr.basic(
  formula = formula_gwr, 
  data = dataSp,
  bw = bw, 
  adaptive = TRUE, 
  kernel =  "bisquare"
)

##Output modelo
modelo_gwr

#ANALISE

#conversoes
resultados_sf <- st_as_sf(modelo_gwr$SDF) #conversão para sf
tmap_mode("view") # Modo interativo do mapa


##Mapa para o coeficiente de declividade_encosta_graus
tm_shape(resultados_sf) +
  tm_dots(col = "declividade_encosta_graus",
          size = 0.2,
          palette = "RdBu", # azul para negativo, vermelho para positivo
          title = "Coef. Declividade da Encosta") +
  tm_layout(title = "Coef.da Declividade da Encosta")

##Mapa  para o coeficiente de presenca_agua_subterranea
tm_shape(resultados_sf) +
  tm_dots(col = "presenca_agua_subterranea",
          size = 0.2,
          palette = "RdBu", # azul para negativo, vermelho para positivo
          title = "Coef. Água Subterrânea") +
  tm_layout(title = "Coef. da Presença de Água Subterrânea")

##Exemplo de mapa para o R-quadrado Local
tm_shape(resultados_sf) +
  tm_dots(col = "Local_R2",
          size = 0.2,
          palette = "Greens", # Paleta sequencial (verde escuro = maior R2)
          title = "R-quadrado Local") +
  tm_layout(title = "Poder Explicativo Local do Modelo")

#MODELO PREDITIVO#

##dados de teste
dataTeste <- read.csv2("C:/Users/Userv/OneDrive/Documentos/Fiap/4a Fase/GS1/Dados/deslizamentos_ficticio_teste.csv", 
                       sep =",",
                       dec ="."
                       )
names(dataTeste)

#TIPAGEM DATA FRAME DE TESTE

##check3
str(dataTeste$latitude)
str(dataTeste$longitude)

##dados coordenadas
dataTeste$latitude <- as.numeric(dataTeste$latitude)
dataTeste$longitude <- as.numeric(dataTeste$longitude)

##dados numericos
dataTeste$declividade_encosta_graus <- as.numeric(dataTeste$declividade_encosta_graus)
dataTeste$nivel_agua_profundidade_mt <- as.numeric(dataTeste$nivel_agua_profundidade_mt)
dataTeste$pressao_media_poros_kPa <- as.numeric(dataTeste$pressao_media_poros_kPa)
dataTeste$precipitacao_mm_24h <- as.numeric(dataTeste$precipitacao_mm_24h)
dataTeste$temperatura_media_c <- as.numeric(dataTeste$temperatura_media_c)
dataTeste$umidade_solo_percent <- as.numeric(dataTeste$umidade_solo_percent)
dataTeste$vibracao_terreno_hz <- as.numeric(dataTeste$vibracao_terreno_hz)

##dados temporais
dataTeste$timestamp <- as.POSIXct(dataTeste$timestamp, format = "%d/%m/%Y %H:%M", tz = "America/Sao_Paulo")

##fatores origem
dataTeste$tipo_solo <- as.factor(dataTeste$tipo_solo)

##Tratamento para converter em tipo coordenadas
coordenadas2 <- dataTeste[, c("longitude", "latitude")]	

#criando bd espacial para analises

dataSpTeste <- SpatialPointsDataFrame(
  coords = coordenadas2, 
  data = dataTeste, 
  proj4string = CRS("+proj=longlat +datum=WGS84 +no_defs")
) 

#fatores2
dataSpTeste$tipo_solo <- as.factor(dataSpTeste$tipo_solo)

#check2
class(dataSpTeste)
summary(dataSpTeste)

##MODELAGEM

##predição
predict_gwr <- gwr.predict(
  formula = formula_gwr,
  data = dataSp,
  predictdata = dataSpTeste,
  bw = bw,
  adaptive = TRUE, 
  kernel = "bisquare"
  )

##Resultados gerais
predict_gwr$SDF
head(predict_gwr$SDF@data)

##Resultados no data frame de teste
dataTeste$risco_previsto <- predict_gwr$SDF@data$prediction
head(dataTeste)

#SISTEMA DE ALERTAS

##limiares de monitoramento
limiar_vermelho <- 0.7 #alerta critico, exige ação imediata
limiar_amarelo <- 0.4 #alerta alto, exige atenção

##Alertas
dataTeste$status_alerta <- "Verde"
dataTeste$status_alerta[dataTeste$risco_previsto >= limiar_amarelo] <- "Amarelo"
dataTeste$status_alerta[dataTeste$risco_previsto >= limiar_vermelho] <- "Vermelho"

dataTeste$status_alerta <- factor(dataTeste$status_alerta,
                                  levels = c("Verde", "Amarelo", "Vermelho"),
                                  ordered = TRUE)

head(dataTeste[, c("risco_deslizamento", "risco_previsto", "status_alerta")])

table(dataTeste$status_alerta)


#MAPA DE ALERTAS

##conversoes
dataTeste_sf <- st_as_sf(dataTeste, coords = c("longitude", "latitude"), crs = 4326)

##dataviz
cores_alerta <- c("Verde" = "forestgreen", "Amarelo" = "gold", "Vermelho" = "red")
tmap_mode("view") 

tm_shape(dataTeste_sf) +
  tm_dots(col = "status_alerta", 
          palette = cores_alerta, 
          size = 0.3, 
          title = "Predição de risco de deslizamentos") +
  tm_layout(title = "Status de risco", 
            legend.position = c("right", "bottom"))











