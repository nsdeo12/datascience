# Edited using [stackedit](https://stackedit.io/app#)
## Follow the steps for installation at [Sundog Education](https://sundog-education.com/spark-python/)

- Download python3 from Anaconda
- Download JDK at c:/jdk
- Download jre: at c:jre
- Download pre built spark .tgz file (spark2.1,hadoop 2.7)
- Download winrar from rarlabs
- at c/spark/copy paste unrared files here
- Change c/spark/conf/log4j.properties.template to log4j.properties 
- Open c/spark/conf/log4j.properties and change log4j.rootCategory to ERROR (from info)
- Download winutils.exe from https://sundog-soark.s3.amazonaws.com/winutils.exe
- create c/winutils/bin and paste the exe here
- winutils.exe chmod 777 \tmp\hive (the folder should be created AT c:\tmp\hive prior to that)
- Set env variables for 
  - SPARK_HOME
  - jAVA_HOME
  - HADOOP_HOME
---
- Altenatively use Databricks community edition
---
# Dataframe steps from Josh's lectures
