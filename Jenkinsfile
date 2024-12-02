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
                    def status_nginx = sh(script: 'systemctl is-active nginx', returnStatus: true)
                    if (status_nginx == 0) {
                        sh 'sudo systemctl stop nginx'
                    } else {
                        echo 'Nginx is not running. No action needed.'
                    }

                    def status_postgres = sh(script: 'systemctl is-active postgres', returnStatus: true)
                    if (status_postgres == 0) {
                        sh 'sudo systemctl stop postgres'
                    } else {
                        echo 'postgres is not running. No action needed.'
                    }
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
                    sh 'docker-compose up -d'
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
   
