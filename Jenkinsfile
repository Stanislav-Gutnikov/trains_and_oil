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
                       //sh 'docker rm -f $(docker ps -aq)' // Удаляем старые контейнеры
                       script {
                    // Получаем список всех контейнеров
                            def containers = sh(script: 'docker ps -aq', returnStdout: true).trim()
                    
                    // Проверяем, есть ли контейнеры для удаления
                            if (containers) {
                        // Удаляем все контейнеры
                                sh "docker rm -f ${containers}"
                            } else {
                                echo 'No containers to remove.'
                            }
                       sh 'docker-compose up -d'
                        } // Собираем и запускаем новые контейнеры
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
   
