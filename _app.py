from flask import Flask, request
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.propagate import inject
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)

# Configure the tracer to export traces to Jaeger
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name='localhost',
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

# Automatically trace all requests
FlaskInstrumentor().instrument_app(app)

@app.route('/')
def index():
    with trace.get_tracer(__name__).start_as_current_span('index'):
        # Your application logic here
        return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)