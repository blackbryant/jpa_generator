#!/usr/bin/python
# -*- coding: utf-8 -*-

class bean_master():
   def __init__(self):
       self._detail = []

   @property
   def table(self):
       return self.table
   @property
   def project(self):
       return self.project
   @property
   def className(self):
       return self.className
   @property
   def package(self):
       return self.package
   @property
   def entity(self):
       return self.entity
   @property
   def author(self):
       return self.author   
   @property
   def descript(self):
       return self.descript     
   @property
   def model(self):
       return self.model  
   @property
   def version(self):
       return self.version
   
   @property
   def tool(self):
       return self.tool
   
   def add_detail(self,new_detail):
       self._detail.append(new_detail)

   def get_detail(self):
       return self._detail
   
   def toString(self):
       context = '[project]:{0},[table]:{1},[className]:{2},[package]:{3},[entity]:{4},[author]:{5},[descript]:{6} \
                  [model]:{7}, [version]:{8} '.format(
           self.project,self.table,self.className,self.package, self.entity,self.author,self.descript,self.model, self.version)
       return context




class bean_detail():
   def __init__(self):
       self.entity_name=None
  
   @property
   def entity_name(self):
       return self.entity_name
   @property
   def field_dataType(self):
       return self.field_dataType
   @property
   def field_isKey(self):
       return self.field_isKey
   @property
   def field_name(self):
       return self.field_name
   @property
   def field_desc(self):
       return self.field_desc
   @property
   def field_width(self):
       return self.field_width
   @property
   def field_format(self):
       return self.field_format   
   @property
   def field_default(self):
       return self.field_default 


   def __repr__(self):
       return str(self.__dict__)
 



