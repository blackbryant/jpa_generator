#!/usr/bin/python
# -*- coding: utf-8 -*-
import bean
import commUtil
import jpaGen
FOUR_SPACE="    "




def choseServiceScript(bean):
    content=""
    content=getJPAService(bean)
    return content

def getTitle(bean,className):
    title="/*----------------------------------------------------------------------------*/"+"\n"\
          "/* "+ className+"                                                      "+"\n"\
          "/*----------------------------------------------------------------------------*/"+"\n"\
          "/* author : "+bean.bean_master.author+"\n"\
          "/* target : "+bean.bean_master.descript+"\n"\
          "/* create : "+commUtil.getCurDate()+" "+commUtil.getCurTime() +"\n"\
          "/* update : "+commUtil.getCurDate()+" "+commUtil.getCurTime() +"\n"\
          "/* version: "+bean.bean_master.version+"\n "\
          "/*----------------------------------------------------------------------------*/"+"\n"
    return title

#######Service interface


def getJPAInterfaceService(bean):
    packageName = "package "+bean.bean_master.package+";"+"\n"*3
    entity_name= getInterfaceClassName(bean.bean_master.entity)
    title = getTitle(bean,entity_name)
    context=[]
    context.append("public interface "+entity_name+"Service { "+"\n")
    context.append(FOUR_SPACE+"public final static String AppId = \""+bean.bean_master.entity.upper()+" \" ; "+"\n")
    context.append(FOUR_SPACE+"public final static String CLASS_VERSION =\"\" ; "+"\n")
    context.append("} ")

    return packageName+title+''.join(context)


def getInterfaceClassName(entity_name):
	return "I"+entity_name

#######Service implement

def getImportJar(rep_location):
    importList=["org.slf4j.Logger","org.slf4j.LoggerFactory",\
    "org.springframework.stereotype.Service"]
    importList.append(rep_location)
    importStr=""
    for importa in importList:
        importStr= importStr+"import "+importa+";\n"
    return str(importStr)+"\n"+"\n"

def getJPAService(bean,rep_location):
    packageName = "package "+bean.bean_master.package+";"+"\n"*3
    
    entity_name=bean.bean_master.entity
    title = getTitle(bean,entity_name)
    repositoey_name=jpaGen.getRepositoryClassName(bean.bean_master.entity)
    importa = getImportJar(rep_location+"."+repositoey_name)
    context=[]
    context.append("@Service "+"\n")
    context.append("public class "+getImpClassName(entity_name)+" implements "+getInterfaceClassName(entity_name)+" { "+"\n")
    context.append(FOUR_SPACE+"public final static String AppId = \""+bean.bean_master.entity.upper()+" \" ; "+"\n")
    context.append(FOUR_SPACE+"public final static String CLASS_VERSION =\"\" ; "+"\n"*2)
    context.append(getAttributeDesc(bean))
    context.append(FOUR_SPACE+"@Autowired "+"\n")
    context.append(FOUR_SPACE+"private "+repositoey_name+" "+repositoey_name[0].upper()+repositoey_name[1:]+"; \n ")
    context.append("} ")
    
    return packageName+importa+title+''.join(context)


def getImpClassName(entity_name):
	return entity_name+"ServiceImp"


def getAttributeDesc(bean):
    desc=[]
    desc.append(FOUR_SPACE+"/** "+"\n" )
    desc.append(FOUR_SPACE+" *   "+bean.bean_master.descript+"\n" )
    desc.append(FOUR_SPACE+" * @since  "+commUtil.getCurDate()+"\n" )
    desc.append(FOUR_SPACE+" */"+"\n")
    return ''.join(desc)






