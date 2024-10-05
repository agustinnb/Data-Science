# Read before trying to run this notebooks
To run this notebooks you need to install pyspark, here's a brief way to do it on Windows.

## Installing PySpark
If you are using windows like me, you should install PySpark and it dependencies first
Step 1: <br>
* Download JDK 8: <br> 
https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html or <br>
https://www.openlogic.com/openjdk-downloads?field_java_parent_version_target_id=416&field_operating_system_target_id=436&field_architecture_target_id=All&field_java_package_target_id=All  <br>
* Download Spark: https://spark.apache.org/downloads.html (3.5.3) <br>
* Download WinUtils: https://github.com/steveloughran/winutils (hadoop 3.0.0) <br>

Step 2: <br>
* Install JDK 8 (Make sure to know the path)  <br>
* Uncompress Spark (C:\Program Files\Spark\spark-3.5.3-bin-hadoop3)  <br>
* Uncompress WinUtils (C:\Program Files\Spark\winutils\bin) (Get the bin folder from hadoop 3.0.0 folder) <br>

Step 3: <br>
* Declare in the PATH variable of your enviroment C:\Program Files\Spark\spark-3.5.3-bin-hadoop3\bin and C:\Program Files\Spark\winutils\bin)

Step 4: <br>
* Declare SPARK_HOME as C:\Program Files\Spark\spark-3.5.3-bin-hadoop3 <br>
* Declare HADOOP_HOME as C:\Program Files\Spark\winutils\bin <br>
* Declare JAVA_HOME where you installed JDK 8 <br>

Step 5: <br>
* Create folder C:\tmp\hive and in a terminal with admin privileges write "cd C:\tmp % winutils chmod 777 hive" <br>
Step 6: <br>
* pip install PySpark