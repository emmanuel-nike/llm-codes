from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Configure the tracer provider and exporter
trace.set_tracer_provider(TracerProvider())
tracer_provider = trace.get_tracer_provider()
tracer_provider.add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)

# Initialize Flask application and instrument it
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

# Define a route
@app.route("/example")
def example_endpoint():
    with trace.get_tracer(__name__).start_as_current_span("example-request"):
        # Your endpoint logic here
        return "Hello, World!"

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)