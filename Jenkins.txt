pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash

virtualenv --python=/usr/bin/python3.8 flask
source flask/bin/activate	
pip install -r requirements.txt'''
            }
        }
    


        stage('Test') {
            steps {
               sh '''#!/bin/bash

virtualenv --python=/usr/bin/python3.8 flask
source flask/bin/activate	
pip install -r requirements.txt
coverage run -m unittest
coverage report -m'''

            }
        }
    

        stage('Package') {
            steps {
                sh '''#!/bin/bash

virtualenv --python=/usr/bin/python3.8 flask
source flask/bin/activate	
pip install -r requirements.txt
cd devops_demo/docs/
make clean
make html
'''
            }
        }
    }
}
