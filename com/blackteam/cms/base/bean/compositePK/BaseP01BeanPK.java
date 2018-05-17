/*----------------------------------------------------------------------------*/
/* BaseP01                                                      
/*----------------------------------------------------------------------------*/
/* author : 000611
/* table  : DBO.BASEP01
/* target : 共用參數設定主檔
/* create : 2018/05/17 23:50:51
/* update : 2018/05/17 23:50:51
/* version: 1.0
 /*----------------------------------------------------------------------------*/
package com.blackteam.cms.base;


public class BaseP01PK implements Serializable { 
    /** 
     *   參數代碼
     * @since  2018/05/17
     */
    @NotNull 
    @Size(max = 10) 
    private String RefCode;

    /** 
     *   參數名稱
     * @since  2018/05/17
     */
    @NotNull 
    @Size(max = 50) 
    private String RefName;

    public BaseP01PK( String ref_code,String ref_name) {
         this.ref_code=ref_code
     this.ref_name=ref_name
    } 
        /** 
         * 設定參數代碼
         * @since  2018/05/17
         */ 
        public void setRefCode(String RefCode){ 
            this.RefCode=(RefCode==null)?"" : RefCode; 
        } 
        /** 
         * 取得參數代碼
         * @since  2018/05/17
         */ 
        public String getRefCode(){ 
             return this.RefCode 
        } 
        /** 
         * 設定參數名稱
         * @since  2018/05/17
         */ 
        public void setRefName(String RefName){ 
            this.RefName=(RefName==null)?"" : RefName; 
        } 
        /** 
         * 取得參數名稱
         * @since  2018/05/17
         */ 
        public String getRefName(){ 
             return this.RefName 
        } 
    /*----------------------------------------------------------------------------*/
    /*public methods 
    /*----------------------------------------------------------------------------*/

    public String toString( ) { 
        return new ToStringBuilder(this, ToStringStyle.DEFAULT_STYLE) 

        .append("compId", compId) 
        .append("RefCode", RefCode) 
        .append("RefName", RefName) 
        .append("RefDesc", RefDesc) 
        .append("RefValue", RefValue) 
        .append("Field1Name", Field1Name) 
        .append("Field2Name", Field2Name) 
        .append("Field3Name", Field3Name) 
        .append("Field4Name", Field4Name) 
        .append("Field5Name", Field5Name) 
        .append("Field6Name", Field6Name) 
        .append("Field7Name", Field7Name) 
        .append("Field8Name", Field8Name) 
        .append("Field9Name", Field9Name) 
        .append("Field10Name", Field10Name) 
        .append("createUser", createUser) 
        .append("createDate", createDate) 
        .append("createTime", createTime) 
        .append("updateUser", updateUser) 
        .append("updateDate", updateDate) 
        .append("updateTime", updateTime) 
    } 
 } 

