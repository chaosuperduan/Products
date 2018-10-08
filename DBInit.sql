create database ihome DEFAULT character  set utf8;

create table ih_user_profile(
     up_user_id bigint unsigned not null auto_increment comment '用户id',
     up_name varchar(32) not null comment '昵称',
     up_mobile char(11) not null comment '手机号',
     up_passwd varchar(64) not null comment '密码',
     up_real_name varchar(32) not null comment '真实姓名',
     up_id_card varchar(20) null comment '身份证号码',
     up_avatar varchar(128) null comment '用户头像',
     up_admin tinyint not null default '0' comment '是否是管理员 0不是 1是',
     up_utime datetime not null default current_timestamp on update current_timestamp comment '最后更新时间',
     up_ctime datetime not null default current_timestamp comment '创建时间',
     primary key (up_user_id),
     unique (up_name),
     unique (up_mobile)

)Engine=InnoDB AUTO_INCREMENT=10000 DEFAULT charset = utf8 comment '用户信息表';

create table ih_area_info (

     ai_area_id bigint unsigned not null auto_increment  comment'区域id',
     ai_name_id varchar(32) not null comment '区域名称',
     ai_ctime datetime not null default current_timestamp comment '创建时间',
     primary key (ai_area_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT'房源区域表';

create  table ih_house_info(
     hi_house_id bigint unsigned not null auto_increment comment '房屋id',
     hi_user_id bigint unsigned not null  comment '用户id',
     hi_title varchar(64) not null comment '房屋的名称',
     hi_price int unsigned not null default '0' comment '房屋的价格',
     hi_area_id bigint unsigned not null comment '房屋的区域id',
     hi_address varchar(512) not null default '' comment '房屋的地址',
     hi_room_count tinyint unsigned not null default '0' comment '房屋的间数',
     hi_acreage int unsigned not null default '0' comment '房屋的面积',
     hi_house_unit varchar(32) not null default '' comment '房屋的户型',
     hi_capacity int unsigned not null default '1' comment '容纳人数',
     hi_beds varchar(64) not null default '' comment '床的配置',
     hi_deposit int unsigned not null default '0' comment '押金单位分',
     hi_min_days int unsigned not null default '0' comment '最短入住时间',
     hi_max_days int unsigned not null default '0' comment '最长入住时间0-0代表不限时',
     hi_order_count int unsigned not null default '0' comment '下单数量',
     hi_verify_status tinyint not null default '0' comment '审核状态 0,待审核，1审核未通过，2审核通过',
     hi_online_status tinyint not null default  '1' comment '0在线,1下线',
     hi_index_image_url varchar(256) null comment '房屋主图片',
     hi_utime datetime not null default current_timestamp on update current_timestamp comment '最后更新时间',
     hi_ctime datetime not null default current_timestamp comment '创建时间',
     primary key (hi_house_id),
     key hi_status (hi_verify_status,hi_online_status),


     constraint foreign key (hi_user_id) references ih_user_profile(up_user_id),
     constraint  foreign key (hi_area_id) references ih_area_info(ai_area_id)

)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT'房源信息表';

-- 订单表----。
create  table  ih_order_info(

       oi_order_id bigint unsigned not null auto_increment comment'订单id',
       oi_user_id bigint unsigned not null comment '用户id',
       oi_house_id bigint unsigned not null comment '房屋id',
       oi_begin_date date not null comment '入住时间',
       oi_end_date date not null comment '离开时间',
       oi_days int unsigned not null comment '入住天数',
       oi_house_price int unsigned not null comment '房屋价格',
       oi_ammount int unsigned not null comment '订单金额',
       oi_status tinyint not null default '0' comment'订单状态,0待接单，1待支付,2已支付，3待评价，4已完成，5已取消，6局接单',
       oi_comment text null comment '订单评论',
       oi_utime datetime not null default current_timestamp on update current_timestamp comment '更新时间',
       oi_ctime datetime not null default current_timestamp comment '创建时间',
       primary key(oi_order_id),
       key oi_status(oi_status),
       constraint foreign key (oi_user_id) references ih_user_profile(up_user_id),
       constraint foreign key (oi_house_id) references ih_house_info(hi_house_id)


)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT'订单信息表';

create  table  in_house_facility(

      hf_id bigint unsigned not null auto_increment comment '自增id',
      hf_house_id bigint unsigned not null comment '房屋id',
      hf_facility_id int unsigned not null comment '房屋设施',
      hf_ctime datetime not null default current_timestamp comment '创建时间',
      primary key (hf_id),
      constraint foreign key (hf_house_id) references ih_house_info(hi_house_id)


)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT'房源设施表';


create table ih_house_image(
     hi_image_id bigint unsigned not null auto_increment comment'图片id',
     hi_house_id bigint unsigned not null comment '房屋的id',
     hi_url varchar() null



)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT'房源图片';
