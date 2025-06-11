<a id="readme-top"></a>
<!--
*** Thanks for checking out AgenticEditor. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">AgenticEditor</h1>

  <p align="center">
    A Python-based agentic code editor prototype
    <br />
    <a href="#getting-started"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/lavis0/AgenticEditor/issues/new?labels=bug">Report Bug</a>
    ·
    <a href="https://github.com/lavis0/AgenticEditor/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

AgenticEditor is a prototype agentic code editor built in Python that demonstrates the power of AI-driven development tools. Originally created as a foundation for the ResRover project, this tool showcases how AI agents can interact with codebases through a secure, function-based API.

The project includes a built-in calculator example to demonstrate the agent's capabilities in a controlled environment. The agent can read files, execute Python code, write new files, and navigate directory structures—all while being constrained to a safe working directory.

**Here's what makes AgenticEditor special:**

- **Security-first design** - All operations are sandboxed to a specific working directory
- **Function-based architecture** - Clean API for extending agent capabilities
- **Real-world testing** - Includes a functional calculator project for demonstration
- **Extensible framework** - Easy to add new functions and capabilities

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This project is built using modern Python tools and the Google Gemini API:

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
- ![dotenv](https://img.shields.io/badge/.env-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8 or higher
- A Google Gemini API key
- pip (Python package installer)

### Installation

1. **Get a Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key for your project

2. **Clone the repository**

   ```bash
   git clone https://github.com/lavis0/AgenticEditor.git
   cd AgenticEditor
   ```

3. **Install Python packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

5. **⚠️ IMPORTANT: Commit your changes before running the agent**

   ```bash
   git add .
   git commit -m "Initial setup"
   ```

   **This allows you to revert any changes the agent makes to your codebase.**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- USAGE EXAMPLES -->

## Usage

AgenticEditor works by taking natural language prompts and executing them using a set of predefined functions. The agent can read files, write code, execute Python scripts, and navigate directories.

### Basic Usage

```bash
python main.py "Create a simple hello world program"
```

### Calculator Example

The project includes a calculator application that demonstrates the agent's capabilities:

```bash
# Ask the agent to use the calculator
python main.py "Calculate 15 + 27 using the calculator"

# Have the agent run tests
python main.py "Run the calculator tests and show me the results"

# Request code improvements
python main.py "Review the calculator code and suggest improvements"
```

### Advanced Usage

```bash
# Enable verbose output to see detailed function calls
python main.py --verbose "Analyze the project structure and create documentation"

# Complex refactoring tasks
python main.py "Refactor the calculator to support parentheses in expressions"
```

### Available Functions

The agent has access to these core functions:

- `get_files_info` - List files and directories with sizes
- `get_file_content` - Read file contents
- `run_python` - Execute Python files with optional arguments
- `write_file` - Create or overwrite files

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- ROADMAP -->

## Roadmap

- [x] File system navigation and reading
- [x] Python code execution
- [x] File writing and modification
- [x] Secure working directory constraints
- [x] Calculator demonstration project
- [ ] **Enhanced Debugging**: Fix harder and more complex bugs automatically
- [ ] **Code Refactoring**: Intelligent refactoring of code sections
- [ ] **Feature Development**: Add entirely new features to existing codebases
- [ ] **Configuration Management**: Easier customization of agent behavior
- [ ] **Multi-language Support**: Extend beyond Python to other languages
- [ ] **Advanced Functions**: Add more sophisticated development tools

### Extensibility Ideas

- [ ] **Other LLM Providers**: Support for OpenAI, Anthropic, etc.
- [ ] **Alternative Models**: Different Gemini model configurations
- [ ] **Custom Functions**: Easy addition of domain-specific functions
- [ ] **Integration**: Work with various codebases and project types

See the [open issues](https://github.com/lavis0/AgenticEditor/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- CONTACT -->

## Contact
Joshua Banga - <josh@folient.com>

Project Link: [https://github.com/lavis0/AgenticEditor](https://github.com/lavis0/AgenticEditor)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
