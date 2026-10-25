# Base image: Ruby with necessary dependencies for Jekyll
FROM ruby:3.2

# Install system dependencies, Python, and virtual environment support
RUN apt-get update && apt-get install -y \
    build-essential \
    nodejs \
    python3 \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create a Python virtual environment
RUN python3 -m venv /opt/venv

# Add the virtual environment to PATH
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
RUN pip install --no-cache-dir pybtex

# Create a non-root user with UID 1000
RUN groupadd -g 1000 vscode && \
    useradd -m -u 1000 -g vscode vscode

# Set the working directory
WORKDIR /usr/src/app

# Set permissions for the working directory
RUN chown -R vscode:vscode /usr/src/app

# Switch to the non-root user
USER vscode

# Copy Gemfile into the container
COPY Gemfile ./

# Install Bundler and Ruby dependencies
RUN gem install connection_pool:2.5.0
RUN gem install bundler:2.3.26
RUN bundle install

# Command to serve the Jekyll site
CMD ["jekyll", "serve", "-H", "0.0.0.0", "-w", "--config", "_config.yml,_config_docker.yml"]



# bundle exec jekyll serve -H 0.0.0.0 -w --config _config.yml,_config_docker.yml