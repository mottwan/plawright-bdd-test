pipeline {
    agent any

    environment {
        PYTHON_ENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mottwan/playwright-bdd-test.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh """
                            python3 -m venv $PYTHON_ENV
                            source $PYTHON_ENV/bin/activate
                            pip install --upgrade pip
                            pip install -e .[dev]
                            npx playwright install
                        """
                    } else {
                        bat """
                            python -m venv %PYTHON_ENV%
                            call %PYTHON_ENV%\\Scripts\\activate
                            pip install --upgrade pip
                            pip install -e .[dev]
                            npx playwright install
                        """
                    }
                }
            }
        }

        stage('Lint Check') {
            steps {
                script {
                    sh """
                        flake8 --count --statistics
                    """
                }
            }
        }

        stage('Run Tagged Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh """
                    source $PYTHON_ENV/bin/activate
                    pytest -m basic_search --junitxml=results.xml
                """
                    } else {
                        bat """
                    call %PYTHON_ENV%\\Scripts\\activate
                    pytest -m basic_search --junitxml=results.xml
                """
                    }
                }
            }
        }


        stage('Run All Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh """
                            source $PYTHON_ENV/bin/activate
                            pytest --junitxml=results.xml
                        """
                    } else {
                        bat """
                            call %PYTHON_ENV%\\Scripts\\activate
                            pytest --junitxml=results.xml
                        """
                    }
                }
            }
        }

        stage('Publish Reports') {
            steps {
                script {
                    if (fileExists('test-results.xml')) {
                        junit 'test-results.xml'
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
