/*----------------------------------------------------------------------------*/
/* BaseP01                                                      
/*----------------------------------------------------------------------------*/
/* author : 000611
/* table  : DBO.BASEP01
/* target : 共用參數設定主檔
/* create : 2018/05/17 23:50:51
/* update : 2018/05/17 23:50:51
/*----------------------------------------------------------------------------*/
package com.blackteam.cms.base;



import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;


@Repository
public interface BaseP01 extends JpaRepository<BaseP01, String> { 
    public final static String AppId = "BASEP01 " ; 
    public final static String CLASS_VERSION ="" ; 
}
