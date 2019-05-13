# library for creating graphics
library(ggplot2)
# library for 
library(GGally)
# Data Mining with R
library(DMwR)
set.seed(300)
SKUjoinHardlines <- read.csv("/Users/qiancai/Downloads/2019Hackathon/SKUjoinHardlines.csv", header = TRUE)

SKUjoinHardlines.y = SKUjoinHardlines[32]

# function for withinSSrange for centreroids
withinSSrange <- function(data, low, high, maxiter){
  withinss = array(0, dim=c(high-low+1));
  for(i in low:high){
    withinss[i-low+1] <- kmeans(data, i, maxiter)$tot.withinss
  }
  withinss
}
# plotting of scaled centres from 2 to 15
plot(withinSSrange(Customer.scale,2,15,150))
# creating and assigning data to clusters
SpUkm = kmeans(SKUjoinHardlines.SpU, 2, 150)
# taking out the real centres-unscaling
Customer.realCenters = unscale(ckm$centers, Customer.scale)
# binding the cluster with data.
ClusteredSKUjoinHardlines = cbind(SKUjoinHardlines, SpUkm$cluster)
plot(ClusteredSKUjoinHardlines[5:6], col=SpUkm$cluster)
write.csv(ClusteredSKUjoinHardlines, file = "/Users/qiancai/Downloads/2019Hackathon/ClusteredSKUjoinHardlines.csv", col.names = TRUE)

# Products
set.seed(42)
Product <- read.csv("/Users/qiancai/OneDrive - Saint Marys University/semaster2/5580Data&TextMining/A1/ProductCluster2.csv")
ggpairs(Product[,which(names(Product)!="ITEM_SK")], upper = list(continuos = ggally_points), lower = list(continuos = "points"), title = "Product before outlier removal")
pro.clean <- Product[Product$ITEM_SK != 11740941,]
pro.clean_1 <- pro.clean[pro.clean$Month != 9,]
View(pro.clean_1)
Product.scale = scale(pro.clean_1[2:4])
View(Product.scale)
plot(withinSSrange(Product.scale,2,15,150))
pkm = kmeans(Product.scale, 5, 150)
Product.realCenters = unscale(pkm$centers, Product.scale)
plot(ClusteredCustomer[2:5], col=pkm$cluster)
ProductCluster = cbind(pro.clean_1, pkm$cluster)
plot(ProductCluster[2:5], col=pkm$cluster)
write.csv(ProductCluster, file = "/Users/qiancai/OneDrive - Saint Marys University/semaster2/5580Data&TextMining/A1/ProductCluster.csv", col.names = FALSE)
