# **Legal Dataset Generation with a Teacher LLM**

This project is dedicated to creating a specialized legal dataset for Tunisian law. The generation process is assisted by a "Teacher LLM" to produce complex and relevant question-answer examples.

The primary tool used for this generation is **Google AI Studio** with the **Gemini 3 Pro** model.

## **Repository Structure**

This repository contains the following elements:

- **/Batch_Outputs/**: This folder contains all generated data batches in JSON format. Each file represents a batch of question-answer pairs based on a specific legal text.
- **Output_Sample.json**: This file serves as a template and example for the expected JSON structure for each data batch.

## **Data Structure**

Each JSON file in `Batch_Outputs` follows a precise structure to ensure dataset consistency. Here are the main fields:

- `batch_id`: A unique identifier for the batch.
- `source`: The name of the source legal text (e.g., "Tunisian Customs Code").
- `articles_covered`: A list of article numbers used to generate the examples in this batch.
- `examples`: A list of objects, where each object is a question-answer example.
  - `example_id`: A unique identifier for the example.
  - `language`: The language of the example (`fr`, `ar`, `derja`).
  - `category`: The category of legal reasoning (e.g., `direct`, `multi_article`, `principle_exception`).
  - `messages`: A structured conversation between a `system`, a `user`, and an `assistant`.
- `coverage_summary`: A summary of the article coverage from the legal text within the batch.

## **Contents of Data**

- Multi-hop reasoning QA pairs
- Context provided with each question (to simulate chunks coming from RAG to LLMs + Query)
- Samples in Arabic (MSA and Derja) and French

## **📈 Next Steps**

- Scale to 1000+ samples
- Human validation with legal expert

## **Keywords**

- Legal Tech
- Legal Dataset
- Data Generation
- Large Language Model (LLM)
- Gemini
- Google AI Studio
- Tunisian Law
- Question-Answering (QA)
- Instruction Following
- Fine-tuning
