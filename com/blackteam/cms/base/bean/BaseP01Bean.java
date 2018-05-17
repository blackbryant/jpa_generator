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


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;


/**
* 共用參數設定主檔 Value Object 
* Table Name        :DBO.BASEP01
* Table Description :共用參數設定主檔
* Repository        :baseP01DAO
* @Version          :JPA 1.0
* @since            :baseP01DAO 2018/05/17
**/

@Entity(name="baseP01") 
@Table (name="DBO.BASEP01") 
public class BaseP01 implements Serializable   , RowMapper<BaseP01> { 
    public final static String AppId = "BASEP01 " ; 
    public final static String CLASS_VERSION ="" ; 
/*----------------------------------------------------------------------------*/
/* DBO.BASEP01 column Name */
/*----------------------------------------------------------------------------*/
    /** 
     *   公司別
     * @since  2018/05/17
     */
    @Column(name ="compId" ) 
    @Max(value=18, message = "公司別長度不能超過[18] ")
    private String compId ;

    /** 
     *   參數代碼
     * @since  2018/05/17
     */
    @EmbeddedId 
    @Column(name = "ref_code", nullable = false) 
    @Max(value=10, message = "參數代碼長度不能超過[10] ")
    private String RefCode ;

    /** 
     *   參數名稱
     * @since  2018/05/17
     */
    @EmbeddedId 
    @Column(name = "ref_name", nullable = false) 
    @Max(value=50, message = "參數名稱長度不能超過[50] ")
    private String RefName ;

    /** 
     *   用途說明
     * @since  2018/05/17
     */
    @Column(name ="ref_desc" ) 
    @Max(value=100, message = "用途說明長度不能超過[100] ")
    private String RefDesc ;

    /** 
     *   參數值
     * @since  2018/05/17
     */
    @Column(name ="ref_value" ) 
    @Max(value=18, message = "參數值長度不能超過[18] ")
    private String RefValue ;

    /** 
     *   明細欄位1名稱
     * @since  2018/05/17
     */
    @Column(name ="field1_name" ) 
    @Max(value=20, message = "明細欄位1名稱長度不能超過[20] ")
    private String Field1Name ;

    /** 
     *   明細欄位2名稱
     * @since  2018/05/17
     */
    @Column(name ="field2_name" ) 
    @Max(value=20, message = "明細欄位2名稱長度不能超過[20] ")
    private String Field2Name ;

    /** 
     *   明細欄位3名稱
     * @since  2018/05/17
     */
    @Column(name ="field3_name" ) 
    @Max(value=20, message = "明細欄位3名稱長度不能超過[20] ")
    private String Field3Name ;

    /** 
     *   明細欄位4名稱
     * @since  2018/05/17
     */
    @Column(name ="field4_name" ) 
    @Max(value=20, message = "明細欄位4名稱長度不能超過[20] ")
    private String Field4Name ;

    /** 
     *   明細欄位5名稱
     * @since  2018/05/17
     */
    @Column(name ="field5_name" ) 
    @Max(value=20, message = "明細欄位5名稱長度不能超過[20] ")
    private String Field5Name ;

    /** 
     *   明細欄位6名稱
     * @since  2018/05/17
     */
    @Column(name ="field6_name" ) 
    @Max(value=20, message = "明細欄位6名稱長度不能超過[20] ")
    private String Field6Name ;

    /** 
     *   明細欄位7名稱
     * @since  2018/05/17
     */
    @Column(name ="field7_name" ) 
    @Max(value=20, message = "明細欄位7名稱長度不能超過[20] ")
    private String Field7Name ;

    /** 
     *   明細欄位8名稱
     * @since  2018/05/17
     */
    @Column(name ="field8_name" ) 
    @Max(value=20, message = "明細欄位8名稱長度不能超過[20] ")
    private String Field8Name ;

    /** 
     *   明細欄位9名稱
     * @since  2018/05/17
     */
    @Column(name ="field9_name" ) 
    @Max(value=20, message = "明細欄位9名稱長度不能超過[20] ")
    private String Field9Name ;

    /** 
     *   明細欄位10名稱
     * @since  2018/05/17
     */
    @Column(name ="field10_name" ) 
    @Max(value=20, message = "明細欄位10名稱長度不能超過[20] ")
    private String Field10Name ;

    /** 
     *   建立使用者
     * @since  2018/05/17
     */
    @Column(name ="create_user" ) 
    @Max(value=10, message = "建立使用者長度不能超過[10] ")
    private String createUser ;

    /** 
     *   建立日期
     * @since  2018/05/17
     */
    @Column(name ="create_date" ) 
    @Max(value=8, message = "建立日期長度不能超過[8] ")
    private String createDate ;

    /** 
     *   建立時間
     * @since  2018/05/17
     */
    @Column(name ="create_time" ) 
    @Max(value=6, message = "建立時間長度不能超過[6] ")
    private String createTime ;

    /** 
     *   修改使用者
     * @since  2018/05/17
     */
    @Column(name ="update_user" ) 
    @Max(value=10, message = "修改使用者長度不能超過[10] ")
    private String updateUser ;

    /** 
     *   修改日期
     * @since  2018/05/17
     */
    @Column(name ="update_date" ) 
    @Max(value=8, message = "修改日期長度不能超過[8] ")
    private String updateDate ;

    /** 
     *   修改時間
     * @since  2018/05/17
     */
    @Column(name ="update_time" ) 
    @Max(value=6, message = "修改時間長度不能超過[6] ")
    private String updateTime ;

    /*----------------------------------------------------------------------------*/
    /* 建構子 constructor 
    /*----------------------------------------------------------------------------*/


    /** 
     * 建構子 
     * @since  2018/05/17
     */
    public BaseP01() { 
 clear() ; }
    public BaseP01(SString  RefCodetString  RefCoderString  RefCodeiString  RefCodenString  RefCodegString  RefCode String  RefCode String  RefCodeRString  RefCodeeString  RefCodefString  RefCodeNString  RefCodeaString  RefCodemString  RefCodee) { 
        this.RefCode=RefCode
        this.RefName=RefName
    }
    /** 
     * 將所有的欄位 reset 成預設值 
     * @since  2018/05/17
     */
    public void clear() { 
       this.compId="" 
       this.RefCode="" 
       this.RefName="" 
       this.RefDesc="" 
       this.RefValue="" 
       this.Field1Name="" 
       this.Field2Name="" 
       this.Field3Name="" 
       this.Field4Name="" 
       this.Field5Name="" 
       this.Field6Name="" 
       this.Field7Name="" 
       this.Field8Name="" 
       this.Field9Name="" 
       this.Field10Name="" 
       this.createUser="" 
       this.createDate= new Date() 
       this.createTime= new Date() 
       this.updateUser="" 
       this.updateDate= new Date() 
       this.updateTime= new Date() 
    } 
/** 
 * 將自己複制一份出來 
 */ 
    public BaseP01Bean myClone() { 
       this.compId="" 
       this.RefCode="" 
       this.RefName="" 
       this.RefDesc="" 
       this.RefValue="" 
       this.Field1Name="" 
       this.Field2Name="" 
       this.Field3Name="" 
       this.Field4Name="" 
       this.Field5Name="" 
       this.Field6Name="" 
       this.Field7Name="" 
       this.Field8Name="" 
       this.Field9Name="" 
       this.Field10Name="" 
       this.createUser="" 
       this.createDate= new Date() 
       this.createTime= new Date() 
       this.updateUser="" 
       this.updateDate= new Date() 
       this.updateTime= new Date() 
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
    /*----------------------------------------------------------------------------*/
    /* get and set methods for the instance variables 
    /*----------------------------------------------------------------------------*/

        /** 
         * 設定公司別
         * @since  2018/05/17
         */ 
        public void setCompId(String compId){ 
            this.compId=(compId==null)?"" : compId; 
        } 
        /** 
         * 取得公司別
         * @since  2018/05/17
         */ 
        public String getCompId(){ 
             return this.compId 
        } 
        /** 
         * 取得公司別 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getCompIdS(){ 
             return this.compId 
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
         * 取得參數代碼 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getRefCodeS(){ 
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
        /** 
         * 取得參數名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getRefNameS(){ 
             return this.RefName 
        } 
        /** 
         * 設定用途說明
         * @since  2018/05/17
         */ 
        public void setRefDesc(String RefDesc){ 
            this.RefDesc=(RefDesc==null)?"" : RefDesc; 
        } 
        /** 
         * 取得用途說明
         * @since  2018/05/17
         */ 
        public String getRefDesc(){ 
             return this.RefDesc 
        } 
        /** 
         * 取得用途說明 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getRefDescS(){ 
             return this.RefDesc 
        } 
        /** 
         * 設定參數值
         * @since  2018/05/17
         */ 
        public void setRefValue(String RefValue){ 
            this.RefValue=(RefValue==null)?"" : RefValue; 
        } 
        /** 
         * 取得參數值
         * @since  2018/05/17
         */ 
        public String getRefValue(){ 
             return this.RefValue 
        } 
        /** 
         * 取得參數值 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getRefValueS(){ 
             return this.RefValue 
        } 
        /** 
         * 設定明細欄位1名稱
         * @since  2018/05/17
         */ 
        public void setField1Name(String Field1Name){ 
            this.Field1Name=(Field1Name==null)?"" : Field1Name; 
        } 
        /** 
         * 取得明細欄位1名稱
         * @since  2018/05/17
         */ 
        public String getField1Name(){ 
             return this.Field1Name 
        } 
        /** 
         * 取得明細欄位1名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField1NameS(){ 
             return this.Field1Name 
        } 
        /** 
         * 設定明細欄位2名稱
         * @since  2018/05/17
         */ 
        public void setField2Name(String Field2Name){ 
            this.Field2Name=(Field2Name==null)?"" : Field2Name; 
        } 
        /** 
         * 取得明細欄位2名稱
         * @since  2018/05/17
         */ 
        public String getField2Name(){ 
             return this.Field2Name 
        } 
        /** 
         * 取得明細欄位2名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField2NameS(){ 
             return this.Field2Name 
        } 
        /** 
         * 設定明細欄位3名稱
         * @since  2018/05/17
         */ 
        public void setField3Name(String Field3Name){ 
            this.Field3Name=(Field3Name==null)?"" : Field3Name; 
        } 
        /** 
         * 取得明細欄位3名稱
         * @since  2018/05/17
         */ 
        public String getField3Name(){ 
             return this.Field3Name 
        } 
        /** 
         * 取得明細欄位3名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField3NameS(){ 
             return this.Field3Name 
        } 
        /** 
         * 設定明細欄位4名稱
         * @since  2018/05/17
         */ 
        public void setField4Name(String Field4Name){ 
            this.Field4Name=(Field4Name==null)?"" : Field4Name; 
        } 
        /** 
         * 取得明細欄位4名稱
         * @since  2018/05/17
         */ 
        public String getField4Name(){ 
             return this.Field4Name 
        } 
        /** 
         * 取得明細欄位4名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField4NameS(){ 
             return this.Field4Name 
        } 
        /** 
         * 設定明細欄位5名稱
         * @since  2018/05/17
         */ 
        public void setField5Name(String Field5Name){ 
            this.Field5Name=(Field5Name==null)?"" : Field5Name; 
        } 
        /** 
         * 取得明細欄位5名稱
         * @since  2018/05/17
         */ 
        public String getField5Name(){ 
             return this.Field5Name 
        } 
        /** 
         * 取得明細欄位5名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField5NameS(){ 
             return this.Field5Name 
        } 
        /** 
         * 設定明細欄位6名稱
         * @since  2018/05/17
         */ 
        public void setField6Name(String Field6Name){ 
            this.Field6Name=(Field6Name==null)?"" : Field6Name; 
        } 
        /** 
         * 取得明細欄位6名稱
         * @since  2018/05/17
         */ 
        public String getField6Name(){ 
             return this.Field6Name 
        } 
        /** 
         * 取得明細欄位6名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField6NameS(){ 
             return this.Field6Name 
        } 
        /** 
         * 設定明細欄位7名稱
         * @since  2018/05/17
         */ 
        public void setField7Name(String Field7Name){ 
            this.Field7Name=(Field7Name==null)?"" : Field7Name; 
        } 
        /** 
         * 取得明細欄位7名稱
         * @since  2018/05/17
         */ 
        public String getField7Name(){ 
             return this.Field7Name 
        } 
        /** 
         * 取得明細欄位7名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField7NameS(){ 
             return this.Field7Name 
        } 
        /** 
         * 設定明細欄位8名稱
         * @since  2018/05/17
         */ 
        public void setField8Name(String Field8Name){ 
            this.Field8Name=(Field8Name==null)?"" : Field8Name; 
        } 
        /** 
         * 取得明細欄位8名稱
         * @since  2018/05/17
         */ 
        public String getField8Name(){ 
             return this.Field8Name 
        } 
        /** 
         * 取得明細欄位8名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField8NameS(){ 
             return this.Field8Name 
        } 
        /** 
         * 設定明細欄位9名稱
         * @since  2018/05/17
         */ 
        public void setField9Name(String Field9Name){ 
            this.Field9Name=(Field9Name==null)?"" : Field9Name; 
        } 
        /** 
         * 取得明細欄位9名稱
         * @since  2018/05/17
         */ 
        public String getField9Name(){ 
             return this.Field9Name 
        } 
        /** 
         * 取得明細欄位9名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField9NameS(){ 
             return this.Field9Name 
        } 
        /** 
         * 設定明細欄位10名稱
         * @since  2018/05/17
         */ 
        public void setField10Name(String Field10Name){ 
            this.Field10Name=(Field10Name==null)?"" : Field10Name; 
        } 
        /** 
         * 取得明細欄位10名稱
         * @since  2018/05/17
         */ 
        public String getField10Name(){ 
             return this.Field10Name 
        } 
        /** 
         * 取得明細欄位10名稱 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getField10NameS(){ 
             return this.Field10Name 
        } 
        /** 
         * 設定建立使用者
         * @since  2018/05/17
         */ 
        public void setCreateUser(String createUser){ 
            this.createUser=(createUser==null)?"" : createUser; 
        } 
        /** 
         * 取得建立使用者
         * @since  2018/05/17
         */ 
        public String getCreateUser(){ 
             return this.createUser 
        } 
        /** 
         * 取得建立使用者 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getCreateUserS(){ 
             return this.createUser 
        } 
        /** 
         * 設定建立日期
         * @since  2018/05/17
         */ 
        public void setCreateDate( Date createDate){ 
            this.createDate=(createDate==null)?"" : createDate; 
        } 
        /** 
         * 取得建立日期
         * @since  2018/05/17
         */ 
        public Date getCreateDate(){ 
             return this.createDate 
        } 
        /** 
         * 取得建立日期 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getCreateDateS(){ 
             return this.createDate 
        } 
        /** 
         * 設定建立時間
         * @since  2018/05/17
         */ 
        public void setCreateTime( Date createTime){ 
            this.createTime=(createTime==null)?"" : createTime; 
        } 
        /** 
         * 取得建立時間
         * @since  2018/05/17
         */ 
        public Date getCreateTime(){ 
             return this.createTime 
        } 
        /** 
         * 取得建立時間 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getCreateTimeS(){ 
             return this.createTime 
        } 
        /** 
         * 設定修改使用者
         * @since  2018/05/17
         */ 
        public void setUpdateUser(String updateUser){ 
            this.updateUser=(updateUser==null)?"" : updateUser; 
        } 
        /** 
         * 取得修改使用者
         * @since  2018/05/17
         */ 
        public String getUpdateUser(){ 
             return this.updateUser 
        } 
        /** 
         * 取得修改使用者 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getUpdateUserS(){ 
             return this.updateUser 
        } 
        /** 
         * 設定修改日期
         * @since  2018/05/17
         */ 
        public void setUpdateDate( Date updateDate){ 
            this.updateDate=(updateDate==null)?"" : updateDate; 
        } 
        /** 
         * 取得修改日期
         * @since  2018/05/17
         */ 
        public Date getUpdateDate(){ 
             return this.updateDate 
        } 
        /** 
         * 取得修改日期 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getUpdateDateS(){ 
             return this.updateDate 
        } 
        /** 
         * 設定修改時間
         * @since  2018/05/17
         */ 
        public void setUpdateTime( Date updateTime){ 
            this.updateTime=(updateTime==null)?"" : updateTime; 
        } 
        /** 
         * 取得修改時間
         * @since  2018/05/17
         */ 
        public Date getUpdateTime(){ 
             return this.updateTime 
        } 
        /** 
         * 取得修改時間 (處理單引號的問題) 
         * @since  2018/05/17
         */ 
        public String getUpdateTimeS(){ 
             return this.updateTime 
        } 
