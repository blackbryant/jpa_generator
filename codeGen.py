#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, getopt
import bean
import jpaGen
import serviceGen
import commUtil
import os

## set default location 
base_location=""
bean_default_location=".bean"
repository_defalut_location=".repository"
pk_defalut_location=".bean.compositePK"
service_default_interface_location=".service.face"
service_default_imp_location=".service.imp"
dot_java=".java"


def usage():
  print "===JPA Generator Tool==="
  print "syntax: codeGen.py [options] [file]"
  print "-i --ifile "
  print "example: "
  print "codeGen.py -if baseP01.dao"
  sys.exit(0) 



def get_bean(filename):
   attributes = ['project','table','class','package','entity','author','descript','model','version']
   master = bean.bean_master()
   with open(filename, 'r') as f:
       for line in f.readlines():
           print line[0]
           if line[0] =="#" or line.count("-",0,len(line))>=1:
               continue
           if is_meta(line) ==True:
             if get_meta(line,"project") !="":
               master.project = get_meta(line,"project")
             elif get_meta(line,"table") !="":
               master.table = get_meta(line,"table")
             elif get_meta(line,"class") !="":
               master.className = get_meta(line,"class")
             elif get_meta(line,"package") !="":
               master.package = get_meta(line,"package")                 
             elif get_meta(line,"entity") !="":
               master.entity = get_meta(line,"entity")   
             elif get_meta(line,"author") !="":
               master.author = get_meta(line,"author")   
             elif get_meta(line,"descript") !="":
               master.descript = get_meta(line,"descript")   
             elif get_meta(line,"model") !="":
               master.model = get_meta(line,"model") 
             elif get_meta(line,"version") !="":
               master.version = get_meta(line,"version") 
             elif get_meta(line,"tool") !="":
               master.tool = get_meta(line,"tool") 
           if is_detail(line) == True:
              detail = bean.bean_detail()
              data =get_detail(line)
              detail.entity_name =data[0]
              detail.field_dataType=data[1]
              detail.field_isKey=data[2]
              detail.field_desc=data[3]
              detail.field_name=data[4]
              detail.field_width=data[5]
              #detail.field_format=data[6]
              detail.field_default=data[6]
              #print(detail)
              master.add_detail(detail)
      
   return master



def is_meta(str_line):
   data = str_line.split(":")
   if len(data)==2 :
       return True
   else:
       return False


def get_meta(str_line,name):
   data = str_line.split(':')
   try:
      if len(data)<=1 :
           raise Exception(""+str_line+" parse error ", data)
      else:
          if data[0].strip()==name:
              return  data[1].strip()
   except Exception,err:
        print(err)
   
   return ""
def is_detail(str_line):
   data = str_line.split(" ")
   if len(data)>=8 and  str_line.find(":")<=0 :
       return True
   return False
def del_space(string):
   split_string = string.replace("\t"," ")
   split_string = split_string.replace("\r"," ")
   #print(split_string)
   result_string = ','.join(split_string.split())
   #print(result_string)
   #print(result_string.split(",")[1])
   return result_string

def get_detail(str_line):
   data = del_space(str_line)
   return data.split(",")


def execute(filename):
  bean.bean_master =get_bean(filename)
  base_location = bean.bean_master.package
  dao_script=jpaGen.choseDaoScript(bean)
  bean_script=jpaGen.choseBeanScript(bean)
  pk_script = jpaGen.genPKClass(bean)

  bean_filename=commUtil.writeFile(commUtil.dot2Slash(base_location+bean_default_location)  ,jpaGen.getBeanClassName(bean.bean_master.entity)+dot_java,bean_script) 
  resitory_filename=commUtil.writeFile(commUtil.dot2Slash(base_location+repository_defalut_location)  ,jpaGen.getRepositoryClassName(bean.bean_master.entity)+dot_java,dao_script) 
  pk_filename=""
  if pk_script is not "":
      pk_filename=commUtil.writeFile(commUtil.dot2Slash(base_location+pk_defalut_location)  ,jpaGen.getPKClassName(bean.bean_master.entity)+dot_java,pk_script) 

  #service
  interface_service_script = serviceGen.getJPAInterfaceService(bean)
  sface_filename=commUtil.writeFile(commUtil.dot2Slash(base_location+service_default_interface_location), serviceGen.getInterfaceClassName(bean.bean_master.entity)+dot_java,interface_service_script )
  imp_service_script = serviceGen.getJPAService(bean,base_location+repository_defalut_location)
  simp_filename=commUtil.writeFile(commUtil.dot2Slash(base_location+service_default_imp_location), serviceGen.getImpClassName(bean.bean_master.entity)+dot_java,imp_service_script )
  return bean_filename, resitory_filename, pk_filename, sface_filename, simp_filename



def main(argv):
 
  inputfile = ''
  outputfile = ''
  if not len(sys.argv[1:]):
     usage()

  try:
     opts, args = getopt.getopt(sys.argv[1:],"i:h",["help","ifile"])
  except getopt.GetoptError:
     print 'codeGen.py -i <inputfile> -o <outputfile>'
     sys.exit(2)
  for opt, arg in opts:
    print arg
    if opt in ('-h',"--help"):
      usage()

    elif opt in ("-i","--ifile"):
      inputfile = arg
      b,r,pk,sf,si =execute(inputfile)

  print 'Input file : ' +inputfile
  print 'Bean output file : '+b
  print 'Repository output file : '+r
  print 'PK compiste output file : '+pk
  print 'Service interface output file :'+sf
  print 'Service implement output file : '+si

if __name__=="__main__":
  main(sys.argv)


