import os

from src.config import BASE_DIR, PROJECT_NAME
from src.log import logger


def create_project_dir(project_name):
    '''Create a project forlder/directory'''
    search_dir = os.path.join(BASE_DIR, project_name)
    if not os.path.exists(search_dir):
        logger.info('Creating project {}'.format(project_name))
        os.makedirs(search_dir)


def create_data_files(project_name):
    '''
    Create queue and crawled files (if not created)
    '''
    queue = '{}{}'.format(project_name, '/queue.txt')
    crawled = '{}{}'.format(project_name, '/crawled.txt')
    restore = '{}{}'.format(project_name, '/restore.txt')

    def _creator(path_file):
        if not os.path.isfile(path_file):
            create_file(path_file)
            logger.info('file succses created: {}'.format(path_file))

    _creator(queue)
    _creator(crawled)
    _creator(restore)


def create_file(path):
    ''' write data a file'''
    with open(path, 'w') as file:
        file.write('')


def append_data_to_file(path, data):
    with open(path, 'a') as file:
        file.write('{}\n'.format(data))


def file_to_list(path):
    results_list = []
    with open(path) as f:
        for line in f:
            results_list.append(line.replace('\n', ''))

    return results_list


def append_list_to_file(path, list_data, to_new_file=False):
    key = 'a'
    if to_new_file:
        key = 'w'

    with open(path, key) as f:
        for i in list_data:
            f.write('{}\n'.format(i))


def create_restore_file(path_queue_file, path_crawled_file, path_restore_file):
    queue_set = set(_open(path_queue_file))
    crawled_set = set(_open(path_crawled_file))

    restore_queue = list(queue_set - crawled_set)

    append_list_to_file(
        path_restore_file,
        restore_queue,
        to_new_file=True
    )

    logger.info('restore file created')
    return True


def _open(path):
    with open(path) as f:
        return f.read().split('\n')[:-1]


def param_change_agent():
    user_agent_path = os.path.join(BASE_DIR, 'user-agent.txt')
    resolution_path = os.path.join(BASE_DIR, 'resolutions.txt')

    user_agent = _open(user_agent_path)
    resolutions = _open(resolution_path)

    return user_agent, resolutions


if __name__ == '__main__':

    # create_restore_file(file1, file2)
    create_project_dir(PROJECT_NAME)
