pipeline {
    agent any

    environment {
        IMAGE_NAME = "cossiala7/gestion_notes:latest"
        COMPOSE_PROJECT_NAME = "gestion_notes_ci"
    }

    stages {
        stage('Cloner le projet') {
            steps {
                git 'https://github.com/cossiala7/Application_gestion_notes.git'
            }
        }

        stage('Build de l’image Docker') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push vers Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'delatchaille',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }

        stage('Démarrage avec docker-compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '''
                        docker container stop django_app || true
                        docker container rm django_app || true
                        docker container run -d \
                            --name django_app \
                            -e DB_NAME=gestion_notes \
                            -e DB_USER=django_user \
                            -e DB_PASSWORD=django_pass \
                            -e DB_HOST=mysql_django \
                            -p 8000:8000 \
                            $IMAGE_NAME
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Build status: ${currentBuild.result}"
        }
        success {
            emailext (
                subject: "✅ Déploiement réussi - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Le déploiement a réussi !
                    Job: ${env.JOB_NAME}
                    Build #${env.BUILD_NUMBER}
                    Consulter: ${env.BUILD_URL}
                """,
                to: 'ayambathieu8@gmail.com, antaliguerefab@gmail.com, diawpmkamil@gmail.com, djimsoncompany@gmail.com, diopmadicke351@gmail.com'
            )
        }
        failure {
            emailext (
                subject: "❌ Échec du déploiement - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Le déploiement a échoué !
                    Job: ${env.JOB_NAME}
                    Build #${env.BUILD_NUMBER}
                    Erreur: ${currentBuild.currentResult}
                    Consulter: ${env.BUILD_URL}
                """,
                to: 'sylcohennossiala@gmail.com, devops@example.com'
            )
        }
    }
}
