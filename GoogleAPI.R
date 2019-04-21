library(RoogleVision)
library(jpeg)

# Authenticate
options("googleAuthR.client_id" = "<<YOUR  CLIENT ID>>")
options("googleAuthR.client_secret" = "<<YOUR CLIENT SECRET>>")
options("googleAuthR.scopes.selected" = c("https://www.googleapis.com/auth/cloud-platform"))
googleAuthR::gar_auth()

# Labels  
getGoogleVisionResponse("<<PATH TO YOUR IMAGE>>", feature="LABEL_DETECTION")

# Emotions
face1 =  getGoogleVisionResponse("<<PATH  TO YOUR IMAGE>>", feature="FACE_DETECTION")
face1$joyLikelihood
face1$sorrowLikelihood
sl2 = readJPEG("<<PATH TO YOUR IMAGE>>")

# Plot image with  bounding boxes
par(mar=c(0,0,0,0))
plot(0, type='n', xlim=c(0,1200), ylim=c(0,1520), xaxt="n", yaxt="n", axes=FALSE, xlab="", ylab="")
rasterImage(sl2,0,0, 1199, 1519)
polygon(face1$boundingPoly$vertices[[1]]$x, 1520-(face1$boundingPoly$vertices[[1]]$y), lwd=2, col=NA, border="green")
points(face1$landmarks[[1]]$position$x, 1520-face1$landmarks[[1]]$position$y, col="blue", lwd=2, pch=16)

