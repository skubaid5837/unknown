https://github.com/skubaid5837/unknown.git


step1:(zookeeper)bin/zookeeper-server-start.sh config/zookeeper.properties.

step2:(kafka server)bin/kafka-server-start.sh config/server.properties.

step3:(flink)bin/start-cluster.sh

step4: run java program in ide.
compile:-javac -cp /usr/local/kafka/libs/* YourJavaFile.java OR  javac -cp /usr/local/kafka/libs/*:. AdImpressionProducer.java

Run:-java -cp /usr/local/kafka/libs/*:. AdImpressionsProducer

Create Topics:-bin/kafka-topics.sh --create --topic ad-impressions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1


bin/kafka-topics.sh --create --topic clickstream --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

List the topics:-bin/kafka-topics.sh --list --bootstrap-server localhost:9092


step5:
Verify Ad-Impression:-bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic ad-impressions --from-beginning


verify ClickStream:-bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic clickstream --from-beginning


Step6:-Start Spark:-
.\bin\spark-class org.apache.spark.deploy.master.Master

.\bin\spark-class org.apache.spark.deploy.worker.Worker spark://localhost:7077
