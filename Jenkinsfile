pipeline {
  agent { docker { image 'python:3.8' } }
  stages {
    stage('build') {
      steps {
        sh 'sudo chmod 666 /var/run/docker.sock'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('deploy') {
      steps {
        sh 'python3 wsgi.py'
      }
    }
  }
}