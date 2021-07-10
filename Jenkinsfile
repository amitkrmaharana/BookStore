pipeline {
  agent 'python 3.8'
  stages {
    stage('build') {
      steps {
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