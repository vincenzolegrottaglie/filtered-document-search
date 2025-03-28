from cat.mad_hatter.decorators import hook

@hook
def before_rabbithole_stores_documents(docs, cat):
    """Adds the explicit user ID to all documents."""
    user_id = cat.user_id
    
    for doc in docs:
        doc.metadata["user_id"] = user_id
    
    return docs

@hook
def before_cat_stores_episodic_memory(doc, cat):
    """Adds the explicit user ID to the episodic memory."""
    doc.metadata["user_id"] = cat.user_id
    
    return doc

@hook
def before_cat_recalls_declarative_memories(declarative_recall_config, cat):
    """Filters the search to show only the documents of the current user."""
    user_id = cat.user_id
    
    if "metadata" not in declarative_recall_config:
        declarative_recall_config["metadata"] = {}
    
    declarative_recall_config["metadata"]["user_id"] = user_id

    return declarative_recall_config
