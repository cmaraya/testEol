# Use an official Node.js runtime as a parent image
FROM node:18.17.0

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Update npm to the latest version
RUN npm install -g npm@latest

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port and start application
EXPOSE 3000
CMD ["npm", "start"]
