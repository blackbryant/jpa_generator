# JPA Class 產生器

使用說明
語法： codeGen.py [options] [file]  <br>
指令參數 ： -i --ifile    <br>
指令參數 ： -h -help .   <br>

本產生器用來產生Bean, Repository, compositePK, Service interface, Service impelemt的類別，目錄預設的方式

 - 根目錄：由 XXX.jpa的package中取得 
 - Bean目錄    :  根目錄＋.bean 
 - Repository目錄  :  根目錄＋.repository 
 - ＣompositePK目錄  :  根目錄＋.bean.compositePK 
 - 服務介面目錄  : 根目錄＋service.face 
 - 服務實作目錄 ： 根目錄＋.service.imp

範例1： python codeGen.py --help
>結果
===JPA Generator Tool===
syntax: codeGen.py [options] [file]
-i --ifile 
example: 
codeGen.py -if baseP01.dao

範例2：python codeGen.py -i baseP01.jpa
>結果
Input file : baseP01.jpa
Bean output file : com/blackteam/cms/base/bean/BaseP01Bean.java  <br>
Repository output file : com/blackteam/cms/base/repository/BaseP01Repository.java  <br>
PK compiste output file : com/blackteam/cms/base/bean/compositePK/BaseP01BeanPK.java  <br>
Service interface output file :com/blackteam/cms/base/service/face/IBaseP01.java  <br>
Service implement output file : com/blackteam/cms/base/service/imp/BaseP01ServiceImp.java  <br>
