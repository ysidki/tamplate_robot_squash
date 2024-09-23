import yaml
import subprocess
from utils.gamera_client import Gamera

# Load the YAML configuration
with open('robot.yml', 'r') as file:
    config = yaml.safe_load(file)

# Prepare to use Pabot if the configuration exists
use_gamera = 'gamera' in config
if use_gamera:
    list_tests_to_execute = []
    options_gamera = ""
    gamera_config = config.get('gamera', {})
    gamera_campaign = gamera_config.get('campaign')
    gamera_username = gamera_config.get('username')
    gamera_password = gamera_config.get('password')
    gamera = Gamera(gamera_campaign, gamera_username, gamera_password)
    list_tests = gamera.get_test_plan()
    for test in list_tests:
        id_testcase = test['referenced_test_case']['id']
        title_testcase = test['referenced_test_case']['name']
        id_execution = test['id']
        list_tests_to_execute.append([id_execution,title_testcase,id_testcase])
        options_gamera += " --include "+str(id_testcase)
    print('here is the list of tests to execute')
    print(list_tests_to_execute)

    print('\nhere is the constructed options of gamera')
    print(options_gamera)

use_pabot = 'pabot' in config
command = ['pabot'] if use_pabot else ['robot']


# Handle Pabot-specific options
if use_pabot:
    pabot_config = config.get('pabot', {})

    # Add Pabot-specific options
    pabot_options = pabot_config.get('options', [])
    for option in pabot_options:
        command.append(option)
    
    # Add number of processes
    # processes = pabot_config.get('processes', 4)
    # command.append(f'--processes {processes} ')
    


# Get the RobotFramework options from the configuration
robot_config = config.get('robot', {})

# Add logging level
log_level = robot_config.get('logLevel', 'INFO')
command.append(f'--loglevel={log_level}')

# Add output directory
output_dir = robot_config.get('outputDir', 'results/')
command.append(f'--outputdir={output_dir}')

# Add variables files
variables = robot_config.get('variables', [])
for var_file in variables:
    command.append(f'--variablefile={var_file}')

# Add tags to include/exclude
includes = robot_config.get('include', [])
excludes = robot_config.get('exclude', [])
for tag in includes:
    command.append(f'--include={tag}')
for tag in excludes:
    command.append(f'--exclude={tag}')
if use_gamera:
    command.append(options_gamera)



# Add test suites to the command
suites = robot_config.get('suites', [])
command.extend(suites)

# Execute the command
print(f"Running command: {' '.join(command)}")
command_str = ' '.join(command)
subprocess.run(command_str)
