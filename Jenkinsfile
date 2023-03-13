import java.text.SimpleDateFormat
def dateFormat = new SimpleDateFormat("yyyyMMddHHmm")
def dockerTag = dateFormat.format(new Date())
pipeline {
    agent any
    environment {
        dockerName='labelfree/mkdocs'
    }
    stages {
        stage('Docker build') {
            steps {
                sh 'pwd'
                sh 'ls'
                sh "docker build -t  ${dockerName}:latest ."
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh """
                # 重启docker compose
                docker stop laeblfre_doc | true
                docker rm laeblfre_doc | true
                docker run -d -p 18002:80 --name laeblfre_doc ${dockerName}:latest | true
                """
            }
        }
        //  stage('Cleanup') {
        //         steps {
        //             echo 'Cleanup...'
        //             sh """
        //             docker rmi -f `docker images | grep '<none>' | grep -v IMAGE | awk '{ print \$3 }' | xargs`
        //             """
        //         }
        //     }
    }

    // post{
    //     success{
    //         echo "========pipeline executed successfully ========"
    //         sh """
    //         curl -X POST -H "Content-Type: application/json" -d '{"msg_type":"text","content":{"text":"后端测试环境已更新"}}' https://open.feishu.cn/open-apis/bot/v2/hook/87319123-33a9-48d5-9104-fc6bc0a7b0d7
    //         """
    //     }
    //     failure{
    //         echo "========pipeline execution failed========"
    //     }
    // }
    }
