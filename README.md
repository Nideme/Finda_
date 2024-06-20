
# FINDA

FINDA is a web application that enhances interaction with a language model (LLM) assistant, designed to generate intelligent responses and conduct web searches to augment information delivery. This integration fetches additional data from Google, YouTube, and Wikipedia, enriching user interactions.

## Project Overview

FINDA is built to provide a cutting-edge, intuitive interface where users can engage with an LLM assistant. The goal is to deliver not only direct answers but also extended information through seamless web searches.

## Features

### Frontend

- **Chat Interface**
  - Sleek, modern chat design enabling users to send messages through a text input field at the bottom.
  - Displays conversation history above, allowing users to follow the dialogue seamlessly.

- **Assistant Instructions Input Field**
  - Positioned at the top of the chat interface for users to guide the assistant's operations.

- **Search Integration**
  - **Google Search**: Integrated checkbox (enabled by default) adjacent to the message input to trigger searches based on LLM-generated keywords.
  - **Additional Search Engines**: Options to extend searches to YouTube and Wikipedia via checkboxes.

### Backend

- **Language Model Assistant Integration**
  - Incorporates Groq as the LLM assistant, processing user inputs and formulating responses.
  - Extracts pertinent keywords from responses to trigger web searches.

- **Search Initiation**
  - Dynamically starts searches on Google, YouTube, and Wikipedia depending on user selection and extracted keywords.

- **Display Search Results**
  - Efficiently fetches and displays search results under the LLM’s responses within the chat interface.

## Technical Specifications

### Frontend
- Crafted using the React.js framework, emphasizing responsiveness, accessibility, performance, and secure practices.

### Backend
- Developed in Python, ensuring secure API interactions.
- Optimizes the extraction of keywords and initiates searches effectively.

## Installation

### Prerequisites
- Ensure installation of Node.js, npm, Python, pip, and Git.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
   ```


2. **Setup Backend**

   - Navigate to the backend directory

     ```bash
     cd backend
     ```

   - Create and activate a virtual environment

     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

   - Install dependencies

     ```bash
     pip install -r requirements.txt
     ```

   - Download NLTK data packages

     ```bash
     python -m nltk.downloader punkt stopwords
     ```

   - Create a `.env` file with your API keys

     ```plaintext
     GROQ_API_KEY=your_groq_api_key
     GOOGLE_API_KEY=your_google_api_key
     SEARCH_ENGINE_ID=your_search_engine_id
     YOUTUBE_API_KEY=your_youtube_api_key
     ```

   - Run the backend server

     ```bash
     python app.py
     ```

3. **Setup Frontend**

   - Navigate to the frontend directory

     ```bash
     cd ../frontend
     ```

   - Install dependencies

     ```bash
     npm install
     ```

   - Start the frontend development server

     ```bash
     npm start
     ```

4. **Open the Application**

   Open your browser and go to `http://localhost:3000` to use the FINDA application.

## Usage

1. Enter your message in the chat input field at the bottom of the chat interface.
2. Optionally, provide instructions for the assistant in the top input field.
3. Select the search options (Google, YouTube, Wikipedia) as needed.
4. Press the "Send" button to receive a response from the LLM and see search results if applicable.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

```

Replace `YOUR_GITHUB_USERNAME` and `YOUR_REPOSITORY_NAME` with your actual GitHub username and repository name. This README file provides a comprehensive overview of the project, installation instructions, usage guidelines, and contribution information.# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
