## 外链接

- 1. 左连接  left join 或 left outer join
  SQL语句：select * from 表1 left join 表2 on 表1.ID=表2.ID
   左外连接包含左表所有行，如果左表中某行在右表没有匹配，则结果中对应行右表的部分全部为空(NULL).

- 2. 右连接
   与左连接反之
   右外连接包含右表所有行，如果右表中某行在左表没有匹配，则结果中对应行左表的部分全部为空(NULL).

- 3. 完全外连接  full join 或 full outer join
   SQL语句：select * from 表1 full join 表2 on 表1.ID=表2.ID

## 内连接 join 或 inner join
   SQL语句：select * from 表1 inner join 表2 on 表1.ID=表2.ID
            select * from 表1,表2 where 表1.ID=表2.ID

## 交叉连接  cross join
   SQL语句：select * from 表1 cross join 表2
   