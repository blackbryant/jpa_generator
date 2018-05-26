#!/usr/bin/python
# -*- coding: utf-8 -*-
import bean
import commUtil
 
'''
    選擇JAP腳本切換
'''
FOUR_SPACE="    "
BEAN_PRE_NAME="Bean"
BEAN_REPOSITORY_NAME="Repository"



def getTitle(bean):
	title="/*----------------------------------------------------------------------------*/"+"\n"\
	      "/* "+ bean.bean_master.entity+BEAN_PRE_NAME+"                                                      "+"\n"\
	      "/*----------------------------------------------------------------------------*/"+"\n"\
	      "/* author : "+bean.bean_master.author+"\n"\
	      "/* table  : "+bean.bean_master.table +"\n"\
	      "/* target : "+bean.bean_master.descript+"\n"\
	      "/* create : "+commUtil.getCurDate()+" "+commUtil.getCurTime() +"\n"\
	      "/* update : "+commUtil.getCurDate()+" "+commUtil.getCurTime() +"\n"\
		  "/* version: "+bean.bean_master.version+"\n "\
	      "/*----------------------------------------------------------------------------*/"+"\n"
	return title


def choseBeanScript(bean):
	content=""
	if bean.bean_master.version == "1.0" :
	       content=getJPA1VO(bean)
	return content

def getImportVOJar():
	importList=["java.io.Serializable","org.springframework.jdbc.core.RowMapper",\
	"javax.validation.constraints.*","org.apache.commons.lang.builder.ToStringBuilder",\
	"org.apache.commons.lang.builder.ToStringStyle","javax.validation.constraints.*",\
	"javax.persistence.Entity","javax.persistence.*","java.io.Serializable","java.util.Date"]
	importStr=""
	for importa in importList:
	    importStr= importStr+"import "+importa+";\n"
	return str(importStr)+"\n"+"\n"



def getJPA1VO(bean):
	packageName = "package "+bean.bean_master.package+".bean;"+"\n"*3
	title = getTitle(bean)
	preface ="/**"+"\n" \
	         "* "+bean.bean_master.descript+" Value Object "+"\n" \
	         "* Table Name        :"+bean.bean_master.table+"\n" \
	         "* Table Description :"+bean.bean_master.descript+"\n" \
	         "* Repository        :"+bean.bean_master.className+"\n" \
	         "* @Version          :"+bean.bean_master.model+" "+bean.bean_master.version+"\n" \
	         "* @since            :"+bean.bean_master.className+" "+commUtil.getCurDate()+"\n"\
	         "**/"+"\n"*2
	context=[]
	context.append("@Entity(name=\""+str(bean.bean_master.entity[0]).lower()+bean.bean_master.entity[1:]+"\") \n")
	context.append("@Table (name=\""+bean.bean_master.table+"\") \n")
	context.append("public class "+bean.bean_master.entity+BEAN_PRE_NAME+" implements Serializable  ")
	#if bean.bean_master.tool == "RowMapper":
	#   context.append(" , RowMapper<"+bean.bean_master.entity+"> ")
	context.append("{ "+"\n")
	
	context.append(FOUR_SPACE+"public final static String AppId = \""+bean.bean_master.entity.upper()+BEAN_PRE_NAME.upper()+" \" ; "+"\n")
	context.append(FOUR_SPACE+"public final static String CLASS_VERSION =\"\" ; "+"\n")
	context.append("/*----------------------------------------------------------------------------*/"+"\n"\
	               "/* "+bean.bean_master.table+" column Name */"+"\n"\
	               "/*----------------------------------------------------------------------------*/"+"\n")
	pkParamStr=[];
	pkParamTypes=[];
	pkParamNames=[];
	pk_count=0
	for detail in bean.bean_master.get_detail() : 
	    if detail.field_isKey.upper() == "Y":
	       pkParamTypes.append(detail.field_dataType)
	       pkParamNames.append(detail.entity_name)
	       pkParamStr.append(detail.field_dataType+" "+detail.entity_name)
	       pk_count=pk_count+1

	#field
	for detail in bean.bean_master.get_detail() :
	   context.append(FOUR_SPACE+"/** "+"\n" )
	   context.append(FOUR_SPACE+" *   "+detail.field_desc+"\n" )
	   context.append(FOUR_SPACE+" * @since  "+commUtil.getCurDate()+"\n" )
	   context.append(FOUR_SPACE+" */"+"\n")
	   if detail.field_isKey.upper() == "Y":
	      if pk_count >1:
	         context.append(FOUR_SPACE+"@EmbeddedId "+"\n" )
	      else:
	         context.append(FOUR_SPACE+"@Id "+"\n")
	      context.append(FOUR_SPACE+"@Column(name = \""+detail.field_name+"\", nullable = false) "+"\n")
	   else:
	      context.append(FOUR_SPACE+"@Column(name =\""+detail.field_name+"\" ) "+"\n")
	   
	   context.append(FOUR_SPACE+"@Max(value="+detail.field_width+", message = \""+detail.field_desc+"長度不能超過["+detail.field_width+"] \")"+"\n")

	   if detail.field_dataType.upper() =="DATE":
	      context.append(FOUR_SPACE+"@Temporal(value=TemporalType.DATE) "+"\n")
	      context.append(FOUR_SPACE+"private Date "+detail.entity_name+" ;"+"\n"*2)
	   elif detail.field_dataType.upper() =="TIME":
	      context.append(FOUR_SPACE+"@Temporal(value=TemporalType.TIME) "+"\n")
	      context.append(FOUR_SPACE+"private Date "+detail.entity_name+" ;"+"\n"*2)
	   else:
	      context.append(FOUR_SPACE+"private "+detail.field_dataType+" "+detail.entity_name+" ;"+"\n"*2)

	   

	#context.append("/** \n "+" * "+detail.field_desc+" \n  * @since "+commUtil.getCurDate() +" \n */"+"\n")

	# 建構子 constructor
	context.append(FOUR_SPACE+"/*----------------------------------------------------------------------------*/"+"\n"\
	               +FOUR_SPACE+"/* 建構子 constructor "+"\n"\
	               +FOUR_SPACE+"/*----------------------------------------------------------------------------*/"+"\n"*3)
	

	context.append(FOUR_SPACE+"/** \n"+FOUR_SPACE+" * 建構子 \n"+FOUR_SPACE+" * @since  "+commUtil.getCurDate()+"\n" +""+FOUR_SPACE+" */\n")
	context.append(FOUR_SPACE+"public "+bean.bean_master.entity+BEAN_PRE_NAME+"() { "+"\n"+" clear() ; }"+"\n")
	context.append(FOUR_SPACE+"public "+bean.bean_master.entity+BEAN_PRE_NAME+"("+','.join(pkParamStr)+") { "+"\n")
	for i in range(0,len(pkParamNames),1):
		context.append(FOUR_SPACE*2+"this."+pkParamNames[i]+"="+pkParamNames[i]+";\n")
	context.append(FOUR_SPACE+"}"+"\n")  

	#reset
	context.append(FOUR_SPACE+"/** \n"+FOUR_SPACE+" * 將所有的欄位 reset 成預設值 \n"+FOUR_SPACE+" * @since  "+commUtil.getCurDate()+"\n" +""+FOUR_SPACE+" */\n")
	context.append(FOUR_SPACE+"public void clear() { "+"\n")
	for detail in bean.bean_master.get_detail() :
	   if detail.field_format=="String":
	      context.append(FOUR_SPACE+"   this."+detail.entity_name+"=\"\" ;\n" )
	   elif detail.field_format=="int":
	      context.append(FOUR_SPACE+"   this."+detail.entity_name+"=0 ;\n" )
	   elif detail.field_format=="date" or detail.field_format=="time" :
	      context.append(FOUR_SPACE+"   this."+detail.entity_name+"= new Date() ;\n" )
	context.append(FOUR_SPACE+"} "+"\n")

	'''
	context.append("/** \n * 將自己複制一份出來 \n */ \n")
	context.append(FOUR_SPACE+"public "+bean.bean_master.entity+" myClone() { "+"\n")
	for detail in bean.bean_master.get_detail() :
	   if detail.field_format=="String":
	      context.append(FOUR_SPACE+"   this."+detail.entity_name+"=\"\" ;\n" )
	   elif detail.field_format=="int":
	      context.append(FOUR_SPACE+"   this."+detail.entity_name+"=0 ;\n" )
	   elif detail.field_format=="date" or detail.field_format=="time" :
	      context.append(FOUR_SPACE+"   this."+detail.entity_name+"= new Date() ;\n" )
	context.append(FOUR_SPACE+"} "+"\n")	
	'''
	#toString
	context.append(FOUR_SPACE+"/*----------------------------------------------------------------------------*/"+"\n"\
	               +FOUR_SPACE+"/*public methods "+"\n"\
	               +FOUR_SPACE+"/*----------------------------------------------------------------------------*/"+"\n"*2)
	context.append(FOUR_SPACE+"public String toString( ) { "+"\n")
	context.append(FOUR_SPACE*2+"return new ToStringBuilder(this, ToStringStyle.DEFAULT_STYLE) "+"\n")
	for detail in bean.bean_master.get_detail() :
	    context.append(FOUR_SPACE*2+".append(\""+detail.entity_name+"\", "+detail.entity_name+") "+"\n")
	context.append(".toString(); "+"\n")
	context.append(FOUR_SPACE+" } "+"\n")

	# detail
	context.append(FOUR_SPACE+"/*----------------------------------------------------------------------------*/"+"\n"\
	               +FOUR_SPACE+"/* get and set methods for the instance variables "+"\n"\
	               +FOUR_SPACE+"/*----------------------------------------------------------------------------*/"+"\n"*2)
	
	for detail in bean.bean_master.get_detail() :
	   if detail.field_format=="String":
	       #setter
	       context.append(FOUR_SPACE*2+"/** "+"\n")
	       context.append(FOUR_SPACE*2+" * "+"設定"+detail.field_desc+"\n")
	       context.append(FOUR_SPACE*2+" * @since  "+commUtil.getCurDate()+"\n" )
	       context.append(FOUR_SPACE*2+" */ "+"\n")
	       context.append(FOUR_SPACE*2+"public void set"+detail.entity_name[0].upper()+detail.entity_name[1:]+"("+detail.field_dataType+" "+detail.entity_name+"){ \n")
	       context.append(FOUR_SPACE*3+"this."+detail.entity_name+"=("+detail.entity_name+"==null)?\"\" : "+detail.entity_name+"; \n")
	       context.append(FOUR_SPACE*2+"} "+"\n")
	       #getter
	       context.append(FOUR_SPACE*2+"/** "+"\n")
	       context.append(FOUR_SPACE*2+" * "+"取得"+detail.field_desc+"\n")
	       context.append(FOUR_SPACE*2+" * @since  "+commUtil.getCurDate()+"\n" )
	       context.append(FOUR_SPACE*2+" */ "+"\n")
	       context.append(FOUR_SPACE*2+"public "+detail.field_dataType+" get"+detail.entity_name[0].upper()+detail.entity_name[1:]+"(){ \n")
	       context.append(FOUR_SPACE*3+" return this."+detail.entity_name+" ;\n")
	       context.append(FOUR_SPACE*2+"} "+"\n")
	       #getter ( 處理單引號的問題 )
	       context.append(FOUR_SPACE*2+"/** "+"\n")
	       context.append(FOUR_SPACE*2+" * "+"取得"+detail.field_desc+" (處理單引號的問題) \n")
	       context.append(FOUR_SPACE*2+" * @since  "+commUtil.getCurDate()+"\n" )
	       context.append(FOUR_SPACE*2+" */ "+"\n")
	       context.append(FOUR_SPACE*2+"public "+detail.field_dataType+" get"+detail.entity_name[0].upper()+detail.entity_name[1:]+"S(){ \n")
	       context.append(FOUR_SPACE*3+" return this."+detail.entity_name+" ; \n")
	       context.append(FOUR_SPACE*2+"} "+"\n")
	   elif detail.field_format.upper()=="DATE" or detail.field_format.upper()=="TIME" :
	       #setter
	       context.append(FOUR_SPACE*2+"/** "+"\n")
	       context.append(FOUR_SPACE*2+" * "+"設定"+detail.field_desc+"\n")
	       context.append(FOUR_SPACE*2+" * @since  "+commUtil.getCurDate()+"\n" )
	       context.append(FOUR_SPACE*2+" */ "+"\n")
	       context.append(FOUR_SPACE*2+"public void set"+detail.entity_name[0].upper()+detail.entity_name[1:]+"( Date "+detail.entity_name+"){ \n")
	       context.append(FOUR_SPACE*3+"this."+detail.entity_name+"=("+detail.entity_name+"==null)? new Date() : "+detail.entity_name+"; \n")
	       context.append(FOUR_SPACE*2+"} "+"\n")
	       #getter
	       context.append(FOUR_SPACE*2+"/** "+"\n")
	       context.append(FOUR_SPACE*2+" * "+"取得"+detail.field_desc+"\n")
	       context.append(FOUR_SPACE*2+" * @since  "+commUtil.getCurDate()+"\n" )
	       context.append(FOUR_SPACE*2+" */ "+"\n")
	       context.append(FOUR_SPACE*2+"public Date get"+detail.entity_name[0].upper()+detail.entity_name[1:]+"(){ \n")
	       context.append(FOUR_SPACE*3+" return this."+detail.entity_name+" ; \n")
	       context.append(FOUR_SPACE*2+"} "+"\n")
	       #getter ( 處理單引號的問題 )
	       context.append(FOUR_SPACE*2+"/** "+"\n")
	       context.append(FOUR_SPACE*2+" * "+"取得"+detail.field_desc+" (處理單引號的問題) \n")
	       context.append(FOUR_SPACE*2+" * @since  "+commUtil.getCurDate()+"\n" )
	       context.append(FOUR_SPACE*2+" */ "+"\n")
	       context.append(FOUR_SPACE*2+"public String get"+detail.entity_name[0].upper()+detail.entity_name[1:]+"S(){ \n")
	       context.append(FOUR_SPACE*3+" return this."+detail.entity_name+".toString() ; \n")
	       context.append(FOUR_SPACE*2+"} "+"\n")
	context.append("} ")
	return title+packageName+str(getImportVOJar())+preface+''.join(context)   

'''
   產出PK類別
'''
def genPKClass(bean):
	pk_count=0
	for detail in bean.bean_master.get_detail() :
	    if detail.field_isKey.upper() == "Y":
	       pk_count = pk_count +1
	if pk_count<=1:
	   return ""

	title=getTitle(bean)
	packageName = "package "+bean.bean_master.package+";"+"\n"*3   
	voName=""+bean.bean_master.entity[0].upper()+bean.bean_master.entity[1:]+'PK'
	context=[]
	context.append("public class "+voName+" implements Serializable { \n")
	pk=[]
	constructor_field=""
	for detail in bean.bean_master.get_detail() :
	    if detail.field_isKey.upper() == "Y":
	       context.append(FOUR_SPACE+"/** "+"\n" )
	       context.append(FOUR_SPACE+" *   "+detail.field_desc+"\n" )
	       context.append(FOUR_SPACE+" * @since  "+commUtil.getCurDate()+"\n" )
	       context.append(FOUR_SPACE+" */"+"\n")
	       context.append(FOUR_SPACE+"@NotNull "+"\n")
	       context.append(FOUR_SPACE+"@Size(max = "+detail.field_width+") "+"\n")
	       context.append(FOUR_SPACE+"private String "+detail.entity_name +";"+"\n"*2)
	       pk.append(detail.field_dataType + ' '+detail.field_name)
	       constructor_field = constructor_field +FOUR_SPACE+" this."+detail.field_name+"="+detail.field_name+"\n"
	#constructor
	context.append(FOUR_SPACE+"public "+voName+"( "+','.join(pk)+") {"+"\n")
	context.append(FOUR_SPACE+constructor_field)

	context.append(FOUR_SPACE+"} "+"\n")
	#setter/getter
	for detail in bean.bean_master.get_detail() :
	   if detail.field_isKey.upper() == "Y":
	      context.append(getGetterAndSetterStr(detail))
	

	#toString
	context.append(FOUR_SPACE+"/*----------------------------------------------------------------------------*/"+"\n"\
	               +FOUR_SPACE+"/*public methods "+"\n"\
	               +FOUR_SPACE+"/*----------------------------------------------------------------------------*/"+"\n"*2)
	context.append(FOUR_SPACE+"public String toString( ) { "+"\n")
	context.append(FOUR_SPACE*2+"return new ToStringBuilder(this, ToStringStyle.DEFAULT_STYLE) "+"\n"*2)

	for detail in bean.bean_master.get_detail() :
	    context.append(FOUR_SPACE*2+".append(\""+detail.entity_name+"\", "+detail.entity_name+") "+"\n")
	context.append(FOUR_SPACE+"} "+"\n")

	context.append(" } "+"\n"*2)
	return  title+packageName+''.join(context)


def getGetterAndSetterStr(detail):
	sgStr=[]
	if detail.field_format=="String":
	    #setter
	    sgStr.append(FOUR_SPACE*2+"/** "+"\n")
	    sgStr.append(FOUR_SPACE*2+" * "+"設定"+detail.field_desc+"\n")
	    sgStr.append(FOUR_SPACE*2+" * @since  "+commUtil.getCurDate()+"\n" )
	    sgStr.append(FOUR_SPACE*2+" */ "+"\n")
	    sgStr.append(FOUR_SPACE*2+"public void set"+detail.entity_name[0].upper()+detail.entity_name[1:]+"("+detail.field_dataType+" "+detail.entity_name+"){ \n")
	    sgStr.append(FOUR_SPACE*3+"this."+detail.entity_name+"=("+detail.entity_name+"==null)?\"\" : "+detail.entity_name+"; \n")
	    sgStr.append(FOUR_SPACE*2+"} "+"\n")
	    #getter
	    sgStr.append(FOUR_SPACE*2+"/** "+"\n")
	    sgStr.append(FOUR_SPACE*2+" * "+"取得"+detail.field_desc+"\n")
	    sgStr.append(FOUR_SPACE*2+" * @since  "+commUtil.getCurDate()+"\n" )
	    sgStr.append(FOUR_SPACE*2+" */ "+"\n")
	    sgStr.append(FOUR_SPACE*2+"public "+detail.field_dataType+" get"+detail.entity_name[0].upper()+detail.entity_name[1:]+"(){ \n")
	    sgStr.append(FOUR_SPACE*3+" return this."+detail.entity_name+" \n")
	    sgStr.append(FOUR_SPACE*2+"} "+"\n")
	return ''.join(sgStr)
	



########################## DAO #########################################################
def choseDaoScript(bean):
	content=""
	if bean.bean_master.version == "1.0" :
	       content=getJPA1Repository(bean)
	return content

def getJPA1Repository(bean):
	entity_name =  bean.bean_master.entity+BEAN_PRE_NAME #BaseP01+Bean
	repository_name=bean.bean_master.entity+BEAN_REPOSITORY_NAME 
	repository_package="repository"
	title="/*----------------------------------------------------------------------------*/"+"\n"\
	      "/* "+ repository_name +"                                  "+"\n"\
	      "/*----------------------------------------------------------------------------*/"+"\n"\
	      "/* author : "+bean.bean_master.author+"\n"\
	      "/* table  : "+bean.bean_master.table +"\n"\
	      "/* target : "+bean.bean_master.descript+"\n"\
	      "/* create : "+commUtil.getCurDate()+" "+commUtil.getCurTime() +"\n"\
	      "/* update : "+commUtil.getCurDate()+" "+commUtil.getCurTime() +"\n"\
	      "/*----------------------------------------------------------------------------*/"+"\n"
	packageName = "package "+bean.bean_master.package+"."+repository_package+";"+"\n"*4
	context=[]
	context.append("@Repository"+"\n")
	context.append("public interface "+repository_name+" extends JpaRepository<"+entity_name+", String> { "+"\n")
	context.append(FOUR_SPACE+"public final static String AppId = \""+entity_name.upper()+" \" ; "+"\n")
	context.append(FOUR_SPACE+"public final static String CLASS_VERSION =\"\" ; "+"\n")
	context.append("\n"*2)
	count = getPKCount(bean.bean_detail)
	#method
	no=1
	where=[]
	param=[]
	for detail in bean.bean_master.get_detail() : 
	    print "no:"+str(no)
	    if detail.field_isKey.upper() == "Y":
	       where.append(" b."+detail.field_name+"=:"+detail.field_name)
	       data_type = "Date" if detail.field_dataType.upper() == "TIME" else detail.field_dataType
	       param.append("@Param(\""+detail.field_name+"\") "+data_type +" "+ detail.field_name)
	       context.append(FOUR_SPACE+"@Query(value=\"SELECT b FROM "+entity_name+" b WHERE "+" AND ".join(where)+" \" )"+"\n" )
	       if count==1 or no==count:
	          context.append(FOUR_SPACE+"public  "+entity_name+ " findByAllPK("+", ".join(param)+");"+"\n")
	       else :	
	             serial = str(no)
	             context.append(FOUR_SPACE+"public  "+entity_name+ " findByPK"+serial+"("+str(", ".join(param))+");"+"\n"*2)
	       no=no+1
	importp = bean.bean_master.package+".bean."+entity_name



	context.append("\n\n"+"}"+"\n")
	return title + packageName+ getImportDAOJar(importp)+''.join(context)

def getPKCount(detail):
	pk_count=0
	for detail in bean.bean_master.get_detail() : 
	    if detail.field_isKey.upper() == "Y":
	       pk_count=pk_count+1
	return pk_count




def getImportDAOJar(importp):
	importList=["org.springframework.data.jpa.repository.JpaRepository",\
	"org.springframework.data.jpa.repository.Query","org.springframework.data.repository.query.Param",\
	"org.springframework.stereotype.Repository"]
	importStr=""
	importList.append(importp)
	for importa in importList:
	    importStr= importStr+"import "+importa+";\n"
	return str(importStr)+"\n"+"\n"	


def getBeanClassName(entity_name):
	return entity_name+"Bean"

def getPKClassName(entity_name):
	return entity_name+"BeanPK"

def getRepositoryClassName(entity_name):
	return entity_name+"Repository"


