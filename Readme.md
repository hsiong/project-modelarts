# 相关文章
+ 海量实战教你零门槛进场AI开发，无成本负担玩转AI应用: https://developer.huawei.com/consumer/cn/forum/topic/0201624201203780162
+ 【B站UP主-同济子豪兄】华为云ModelArts零代码开发病虫害识别应用: https://bbs.huaweicloud.com/blogs/197741
+ 基于ModelArts自动学习零代码开发深圳地标识别模型: https://bbs.huaweicloud.com/blogs/386043
+ 业务开发者：使用自动学习构建模型: https://github.com/huaweicloudDocs/modelarts/blob/master/cn.zh-cn/%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/%E4%B8%9A%E5%8A%A1%E5%BC%80%E5%8F%91%E8%80%85-%E4%BD%BF%E7%94%A8%E8%87%AA%E5%8A%A8%E5%AD%A6%E4%B9%A0%E6%9E%84%E5%BB%BA%E6%A8%A1%E5%9E%8B.md
+ ModelArts在数据标注、数据过滤上的应用技巧：自动分组: https://bbs.huaweicloud.com/blogs/187175
+ 自动分组: https://github.com/huaweicloudDocs/modelarts/blob/master/cn.zh-cn/AI%E5%B7%A5%E7%A8%8B%E5%B8%88%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/%E8%87%AA%E5%8A%A8%E5%88%86%E7%BB%84.md
+ ModelArts智能标注提升70%数据标注效率: https://github.com/huaweicloud/ModelArts-Lab/tree/master/train_inference/Auto_Labeling/Auto_Labeling
+ 基于MindSpore的ChatGLM微调: https://www.cnblogs.com/huaweiyun/p/17766924.html

# 注意
+  说明： 只能在“全部“页签下启动自动分组任务
+ obs 要和modelarts在同一个地区      热销专场有活动促销
+ 只有支持cpu计算的模型, 才能选cpu算力
+ 专属资源的记账周期和公共资源池不一样   公共资源池的按需使用, 训练一个小时算一个小时的钱; 专属资源池只要启动了, 不训练也扣钱
+ 部署模型, 必须设置停止时间, 否则会报错
+ 华为API鉴权SDK需使用以下方式
```xml
    <profiles>
        <profile>
            <id>MyProfile</id>
            <repositories>
                <repository>
                    <id>central</id>
                    <name>Maven Central Repository</name>
                    <url>https://repo1.maven.org/maven2/</url>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                    <snapshots>
                        <enabled>false</enabled>
                    </snapshots>
                </repository>
            </repositories>
            <pluginRepositories>
                <pluginRepository>
                    <id>central</id>
                    <name>Maven Central Repository</name>
                    <url>https://repo1.maven.org/maven2/</url>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                    <snapshots>
                        <enabled>false</enabled>
                    </snapshots>
                </pluginRepository>
            </pluginRepositories>
        </profile>
    </profiles>
    
```