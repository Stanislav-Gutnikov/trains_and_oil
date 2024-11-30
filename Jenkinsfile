   pipeline {
       agent any
       stages {
           stage('Clone Repository') {
               steps {
                   git url: 'https://github.com/Stanislav-Gutnikov/trains_and_oil', branch: 'docker'
               }
           }
           stage('Build and Deploy') {
               steps {
                   script {
                       def output = sh(script: 'docker ps -aq', returnStdout: true).trim()
                    def containers = output ? output.split('\n') : []
                    
                    // Проверяем, есть ли контейнеры для удаления
                    if (containers.size() > 0) {
                        // Удаляем каждый контейнер по отдельности
                        for (container in containers) {
                            sh "docker rm -f ${container}"
                        }
                    } else {
                        echo 'No containers to remove.'
                    }
                   }
               }
           }
       }
       post {
           success {
               echo 'Deployment was successful!'
           }
           failure {
               echo 'Deployment failed.'
           }
       }
   }
   
