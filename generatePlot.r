mydata = read.xls("mydata.xls")
deviceId = args[1]
time = args[2]
time <- mydata$ExcelDate
kWh <- mydata$kWh
fileNm = cbind("figure",deviceId, time)
lines(time, kWh, type="l", lwd=2, xlab="Time" lwd=2)
pdf(file=fileNm, height=3.5, width=5) 
