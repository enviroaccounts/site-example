FROM python:3


# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 \
    && chmod +x tailwindcss-linux-x64 \
    && mv tailwindcss-linux-x64 /bin/tailwindcss


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



# Expose port 8050
EXPOSE 8050

# Define an environment variable for the port number
ENV PORT=8050