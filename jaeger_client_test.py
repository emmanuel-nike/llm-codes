# from jaeger_client import Config
# from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
# from jaeger_client.metrics import Metrics
# from prometheus_client import start_http_server
# import requests

# # Configure Jaeger client
# config = Config(
#     config={
#         'sampler': {'type': 'const', 'param': 1},
#         'logging': True,
#         'reporter_batch_size': 1,
#     },
#     service_name='your-service',
#     validate=True,
#     metrics_factory=PrometheusMetricsFactory(),
# )

# # Start Prometheus metrics server
# start_http_server(9000)

# # Initialize Jaeger tracer
# metrics = Metrics()
# tracer = config.initialize_tracer(metrics=metrics)

# # Fetch traces from Jaeger
# def get_traces(service_name, limit=100):
#     query = {
#         'service': service_name,
#         'limit': limit,
#     }
#     response = requests.get('http://localhost:16686/api/traces', params=query)
#     if response.status_code == 200:
#         return response.json()['data']
#     else:
#         raise Exception('Failed to fetch traces')

# # Analyze traces
# traces = get_traces('your-service')
# for trace in traces:
#     print(f"Trace ID: {trace['traceID']}")
#     for span in trace['spans']:
#         print(f"  Span ID: {span['spanID']}, Operation: {span['operationName']}, Duration: {span['duration']}μs")
#         if 'tags' in span:
#             for tag in span['tags']:
#                 if tag['key'] == 'error':
#                     print(f"    Error: {tag['value']}")

# # Close the tracer
# tracer.close()

# from jaeger_client import Config
# import requests

# # Configure Jaeger client
# config = Config(
#     config={
#         'sampler': {
#             'type': 'const',
#             'param': 1,
#         },
#         'logging': True,
#         'reporter_batch_size': 1,
#     },
#     service_name='my-service',
# )
# tracer = config.initialize_tracer()

# # Retrieve trace data from Jaeger's HTTP API
# trace_id = 'your-trace-id'
# response = requests.get(f'http://localhost:16686/api/traces/{trace_id}')
# trace_data = response.json()

# # Analyze trace data
# for span in trace_data['data'][0]['spans']:
#     print(f"Operation: {span['operationName']}")
#     print(f"Start Time: {span['startTime']} End Time: {span['startTime'] + span['duration']}")
#     print(f"Tags: {span['tags']}")
#     if 'logs' in span:
#         for log in span['logs']:
#             print(f"Log: {log['message']} Timestamp: {log['timestamp']}")

# # Close the tracer
# tracer.close()

from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from prometheus_client import start_http_server
import requests

# Configure Jaeger client
config = Config(
    config={
        'sampler': {'type': 'const', 'param': 1},
        'logging': True,
        'reporter_batch_size': 1,
    },
    service_name='your-service',
    validate=True,
    metrics_factory=PrometheusMetricsFactory(),
)

# Start Prometheus metrics server
start_http_server(9000)

# Initialize Jaeger tracer
tracer = config.initialize_tracer()

# Fetch traces from Jaeger
def get_traces(service_name, limit=100):
    query = {
        'service': service_name,
        'limit': limit,
    }
    response = requests.get('http://localhost:16686/api/traces', params=query)
    if response.status_code == 200:
        return response.json()['data']
    else:
        raise Exception('Failed to fetch traces')

# Analyze traces
traces = get_traces('your-service')
for trace in traces:
    print(f"Trace ID: {trace['traceID']}")
    for span in trace['spans']:
        print(f"  Span ID: {span['spanID']}, Operation: {span['operationName']}, Duration: {span['duration']}μs")
        if 'tags' in span:
            for tag in span['tags']:
                if tag['key'] == 'error':
                    print(f"    Error: {tag['value']}")

# Close the tracer
tracer.close()