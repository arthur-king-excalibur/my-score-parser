import os

from config import BASE_DIR, PROJECT_NAME


def create_project_dir(project_name):
    '''Create a project forlder/directory'''
    search_dir = os.path.join(BASE_DIR, project_name)
    if not os.path.exists(search_dir):
        print('Creating project {}'.format(project_name))
        os.makedirs(search_dir)


def create_data_files(project_name, base_url):
    '''
    Create queue and crawled files (if not created)
    '''
    queue = '{}{}'.format(project_name, '/queue.txt')
    crawled = '{}{}'.format(project_name, '/crawled.txt')

    if not os.path.isfile(queue):
        write_data_to_file(queue, base_url)
        print('file succses created: {}'.format(queue))

    if not os.path.isfile(crawled):
        write_data_to_file(crawled, '')
        print('file succses created: {}'.format(crawled))


def write_data_to_file(path, data):
    ''' write data a file'''
    with open(path, 'w') as file:
        file.write('{}\n'.format(data))


def append_data_to_file(path, data):
    with open(path, 'a') as file:
        file.write('{}\n'.format(data))


def file_to_list(path):
    results_list = []
    with open(path) as f:
        for line in f:
            results_list.append(line.replace('\n', ''))

    return results_list


def delete_data_from_file():
    pass


def param_change_agent():
    proxy_path = os.path.join(BASE_DIR, 'proxy.txt')
    user_agent_path = os.path.join(BASE_DIR, 'user-agent.txt')
    resolution_path = os.path.join(BASE_DIR, 'resolutions.txt')

    def _open(path):
        with open(path) as f:
            return f.read().split('\n')[:-1]

    proxy = _open(proxy_path)
    user_agent = _open(user_agent_path)
    resolutions = _open(resolution_path)

    return proxy, user_agent, resolutions
