# Filtered Document Search

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=383938&style=for-the-badge&logo=cheshire_cat_ai)](https://)

<p align="center">
  <img src="logo.png" alt="Filtered Document Search Logo" width="200"/>
</p>

A Cheshire Cat AI plugin that enables user-specific document filtering and search capabilities. This plugin ensures that each user can only access and search through their own documents, providing a secure and personalized experience.

## Features

- **User-Specific Document Storage**: Automatically tags all stored documents with the current user's ID
- **Filtered Memory Access**: Ensures users can only access their own documents during memory recall
- **Secure Episodic Memory**: Adds user identification to episodic memories
- **Privacy by Design**: Built-in user isolation for multi-user environments

## Installation

1. Clone this repository into your Cheshire Cat AI's plugins folder:
```bash
cd /path/to/cheshire-cat/plugins
git clone https://github.com/vincenzolegrottaglie/filtered-document-search.git
```

2. Restart your Cheshire Cat AI instance to load the plugin.

## How It Works

The plugin implements three main hooks to manage document access:

1. **Document Storage Hook** (`before_rabbithole_stores_documents`):
   - Adds the current user's ID to all documents before storage
   - Ensures proper document ownership tracking

2. **Episodic Memory Hook** (`before_cat_stores_episodic_memory`):
   - Tags episodic memories with user identification
   - Maintains user context in memory storage

3. **Memory Recall Hook** (`before_cat_recalls_declarative_memories`):
   - Filters document searches based on the current user's ID
   - Ensures users only access their own documents

## Use Cases

- Multi-user chatbot environments
- Secure document management systems
- Privacy-focused applications
- User-isolated knowledge bases

## Requirements

- Cheshire Cat AI platform
- Python 3.x

## Version

Current version: 0.0.1

## Authors

Developed by [Net7](https://www.netseven.it/)

## License

This project is open source. See the LICENSE file for details.

