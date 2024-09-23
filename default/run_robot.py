import yaml
import subprocess
from utils.squash_client import Squash

with open('robot.yml', 'r') as file:
    config = yaml.safe_load(file)


use_squash = 'squash' in config
if use_squash:
    list_tests_to_execute = []
    options_squash = ""
    squash_config = config.get('squash', {})
    squash_campaign = squash_config.get('campaign')
    squash_username = squash_config.get('username')
    squash_password = squash_config.get('password')
    squash = Squash(squash_campaign, squash_username, squash_password)
    list_tests = squash.get_test_plan()
    for test in list_tests:
        id_testcase = test['referenced_test_case']['id']
        title_testcase = test['referenced_test_case']['name']
        id_execution = test['id']
        list_tests_to_execute.append([id_execution,title_testcase,id_testcase])
        options_squash += " --include "+str(id_testcase)
    print('here is the list of tests to execute')
    print(list_tests_to_execute)

    print('\nhere is the constructed options of squash')
    print(options_squash)

use_pabot = 'pabot' in config
command = ['pabot'] if use_pabot else ['robot']


if use_pabot:
    pabot_config = config.get('pabot', {})
    pabot_options = pabot_config.get('options', [])
    for option in pabot_options:
        command.append(option)


robot_config = config.get('robot', {})

log_level = robot_config.get('logLevel', 'INFO')
command.append(f'--loglevel={log_level}')

output_dir = robot_config.get('outputDir', 'results/')
command.append(f'--outputdir={output_dir}')

variables = robot_config.get('variables', [])
for var_file in variables:
    command.append(f'--variablefile={var_file}')

includes = robot_config.get('include', [])
excludes = robot_config.get('exclude', [])
for tag in includes:
    command.append(f'--include={tag}')
for tag in excludes:
    command.append(f'--exclude={tag}')
if use_squash:
    command.append(options_squash)


suites = robot_config.get('suites', [])
command.extend(suites)

print(f"Running command: {' '.join(command)}")
command_str = ' '.join(command)
subprocess.run(command_str)
