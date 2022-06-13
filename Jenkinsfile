#!/usr/bin/env groovy

pipeline {

    agent {
        node {
            label 'dev-node'
        }
    }

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws_access_key_id') 
        AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key') 
        AWS_REGION = credentials('aws_region') 
        AWS_OUTPUT = credentials('aws_output') 
        AWS_ACCOUNT_ID = credentials('aws_account_id') 
    }

    stages {

        stage('Build Tests') {
            steps {
                sh 'mvn clean verify'
            }
        }

        stage('Sonar Scan') {
            steps {
                withSonarQubeEnv(installationName: 'sonarqube') {
                  sh 'mvn sonar:sonar'
                }
            }
        }

        stage("Quality Gates") {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build Jar') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Build Docker Image Tagged For ECR') {
            steps {
                sh 'sudo docker build . -t ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/sf-aline-gateway-microservice:${GIT_COMMIT}'
            }
        }

        stage('AWS Credentials and Login') {
            steps {
                sh 'aws configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}'
                sh 'aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}'
                sh 'aws configure set default.region ${AWS_REGION}'
                sh 'aws configure set output ${AWS_OUTPUT}'
                sh 'aws ecr get-login-password --region ${AWS_REGION} | sudo docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com'
            }
        }

        stage('Push Image To ECR') {
            steps {
                sh 'sudo docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/sf-aline-gateway-microservice:${GIT_COMMIT}'
            }
        }

    }

    post {
        always {
            sh 'sudo docker image prune --all -f'  // removes docker images from worker node
            sh 'sudo docker logout'  // logs out of docker removing credentials
            sh 'sudo rm -rf ~/.aws/'  // logs out of aws cli removing credentials
            sh 'sudo rm -rf ~/.sonar/*'  // removes sonar cache
            sh 'sudo rm -rf ~/jenkins/workspace/${JOB_NAME}/*'  // removes all files in job workspace
            sh 'sudo rm -rf ~/jenkins/workspace/${JOB_NAME}/.git*'  // removes all .git files in job workspace
        }
    }

}

