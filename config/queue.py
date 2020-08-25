from pyframework.helpers.configuration import env

"""
|--------------------------------------------------------------------------
| Database Connections
|--------------------------------------------------------------------------
|
| Here you may configure the connection information for each server that
| is used by your application. A default configuration has been added
| for each back-end shipped with pika. You are free to add more.
|
"""
connections = {
    'rabbitMQ': {
        # Hosts With Random Load Balancing
        'hosts': env('RABBITMQ_HOSTS', '10.10.10.24:5672').split(','),
        'vhost': env('RABBITMQ_VHOST', '/local'),
        'exchange': env('RABBITMQ_EXCHANGE', 'events'),
        'username': env('RABBITMQ_USER', 'guest'),
        'password': env('RABBITMQ_PASS', 'guest'),
        'read_timeout': 10,
        'write_timeout': 10,
        'connect_timeout': 5,
        'prefetchCount': 1,
    }
}

params = {
    'cliTimeout': 1800,  # Max time to execute event.
    'forceClean': 900,  # Seconds until clean process resources.
    'queues': {
        # |--------------------------------------------------------------------------
        # | Crawler Queue
        # |--------------------------------------------------------------------------
        # | Queue to managements crawler tasks.
        #
        'download_ready': {
            'eventsNames': [
                'download.place.ready.action',
                'download.info.ready.action',
                'download.place.ready.task',
                'download.info.ready.task',
            ],
        },
    }
}
