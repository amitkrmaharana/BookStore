pipeline {
  agent { docker { image 'book_store' } }
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