 <h1>Intelligent Summarizing System Using The T5 Model</h1>
 
  <p>
Summarization creates a shorter version of a document or an article that captures all the important information. In this project we will finetune T5 on the California state bill subset of the BillSum dataset for abstractive summarization.
  </p>

<br>

# Table of Contents

- [About the Project](#about-the-project)

  * [Tech Stack](#tech-stack)
  * [Features](#features)

- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)

- [Usage](#usage)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)
  
## About the Project
This project implements a text summarization tool utilizing the T5 (Text-to-Text Transfer Transformer) model from Hugging Face's Transformers library. Designed to efficiently condense lengthy documents into concise summaries, this tool is particularly tailored for processing legislative texts, drawing on the California BillSum dataset for training.

The California BillSum dataset consists of a rich collection of California legislative bills and their corresponding summaries, enabling the model to learn the intricacies of legal language and context. By leveraging the capabilities of the T5 model, this project aims to provide accurate, context-aware summaries that retain the essential information from the original texts.

### Tech Stack

<details>
 
  <ul>
    <li><a href="https://pytorch.org">PyTorch</a></li>
    <li><a href="https://huggingface.co/docs/transformers/en/index">HuggingFace Transformers</a></li>
    <li><a href="https://https://streamlit.io"> Streamlit</a></li>
  </ul>
</details>

### Features
- **Advanced Text Summarization:** Leverages the T5 model to generate high-quality, concise summaries from lengthy legislative texts.

- **Contextual Understanding:** Trained on the California BillSum dataset, the model effectively captures the nuances of legal language and context.

- **Customizable Output:** Easily adjust parameters for summary length and style to fit specific needs or preferences.

- **User-Friendly Interface:** Designed for easy integration and use, whether for individual projects or larger applications.

- **Performance Metrics:** Includes metrics for evaluating summarization quality, such as ROUGE scores, to ensure effectiveness.

- **Open Source:** Fully accessible codebase allows for modification, experimentation, and contributions from the community.



### Prerequisites

This project uses pip as package manager

```python
 pip install transformers
 pip install tensorflow[and-cuda]
 pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
 pip install streamlit
```

or install the packages through cmd by running pip with the requirements file in the
[repository](https://github.com/ezahpizza/BERT_Question_Answering)
## Usage



### Getting Started

1. **Installation**:
   - Clone the repository or download the project files.
   - Ensure you have Python installed (version 3.9 or higher).
   - Install the required libraries using pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Application**:
   - Navigate to the project directory in your terminal.
   - Start the web application with the following command:
     ```bash
     python app.py
     ```
   - Open your web browser and go to `http://127.0.0.1:5000` (or the specified port) to access the interface.

### Interacting with the System

1. **Inputting Context**:
   - In the provided text box, paste or type the passage you want the model to reference when summarizing.


2. **Receiving Answers**:
   - Click the "Summarize" button to send your paragraph. The system will process your input and display the summarized text below.


#### Example Workflow

1. **Provide Context**:
   - Example passage: "summarize: An Act to regulate the construction and operation of certain transportation projects in California.
The legislation outlines requirements for environmental assessments, public consultations, and funding allocations.""


2. **Get an Answer**:
   - The system might respond with: "Summary: This Act regulates transportation projects in California, detailing environmental assessments and funding."
"""
#### Documentation and Support

- For detailed instructions on configuration, customization, and troubleshooting, refer to the `README.md` file in the project repository.
- For any issues or questions, you can reach out through the project’s issue tracker or contacts. 

This straightforward usage guide enables users to quickly engage with the Question Answering system, making it easy to access its functionalities and derive meaningful insights.


## License

Distributed under the Apache License. See LICENSE.txt for more information.

## Contact

Prateek Mohapatra - [LinkedIn](www.linkedin.com/in/prateekmp) - prateekmsoa@gmail.com

Project Link: [T5-Text-Summarisation](https://github.com/ezahpizza/T5-Text-Summarization)

## Acknowledgements

 - [HuggingFace](https://huggingface.co/docs/transformers/index)

This project not only enhances understanding of NLP techniques but also contributes to the growing field of intelligent systems that can interact with users in a meaningful way.