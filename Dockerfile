FROM python:3


RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 \
    && chmod +x tailwindcss-linux-x64 \
    && mv tailwindcss-linux-x64 /bin/tailwindcss \
    && apt-get update \
    && apt-get install -y iputils-ping iputils-tracepath iproute2


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY .devcontainer/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8050
EXPOSE 8050

# Define an environment variable for the port number
ENV PORT=8050


WORKDIR /site
COPY . /site

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --shell /bin/bash --disabled-password --gecos "" appuser && chown -R appuser /site
USER appuser

# Install Node.js
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
RUN export NVM_DIR="$HOME/.nvm" \ 
    && \. "$NVM_DIR/nvm.sh"\
    && nvm install node \
    && npm install



# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["pyhon", "-m", "wsgi"]
ENTRYPOINT [ "" ]