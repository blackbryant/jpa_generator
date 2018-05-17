package com.blackteam.cms.base;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import com.blackteam.cms.base.repository.BaseP01Repository;


/*----------------------------------------------------------------------------*/
/* BaseP01                                                      
/*----------------------------------------------------------------------------*/
/* author : 000611
/* target : 共用參數設定主檔
/* create : 2018/05/17 23:50:51
/* update : 2018/05/17 23:50:51
/* version: 1.0
 /*----------------------------------------------------------------------------*/
@Service 
public class BaseP01ServiceImp implements IBaseP01 { 
    public final static String AppId = "BASEP01 " ; 
    public final static String CLASS_VERSION ="" ; 

    /** 
     *   共用參數設定主檔
     * @since  2018/05/17
     */
    @Autowired 
    private BaseP01Repository BaseP01Repository; 
 } 