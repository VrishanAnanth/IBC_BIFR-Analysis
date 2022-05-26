library(rvest)
library(dplyr)
library(readxl)
library(RCurl)
library(pbapply)
library(stringr)

setwd("/Users/harneetsingh/Documents")

for (page_result in seq(1, 585, 1)){
  link = paste0("https://ibbi.gov.in/orders/nclt?title=&date=&nclt=&page=", page_result)
  page = read_html(link)
  case.date = page %>% html_nodes("td:nth-child(1)") %>% html_text()
  case.name = page %>% html_nodes("td:nth-child(2)") %>% html_text()
  case.remark = page %>% html_nodes("td:nth-child(3)") %>% html_text()
  case.details = rbind(case.details, data.frame(case.date, case.name, case.remark))
  print(paste("Page:", page_result))
}

write.csv(case.details, "IBC.Orders.csv")
