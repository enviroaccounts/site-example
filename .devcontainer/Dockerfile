FROM python:3


RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 \
    && chmod +x tailwindcss-linux-x64 \
    && mv tailwindcss-linux-x64 /bin/tailwindcss

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
RUN export NVM_DIR="$HOME/.nvm" \ 
    && \. "$NVM_DIR/nvm.sh"\
    && nvm install node

# Expose port 8050
EXPOSE 8050

# Define an environment variable for the port number
ENV PORT=8050