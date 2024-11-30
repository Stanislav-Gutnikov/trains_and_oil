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
                       // Получаем список всех контейнеров
                       def containers = sh(script: 'docker ps -aq', returnStdout: true).trim().split(/s+/)
                    // Проверяем, есть ли контейнеры для удаления
                    if (containers.size() > 0 && containers[0] != '') {
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
   
