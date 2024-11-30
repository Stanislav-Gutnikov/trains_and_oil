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
                       // Убедитесь, что Docker и Docker Compose установлены на вашем сервере
                       sh 'sudo docker-compose down' // Останавливаем старые контейнеры
                       sh 'sudo docker-compose up -d --build' // Собираем и запускаем новые контейнеры
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
   
