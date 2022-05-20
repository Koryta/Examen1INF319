install.packages("dplyr")
mean(df$App)

# vectores de las cartas
palo<-c("corazon","trebol","espada","diamante")

numeroC<-c(1,2,3,4,5,6,7,8,9,10,11,12,13)
numeroT<-c(1,2,3,4,5,6,7,8,9,10,11,12,13)
numeroE<-c(1,2,3,4,5,6,7,8,9,10,11,12,13)
numeroD<-c(1,2,3,4,5,6,7,8,9,10,11,12,13)

colorpalo<-c("rojo","negro")

#creamos el dataframe de las cartas

cartas_df <-data.frame(palo,numeroC,numeroD,numeroE,numeroT,colorpalo)
#mostrar el dataframe
cartas_df

# mostrar una carta
cartas_df[1,1]


