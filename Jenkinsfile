pipeline{
    agent any
    stages{
        stage('clone'){
            steps{
                git 'https://github.com/seungfwani/sampleUnittest.git'
            }
        }
        stage('build'){
            steps{
                sh '''chmod 755 start.sh end.sh pyenvInit.sh;\
                    ./start.sh'''
            }
        }
    }
    post{
        always{
            sh './end.sh'
            
            recordIssues enabledForFailure: true, aggregatingResults: true, tool: pyLint(pattern: '**/*.log')
        }
    }
}