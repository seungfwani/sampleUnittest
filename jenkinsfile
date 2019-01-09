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
                sh './start.sh'
            }
        }
    }
    post{
        always{
            sh './end.sh'
            
            recordIssues enabledForFailure: true, aggregatingResults: true, tool: pyLint(pattern: '**/*.log')
            cobertura coberturaReportFile: 'QualityReports/coverage.xml', onlyStable: true
            junit 'QualityReports/unittest_results.xml'
        }
    }
}