import pytest
import taskcluster
import urllib, json, os

@pytest.fixture
def driver_class(scope='session'):
    from appium import webdriver
    return webdriver.Remote

@pytest.fixture
def capabilities(capabilities,variables):
    taskId = getTaskId(variables['taskClusterTask'])
    variables['taskId'] = taskId
    capabilities['app'] = variables['taskClusterUrl'] + taskId + variables['taskClusterArtifactName']
    build = getBuildInfo(variables['taskClusterUrl'] + variables['taskId'])
    capabilities['build'] = build
    capabilities.setdefault('tags', []).append('nmx')
    return capabilities

@pytest.fixture
def appium(capabilities, variables, request, driver):

    yield driver
    if 'app' in capabilities:
        driver.close_app()
        driver.remove_app(capabilities['appPackage'])

    # Prepare reports when running locally
    if os.getenv('SAUCELABS_USERNAME') is None:
        test_name = request.node.name
        with(open(test_name + '.testlog', 'w')) as outfile:
            outfile.write("SauceOnDemandSessionID=%s \ntest-name=%s\n" % (driver.session_id, test_name))
            outfile.write("Build ID=%s\n" % (capabilities['build']))
            outfile.write("Taskcluster URL=%s\n" % (capabilities['app']))

# Get the build's task ID in taskcluster
def getTaskId(taskClusterTask):
    index = taskcluster.Index()
    queue = taskcluster.Queue()

    # Find the latest TaskId
    taskId = index.findTask(taskClusterTask)['taskId']
    # Make sure the job is completed
    assert queue.status(taskId)['status']['state'] == 'completed'

    return taskId

# 2nd entry of the json has the pushdate information
def getBuildInfo(url):
    try:
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        return data['routes'][1]
    except urllib.error.URLError as e:
        return "URL Error"